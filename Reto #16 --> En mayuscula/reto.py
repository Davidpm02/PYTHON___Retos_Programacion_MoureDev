#/*
#* Crea una función que reciba un String de cualquier tipo y se encargue de
#* poner en mayúscula la primera letra de cada palabra.
#* - No se pueden utilizar operaciones del lenguaje que
#*   lo resuelvan directamente.
#*/


#Este reto nos pide un resultado sin utilizar funciones para resolverlo directamente.

#Es por esto que creo una funcion con un parametro de tipo string. Este string deberia de tener como delimitador
# entre las palabras un espacio en blanco (' ').


def funcion(str):
    #str = input('Escribe una cadena de ecualquier tipo:')  <-- Seria la opcion mas correcta de pedirle al usuario un texto.
    listaString = str.split()  #Con el metodo .split(), cada palabra del string se introducira una por una en listaString.
    
    listaFinal = []  # Inicializamos una lista, que contendra las palabras de listaString pero con la primera letra en mayuscula.
    
    for item in listaString:               # Con un bucle for recorremos los elementos de listaString (osea, cada palabra del
        itemMayuscula = item.title()       # string pasado como argumento). Creamos una copia de cada elemento con la letra 
        listaFinal.append(itemMayuscula)   # inicial en mayuscula y lo anadimos a la lista 'listaFinal'.
        
    resultado = ' '.join(listaFinal)       # Creamos el string que sera devuelto por la funcion con el metodo .join(), indicando
                                           # un espacio en blanco como delimitador === ' '.join(listaFinal) 
    return resultado

if __name__ == '__main__':
    print(funcion('mi sister macarena es la mejor'))