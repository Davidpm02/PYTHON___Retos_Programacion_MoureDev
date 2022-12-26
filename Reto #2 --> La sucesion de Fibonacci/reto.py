#/*
#* Escribe un programa que imprima los 50 primeros números de la sucesión
#* de Fibonacci empezando en 0.
#* - La serie Fibonacci se compone por una sucesión de números en
#*   la que el siguiente siempre es la suma de los dos anteriores.
#*   0, 1, 1, 2, 3, 5, 8, 13...
#*/


def sucesionFibonacci():
    num1 = num2 = 1
    numDevuelto = 0
    
    for num in range(1,51):    #Utilizamos la funcion range() de Pytohn con dos parametros para delimitar un inicio y un final.
        if num1 == 1 and num2 == 1:  # Si num1 y num2 son ambos == 1, los imprimimos y asignamos la suma de ambos a numDevuelto.
            print(str(num1) + '\n')  # Imprimimos numDevuelto y modificamos num1 asignandole el valor de num2, 
            print(str(num2) + '\n')  # y num2 asignandole el valor de numDevuelto
            numDevuelto = num1 + num2
            print(str(numDevuelto) + '\n')
            num1 = num2
            num2 = numDevuelto
        else:                               # Cuando no se cumpla la condificion del if (nunca se cumple pasada la primera iteracion)
            numDevuelto = num1 + num2       # asignaremos a numDevuelto la suma de num1 y num2,
            num1 = num2                     # y modificaremos los valores de sum1 y sum2 igual que antes (desplazamos los valores)
            num2 = numDevuelto              # num1 = num2, num2 = numDevuelto
            print(str(numDevuelto) + '\n')
            
            
        

if __name__ == '__main__':
    sucesionFibonacci()