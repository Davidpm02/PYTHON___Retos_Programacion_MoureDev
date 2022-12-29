#/*
#* Crea un programa que cuente cuantas veces se repite cada palabra
#* y que muestre el recuento final de todas ellas.
#* - Los signos de puntuación no forman parte de la palabra.
#* - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#* - No se pueden utilizar funciones propias del lenguaje que
#*   lo resuelvan automáticamente.
#*/

# En este reto hago uso del metodo integrado de Python .split().
# El usuario introducira una oracion al inicio del programa, y esta oracion se dividira en una lista.
# El metodo .split() sin parametros toma como delimitador un espacio (' ') para introducir cada para en la lista.
def contarPalabras(oracion):
    oracionLowercase = oracion.lower()
    
    
    
    listaPalabras = oracionLowercase.split()
    palabras_Comprobar = oracionLowercase.split()
    for palabra in listaPalabras:                              # Se va a iniciar un contador en 0, que ira sumando segun se
        contador = 0                                           # adviertan casualidades en el siguiente bucle for.
        for comprobacion in palabras_Comprobar:
            if palabra == comprobacion:
                contador +=1     
            if comprobacion == palabras_Comprobar[-1]:         # Cuando el bucle llega al final de la lista, se imprime 
                print('{} --> {} repeticiones.'.format(palabra,# por pantalla el resultado.
                                                       contador))
            
    


if __name__ == '__main__':
    oracion = input('Escribe una oracion (con las palabras separadas por espacios!):')
    print('\n'*2)
    contarPalabras(oracion)
    print('\n'*2)
    