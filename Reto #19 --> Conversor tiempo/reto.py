#/*
#* Crea una función que reciba días, horas, minutos y segundos (como enteros)
#* y retorne su resultado en milisegundos.
#*/

def conversorTiempo(dias,horas,minutos,segundos):   # La uncion creada recibira como argumentos los valores correspondientes a estos 4 parametros.
    
    tiempoTotal = 0                                 # Inicializamos el tiempo inicial a 0 segundos.
    tiempoTotal += dias*(3600*24*1000)              # Iremos aumentando el valor de tiempoTotal en funcion del valor del parametro
    tiempoTotal += horas*(3600*1000)                # multiplicado por los milisegundos en cuestion.
    tiempoTotal += minutos*(60*1000)
    tiempoTotal += segundos*1000
    
    return 'En el tiempo introducido, han transcurrido {} milisegundos.'.format(tiempoTotal)   # Finalmente, hacemos que la funcion retorne un string
                                                                                               # con el resultado final.
if __name__ == '__main__':
    print(conversorTiempo(0,0,0,1))
    