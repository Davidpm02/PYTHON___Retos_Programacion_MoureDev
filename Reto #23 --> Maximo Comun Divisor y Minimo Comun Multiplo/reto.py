#/*
#* Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
#* que calcule el mínimo común múltiplo (mcm) de dos números enteros.
#* - No se pueden utilizar operaciones del lenguaje que 
#*   lo resuelvan directamente.
#*/


def mcd(num1,num2):
    """Funcion con dos parametros que calcula el Maximo Comun Divisor de ambos parametros y retorna su valor."""
    maximoDivisor_num1 = []
    
    contador1 = 1
    while contador1 < num1:
        if num1 % contador1 == 0:
            maximoDivisor_num1.append(contador1)
            contador1 +=1                 # Como el numero que guarda la variable contador1 es divisor de num1, la asignamos
            continue                      # su valor a maximoDivisor_num1
        else:
            contador1 +=1
            continue



    maximoDivisor_num2 = []    
    
    contador2 = 1
    while contador2 < num2:
        if num2 % contador2 == 0:
            maximoDivisor_num2.append(contador2)
            contador2 +=1                 # Como el numero que guarda la variable contador2 es divisor de num2, la asignamos
            continue                      # su valor a maximoDivisor_num2
        else:
            contador2 +=1
            continue
        
        
        
  
    divisoresComunes = []    # Inicializo una lista vacia que contendra los divisores en comun
    
    for numero in maximoDivisor_num1:
        for numero2 in maximoDivisor_num2:          # Los divisores que esten en maximoDivisor_num1 y maximoDivisor_num2 se introduciran
            if numero == numero2:                      # en la lista que acabo de crear.
                divisoresComunes.append(numero)
  
    
    resultado = max(divisoresComunes)    # La variable resultado almacena el mayor de todos los valores contenidos en la lista divisoresComunes.
    
    return '{} y {} tienen como maximo comun divisor el numero {}.'.format(num1,num2,resultado)

 # -----------------------------------------------------------------------------------------------------------------------------------#

def mcm(num1,num2):
    """Funcion con dos parametros que calcula el Minimo Comun Multiplo de ambos parametros y retorna su valor."""
    
    minimoMultiplo_num1 = []                        # Inicializo una lista vacia.
     
    for multiplo1 in range(1,20):                   # En un rango de uno 20 numeros, introduzco en la lista vacia el valor resultante 
        minimoMultiplo_num1.append(multiplo1*num1)  # de multiplicar el argumento num1 por el numero del rango en la iteracion
    
    
    minimoMultiplo_num2 = []
    
    for multiplo2 in range(1,20):                   # hago el mismo proceso con num2
        minimoMultiplo_num2.append(multiplo2*num2)
        
        
    multiplosComunes = []                           # Inicializo otra lista vacia, que almacenara los multiplos coincidentes en ambas listas.
    
    for numero in minimoMultiplo_num1:              # Creo un bucle for anidado, en el que se recorren las dos listas que contienen los
        for numero2 in minimoMultiplo_num2:         # resultados de las operaciones.
            if numero == numero2:
                multiplosComunes.append(numero)     # En el caso de que el numero de una lista coincida con el de la otra lista, 
                                                    # inserto dicho numero en la lista vacia 'multiplosComunes'.
                
    resultado = min(multiplosComunes)               # La variable resultado almacena el valor mas pequeno de la lista 'multiplosComunes'.
    
    return '{} y {} tienen como minimo comun multiplo el numero {}'.format(num1,num2,resultado)  # La funcion retorna un string con el resultado.  
        
        
        
if __name__ == '__main__':
    print(mcd(15,20))
    print(mcm(3,4))