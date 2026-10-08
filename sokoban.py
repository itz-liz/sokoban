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
            [ 2,4,4,3,4,4,2 ],
            [ 2,4,0,1,4,4,2 ],
            [ 2,4,4,4,4,4,2 ],
            [ 2,2,2,2,2,2,2 ]
            ]

        #Definir la psoicion inicial del personaje 
        self.personaje_fila= 4
        self.personaje_columna= 2
        

    
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

        #2 Cuando el personaje es 6 y se desea mover se debe quedar 3 el camino anterior a el y el de enfrente vuelve a ser 0 
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6 # es el estado inical del personaje como esta en la meta ahora es 6
            and self.mapa[self.personaje_fila][self.personaje_columna+1] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje en este caso es 3 porque el personaje estaba en la meta
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            #Actualiza la posición del personaje para la derecha
            self.personaje_columna = self.personaje_columna + 1
            self.mapa[self.personaje_fila][self.personaje_columna] = 0 #Coloca un personaje donde estaba el camino

        #|3. Personaje, meta (0,3) -> (4,6)
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

        #4. personaje empuja caja en camino (0,1,4) -> (4,0,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila][self.personaje_columna+1] == 1 #Revisar si el camino de enfrente del personaje es 1
            and self.mapa[self.personaje_fila][self.personaje_columna+2] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 0
            #Actualiza la posición del personaje
            self.personaje_columna = self.personaje_columna + 1 
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 1 #Coloca una caja donde estaba el camino

        #5. personaje empuja caja en meta (0,1,3) -> (4,0,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila][self.personaje_columna+1] == 1 #Revisar si el camino de enfrente del personaje es 1
            and self.mapa[self.personaje_fila][self.personaje_columna+2] == 3 #Revisar si el camino de enfrente del personaje es 3
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 0
            #Actualiza la posición del personaje
            self.personaje_columna = self.personaje_columna + 1 
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 5 #Coloca una caja_meta donde estaba el camino

        #6. Mover la caja de la meta (0,5,4) -> (4,6,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 # es el estado inical del personaje como esta en la meta ahora es 0
            and self.mapa[self.personaje_fila][self.personaje_columna+1] == 5 #Revisar si el camino de enfrente del personaje es 5
            and self.mapa[self.personaje_fila][self.personaje_columna+2] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje en este caso es 3 porque el personaje estaba en la meta
            self.mapa[self.personaje_fila][self.personaje_columna] = 4    
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 6
            #Actualiza la posición del personaje
            self.personaje_columna = self.personaje_columna + 1 
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 1 #Coloca una caja_meta donde estaba el camino
            
        #7. Mover el personaje de la meta para empujar una caja (6,1,4) -> (3,0,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6 # es el estado inical del personaje como esta en la meta ahora es 6
            and self.mapa[self.personaje_fila][self.personaje_columna+1] == 1 #Revisar si el camino de enfrente del personaje es 1
            and self.mapa[self.personaje_fila][self.personaje_columna+2] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje en este caso es 3 porque el personaje estaba en la meta
            self.mapa[self.personaje_fila][self.personaje_columna] = 3    
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 0
            #Actualiza la posición del personaje
            self.personaje_columna = self.personaje_columna + 1 
            self.mapa[self.personaje_fila][self.personaje_columna+1] = 1 #Coloca una caja_meta donde estaba el camino

        #8. Mover la caja cuando ya esta en la meta y tienen dos metas (6,5,3) -> (3,6,5)


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

        #2. Cuando el personaje es 6 y se desea mover se debe quedar 3 el camino anterior a el y el de enfrente vuelve a ser 0 
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 6 # es el estado inical del personaje como esta en la meta ahora es 6
            and self.mapa[self.personaje_fila][self.personaje_columna-1] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje en este caso es 3 porque el personaje estaba en la meta
            self.mapa[self.personaje_fila][self.personaje_columna] = 3
            #Actualiza la posición del personaje para la izquierda
            self.personaje_columna = self.personaje_columna - 1
            self.mapa[self.personaje_fila][self.personaje_columna] = 0 #Coloca un personaje donde estaba el camino

        #3. Personaje, meta (0,3) -> (4,6)
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
        
        #4. personaje empuja caja en camino (4,0,1) -> (0,1,4)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila][self.personaje_columna-1] == 1 #Revisar si el camino de enfrente del personaje es 1
            and self.mapa[self.personaje_fila][self.personaje_columna-2] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila][self.personaje_columna-1] = 0
            #Actualiza la posición del personaje
            self.personaje_columna = self.personaje_columna - 1 
            self.mapa[self.personaje_fila][self.personaje_columna-1] = 1 #Coloca una caja donde estaba el camino  

       #5. personaje empuja caja en meta (3,1,0) -> (5,0,4)
        elif (
             self.mapa[self.personaje_fila][self.personaje_columna] == 3 
                   and self.mapa[self.personaje_fila][self.personaje_columna-1] == 1 #Revisar si el camino de enfrente del personaje es 1
                   and self.mapa[self.personaje_fila][self.personaje_columna-2] == 0 #Revisar si el camino de enfrente del personaje es 3
               ): #Coloca un camino donde estaba en el personaje 
                   self.mapa[self.personaje_fila][self.personaje_columna] = 5
                   #Coloca un personaje donde estaba el camino
                   self.mapa[self.personaje_fila][self.personaje_columna+1] = 0
                   #Actualiza la posición del personaje
                   self.personaje_columna = self.personaje_columna - 1 
                   self.mapa[self.personaje_fila][self.personaje_columna-1] = 4 #Coloca una caja_meta donde estaba el camino
       #6. Mover la caja de la meta (4,5,0) -> (1,6,4)
       #7. Mover el personaje de la meta para empujar una caja (4,1,6) -> (1,0,3)


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

        #3. Personaje empuja caja en camino (0,1,4) -> (4,0,1)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila-1][self.personaje_columna] == 1 #Revisar si el camino de enfrente del personaje es 1
            and self.mapa[self.personaje_fila-2][self.personaje_columna] == 4 #Revisar si el camino de enfrente del personaje es 4
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 0
            #Actualiza la posición del personaje
            self.personaje_fila = self.personaje_fila - 1 
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 1 #Coloca una caja donde estaba el camino

        #4. personaje empuja caja en meta (0,1,3) -> (4,0,5)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila-1][self.personaje_columna] == 1 #Revisar si el camino de enfrente del personaje es 1
            and self.mapa[self.personaje_fila-2][self.personaje_columna] == 3 #Revisar si el camino de enfrente del personaje es 3
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 0
            #Actualiza la posición del personaje
            self.personaje_fila = self.personaje_fila - 1 
            self.mapa[self.personaje_fila-1][self.personaje_columna] = 5 #Coloca una caja_meta donde estaba el camino



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
    
    
        #3. Personaje empuja caja en camino (4,0,1) -> (0,1,4)
         elif (
                self.mapa[self.personaje_fila][self.personaje_columna] == 0 
                and self.mapa[self.personaje_fila+1][self.personaje_columna] == 1 #Revisar si el camino de enfrente del personaje es 1
                and self.mapa[self.personaje_fila+2][self.personaje_columna] == 4 #Revisar si el camino de enfrente del personaje es 4
            ): #Coloca un camino donde estaba en el personaje 
                self.mapa[self.personaje_fila][self.personaje_columna] = 4
                #Coloca un personaje donde estaba el camino
                self.mapa[self.personaje_fila+1][self.personaje_columna] = 0
                #Actualiza la posición del personaje
                self.personaje_fila = self.personaje_fila + 1 
                self.mapa[self.personaje_fila+1][self.personaje_columna] = 1 #Coloca una caja donde estaba el camino

        #4. personaje empuja caja en meta (0,1,3) -> (4,0,5)
         elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0 
            and self.mapa[self.personaje_fila+1][self.personaje_columna] == 1 #Revisar si el camino de enfrente del personaje es 1
            and self.mapa[self.personaje_fila+2][self.personaje_columna] == 3 #Revisar si el camino de enfrente del personaje es 3
        ): #Coloca un camino donde estaba en el personaje 
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            #Coloca un personaje donde estaba el camino
            self.mapa[self.personaje_fila+1][self.personaje_columna] = 0
            #Actualiza la posición del personaje
            self.personaje_fila = self.personaje_fila + 1 
            self.mapa[self.personaje_fila+1][self.personaje_columna] = 5 #Coloca una caja_meta donde estaba el camino



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