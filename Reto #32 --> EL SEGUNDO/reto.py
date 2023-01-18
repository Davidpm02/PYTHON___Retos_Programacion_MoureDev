#/*
#* Dado un listado de números, encuentra el SEGUNDO más grande.
#*/


def segundoMasGrande(lista):
    """Funcion parametrizada que evalua el argumento pasado al momento de su invocacion (el argumento debe ser una secuencia)
       y devuelve al usuario el segundo numero mas grande de la misma.
       
       Parametros:
            - lista: es una secuencia que deberia contener numeros, los cuales seran evaluados por la funcion para retornar un 
            resultado acorde.
            
            **Ojo**: si el argumento 'lista' posee como elemento una cadena de texto, el programa no fallara, simplemente evaluara esta
            cadena de acuerdo a la suma total de punto de codigo de las letras que la compongan."""
    
    
    
    numeroMasGrande = max(lista)
    
    for numero in lista:
        if numero == numeroMasGrande:
            lista.remove(numero)
        
    segundoMasGrande = max(lista)
    return 'El segundo numero mas grande de la secuencia-argumento es el {}'.format(segundoMasGrande)
    



if __name__ == '__main__':
    
    lista = [1,3,5,2,7,45,2,98]
    print(segundoMasGrande(lista))
        