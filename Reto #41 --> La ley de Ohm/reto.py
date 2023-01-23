#/*
#* Enunciado: Crea una función que calcule el valor del parámetro perdido
#* correspondiente a la ley de Ohm.
#* - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
#*   el valor del tercero (redondeado a 2 decimales).
#* - Si los parámetros son incorrectos o insuficientes, la función retornará
#*   la cadena de texto "Invalid values".
#*/


def ohm(V = 0, R = 0, I = 0):
    """Funcion parametrizada que evalua los argumentos recibidos durante su invocacion, y devuelve un string con el resultado.
       Para que obtengamos el resultado esperado, la funcion debe recibir UNICAMENTE dos argumentos de los tres parametros que tiene.
       
       Parametros:
           - V : almacena un valor por defecto de 0. Representa el voltaje en la formula de la Ley de Ohm.
           - R : almacena un valor por defecto de 0. Representa la resistencia en la formula de la Ley de Ohm.
           - I : almacena un valor por defecto de 0. Representa la intensidad en la formula de la Ley de Ohm.
    """
    
    
    try:
        assert V == 0 or R == 0 or I == 0
        
        if V == 0:
            voltaje = R * I
            return 'El valor de "V" para los argumentos enviados es de {} voltios.'.format(round(voltaje,2))
        elif R == 0:
            resistencia = V / I
            return 'El valor de "R" para los argumentos enviados es de {} ohmios.'.format(round(resistencia,2))
        elif I == 0:
            intensidad = V / R
            return 'El valor de "I" para los argumentos enviados es de {} amperios.'.format(round(intensidad,2))
        
        
    except AssertionError:
        return 'Para calcular el valor del parametro restante, dicho parametro no debe recibir ningun valor en la invacion de la funcion.'
    except:
        return 'Valores no validos. Por favor, intentelo de nuevo.'    
if __name__ == '__main__':
    print(ohm(R = 6.42, I = 12.18))