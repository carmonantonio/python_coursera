ride_time: 30
ride_distance: 7
cost_per_minute: [0.2, 0.35, 0.4, 0.45]
cost_per_mile: [1.1, 1.8, 2.3, 3.5]
def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
     
    lista = list()
    for x in cost_per_minute:
        val = (x) * float((ride_time)) 
        lista.append(val)
        print(lista)
