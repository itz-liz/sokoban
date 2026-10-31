import random
import time


class Sokoban:
    elementos = {
        "personaje": 0,
        "camino": 1,
        "pared": 2,
        "salida": 3,
        "personaje_salida": 4,
    }

    direcciones = {
        "w": (-1, 0),
        "d": (0, 1),
        "s": (1, 0),
        "a": (0, -1),
    }
    personajes = (0,)

    def __init__(self, archivo_nivel="nivel1.txt"):
        self.archivo_nivel = archivo_nivel
        self.mapa_inicial = self._leer_mapa()
        self.mapa = []
        self.personaje_fila = 0
        self.personaje_columna = 0
        self.juego_terminado = False
        self.contador_pasos = 0
        self.reiniciar()

    def _leer_mapa(self):
        with open(self.archivo_nivel, "r", encoding="utf-8") as archivo:
            mapa = [
                [int(caracter) for caracter in linea.strip()]
                for linea in archivo
                if linea.strip()
            ]

        if not mapa or any(not fila for fila in mapa):
            raise ValueError("El nivel no puede estar vacío.")

        return mapa

    def reiniciar(self):
        self.mapa = [fila[:] for fila in self.mapa_inicial]
        self.juego_terminado = False
        self.contador_pasos = 0

        for fila, contenido in enumerate(self.mapa):
            for columna, elemento in enumerate(contenido):
                if elemento in self.personajes:
                    self.personaje_fila = fila
                    self.personaje_columna = columna
                    return

        raise ValueError("El nivel debe tener un personaje.")

    def imprimir_mapa(self):
        for fila in self.mapa:
            print(
                "".join(
                    " " if elemento == self.elementos["camino"] else str(elemento)
                    for elemento in fila
                )
            )

    def _movimiento_valido(self, cambio_fila, cambio_columna):
        nueva_fila = self.personaje_fila + cambio_fila
        nueva_columna = self.personaje_columna + cambio_columna

        if nueva_fila < 0 or nueva_fila >= len(self.mapa):
            return False
        if nueva_columna < 0 or nueva_columna >= len(self.mapa[nueva_fila]):
            return False

        return self.mapa[nueva_fila][nueva_columna] in (
            self.elementos["camino"],
            self.elementos["salida"],
        )

    def mover_personaje(self, cambio_fila, cambio_columna):
        if not self._movimiento_valido(cambio_fila, cambio_columna):
            return False

        nueva_fila = self.personaje_fila + cambio_fila
        nueva_columna = self.personaje_columna + cambio_columna
        elemento_anterior = self.mapa[
            self.personaje_fila
        ][self.personaje_columna]
        elemento_destino = self.mapa[nueva_fila][nueva_columna]

        self.mapa[self.personaje_fila][self.personaje_columna] = (
            self.elementos["salida"]
            if elemento_anterior == self.elementos["personaje_salida"]
            else self.elementos["camino"]
        )
        self.mapa[nueva_fila][nueva_columna] = (
            self.elementos["personaje_salida"]
            if elemento_destino == self.elementos["salida"]
            else self.elementos["personaje"]
        )
        self.personaje_fila = nueva_fila
        self.personaje_columna = nueva_columna
        self.contador_pasos += 1
        self.juego_terminado = elemento_destino == self.elementos["salida"]
        return True

    def _movimientos_mano_derecha(self, direccion_actual):
        return self._movimientos_desde(
            (self.personaje_fila, self.personaje_columna), direccion_actual
        )

    def _movimientos_desde(self, posicion, direccion_actual):
        orden = ["w", "d", "s", "a"]
        indice = orden.index(direccion_actual)
        # La primera opción es la que queda a la derecha del personaje.
        prioridad = [1, 0, -1, 2]
        candidatos = []
        fila, columna = posicion

        for giro in prioridad:
            direccion = orden[(indice + giro) % len(orden)]
            cambio = self.direcciones[direccion]
            nueva_fila = fila + cambio[0]
            nueva_columna = columna + cambio[1]
            if (
                0 <= nueva_fila < len(self.mapa_inicial)
                and 0 <= nueva_columna < len(self.mapa_inicial[nueva_fila])
                and self.mapa_inicial[nueva_fila][nueva_columna]
                in (self.elementos["camino"], self.elementos["salida"])
            ):
                candidatos.append((direccion, cambio))

        return candidatos

    def _intentar_resolver(self, max_pasos, aleatorio):
        self.reiniciar()
        direccion_actual = aleatorio.choice(list(self.direcciones))
        posicion_inicial = (self.personaje_fila, self.personaje_columna)
        visitados = {posicion_inicial}
        camino = []
        pila = [
            (
                posicion_inicial,
                direccion_actual,
                self._movimientos_desde(posicion_inicial, direccion_actual),
            )
        ]
        salida = next(
            (
                (fila, columna)
                for fila, contenido in enumerate(self.mapa_inicial)
                for columna, elemento in enumerate(contenido)
                if elemento == self.elementos["salida"]
            ),
            None,
        )

        while pila:
            posicion, _, candidatos = pila[-1]
            if posicion == salida:
                return camino
            if len(camino) >= max_pasos or not candidatos:
                pila.pop()
                if camino:
                    camino.pop()
                continue

            # La primera opción tiene más probabilidad, pero cada intento
            # puede tomar una ruta distinta en una intersección.
            peso = [4, 2, 1, 1][: len(candidatos)]
            candidato = aleatorio.choices(candidatos, weights=peso, k=1)[0]
            candidatos.remove(candidato)
            direccion_actual, cambio = candidato
            siguiente = (
                posicion[0] + cambio[0],
                posicion[1] + cambio[1],
            )
            if siguiente in visitados:
                continue

            visitados.add(siguiente)
            camino.append(cambio)
            pila.append(
                (
                    siguiente,
                    direccion_actual,
                    self._movimientos_desde(siguiente, direccion_actual),
                )
            )

        return None

    def resolver_automaticamente(
        self, intentos=100, max_pasos=None, pausa=0.1, semilla=None
    ):
        if intentos < 1:
            raise ValueError("intentos debe ser mayor que cero.")

        casillas_transitables = sum(
            elemento in (self.elementos["camino"], self.elementos["salida"])
            for fila in self.mapa_inicial
            for elemento in fila
        )
        if max_pasos is None:
            max_pasos = casillas_transitables
        if max_pasos < 1:
            raise ValueError("max_pasos debe ser mayor que cero.")

        aleatorio = random.Random(semilla)
        mejor_camino = None

        for _ in range(intentos):
            camino = self._intentar_resolver(max_pasos, aleatorio)
            if camino is not None and (
                mejor_camino is None or len(camino) < len(mejor_camino)
            ):
                mejor_camino = camino

        if mejor_camino is None:
            self.reiniciar()
            raise RuntimeError("No se encontró un camino a la salida.")

        self.reiniciar()
        print(f"Camino encontrado: {len(mejor_camino)} pasos.")
        print("Paso 0:")
        self.imprimir_mapa()
        for cambio in mejor_camino:
            self.mover_personaje(*cambio)
            if pausa:
                time.sleep(pausa)
            print()
            print(f"Paso {self.contador_pasos}:")
            self.imprimir_mapa()

        return self.contador_pasos

    def jugar_niveles(self, niveles=None):
        niveles = niveles or [
            "nivel1.txt",
            "nivel2.txt",
            "nivel3.txt",
            "nivel4.txt",
        ]

        for indice, archivo_nivel in enumerate(niveles):
            self.archivo_nivel = archivo_nivel
            self.mapa_inicial = self._leer_mapa()
            self.reiniciar()
            self.resolver_automaticamente()

            if indice == len(niveles) - 1:
                print("Has completado todos los niveles.")
                break

            respuesta = input(
                "\n¿Deseas pasar al siguiente nivel :D? (s/n): "
            ).strip().lower()
            if respuesta not in ("s", "si", "sí"):
                print("Juego terminado.")
                break

    def jugar(self):
        self.jugar_niveles()


if __name__ == "__main__":
    Sokoban().jugar()
