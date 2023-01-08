#/*
#* Crea una función que reciba dos array, un booleano y retorne un array.
#* - Si el booleano es verdadero buscará y retornará los elementos comunes
#*   de los dos array.
#* - Si el booleano es falso buscará y retornará los elementos no comunes
#*   de los dos array.
#* - No se pueden utilizar operaciones del lenguaje que
#*   lo resuelvan directamente.
#*/

def funcion(lista1,lista2,bool):
    """Funcion con tres parametros que devuelve un valor u otro en base al valor del parametro 'bool'.
    
       Parametros:
       - lista1 : Lista que contiene una serie de elementos (estos no tienen porque ser del mismo tipo.)
       - lista2 : Lista que contiene una serie de elementos (estos no tienen porque ser del mismo tipo.)
       - bool : Valor booleano que decidira la ruta del programa en funcion de si almacena True o False.
       
        El enuncia pide que retorne un solo array. En mi caso, he modificado un poco la salida del programa.
        Cuando se ejecute la funcion, esta imprimira por pantalla dos cadenas con las listas de elementos acordes
        al valor almacenado en el parametro 'bool'.
    """
    try:
        assert bool == True or bool == False
        if bool == True:
            listaCoincidencias = []
            listaCoincidencias2 = []
            for item1 in lista1:
                if item1 in lista2:
                    listaCoincidencias.append(item1)
            else:
                print()
                print('Elementos del array 1 que SI estan en el array 2:{}'.format(listaCoincidencias))
            for item2 in lista2:
                if item2 in lista1:
                    listaCoincidencias2.append(item2)
            else:
                print('Elementos del array 2 que SI estan en el array 1:{}'.format(listaCoincidencias2))
                print()
        elif bool == False:
            listaCoincidencias = []
            listaCoincidencias2 = []
            for item1 in lista1:
                if item1 not in lista2:
                    listaCoincidencias.append(item1)
            else:
                print()
                print('Elementos del array 1 que NO estan en el array 2:{}'.format(listaCoincidencias))
            for item2 in lista2:
                if item2 not in lista1:
                    listaCoincidencias2.append(item2)
            else:
                 print('Elementos del array 2 que NO estan en el array 1:{}'.format(listaCoincidencias2))
                 print()
                    
                
    except AssertionError:
        print('XXX No se puede realizar ninguna operacion con el valor booleano especificado. ')
        
    


if __name__ == '__main__':
    lista1 = ['comida','pelo','coche']
    lista2 = [1,45,'comida']
    funcion(lista1,lista2,True)