#/*
#* Crea una función que reciba un texto y muestre cada palabra en una línea,
#* formando un marco rectangular de asteriscos.
#* - ¿Qué te parece el reto? Se vería así:
#*   **********
#*   * ¿Qué   *
#*   * te     *
#*   * parece *
#*   * el     *
#*   * reto?  *
#*   **********
#*/

def texto_en_marco():
    """Funcion sin parametros que solicita al usuario un texto por teclado, para despues imprimirlo dentro de un marco.
       Este marco se compone del caracter '*', y el tamano del marco en cuestion dependera de la longitud de la palabra
       mas grande del texto introducido por el usuario.
    """
    
    texto = input('Por favor, escriba el texto a enmarcar:')
    
    listaPalabras = texto.split()             # Inserto todas las palabras del string 'texto' en una lista (uso un espacio como delimitador!)
    listalongitudes = []   
    
    for palabrita in listaPalabras:
        listalongitudes.append(len(palabrita))
        
    
    palabraMasLarga = max(listalongitudes)    # Esta variable almacena el valor mas alto de las longitudes de las palabras.
    
    
    
    separador = '*'*(palabraMasLarga + 4)  # Este valor '4' representa: 1ro) Para el '*' inicial del lado del marco.
    print(separador)                                                 #  2do) Para un espacio entre el '*' inicial y la palabra
    for palabra in listaPalabras:                                    #  3ro y 4to) Igual que 1ro) y 2do), pero al final de la palabra.
        string = '*' + ' ' + palabra +(' '*(len(separador) - len(palabra) - 3))+'*'  # El valor '3' es debido a que anadimos un '4' a la hora
        print(string)                                                                # de crear el delimitador, pero 1 representa el espacio
                                                                                     # entre el '*' inicial y la palabra.
    else:
        print(separador)

if __name__ == '__main__':
    texto_en_marco()