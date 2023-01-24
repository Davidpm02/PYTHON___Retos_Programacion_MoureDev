#/*
#* Enunciado: Crea una función que transforme grados Celsius en Fahrenheit
#* y viceversa.
#*
#* - Para que un dato de entrada sea correcto debe poseer un símbolo "°" 
#*   y su unidad ("C" o "F").
#* - En caso contrario retornará un error.
#* - ¿Quieres emplear lo aprendido en este reto?
#*   Revisa el reto mensual y crea una App: 
#*   https://retosdeprogramacion.com/mensuales2022
#*/



def cambiarFormatoTemperatura():
    
        formato = int(input('''Seleccione el tipo de grados que va a introducir:
                            
                            > 1. Celsius  (seleccione '1')
                            > 2. Fahrenheit  (seleccione '2')
                            '''))
        if formato == 1:
            confirmacion = int(input('''Desea convertir grados Celsius a Fahrenheit?
                                    
                                    > 1. SI  (seleccione '1')
                                    > 2. NO  (seleccione '2')
                                    '''))
            if confirmacion == 1:
                gradosCelsius = float(input('Por favor, introduzca los grados en formato Celsuis:'))
                
                gradosTransformados = ((gradosCelsius * 9) / 5) + 32
                print('Se ha realizado la conversion de grados Celsius a grados Fahrenheit.')
                return 'El resultado es: {} grados Celsius equivale a {} grados Fahrenheit.'.format(gradosCelsius,
                                                                                                    round(gradosTransformados,2))
            
            elif confirmacion == 2:
                return ('Se ha anulado la conversion.')
            
            
        elif formato == 2:
            confirmacion = int(input('''Desea convertir grados Fahrenheit a Celsius?
                                    
                                    > 1. SI  (seleccione '1')
                                    > 2. NO  (seleccione '2')
                                    '''))
            if confirmacion == 1:
                gradosFahrenheit = float(input('Por favor, introduzca los grados en formato Fahrenheit:'))
                
                gradosTransformados = (gradosFahrenheit - 32) * 5 / 9  
                print('Se ha realizado la conversion de grados Fahrenheit a grados Celsius.')
                return 'El resultado es: {} grados Fahrenheit equivale a {} grados Celsius.'.format(gradosFahrenheit,
                                                                                                    round(gradosTransformados,2))
            
            elif confirmacion == 2:
                 return 'Se ha anulado la conversion.'
            
            
                
if __name__ == '__main__':
    
    print(cambiarFormatoTemperatura()) 
        