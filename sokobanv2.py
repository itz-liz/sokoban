# sokobanv2.py implementa la versión manual de un solo nivel.
# El usuario controla directamente al personaje con las teclas W, A, S y D.
class Sokoban:
    # Esta tabla guarda el número de cada elemento del juego.
    elementos = {
        # 8 representa al personaje en esta versión manual.
        "personaje": 8,
        # 1 represanta un camino.
        "camino": 1,
        # 2 representa una pared (bloquea el movimiento).
        "pared": 2,
        # 3 representa la salida/meta.
        "salida": 3,
        # 4 representa al personaje cuando está parado sobre la salida.
        "personaje_salida": 4,
    }

    def __init__(self):
        # Aquí guardaremos el mapa completo.
        self.mapa = []
        # Abrimos el archivo del nivel en modo lectura.
        archivo = open("nivel1.txt", "r")

        # Recorremos cada línea del archivo.
        for linea in archivo:
            # Esta lista será una fila del mapa.
            fila = []
            # Recorremos cada carácter de la línea (sin salto de línea).
            for caracter in linea.strip():
                # Convertimos el carácter en número y lo guardamos en la fila.
                fila.append(int(caracter))
            # Guardamos la fila completa dentro del mapa.
            self.mapa.append(fila)

        # Cerramos el archivo porque ya terminamos de leerlo.
        archivo.close()

        # Posición inicial por defecto del personaje.
        self.personaje_fila = 0
        # Posición inicial por defecto del personaje.
        self.personaje_columna = 0
        # Esta variable indica si ya se terminó el juego.
        self.juego_terminado = False

        # Recorremos cada fila del mapa para ubicar al personaje.
        for fila in range(len(self.mapa)):
            # Recorremos cada columna de esa fila.
            for columna in range(len(self.mapa[fila])):
                # Si encontramos un 8, esa es la posición del personaje.
                if self.mapa[fila][columna] == self.elementos["personaje"]:
                    # Guardamos la fila del personaje.
                    self.personaje_fila = fila
                    # Guardamos la columna del personaje.
                    self.personaje_columna = columna

    def imprimir_mapa(self):
        # Recorremos todas las filas.
        for fila in self.mapa:
            # Imprimimos una fila del mapa.
            print(str(fila).replace(str(self.elementos["camino"])," ").replace(",","")) #reemplaza el numero del camino que en este caso es 2, somo str o cadena de valores, y lo deja como , el segundo replace ,remplaza la comita por espacio en blanco 

    def mover_personaje(self, cambio_fila, cambio_columna):
        # Calculamos la nueva fila según el movimiento.
        nueva_fila = self.personaje_fila + cambio_fila
        # Calculamos la nueva columna según el movimiento.
        nueva_columna = self.personaje_columna + cambio_columna

        # Si la nueva fila sale del mapa, no se mueve.
        if nueva_fila < 0 or nueva_fila >= len(self.mapa):
            return
        # Si la nueva columna sale del mapa, no se mueve.
        if nueva_columna < 0 or nueva_columna >= len(self.mapa[nueva_fila]):
            return

        # Guardamos qué hay en la casilla destino.
        elemento_destino = self.mapa[nueva_fila][nueva_columna]

        # Si no es camino...
        if elemento_destino != self.elementos["camino"]:
            # ...y tampoco es salida, el movimiento es inválido.
            if elemento_destino != self.elementos["salida"]:
                return

        # Si el personaje estaba sobre la salida...
        if self.mapa[self.personaje_fila][self.personaje_columna] == self.elementos["personaje_salida"]:
            # la casilla anterior vuelve a ser salida.
            self.mapa[self.personaje_fila][self.personaje_columna] = self.elementos["salida"]
        else:
            # Si no, la casilla anterior vuelve a ser camino.
            self.mapa[self.personaje_fila][self.personaje_columna] = self.elementos["camino"]

        # Si llega a la salida 
        if elemento_destino == self.elementos["salida"]:
            # la nueva casilla será personaje_salida (4).
            self.mapa[nueva_fila][nueva_columna] = self.elementos["personaje_salida"]
            # Marcamos que el juego terminó.
            self.juego_terminado = True
            
        else:
            # Si llega a camino, la nueva casilla queda como personaje (8).
            self.mapa[nueva_fila][nueva_columna] = self.elementos["personaje"]

        # Actualizamos la fila actual del personaje.
        self.personaje_fila = nueva_fila
        # Actualizamos la columna actual del personaje.
        self.personaje_columna = nueva_columna


    
    def jugar(self):
        # Mostramos la tecla para salir manualmente.
        print("Usa Q para terminar.")

        # Bucle principal del juego.
        while True:
            # Mostramos el mapa actual.
            self.imprimir_mapa()
            # Leemos una tecla y la pasamos a minúscula.
            movimiento = input("Movimiento: ").lower()

            # Si presiona Q, terminamos.
            if movimiento == "q":
                break
            # Si presiona W, mueve arriba.
            elif movimiento == "w":
                self.mover_personaje(-1, 0)
            # Si presiona S, mueve abajo.
            elif movimiento == "s":
                self.mover_personaje(1, 0)
            # Si presiona A, mueve a la izquierda.
            elif movimiento == "a":
                self.mover_personaje(0, -1)
            # Si presiona D, mueve a la derecha.
            elif movimiento == "d":
                self.mover_personaje(0, 1)
            else:
                # Si escribe otra tecla, avisamos que no es válida.
                print("Esa tecla no es un movimiento.")

            # Si ya llegó a la salida (código 4), termina el juego.
            if self.juego_terminado:
                self.imprimir_mapa()
                break


# Esto evita que el juego se ejecute al importar el archivo desde otro lado.
if __name__ == "__main__":
    # Creamos el juego.
    juego = Sokoban()
    # Iniciamos el juego
    juego.jugar()
