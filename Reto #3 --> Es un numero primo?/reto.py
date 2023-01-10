#/*
#* Escribe un programa que se encargue de comprobar si un número es o no primo.
#* Hecho esto, imprime los números primos entre 1 y 100.
#*/
class EsPrimo(Exception):
    pass

class NoPrimo(Exception):
    pass




def comprobarPrimo():
    """Funcion sin parametros que se encarga de comprobar que numeros son primos y cuales no de una lista de numeros del 2 al 100.
    
       Este funcion utiliza una estructura try: except: para el control de excepciones, pues vamos a provocar una excepcion u otra
       en funcion del resultado de las operaciones del cuerpo de la funcion."""
       
       
    listaNumeros = list(range(2,101))  # Como el numero 1 no se considera numero primo ,el primer numero de nuestra lista sera el 2.
    for x in listaNumeros:             # Iniciamos un bucle for que iterre por cada numero que compone la lista.
        listaNueva = listaNumeros[:]   # Al principio de cada iteracion, creamos una lista que contenga todos los elementos de listaNumeros.
        try:
            assert x <= 100            # Si el numero de la iteracion es menor o igual a 100, el programa seguira su transcurso, en caso contrario,
            listaNueva.remove(x)       # se ejecutara el bloque except: del AssertionError.

            for numero in listaNueva:  # Iteramos por cada numero de la numero lista, comprobando si la division del numero de la iteracion principal (x)
                if x % numero == 0 :   # es o no divisible por el numero de la iteracion de la nueva lista. 
                    raise NoPrimo      # En funcion del resultado, el programa toda un camino u otro.
                elif x % numero != 0:
                    continue
            else:
                raise EsPrimo
        except AssertionError:
            print('FIN')
            
        except NoPrimo:
            print(x,'---> No es primo.')
            
        except EsPrimo:
            print(x,' ---> Es primo.')
            
            
        
            
    
if __name__ == '__main__':
    comprobarPrimo()