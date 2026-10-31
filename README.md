# Proyecto Sokoban

Este repositorio contiene dos versiones de un juego de Sokoban desarrollado en
Python como práctica de fundamentos de inteligencia artificial:

- `sokobanv2.py`: versión manual de un nivel.
- `sokobanv3.py`: versión automática con cuatro niveles y búsqueda de caminos.

## Representación de los mapas

Cada archivo `nivel*.txt` contiene una matriz de números. Cada carácter
representa una casilla:

```text
0 - personaje
1 - camino
2 - pared
3 - salida
4 - personaje sobre la salida
```

La versión actual utiliza exclusivamente `0` para el personaje. Las filas
representan la posición vertical y las columnas la posición horizontal.

Los niveles incluidos son:

```text
nivel1.txt
nivel2.txt
nivel3.txt
nivel4.txt
```

Cada nivel debe contener un personaje `0`, una salida `3`, casillas de camino
`1` y paredes `2`.

## `sokobanv2.py`: juego manual

`sokobanv2.py` es la primera versión funcional del juego. Carga únicamente
`nivel1.txt` al crear el objeto `Sokoban` y permite que el usuario controle el
personaje desde la consola.

### Carga del mapa

El constructor:

1. abre `nivel1.txt`;
2. lee cada línea;
3. convierte los caracteres en números;
4. guarda el resultado en `self.mapa`;
5. busca la fila y columna iniciales del personaje.

Esta versión identifica al personaje con el número `8`, porque conserva el
formato original de la práctica. Por ello, `sokobanv2.py` es independiente de
la versión automática y no debe confundirse con el formato actual de
`sokobanv3.py`.

### Movimiento manual

El método `mover_personaje` recibe un cambio de fila y columna. Antes de mover
el personaje valida que:

- el destino esté dentro del mapa;
- el destino sea camino `1` o salida `3`;
- las paredes no puedan atravesarse.

Cuando el personaje abandona una casilla, esta vuelve a ser camino. Si abandona
la salida, la salida se conserva como `3`. Cuando llega a la salida, el
personaje se representa temporalmente con `4` y la partida termina.

### Controles

Al ejecutar el archivo, el método `jugar` muestra el mapa y solicita una tecla
en cada vuelta:

```text
w - arriba
s - abajo
a - izquierda
d - derecha
q - salir
```

Una tecla distinta muestra un mensaje de movimiento inválido. Esta versión no
busca caminos automáticamente, no usa azar, no cuenta pasos y no cambia entre
niveles.

## `sokobanv3.py`: solucionador automático

`sokobanv3.py` es la versión automática del proyecto. Lee un nivel, encuentra
al personaje `0`, busca una ruta hasta la salida `3` y reproduce la solución en
la consola.

### Carga y validación

El constructor recibe el nombre del archivo, por defecto `nivel1.txt`.
`_leer_mapa` convierte el archivo en una lista de listas de enteros y rechaza
los niveles vacíos. `reiniciar` copia el mapa original, pone el contador en
cero y localiza el personaje.

El personaje es únicamente el número `0`; el número `8` no es válido en esta
versión. Si un nivel no tiene `0`, se lanza:

```text
ValueError: El nivel debe tener un personaje.
```

### Movimiento y contador

`mover_personaje` valida el destino y actualiza la posición. Cada movimiento
válido aumenta `contador_pasos` en uno. El método también conserva la salida
cuando el personaje sale de ella y marca `juego_terminado` al alcanzar `3`.

Durante la reproducción se muestra:

```text
Camino encontrado: N pasos.
Paso 0:
...
Paso 1:
...
```

Se imprime una línea en blanco entre mapas para separar visualmente cada paso.

### Mano derecha y azar

El método `_movimientos_desde` ordena las alternativas siguiendo la regla de
la mano derecha:

1. derecha;
2. frente;
3. izquierda;
4. atrás.

En cada intersección se utiliza `random.choices` para seleccionar una opción,
pero las opciones prioritarias tienen mayor peso. La semilla opcional permite
repetir el mismo comportamiento aleatorio.

### Retroceso y mejor camino

`_intentar_resolver` mantiene una pila de ramas exploradas. Si una ruta queda
bloqueada, retrocede y prueba otra alternativa. También guarda las posiciones
visitadas para evitar ciclos dentro del intento.

`resolver_automaticamente` ejecuta varios intentos, conserva el camino más
corto encontrado y después reproduce ese camino desde el estado inicial.
Sus parámetros principales son:

```python
resolver_automaticamente(
    intentos=100,
    max_pasos=None,
    pausa=0.1,
    semilla=None,
)
```

- `intentos`: cantidad de búsquedas independientes.
- `max_pasos`: límite de pasos de cada intento.
- `pausa`: segundos entre mapas impresos.
- `semilla`: valor opcional para reproducir el azar.

### Cambio entre niveles

`jugar_niveles` procesa automáticamente, en este orden:

```text
nivel1.txt
nivel2.txt
nivel3.txt
nivel4.txt
```

Después de resolver cada nivel, pregunta:

```text
¿Deseas pasar al siguiente nivel :D? (s/n):
```

Se aceptan `s`, `si` y `sí`. Cualquier otra respuesta detiene el juego. Al
resolver el cuarto nivel se muestra un mensaje indicando que todos fueron
completados.

## Ejecución

Desde la carpeta del proyecto:

```bash
python3 sokobanv2.py
```

Ejecuta la versión manual.

```bash
python3 sokobanv3.py
```

Ejecuta el solucionador automático y permite avanzar por los cuatro niveles.
