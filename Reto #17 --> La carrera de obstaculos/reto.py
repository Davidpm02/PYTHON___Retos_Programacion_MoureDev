#/*
#* Crea una función que evalúe si un/a atleta ha superado correctamente una
#* carrera de obstáculos.
#* - La función recibirá dos parámetros:
#*      - Un array que sólo puede contener String con las palabras
#*        "run" o "jump"
#*      - Un String que represente la pista y sólo puede contener "_" (suelo)
#*        o "|" (valla)
#* - La función imprimirá cómo ha finalizado la carrera:
#*      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#*        será correcto y no variará el símbolo de esa parte de la pista.
#*      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#*      - Si hace "run" en "|" (valla), se variará la pista por "/".
#* - La función retornará un Boolean que indique si ha superado la carrera.
#* Para ello tiene que realizar la opción correcta en cada tramo de la pista.
#*/




def carrera(array,str):
    
    try:
        assert len(array) == len(str)
        listaStringPistaFinal = []    # Inicializamos una lista que contendra los elementos que vayamos imprimiendo por pantalla
        contador = 0                  # a lo largo de la carrera, y una variable contador que usaremos para referirnos al indice.
        for accion in array:
            if accion == 'run' and str[contador] == '_':     #Ejecutamos un bucle for para iterar sobre los elementos del array argumento
                print('_',end='')                            
                listaStringPistaFinal.append('_')
                contador +=1                                   # El bucle for contiene cuatro condicionales para actuar en base a las
                                                            # condiciones del enunciado.
                                                            # Si el elemento del array coindice con el elemento del indice correspondiente
            elif accion == 'jump' and str[contador] == '|':    # del string, se imprimira el simbolo de esa parte de la lista Y SE ANADIRA
                print('|',end='')                              # a listaStringPistaFinal.
                listaStringPistaFinal.append('|')              # En caso contrario, se imprimira el simbolo especificado en el enunciado,
                contador +=1                                   # y tambien se anadira a la pista.
                
                
            elif accion == 'run' and str[contador] == '|':
                print('/',end='')
                listaStringPistaFinal.append('/')
                contador +=1
                    
                    
            elif accion == 'jump' and str[contador] == '_':
                print('x',end='')
                listaStringPistaFinal.append('x')
                contador +=1
        
        
        for item in listaStringPistaFinal:        # Finalmente, uso otro bucle for para iterar sobra la nueva lista, y en caso de 
            if item != '_' or item != '|':        # algun elemento sea diferente a '_' o '|' (esto es, el atleta haya fallado en al menos
                print(' ',end='\n')               # una ocasion), el programa retornara False.
                return False                      
            else:
                print(' ',end='\n')               # Si nungun elemento de la lista es diferente a '_' o '|', el programa retornara True.
                True  
    except AssertionError:
        if len(array) > len(str):
            print('La pista es demasiado corta para la cantidad de acciones asignadas al atleta.')   
        elif len(array) < len(str):
            print('La pista es demasiado larga para la cantidad de acciones asignadas al atleta.')    
        else:
            print('Ha ocurrido un error al especificar el array de acciones o el string de la pista.')



if __name__ == '__main__':
    print(carrera(['run','run','jump','run','run','run','jump','run'],'__||_|__'))