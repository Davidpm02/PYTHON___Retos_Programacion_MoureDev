#/*
#* Enunciado: Crea un función que reciba un texto y retorne la vocal que
#* más veces se repita.
#* - Ten cuidado con algunos casos especiales.
#* - Si no hay vocales podrá devolver vacío. 
#*/



def comprobarMasGrande(listaNumeros):
    '''Funcion parametrizada que recibe un array como argumento y retorna el elemento mas grande del mismo.
    
    Parametros
        - listaNumeros: array que debe estar compuesto por enteros. En el caso de que contenga algun string, la funcion evaluara 
                        la suma total del punto de codigo de sus letras.
    '''
    
    
    masGrande = max(listaNumeros)
    
    return masGrande

def contarVocales():
    '''Funcion sin parametros que solicita al usuario un texto por teclado y devuelve por pantalla la vocal que mas veces
       se ha repetido en dicho texto.
    '''
    
    
    texto = input('Escriba cualquier cosa:')
    texto = texto.lower()  # Normalizo el texto para ahorrarnos algo de codigo
    
    
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    
    
    for letra in texto:
        if letra == 'a':
            a +=1
        elif letra == 'e':
            e +=1
        elif letra == 'i':
            i +=1
        elif letra == 'o':
            o +=1
        elif letra == 'u':
            u +=1
            
    
    listaVocales = [a,e,i,o,u]
    masRepetida = max(a,e,i,o,u)  # No se imprime la letra, se impreme el numero de repeticiones de la letra mas repetida.

    if masRepetida == listaVocales[0]:
        return 'La vocal mas repetida es la "a" (se ha repetido un total de {} veces).'.format(masRepetida)
    elif masRepetida == listaVocales[1]:
        return 'La vocal mas repetida es la "e" (se ha repetido un total de {} veces).'.format(masRepetida)
    elif masRepetida == listaVocales[2]:
        return 'La vocal mas repetida es la "i" (se ha repetido un total de {} veces).'.format(masRepetida)
    elif masRepetida == listaVocales[3]:
        return 'La vocal mas repetida es la "o" (se ha repetido un total de {} veces).'.format(masRepetida)
    elif masRepetida == listaVocales[4]:
        return 'La vocal mas repetida es la "u" (se ha repetido un total de {} veces).'.format(masRepetida)
    else:
        return 'Por favor, vuelve a intentarlo.'


if __name__ == '__main__':
    
    print(contarVocales())
    
            
        