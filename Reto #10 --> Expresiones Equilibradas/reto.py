#/*
#* Crea un programa que comprueba si los paréntesis, llaves y corchetes
#* de una expresión están equilibrados.
#* - Equilibrado significa que estos delimitadores se abren y cieran
#*   en orden y de forma correcta.
#* - Paréntesis, llaves y corchetes son igual de prioritarios.
#*   No hay uno más importante que otro.
#* - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#* - Expresión no balanceada: { a * ( c + d ) ] - 5 }
#*/

class ExpresionNoBalanceada(Exception):   #Crea una excepcion personalizada, que detendra el programa en caso de que
    pass                                  # se cumplan las condiciones.


def comprobarEquilibrio():   
    """Funcion sin parametros que solicita una expresion por teclado al usuario y la analiza para comprobar 
       si dicha expresion esta equilibrada o no.
    """             
    stringExpresiones = '(){}[]'          # La variable 'stringExpresiones' contiene todas las expresiones que debera analizar el programa.
    expresion = input("Escribe una expresion:") # Esta variable almacena la expresion que el usuario introduzca por teclado
    
    expresion_copia = expresion[:]  # Se crea una copia de la variable 'expresion'
    
    indice = 0  # Inicializamos un contador a 0, que usaremos como valor del indice en 'expresion_copia'.
    
    try:
        for item in expresion:                     # Ejecutamos un bucle for que itere por cada elemento de la expresion.
            indice -=1                             # Por cada iteracion, el contador disminuye su valor en 1 unidad.
            if item not in stringExpresiones:      # Si el elemento de la iteracion no esta dentro del string, se inicia la siguiente iteracion.
                continue                            
            else:
                for item2 in expresion_copia:      # Si el elemento de la iteracion esta dentro del string, se inicia otro bucle for que compruebe 
                    if expresion_copia[indice] not in stringExpresiones:  # Si el elemento de 'expresion_copia' de la nueva iteracion forma o no parte de 'stringExpresiones'
                        continue                                          # En caso de que si se encuentre en el string, y sea su parte contraria (e.g.: '[' --> ']'),
                    else:                                                 # el bucle continuara con la siguiente iteracion
                                                                          
                        if item == ']' or item == '}' or item == ')':     # En casp de que si se encuentre en el string, y NO SEA su parte contraria, se lanzara una llamada al
                            break                                         # error que hemos creado y se terminara nuestro programa.
                        elif item == '[' and expresion_copia[indice] != ']':
                            raise ExpresionNoBalanceada
                        elif item == '(' and expresion_copia[indice] != ')':
                            raise ExpresionNoBalanceada
                        elif item == '{' and expresion_copia[indice] != '}':
                            raise ExpresionNoBalanceada
                        
                        elif item == '[' and expresion_copia[indice] == ']':
                            continue
                        
                        elif item == '(' and expresion_copia[indice] == ')':
                            continue
                        
                        elif item == '{' and expresion_copia[indice] == '}':
                            continue             
        else:                                        # En el caso de que el bucle for principal termine todas sus iteraciones sin haberse generado ningun error,   
            return 'La expresion esta balanceada.'   # la funcion terminara retorando un string por pantalla de que la expresion si estaba balanceada.
        
    except ExpresionNoBalanceada:
        return 'La expresion no esta balanceada.'
    except:
        return 'Ha ocurrido un error al realizar la comprobacion. Por favor, intentalo de nuevo.'
                
if __name__ == '__main__':
    print(comprobarEquilibrio())
        
    