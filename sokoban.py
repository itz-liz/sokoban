class Sokoban:

    """
    0 - personaje 
    1- caja
    2- pared
    3- meta 
    4- camino
    5- caja_meta
    6- personaje_meta
    """

    def __init__ (self) -> None:
        #Definir el estado inicial del juego
        self.mapa = [ 
            [ 2,2,2,2,2,2,2 ],
            [ 2,4,4,4,4,4,2 ],
            [ 2,4,4,4,4,4,2 ],
            [ 2,4,4,0,3,4,2 ],
            [ 2,4,4,4,4,4,2 ],
            [ 2,2,2,2,2,2,2 ]
            ]

        #Definir la psoicion inicial del personaje 
        self.personaje_fila= 3
        self.personaje_columna=3
        

    
    def imprimirMapa(self) -> None:
        # Toma cada fila del mapa y se imprime en la consola
        for fila in self.mapa:
            print (fila)


    def derecha(self) -> None:
        # TODO: 1. Personaje, Camino (0,4) -> (4,0)
        # TODO: 2. Personaje, meta (0,3) -> (4,6)

        #1. Personaje, Camino (0,4) -> (4,0)
        if ( 
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila][self.personaje_columna+1] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna] = 4

            #Actualiza la posición del personaje
            self.personaje_columna = self.personaje_columna + 1

        #1.1 Cuando el personaje es 6 y se desea mover se debe quedar 3 el camino anterior a el y el de enfrente vuelve a ser 0 
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6 # es el estado inical del personaje como esta en la meta ahora es 6
            and self.mapa[self.personaje_fila][self.personaje_columna+1] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje en este caso es 3 porque el personaje estaba en la meta
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            #Actualiza la posición del personaje para la derecha
            self.personaje_columna = self.personaje_columna + 1
            self.mapa[self.personaje_fila][self.personaje_columna] = 0 #Coloca un personaje donde estaba el camino

        #|2. Personaje, meta (0,3) -> (4,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila][self.personaje_columna+1] == 3 #Revisar si el camino de enfrente del personaje es 3
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 0
            #Actualiza la posición del personaje
            self.personaje_columna = self.personaje_columna + 1 
            self.mapa[self.personaje_fila][self.personaje_columna] = 6 #Coloca un personaje_meta donde estaba el camino
            
        
    def izquierda(self) -> None:

        #1. Personaje, Camino (0,4) -> (4,0)
        if ( 
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila][self.personaje_columna-1] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna-1] = 0
            #Actualiza la posición del personaje
            self.personaje_columna = self.personaje_columna - 1

        #1.1 Cuando el personaje es 6 y se desea mover se debe quedar 3 el camino anterior a el y el de enfrente vuelve a ser 0 
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6 # es el estado inical del personaje como esta en la meta ahora es 6
            and self.mapa[self.personaje_fila][self.personaje_columna-1] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje en este caso es 3 porque el personaje estaba en la meta
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            #Actualiza la posición del personaje para la izquierda
            self.personaje_columna = self.personaje_columna - 1
            self.mapa[self.personaje_fila][self.personaje_columna] = 0 #Coloca un personaje donde estaba el camino

        #2. Personaje, meta (0,3) -> (4,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila][self.personaje_columna-1] == 3 #Revisar si el camino de enfrente del personaje es 3
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna-1] = 0
            #Actualiza la posición del personaje
            self.personaje_columna = self.personaje_columna - 1 
            self.mapa[self.personaje_fila][self.personaje_columna] = 6 #Coloca un personaje_meta donde estaba el camino
    
    def arriba(self) -> None:
        #1. Arriba el personaje 
        if ( 
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila-1][self.personaje_columna] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 0
            #Actualiza la posición del personaje
            self.personaje_fila = self.personaje_fila - 1

        #1.1 Cuando el personaje es 6 y se desea mover se debe quedar 3 el camino anterior a el y el de enfrente vuelve a ser 0 
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6 # es el estado inical del personaje como esta en la meta ahora es 6
            and self.mapa[self.personaje_fila-1][self.personaje_columna] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje en este caso es 3 porque el personaje estaba en la meta
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            #Actualiza la posición del personaje para la izquierda
            self.personaje_fila = self.personaje_fila - 1
            self.mapa[self.personaje_fila][self.personaje_columna] = 0 #Coloca un personaje donde estaba el camino

        #2. Personaje, meta (0,3) -> (4,6)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila-1][self.personaje_columna] == 3 #Revisar si el camino de enfrente del personaje es 3
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 0
            #Actualiza la posición del personaje
            self.personaje_fila = self.personaje_fila - 1 
            self.mapa[self.personaje_fila][self.personaje_columna] = 6 #Coloca un personaje_meta donde estaba el camino

    def abajo(self) -> None:
        #1 - Para abajo el personaje 
         if ( 
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila+1][self.personaje_columna] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila+1][self.personaje_columna] = 0
            #Actualiza la posición del personaje
            self.personaje_fila = self.personaje_fila + 1

        #1.1 Cuando el personaje es 6 y se desea mover se debe quedar 3 el camino anterior a el y el de enfrente vuelve a ser 0 
         elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6 # es el estado inical del personaje como esta en la meta ahora es 6
            and self.mapa[self.personaje_fila+1][self.personaje_columna] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje en este caso es 3 porque el personaje estaba en la meta
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            #Actualiza la posición del personaje para la izquierda
            self.personaje_fila = self.personaje_fila + 1
            self.mapa[self.personaje_fila][self.personaje_columna] = 0 #Coloca un personaje donde estaba el camino

        #2. Personaje, meta (0,3) -> (4,6)
         elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila+1][self.personaje_columna] == 3 #Revisar si el camino de enfrente del personaje es 3
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila+1][self.personaje_columna] = 0
            #Actualiza la posición del personaje
            self.personaje_fila = self.personaje_fila + 1 
            self.mapa[self.personaje_fila][self.personaje_columna] = 6 #Coloca un personaje_meta donde estaba el camino
    
    def jugar (self) -> None:
        """
        a - izquierda
        d - derecha
        w - arriba
        s - abajo
        """

        while True:
            self.imprimirMapa()
            movimiento = input ("A donde quieres mover tu personaje?")
            if movimiento == "d":
                self.derecha()
            elif movimiento == "a":
                self.izquierda()
            elif movimiento == "w":
                self.arriba()
            elif movimiento == "s":
                self.abajo()
            elif movimiento == "q":
                break

soko = Sokoban ()
soko.jugar()