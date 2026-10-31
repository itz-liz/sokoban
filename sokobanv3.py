# Importa el generador de decisiones aleatorias para variar los recorridos.
import random
# Importa las pausas usadas para animar cada movimiento en la consola.
import time


# Define la clase que representa el tablero y el solucionador automático.
class Sokoban:
    # Asocia cada número del archivo de nivel con su significado.
    elementos = {
        # El cero representa exclusivamente al personaje.
        "personaje": 0,
        # El uno representa una casilla transitable.
        "camino": 1,
        # El dos representa una pared que no se puede atravesar.
        "pared": 2,
        # El tres representa la casilla de salida.
        "salida": 3,
        # El cuatro representa al personaje colocado sobre la salida.
        "personaje_salida": 4,
    }

    # Relaciona cada tecla con el cambio de fila y columna correspondiente.
    direcciones = {
        # La tecla W mueve una fila hacia arriba.
        "w": (-1, 0),
        # La tecla D mueve una columna hacia la derecha.
        "d": (0, 1),
        # La tecla S mueve una fila hacia abajo.
        "s": (1, 0),
        # La tecla A mueve una columna hacia la izquierda.
        "a": (0, -1),
    }
    # Define el único valor permitido para el personaje.
    personajes = (0,)

    # Construye el juego leyendo el archivo de nivel indicado.
    def __init__(self, archivo_nivel="nivel1.txt"):
        # Guarda el nombre del archivo para poder cambiar de nivel.
        self.archivo_nivel = archivo_nivel
        # Lee y conserva una copia inmutable lógica del mapa original.
        self.mapa_inicial = self._leer_mapa()
        # Reserva el mapa que se modifica durante la partida.
        self.mapa = []
        # Inicializa la fila del personaje antes de localizarlo.
        self.personaje_fila = 0
        # Inicializa la columna del personaje antes de localizarlo.
        self.personaje_columna = 0
        # Indica si el personaje ya alcanzó la salida.
        self.juego_terminado = False
        # Cuenta únicamente los movimientos válidos realizados.
        self.contador_pasos = 0
        # Carga el mapa y localiza al personaje.
        self.reiniciar()

    # Lee el archivo y convierte cada carácter numérico en un entero.
    def _leer_mapa(self):
        # Abre el nivel garantizando la codificación UTF-8.
        with open(self.archivo_nivel, "r", encoding="utf-8") as archivo:
            # Ignora líneas vacías y transforma cada línea en una fila.
            mapa = [
                # Convierte todos los caracteres de la línea en números.
                [int(caracter) for caracter in linea.strip()]
                # Recorre todas las líneas del archivo.
                for linea in archivo
                # Excluye líneas que solo contienen espacios o saltos.
                if linea.strip()
            ]

        # Rechaza archivos vacíos o filas sin contenido.
        if not mapa or any(not fila for fila in mapa):
            # Informa claramente que el nivel no es válido.
            raise ValueError("El nivel no puede estar vacío.")

        # Devuelve la matriz que representa el nivel.
        return mapa

    # Restaura el nivel y busca la posición inicial del personaje.
    def reiniciar(self):
        # Copia cada fila para no modificar el mapa original.
        self.mapa = [fila[:] for fila in self.mapa_inicial]
        # Marca la nueva partida como no terminada.
        self.juego_terminado = False
        # Reinicia el contador de pasos.
        self.contador_pasos = 0

        # Recorre las filas del mapa actual.
        for fila, contenido in enumerate(self.mapa):
            # Recorre las columnas de cada fila.
            for columna, elemento in enumerate(contenido):
                # Comprueba si la casilla contiene el personaje cero.
                if elemento in self.personajes:
                    # Guarda la fila encontrada.
                    self.personaje_fila = fila
                    # Guarda la columna encontrada.
                    self.personaje_columna = columna
                    # Termina la búsqueda cuando encuentra al personaje.
                    return

        # Informa que el archivo no contiene un personaje válido.
        raise ValueError("El nivel debe tener un personaje.")

    # Imprime el tablero reemplazando el camino por espacios visibles.
    def imprimir_mapa(self):
        # Recorre cada fila del tablero.
        for fila in self.mapa:
            # Convierte los elementos de la fila en una cadena.
            print(
                # Une todos los caracteres sin separadores adicionales.
                "".join(
                    # Muestra un espacio para el camino y el número restante.
                    " " if elemento == self.elementos["camino"] else str(elemento)
                    # Recorre cada elemento de la fila actual.
                    for elemento in fila
                )
            )

    # Comprueba si un desplazamiento puede realizarse.
    def _movimiento_valido(self, cambio_fila, cambio_columna):
        # Calcula la fila destino.
        nueva_fila = self.personaje_fila + cambio_fila
        # Calcula la columna destino.
        nueva_columna = self.personaje_columna + cambio_columna

        # Rechaza destinos que salen por arriba o por abajo del tablero.
        if nueva_fila < 0 or nueva_fila >= len(self.mapa):
            # Indica que el movimiento no es posible.
            return False
        # Rechaza destinos que salen por los lados de una fila.
        if nueva_columna < 0 or nueva_columna >= len(self.mapa[nueva_fila]):
            # Indica que el movimiento no es posible.
            return False

        # Solo permite caminar sobre camino o sobre la salida.
        return self.mapa[nueva_fila][nueva_columna] in (
            # Incluye la casilla transitable.
            self.elementos["camino"],
            # Incluye la casilla de meta.
            self.elementos["salida"],
        )

    # Ejecuta un movimiento válido y actualiza el estado del juego.
    def mover_personaje(self, cambio_fila, cambio_columna):
        # No modifica el tablero si el destino está bloqueado.
        if not self._movimiento_valido(cambio_fila, cambio_columna):
            # Indica al llamador que no hubo movimiento.
            return False

        # Calcula la fila nueva del personaje.
        nueva_fila = self.personaje_fila + cambio_fila
        # Calcula la columna nueva del personaje.
        nueva_columna = self.personaje_columna + cambio_columna
        # Guarda el elemento que ocupaba la posición anterior.
        elemento_anterior = self.mapa[
            # Selecciona la fila anterior.
            self.personaje_fila
            # Selecciona la columna anterior.
        ][self.personaje_columna]
        # Guarda el elemento que había en el destino.
        elemento_destino = self.mapa[nueva_fila][nueva_columna]

        # Restaura la casilla anterior como salida o camino.
        self.mapa[self.personaje_fila][self.personaje_columna] = (
            # Conserva la salida si el personaje estaba encima de ella.
            self.elementos["salida"]
            # Comprueba si la casilla anterior era personaje sobre salida.
            if elemento_anterior == self.elementos["personaje_salida"]
            # Si no, la casilla anterior vuelve a ser camino.
            else self.elementos["camino"]
        )
        # Coloca el personaje en la casilla nueva.
        self.mapa[nueva_fila][nueva_columna] = (
            # Usa cuatro cuando el personaje llega a la salida.
            self.elementos["personaje_salida"]
            # Comprueba si el destino era la salida.
            if elemento_destino == self.elementos["salida"]
            # Usa cero cuando el destino era un camino.
            else self.elementos["personaje"]
        )
        # Actualiza la fila actual.
        self.personaje_fila = nueva_fila
        # Actualiza la columna actual.
        self.personaje_columna = nueva_columna
        # Aumenta el contador porque el movimiento fue válido.
        self.contador_pasos += 1
        # Marca el juego como terminado al llegar a la salida.
        self.juego_terminado = elemento_destino == self.elementos["salida"]
        # Informa que el movimiento sí se ejecutó.
        return True

    # Obtiene los movimientos priorizados según la mano derecha.
    def _movimientos_mano_derecha(self, direccion_actual):
        # Usa la posición actual como origen de la búsqueda.
        return self._movimientos_desde(
            (self.personaje_fila, self.personaje_columna), direccion_actual
        )

    # Calcula movimientos transitables desde cualquier posición del mapa.
    def _movimientos_desde(self, posicion, direccion_actual):
        # Define el orden geométrico de las direcciones.
        orden = ["w", "d", "s", "a"]
        # Encuentra la dirección actual dentro del orden.
        indice = orden.index(direccion_actual)
        # Prioriza derecha, frente, izquierda y finalmente atrás.
        prioridad = [1, 0, -1, 2]
        # Prepara la lista de movimientos posibles.
        candidatos = []
        # Separa la posición en fila y columna.
        fila, columna = posicion

        # Evalúa las cuatro orientaciones en el orden de prioridad.
        for giro in prioridad:
            # Calcula la dirección resultante del giro.
            direccion = orden[(indice + giro) % len(orden)]
            # Obtiene el desplazamiento de esa dirección.
            cambio = self.direcciones[direccion]
            # Calcula la fila candidata.
            nueva_fila = fila + cambio[0]
            # Calcula la columna candidata.
            nueva_columna = columna + cambio[1]
            # Comprueba límites y casillas transitables del mapa original.
            if (
                0 <= nueva_fila < len(self.mapa_inicial)
                and 0 <= nueva_columna < len(self.mapa_inicial[nueva_fila])
                and self.mapa_inicial[nueva_fila][nueva_columna]
                in (self.elementos["camino"], self.elementos["salida"])
            ):
                # Guarda la dirección y el desplazamiento válidos.
                candidatos.append((direccion, cambio))

        # Devuelve los candidatos ordenados por mano derecha.
        return candidatos

    # Busca un camino usando azar controlado y retroceso.
    def _intentar_resolver(self, max_pasos, aleatorio):
        # Reinicia el estado antes de comenzar el intento.
        self.reiniciar()
        # Selecciona una orientación inicial aleatoria.
        direccion_actual = aleatorio.choice(list(self.direcciones))
        # Guarda la posición inicial para la exploración.
        posicion_inicial = (self.personaje_fila, self.personaje_columna)
        # Evita visitar dos veces la misma casilla en un intento.
        visitados = {posicion_inicial}
        # Conserva los desplazamientos del camino provisional.
        camino = []
        # La pila permite retroceder cuando una rama se bloquea.
        pila = [
            (
                # Guarda la posición que se está explorando.
                posicion_inicial,
                # Guarda la orientación usada en esa posición.
                direccion_actual,
                # Guarda sus movimientos aún no probados.
                self._movimientos_desde(posicion_inicial, direccion_actual),
            )
        ]
        # Busca la primera casilla que representa la salida.
        salida = next(
            (
                # Devuelve las coordenadas de la salida.
                (fila, columna)
                # Recorre todas las filas originales.
                for fila, contenido in enumerate(self.mapa_inicial)
                # Recorre todas las columnas de cada fila.
                for columna, elemento in enumerate(contenido)
                # Filtra la casilla marcada como salida.
                if elemento == self.elementos["salida"]
            ),
            # Usa None si el nivel no tiene salida.
            None,
        )

        # Continúa mientras existan ramas pendientes por explorar.
        while pila:
            # Obtiene la rama actual y sus candidatos restantes.
            posicion, _, candidatos = pila[-1]
            # Devuelve el camino cuando alcanza la salida.
            if posicion == salida:
                return camino
            # Retrocede si supera el límite o agota los candidatos.
            if len(camino) >= max_pasos or not candidatos:
                # Retira la rama agotada.
                pila.pop()
                # Retira también el último paso del camino provisional.
                if camino:
                    camino.pop()
                # Continúa explorando la rama anterior.
                continue

            # Da mayor probabilidad a los candidatos prioritarios.
            peso = [4, 2, 1, 1][: len(candidatos)]
            # Escoge aleatoriamente una opción disponible.
            candidato = aleatorio.choices(candidatos, weights=peso, k=1)[0]
            # Evita volver a escogerla dentro de esta rama.
            candidatos.remove(candidato)
            # Separa dirección y desplazamiento.
            direccion_actual, cambio = candidato
            # Calcula la siguiente posición.
            siguiente = (
                posicion[0] + cambio[0],
                posicion[1] + cambio[1],
            )
            # Ignora posiciones ya visitadas en este intento.
            if siguiente in visitados:
                continue

            # Registra la nueva posición.
            visitados.add(siguiente)
            # Agrega el movimiento al camino provisional.
            camino.append(cambio)
            # Añade la nueva rama a la pila de exploración.
            pila.append(
                (
                    # Guarda la posición nueva.
                    siguiente,
                    # Conserva la dirección de llegada.
                    direccion_actual,
                    # Calcula las opciones de la nueva posición.
                    self._movimientos_desde(siguiente, direccion_actual),
                )
            )

        # Indica que este intento no encontró una solución.
        return None

    # Ejecuta varios intentos y reproduce el camino más corto encontrado.
    def resolver_automaticamente(
        self, intentos=100, max_pasos=None, pausa=0.1, semilla=None
    ):
        # Exige al menos un intento de resolución.
        if intentos < 1:
            # Rechaza una configuración sin sentido.
            raise ValueError("intentos debe ser mayor que cero.")

        # Cuenta las casillas que pueden formar parte de un camino.
        casillas_transitables = sum(
            # Comprueba si cada elemento es camino o salida.
            elemento in (self.elementos["camino"], self.elementos["salida"])
            # Recorre todas las filas.
            for fila in self.mapa_inicial
            # Recorre todos los elementos de cada fila.
            for elemento in fila
        )
        # Usa todas las casillas transitables como límite predeterminado.
        if max_pasos is None:
            max_pasos = casillas_transitables
        # Rechaza un límite que no permita ningún movimiento.
        if max_pasos < 1:
            # Informa del valor inválido.
            raise ValueError("max_pasos debe ser mayor que cero.")

        # Crea un generador aislado para que la semilla sea reproducible.
        aleatorio = random.Random(semilla)
        # Inicialmente no existe un camino ganador.
        mejor_camino = None

        # Repite la búsqueda el número de intentos solicitado.
        for _ in range(intentos):
            # Explora una ruta con azar y retroceso.
            camino = self._intentar_resolver(max_pasos, aleatorio)
            # Conserva solo soluciones y reemplaza por una más corta.
            if camino is not None and (
                mejor_camino is None or len(camino) < len(mejor_camino)
            ):
                # Guarda la mejor ruta encontrada hasta el momento.
                mejor_camino = camino

        # Informa si ningún intento consiguió llegar a la salida.
        if mejor_camino is None:
            # Restablece el tablero antes de informar el error.
            self.reiniciar()
            # Detiene la ejecución con un mensaje explícito.
            raise RuntimeError("No se encontró un camino a la salida.")

        # Reinicia para reproducir desde el comienzo la mejor ruta.
        self.reiniciar()
        # Informa cuántos pasos tiene la solución elegida.
        print(f"Camino encontrado: {len(mejor_camino)} pasos.")
        # Etiqueta el estado inicial del tablero.
        print("Paso 0:")
        # Imprime el tablero inicial.
        self.imprimir_mapa()
        # Reproduce cada desplazamiento de la mejor solución.
        for cambio in mejor_camino:
            # Aplica el desplazamiento actual.
            self.mover_personaje(*cambio)
            # Espera si se solicitó una animación visible.
            if pausa:
                time.sleep(pausa)
            # Separa visualmente los mapas consecutivos.
            print()
            # Imprime el número de paso realizado.
            print(f"Paso {self.contador_pasos}:")
            # Imprime el tablero después del movimiento.
            self.imprimir_mapa()

        # Devuelve el total de pasos efectuados.
        return self.contador_pasos

    # Ejecuta todos los niveles y pregunta antes de avanzar.
    def jugar_niveles(self, niveles=None):
        # Define los cuatro niveles predeterminados.
        niveles = niveles or [
            # Primer nivel del juego.
            "nivel1.txt",
            # Segundo nivel del juego.
            "nivel2.txt",
            # Tercer nivel del juego.
            "nivel3.txt",
            # Cuarto nivel del juego.
            "nivel4.txt",
        ]

        # Recorre los niveles en el orden indicado.
        for indice, archivo_nivel in enumerate(niveles):
            # Actualiza el archivo que se está jugando.
            self.archivo_nivel = archivo_nivel
            # Lee el nuevo tablero.
            self.mapa_inicial = self._leer_mapa()
            # Localiza al personaje y reinicia sus contadores.
            self.reiniciar()
            # Resuelve y muestra automáticamente el nivel.
            self.resolver_automaticamente()

            # Si era el último nivel, finaliza sin hacer otra pregunta.
            if indice == len(niveles) - 1:
                # Confirma que se completó la colección.
                print("Has completado todos los niveles.")
                # Sale del bucle de niveles.
                break

            # Pregunta al usuario si desea continuar.
            respuesta = input(
                # Muestra las opciones de respuesta.
                "\n¿Deseas pasar al siguiente nivel :D? (s/n): "
            ).strip().lower()
            # Acepta las formas afirmativas más comunes.
            if respuesta not in ("s", "si", "sí"):
                # Informa que la partida se detuvo.
                print("Juego terminado.")
                # Sale del recorrido de niveles.
                break

    # Inicia el recorrido automático de los niveles.
    def jugar(self):
        # Delega la ejecución en la lista predeterminada.
        self.jugar_niveles()


# Ejecuta el juego solo cuando este archivo se lanza directamente.
if __name__ == "__main__":
    # Crea una instancia usando nivel1.txt.
    Sokoban().jugar()
