import random

def greedyS_local(stations):
    """
    Algoritmo de seleccion aleatoria de estaciones de radio
    para cubrir la mayor cantidad de estados posibles.
    """
    selected_stations = [] #Lista para almacenar las estaciones seleccionadas
    covered_states = set() #Conjunto para almacenar los estados cubiertos
    remain_station = stations.copy() #Copia para no modificar el original, por seguridad
    
    while remain_station:
        #Eleccion de una estación aleatoria
        station = random.choice(list(remain_station.keys()))
        #calculo para saber cuantos estados nuevos cubre
        new_coverage = remain_station[station] - covered_states

        #Si la estación no cubre nuevos estados, la eliminamos y seguimos
        if not new_coverage:
            del remain_station[station]
            continue

        #Agregamos la estación y actualizamos los estados cubiertos
        selected_stations.append(station)
        covered_states.update(remain_station[station])
        del remain_station[station]

    return selected_stations, covered_states