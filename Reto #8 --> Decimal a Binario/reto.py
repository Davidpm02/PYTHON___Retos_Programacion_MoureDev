#/*
#* Crea un programa se encargue de transformar un número
#* decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#*/



# Para este reto debemos saber como se pasa de un numero decimal a uno en codigo binario.
# Esto se hace cogiendo un numero 'n' y dividiendolo entre dos.
# Hecho esto, nos quedamos con el resto de la division y seguimos diviendo el numero.
# Cuando el numero final sea '1' y lo dividamos entre dos, nos seguraremos de guardar el resto y cesar la operacion.
# Si cojemos ahora todos los restos resultantes en orden inverso (desde el ultimo hasta el primero que nos salio),
# tendremos nuestro numero original en codigo binario.

def dividirNumero(numero):
    resultado = numero // 2
    return resultado


def convertir_a_binario():   
    numero = int(input('Introduzca un numero a convertir en binario:'))
    listaDeRestos = []
    
    try:                                            # El programa hace uso de estructuras condicionales, bloques try: except:
        while True:                                 # y la sentencia assert (usada al principio del bucle while para asegurarnos)
            assert numero != 0                      # de que nuestro numero no es lo suficientemente pequeno como para parar el
            if numero == 1:                         # programa.
                listaDeRestos.append(1)
                raise AssertionError
            elif numero % 2 == 0:
                listaDeRestos.append(0)
                numero = dividirNumero(numero)
                if numero % 2 == 0:
                    listaDeRestos.append(0)
                    numero = dividirNumero(numero)
                elif numero % 2 != 0:
                    listaDeRestos.append(1)
                    numero = dividirNumero(numero)
            elif numero % 2 != 0:
                listaDeRestos.append(1)
                numero = dividirNumero(numero)
                if numero % 2 == 0:
                    listaDeRestos.append(0)
                    numero = dividirNumero(numero)
                elif numero % 2 != 0:
                    listaDeRestos.append(1)
                    numero = dividirNumero(numero)
    except AssertionError:                                               # Cuando se ejecuta el bloque except, se invierte la 
        listaDeRestos.reverse()                                          # la lista de restos, y hacemos uso del metood join para
        cadenaBinario = ''.join(str(numero) for numero in listaDeRestos) # para convertir la lista resultante a cadena.
        return cadenaBinario     # Retornamos la cadena final y ya estaria!
            


if __name__ == '__main__':
    print(convertir_a_binario())
        