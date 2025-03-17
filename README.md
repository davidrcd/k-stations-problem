# k-stations-problem

# Algoritmo Greedy para Cobertura de Estados

Este repositorio contiene una implementación de un algoritmo voraz (greedy) para seleccionar estaciones de radio de manera que se cubran la mayor cantidad de estados posibles de manera eficiente.

## Descripción del Algoritmo

La función `greedyS_global` recibe como entrada un diccionario de estaciones de radio y los estados que cada una cubre, junto con un conjunto de estados que necesitan ser cubiertos. Su objetivo es seleccionar un subconjunto de estaciones que minimicen la cantidad total de estaciones mientras cubren todos los estados necesarios.

### Funcionamiento del Algoritmo

1. **Inicialización:**
   - Se crea una lista `selected_stations` para almacenar las estaciones seleccionadas.
   - Se usa un conjunto `covered` para rastrear los estados cubiertos.
   - Se crean listas `gradient_data` y `coverage_progress` para registrar la evolución del proceso de selección.

2. **Proceso de Selección:**
   - Mientras `covered` no contenga todos los `states_needed`, el algoritmo itera para seleccionar la mejor estación en cada paso.
   - Se evalúa cada estación y se selecciona aquella que cubra la mayor cantidad de nuevos estados.
   - Se actualizan las estructuras de datos correspondientes y se elimina la estación utilizada del diccionario de estaciones disponibles.

3. **Salida:**
   - Retorna la lista de estaciones seleccionadas.
   - Proporciona el progreso de cobertura a lo largo de las iteraciones.
   - Muestra los valores de ganancia incremental en cada iteración.
   

## Aplicaciones

Este algoritmo es útil para problemas de cobertura en redes, telecomunicaciones y selección de subconjuntos óptimos en diferentes contextos.

---

# Algoritmo de Búsqueda Aleatoria para Cobertura de Estados

Este repositorio contiene una implementación de un algoritmo de selección aleatoria para elegir estaciones de radio con el objetivo de cubrir la mayor cantidad de estados posibles.

## Descripción del Algoritmo

La función `greedyS_local` recibe un diccionario de estaciones de radio y los estados que cada una cubre. En lugar de utilizar una estrategia voraz determinista, selecciona estaciones de manera aleatoria y evalúa si contribuyen a cubrir nuevos estados.

### Funcionamiento del Algoritmo

1. **Inicialización:**
   - Se crea una lista `selected_stations` para almacenar las estaciones seleccionadas.
   - Se usa un conjunto `covered_states` para rastrear los estados cubiertos.
   - Se crea una copia del diccionario `remain_station` para no modificar el original.

2. **Proceso de Selección:**
   - Mientras existan estaciones disponibles, se elige una al azar.
   - Se evalúa cuántos nuevos estados cubre la estación.
   - Si la estación no aporta nuevos estados, se descarta.
   - Si aporta nuevos estados, se agrega a la lista de seleccionadas y se actualiza `covered_states`.
   - Se elimina la estación usada del conjunto de opciones disponibles.

3. **Salida:**
   - Retorna la lista de estaciones seleccionadas.
   - Devuelve el conjunto de estados cubiertos.

## Aplicaciones

Este algoritmo es útil en escenarios donde la aleatoriedad puede ayudar a explorar soluciones diferentes, como en optimización heurística, simulaciones y enfoques de inteligencia artificial.

---




