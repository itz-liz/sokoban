# sokoban

Parxticas de Fundamentos de ia

Este es un juego de sokoban hecho en Python. La idea es mover al personaje y empujar
las cajas hasta las metas. Cuando todas las cajas estan en una meta aparece:

```text
felicidades juego terminado
```

## Como esta hecho el mapa

El mapa esta guardado en `self.mapa` como una lista de listas. Cada lista de adentro
es una fila y cada numero dentro de esa fila es una columna.

Los numeros significan esto:

```text
0 - personaje
1 - caja
2 - pared
3 - meta
4 - camino
5 - caja_meta
6 - personaje_meta
```

La fila sirve para saber si algo esta arriba o abajo y la columna sirve para saber
si algo esta a la izquierda o a la derecha.

Por ejemplo:

```python
self.mapa[fila][columna]
```

Para movernos a la derecha se deja igual la fila y se aumenta la columna:

```python
self.mapa[self.personaje_fila][self.personaje_columna+1]
```

Para movernos a la izquierda se deja igual la fila y se resta una columna:

```python
self.mapa[self.personaje_fila][self.personaje_columna-1]
```

Para arriba se resta una fila y para abajo se aumenta una fila. Esto se hace asi
porque en una lista de Python las posiciones de las filas empiezan desde arriba y
las columnas van de izquierda a derecha.

## Inicio del juego

La clase `Sokoban` guarda todo lo del juego.

En `__init__` se arma el mapa y se pone al personaje en su posicion inicial:

```python
self.personaje_fila = 4
self.personaje_columna = 2
```

El mapa tiene paredes alrededor para que el personaje no se salga.

## Mostrar el mapa

La funcion `imprimirMapa` recorre cada fila con un `for` y la imprime en la
consola. Por eso el mapa se ve como varias listas de numeros.

## Movimientos

Hay una funcion para cada direccion:

```text
derecha()  - mueve a la derecha
izquierda() - mueve a la izquierda
arriba()   - mueve hacia arriba
abajo()    - mueve hacia abajo
```

Cada funcion revisa que hay en la posicion de enfrente antes de cambiar el mapa.
Primero revisa si hay camino o una meta. Si se puede caminar, cambia el lugar
anterior por camino y coloca al personaje en el nuevo lugar.

Cuando el personaje estaba en una meta, se usa el numero `6`. Al salir de ahi,
esa posicion vuelve a ser una meta con el numero `3`, para no perder la meta.
Lo mismo pasa cuando el personaje llega a otra meta.

## Empujar cajas

Para empujar una caja no basta con revisar una sola posicion. Se revisan dos:

```text
personaje - caja - espacio libre
```

El espacio despues de la caja tiene que ser camino o meta. Si ese espacio esta
libre, la caja avanza una posicion y el personaje ocupa el lugar donde estaba
la caja.

Cuando una caja llega a una meta cambia de `1` a `5`, que significa `caja_meta`.
Si una caja sale de una meta vuelve a ser `1`, y la meta queda disponible otra
vez como `3`.

Las condiciones se escribieron dentro de cada movimiento porque no todos los
casos son iguales. Hay casos para:

- personaje caminando por el camino
- personaje entrando o saliendo de una meta
- personaje empujando una caja en el camino
- personaje empujando una caja hacia una meta
- personaje moviendo una caja que ya estaba en una meta

## Como se juega

La funcion `jugar` mantiene el juego corriendo con un `while True`. En cada vuelta:

1. imprime el mapa
2. pide una tecla
3. llama a la funcion del movimiento
4. revisa si ya se gano

Las teclas son:

```text
a - izquierda
d - derecha
w - arriba
s - abajo
q - salir del juego
```

## Revisar si se gano

La funcion `verificar_ganado` busca si todavia existe alguna caja normal, o sea,
un `1`, dentro de cualquier fila.

Si ya no encuentra ningun `1`, quiere decir que todas las cajas estan en metas,
porque las cajas que estan en metas son `5`. En ese momento imprime el mensaje
de felicitacion y devuelve `True`.

Cuando devuelve `True`, el `break` termina el `while` de `jugar` y se acaba la
partida.

## Ejecutar

Desde la carpeta del proyecto se ejecuta:

```bash
python sokoban.py
```

Despues solo se escriben las teclas de movimiento en la consola.
