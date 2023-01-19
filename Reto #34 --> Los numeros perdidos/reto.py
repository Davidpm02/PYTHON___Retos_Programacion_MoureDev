#/*
#* Enunciado: Dado un array de enteros ordenado y sin repetidos, 
#* crea una función que calcule y retorne todos los que faltan entre
#* el mayor y el menor.
#* - Lanza un error si el array de entrada no es correcto.
#*/


# Numeros-argumento deben estar ordenados
# Numeros-argumento no deben estar repetidos
# Retorna todos los numeros entre el numero mas pequeno y mas grande que falten




class NumerosDesordenados(Exception):
    pass

class NumerosRepetidos(Exception):
    pass

def validacion(listaNumeros):
    """Funcion parametrizada que se encarga de revisar que el argumento pasado en la invocacion de la funcion sea
       valido para la misma."""
        
    contadorNumeros = 0
    
    try:
        for numero in listaNumeros:
            contadorNumeros = listaNumeros.count(numero)
            if contadorNumeros > 1:
                raise NumerosRepetidos
            else:
                contadorNumeros = 0
                continue
            
        
        for numero in listaNumeros:
            if numero > listaNumeros[-1]:
                raise NumerosDesordenados
            
    except NumerosDesordenados:
        print('Los elementos de la lista-argumento estan desordenados.')
        return False
    except NumerosRepetidos:
        print('Algunos elementos de la lista-argumento estan repetidos.')
        return False
    else:
        print('El argumento pasado a la funcion es valido!')
        return True




def numerosPerdidos(listaNumeros):
    """Funcion parametrizada que se encarga de evaluar una lista que recibe como argumento al momento de su invocacion,
       y retorna por pantalla los numeros comprendidos entre el primer elemento del argumento (argumento[0]), y el ultimo
       argumento[-1].
       
       Parametros: 
            - listaNumeros : lista que contienen numeros que seran evaluados por la funcion."""
    
    comprobacion = validacion(listaNumeros)
    if comprobacion == False:
       return 'Por favor, corrige el error y vuelve a intentarlo.'
    elif comprobacion == True:
        
        
        numerosDentro = list(range(listaNumeros[0],listaNumeros[-1]))
        
        for numero in listaNumeros:
            if numero in numerosDentro:
                numerosDentro.remove(numero)
            
        else:
            if len(numerosDentro) == 0:
                return 'La lista-argumento contiene todos los numeros entre el {} y el {}'.format(listaNumeros[0],
                                                                                                  listaNumeros[-1])
            else:
                print('Los numeros perdidos del argumento dado son:')
                return numerosDentro


if __name__ == '__main__':
    print(numerosPerdidos([1,2,5,5,7,8]))
