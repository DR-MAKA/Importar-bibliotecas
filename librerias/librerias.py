# calcular la mediana, la media de los datos almacenados en una lista de 100 elementos
# la lsita debe llenarse de elementos aleatorios de -100 a 100

from random import sample
import random
from numpy import float64
import pandas as pd 

#genera los numeros aleatorios del en un rango del -100 al 100 y a su vez toma 100 elemntos 
#aleatorios dentro de ese rago para operarlos

aleatorios= random.sample(range(-100,100),100)

#para poder calcular la media y la mediiana transformamos la lista aleatorios en unn  DataFrame
#axis=1 se usa para tomar o usar los datos de el DataFrame

jp=pd.DataFrame([aleatorios])
mediana=float64(jp.median(axis=1))
media=float64(jp.mean(axis=1))


print(mediana)
print(media)

print(aleatorios)