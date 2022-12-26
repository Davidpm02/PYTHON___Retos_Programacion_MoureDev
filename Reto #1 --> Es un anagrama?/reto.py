#/*
#* Escribe una función que reciba dos palabras (String) y retorne
#* verdadero o falso (Bool) según sean o no anagramas.
#* - Un Anagrama consiste en formar una palabra reordenando TODAS
#*   las letras de otra palabra inicial.
#* - NO hace falta comprobar que ambas palabras existan.
#* - Dos palabras exactamente iguales no son anagrama.
#*/

                   # ------------------------------------------------------------------ #
                   
                   
# La estructura de nuestra funcion se va a componer de un try: except: para obtener un mayor control de la misma.
# La primera lina del bloque try: nos permite verificar que ambos argumentos pasados a la funcion sean cadenas de texto,
# en caso contrario, se ejecutara el bloque except: avisandonos del error.                   
                   
def comprobar_anagrama(string1,string2):
    
    try:
        assert string1.isalpha() == True and string2.isalpha() == True
        if string1 == string2:   # El enunciado nos indica que dos palabras iguales no son consideradas anagramas.
            print('\n'*2)
            return False
        
        string1_normalizado = string1.lower()   # En caso de que alguno de los argumentos tenga letras en mayuscula, estas
        string2_normalizado = string2.lower()   # se convierten a minusculas.
        
        for letra1 in string1_normalizado:   # PRIMERO, se comprueba que todas las letras de 'string1' esten en 'string2'
            if letra1 in string2_normalizado:# Si la letra se encuentra en en 'string2', la funcion no hace nada.
                pass
            else:
                    print('\n'*2)            # En caso contrario, la funcion acaba y retorna 'False' como resultado.
                    return False
        else:  # El bloque else: de un bucle for se ejecuta cuando acaban todas las iteraciones del bucle.
            for letra2 in string2_normalizado:# SEGUNDO, se comprueba que todas las letras de 'string2' esten en 'string1'
                if letra2 in string1_normalizado:# Si la letra se encuentra en en 'string1', la funcion no hace nada.
                    pass
                else:
                    print('\n'*2)             # En caso contrario, la funcion acaba y retorna 'False' como resultado.
                    return False
        print('\n'*2)
        return True              # Si los bucles for se han ejecutado sin problema, la funcion retorna 'True', indicando
                                 # que ambos argumentos son anagramas.
        
    
    except:
        print('\n'*2)
        print('---- Debes introducir datos que sean de tipo string (cadenas de texto).')
        print('\n'*2)
        
        
if __name__ == '__main__':
    print(comprobar_anagrama('jirfa','jirufa'))
    