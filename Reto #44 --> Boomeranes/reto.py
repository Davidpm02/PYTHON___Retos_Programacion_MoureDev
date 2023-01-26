#/*
#* Enunciado: Crea una función que retorne el número total de bumeranes de 
#* un array de números enteros e imprima cada uno de ellos.
#* - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
#*   seguidos, en el que el primero y el último son iguales, y el segundo
#*   es diferente. Por ejemplo [2, 1, 2].
#* - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] 
#*   y [4, 2, 4]).
#*/



def boomeranes(array):
    """Funcion parametrizada que recibe un array como argumento y es capaz de evaluarlo y segmentarlo en funcion de los elementos
       del propio array.
       
       Parametros:
           - array: lista con numeros enteros, que, en principio, deberia contener algun boomeran (se explica que es un boomeran en
                    el enunciado del problema.) 
    """
    
    conjuntoBoomeran = []   # Inicializo una variable que contiene una lista. En esta lista se iran introduciendo los boomeranes que 
    indice = 0              # el programa encuentre.
    
    try:
        for numero in array:                                    # Recorro todos los numeros del array con un bucle for.
            assert (indice + 2) <= (len(array) - 1)
            if numero == array[indice + 1]:                     # Si el numero de la iteracion es el mismo que el numero siguiente, el indice
                indice +=1                                      # aumenta en uno (el numero intermedio del boomeran debe ser diferente).
            elif numero == array[indice + 2]:                   # En el caso de que el numero de la iteracion sea igual que el del indice (indice + 2),
                conjuntoBoomeran.append(numero)                 # se introducen los tres numeros en cuestion en la lista conjuntoBoomeran (indice,indice + 1, indice + 2)
                conjuntoBoomeran.append(array[indice + 1])
                conjuntoBoomeran.append(array[indice + 2])
                indice +=1
            else:
                indice +=1
                continue
    except AssertionError:
        pass
    
    
    if len(conjuntoBoomeran) < 3:
        return  'En el array {} no contiene ningun boomeran.'.format(array)
        
    
    elif len(conjuntoBoomeran) == 3:
        return  'En el array {} hay 1 boomeran ({}).'.format(array,
                                                            conjuntoBoomeran)
        
   
    elif len(conjuntoBoomeran) > 3:
        indice = 0
        finalBoomeranes = list(range(2,100,3))
        contadorBoomeranes = 0
        for numero in conjuntoBoomeran:
            if indice in finalBoomeranes:
                contadorBoomeranes +=1
                indice +=1
            else:
                indice +=1
         
         
        if contadorBoomeranes == 2:       
            return 'En el array {} hay {} boomeranes : ({} y {}).'.format(array,
                                                                          contadorBoomeranes,
                                                                          conjuntoBoomeran[0:3],
                                                                          conjuntoBoomeran[3:])
        elif contadorBoomeranes > 2:                                # En esta instruccion, hacemos lo mismo que cuando recorrimos el 
            indiceInicial = 0                                       # array argumento.
            indiceFinal = 2
            listaBoomeranes = []                                    # Inicializo una lista que contendra todos los boomeranes.
            print('En el array {} hay {} boomeranes:'.format(array,
                                                             contadorBoomeranes),end=' ')
            try:
                assert indiceFinal < len(conjuntoBoomeran)
                for numero in conjuntoBoomeran:                     # Este bucle for recorre toods los numeros de la variable que creamos al principio.
                    boomeran = []                                   # Por cada numero del bucle, creamos una nueva lista 'boomeran'.
                    if numero == conjuntoBoomeran[indiceFinal]:             # Si se dan las coincidencias, se introducen los numeros en la lista 'boomeran'.
                        boomeran.append(conjuntoBoomeran[indiceInicial])
                        boomeran.append(conjuntoBoomeran[indiceInicial + 1])
                        boomeran.append(conjuntoBoomeran[indiceFinal])
                        indiceInicial +=3                           # Al terminar, se incrementan en 3 los valores de indiceInicial e indiceFinal,
                        indiceFinal +=3                             # y se añade el boomeran encontrado a la lista 'listaBoomeranes'.
                        listaBoomeranes.append(boomeran)
            except:
                return listaBoomeranes          # Una vez que el valor de indiceFinal supera la longitud del array 'conjuntoBoomeran',
                                                # el programa retorna el array 'listaBoomeranes.'
                
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
                
                    
            
                
            
    
    
    
        



if __name__ == '__main__':
    print(boomeranes([4,4,4,3,2,3,5,4,5,6,6,6,5,5,5,4,8,4]))
