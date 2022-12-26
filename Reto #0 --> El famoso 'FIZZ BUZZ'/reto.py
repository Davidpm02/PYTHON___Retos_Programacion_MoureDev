#/*
#* Escribe un programa que muestre por consola (con un print) los
# * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#* cada impresión), sustituyendo los siguientes:
#* - Múltiplos de 3 por la palabra "fizz".
#* - Múltiplos de 5 por la palabra "buzz".
#* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#*/
                           # ------------------------------------------------------------------------ #

# Vamos a hacer uso de la funcion range(n),un generador, el cual cuando es usado con dos parametros (range(n,m)),
# va a generar numeros desde 'n' hasta 'm'-1.
# Es por esto que invocamos a la funcion range() con los argumentos n = 1, m = 101; pues el programa debe ser valido
# para los numeros comprendidos entre 1 y 100 (101-1).
def fizzbuzz():
    for item in range(1,101):
        if item % 3 == 0 and item % 5 == 0:                     # Esta condicion debe ir primero; en caso contrario,
            print('Numero',item,'-->','fizzbuzz', end='\n')     # el programa solo tomaria la ruta del primer if coincidente.
        elif item % 3 == 0:
            print('Numero',item,'-->','fizz', end='\n')
        elif item % 5 == 0:
            print('Numero',item,'-->','buzz', end='\n')
        else:
            pass
            
if __name__ == '__main__':
    fizzbuzz()
    