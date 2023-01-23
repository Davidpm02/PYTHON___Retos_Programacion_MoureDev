#/*
#* Enunciado: Crea un programa se encargue de transformar un número binario
#* a decimal sin utilizar funciones propias del lenguaje que 
#* lo hagan directamente.
#*/


def conversor(num_binario):
    """Funcion parametrizada que evalua el argumento pasado durante su invocacion, y retorna un resultado en funcion del valor
       de dicho argumento.
       
       Parametros:
           - num_binario : es un numero en codigo binario que , tras ser evaluado por la funcion, sera devuelto en forma de numero
                           decimal.
    """
    
    
    str_num_binario = str(num_binario)         # Esta variable me copia el numero binario de argumento como string,
                                               # lo que me permite iterar sobre el.
                                               
    contadorExponente = 0               
    longitudNumBinario = len(str_num_binario)
    
    valorNumeroDecimal = 0                     # Inicialimos una variable que almacena un valor, el cual se va aumentando por cada
                                               # iteracion hasta contener el numero decimal equivalente al numero binario pasado como
    listaResultados = []                       # argumento.
    
    for num in range(longitudNumBinario):
        
        listaResultados.append(2**contadorExponente)
        contadorExponente +=1
    
    else:
        try:
            indice = 0
            listaResultados.reverse()
            
            while indice <= len(listaResultados) and indice <= len(str_num_binario):
                for numero in listaResultados:
                    for numero2 in str_num_binario:                 # Anido dos bucles for, quqe recorreran tanto los resultados de 
                                                                    # los cuadrados, como el string que contiene el argumento en binario.
                        if str_num_binario[indice] == '1':          # Si una 'letra' del string binario es == 1, se actualizara la variable
                            valorNumeroDecimal += numero            # 'valorNumeroDecimal' con el numero que haya en el  mismo indice de los resultados 
                            indice +=1                              # de los cuadrados.
                            break
                        elif str_num_binario[indice] == '0':        # Si una 'letra' del string binario es == 0, se aumentara el indice y se pasara al siguiente
                            indice +=1                              # elemento en la iteracion.
                            break
                        
                else:
                    return "El número '{}' en binario es el equivalente al número '{}' en decimal.".format(num_binario,        # Al terminar el bucle for principal, 
                                                                                                           valorNumeroDecimal) # la funcion se dentendra y retornara un string
        except AssertionError:                                                                                                 # con el resultado.
            print('Ha ocurrido un error al convertir el numero a decimal.')
            return 'Por favor, intentalo de nuevo.'
        
    
        
        



if __name__ == '__main__':
    
    print(conversor(1111))