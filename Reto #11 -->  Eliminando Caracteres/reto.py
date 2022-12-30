#/*
#* Crea una función que reciba dos cadenas como parámetro (str1, str2)
#* e imprima otras dos cadenas como salida (out1, out2).
#* - out1 contendrá todos los caracteres presentes en la str1 pero NO
#*   estén presentes en str2.
#* - out2 contendrá todos los caracteres presentes en la str2 pero NO
#*   estén presentes en str1.
#*/

# En el siguiente reto crearemos una funcion en la que destaca el uso del metodo .join() para formar las cadenas 
# 'out1' y 'out2' a partir de unas cadenas pasadas a la funcion al momento de su invocacion.

def funcion(str1, str2):
    new_str1 = []    # Inicializamos unas listas que nos serviran para , segun vayamos recorriendo los strings, introducir
    new_str2 = []    # aquellos valores de str1 que no esten en str2
    
    for letra1 in str1:
        if letra1 not in str2:        # Si en la iteracion del bucle for, el programa encuentra una letra de str1 que no esta
            new_str1.append(letra1)   # en str2, dicha letra se introducira en la primera lista.
            continue
        
    for letra2 in str2:
        if letra2 not in str1:        # Si en la iteracion del bucle for, el programa encuentra una letra de str2 que no esta
            new_str2.append(letra2)   # en str1, dicha letra se introducira en la segunda lista.
        else:
            continue
        
        
    out1 = ''.join(new_str1)
    out2 = ''.join(new_str2)
    
    return '''    > Nueva Palabra 1 --> {}
    > Nueva Palabra 2 --> {}'''.format(out1,
                                       out2)
              
              
              
if __name__ == '__main__':
    print(funcion('cebolla','cebollino'))