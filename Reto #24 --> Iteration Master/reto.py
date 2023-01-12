#/*
#* Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
#* ¿De cuántas maneras eres capaz de hacerlo?
#* Crea el código para cada una de ellas.
#*/

# Forma numero 1
# Es la forma menos eficiente, pues consistiria en ir imprimiendo cada numero manualmente uno por uno.
print('CONTAR DEL 1 AL 100:')
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
print('Uno por uno hasta el 100...')
print('',end='\n')


# Forma numero dos
# La segunda forma consiste en crear una lista de los numeros del 1 al 100, e iterar sobra cada uno de estos numeros es un bucle for.

numeros100 = list(range(1,101))   # El segundo argumento de range es 101 y no 100, porque la funcion range actua empezando desde el
for numero in numeros100:         # valor del primer argumento, hasta el segundo argumento -1.
    print(numero)                 # range(n,m-1)
    
print('',end='\n')
# Forma numero tres
# La tercera forma consiste en ejecutar el bucle for directamente desde el generador range, e ir iterando cada numero uno por uno.

for num in range(1,101):
    print(num)
    
print('',end='\n')
