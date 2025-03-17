#Script principal para ejecutar las funciones de búsqueda greedy global y muestreo aleatorio

from greedy_search_global import greedyS_global
from greedy_search_local import greedyS_local

#Definir los estados objetivo y los estados adicionales
states_target = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
extra_states = {
    "nm", "tx", "ok", "ks", "co", "ne", "sd", "wy", "nd", "ia", "mn", "mo", "ar", "la"
}
states_target = states_target | extra_states  # Unir los conjuntos

#Definir estaciones con su cobertura de estados respectiva
radio_stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"},
    "ksix": {"nm", "tx", "ok"},
    "kseven": {"ok", "ks", "co"},
    "keight": {"ks", "co", "ne"},
    "knine": {"ne", "sd", "wy"},
    "kten": {"nd", "ia"},
    "keleven": {"mn", "mo", "ar"},
    "ktwelve": {"la"},
    "kthirteen": {"mo", "ar"},
}

if __name__ == "__main__":
    #Copiar el diccionario para evitar modificaciones en la función, por seguridad más que nada
    stations_copy = radio_stations.copy()
    
    #Ejecutar la búsqueda greedy global
    best_stations, coverage_progress, gradient_data, final_coverage = greedyS_global(stations_copy, states_target)
    
    print("Estaciones seleccionadas:", best_stations)
    print("Estados cubiertos al final:", final_coverage)
    print("Progreso de cobertura estación a estación:", coverage_progress)
    print("Gradientes implicados en cada estación:", gradient_data)
    
    print("------------------------------------------------------------------------------------------------------------------------")

    #Ejecutar el muestreo aleatorio
    random_stations, random_coverage = greedyS_local(radio_stations)
    print("Estaciones seleccionadas aleatoriamente:", random_stations)
    print("Estados cubiertos por las estaciones aleatorias:", random_coverage)
