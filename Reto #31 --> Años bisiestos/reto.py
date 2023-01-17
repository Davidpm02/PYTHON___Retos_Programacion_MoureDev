#/*
#* Crea una función que imprima los 30 próximos años bisiestos
#* siguientes a uno dado.
#* - Utiliza el menor número de líneas para resolver el ejercicio.
#*/


def comprobarBisiesto(lista):
    """Funcion parametrizada que evalua los elementos que componen el parametro y retorna un resultado u otro segun cada
       elemento del parametro.
       
       Parametros:
           - lista: es un array cuyos elementos representan cifras de años a evaluar.
           
    """
    
    for anio in lista:
        if anio % 4 == 0:
            print('Año {} --> Bisiesto'.format(anio))
        else:
            print('Año {} --> No bisiesto'.format(anio))
            
if __name__ == '__main__':
    listaAnios = list(anio for anio in range(2023,2023+31)) # Utilizo '2023 + 31' como limite superior del rango por la forma
                                                            # en la que funciona range()

    comprobarBisiesto(listaAnios)


