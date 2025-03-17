
def greedyS_global(stations, states_needed):
    selected_stations = [] #Lista de estaciones seleccionadas
    covered = set() #Conjunto de estados cubiertos
    gradient_data = [] 
    coverage_progress = []

    #Bucle que permite seguir iterando hasta que se cubran todos los estados necesarios
    while covered < states_needed:
        top_station = None 
        max_gain = 0
        
        #Evaluar cada estación y ver cuántos estados nuevos cubre
        #Se selecciona la estación con mayor ganancia
        for station, coverage in stations.items():
            new_coverage = coverage - covered
            if len(new_coverage) > max_gain:
                top_station, max_gain = station, len(new_coverage)
        
        #Si se encontró una estación que cubre nuevos estados, se agrega a la lista y se actualiza el conjunto de estados cubiertos
        if top_station:
            selected_stations.append(top_station)
            covered.update(stations[top_station])
            gradient_data.append(max_gain)
            coverage_progress.append(len(covered))
            del stations[top_station]  #Eliminar la estación usada
    
    return selected_stations, coverage_progress, gradient_data, covered