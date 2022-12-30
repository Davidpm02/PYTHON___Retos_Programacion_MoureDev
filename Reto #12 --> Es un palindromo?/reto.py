#/*
#* Escribe una función que reciba un texto y retorne verdadero o
#* falso (Boolean) según sean o no palíndromos.
#* Un Palíndromo es una palabra o expresión que es igual si se lee
#* de izquierda a derecha que de derecha a izquierda.
#* NO se tienen en cuenta los espacios, signos de puntuación y tildes.
#* Ejemplo: Ana lleva al oso la avellana.
#*/

# En este reto (y con objeto de modularizacion) he creado dos funciones auxilizares con respecto a la funcion principal
# con la que podremos 'moldear' el texto dado como argumento a nuestro gusto.

# La funcion invertirCadena() tiene como parametro una cadena, la cual va a invertir y nos la va a devolver.

def invertirCadena(cadena):
    return cadena[::-1]


# La funcion normalizarTexto() toma como parametro una cadena, y nos va a devolver una copia de esta cadena pero:
# Sin caracteres especiales.
# Con todos los elementos normalizados a minuscula

def normalizarTexto(texto):
    try:
        listaTexto = []
        textoNormalizado = texto.lower()
        
        for letra in textoNormalizado:
            if letra not in ' ,.!/':
                listaTexto.append(letra)
            else:
                pass
        
        stringNormalizado = ''.join(listaTexto)
        
        return stringNormalizado
    
    except AssertionError:
        print('Se requiere introducir una cadena como argumento.')
        
        
        
def funcion(texto):
    texto_normalizado = normalizarTexto(texto)
    
    texto2 = invertirCadena(texto)     # Creamos un segundo texto que contenga la cadena pasada como argumento, pero en 
    texto2_normalizado = normalizarTexto(texto2) # sentido inverso.
    
    contadorInicial = 0   # Inicializamos unos contadores que usaremos como indices
    contadorFinal = 0
    
    for letraInicial in texto_normalizado:     # En la funcion haremos uso de dos bucles for anidados para comparar
        for letraFinal in texto2_normalizado:  # los indices de los dos textos.
            if texto_normalizado[contadorInicial] == texto2_normalizado[contadorFinal]:
                contadorInicial +=1
                contadorFinal +=1              # Si los valores de ambos indices son iguales, se sumara '1'
                break                          # al valor de los contadores y rompemos el 2do bucle.
            else:
                return False
    else:                            # Si terminamos todas las iteraciones del primero bucle for sin darse la condicion
        return True                  # 'texto_normalizado[contadorInicial] != texto2_normalizado[contadorFinal]',
                                     # el programa acabara y devolvera el valor booleano 'True'.
                               
                        
if __name__ == '__main__':
    print(funcion('Ana lleva al oso la avellana'))