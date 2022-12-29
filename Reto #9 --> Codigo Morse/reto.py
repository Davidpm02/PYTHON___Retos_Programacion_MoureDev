#/*
#* Crea un programa que sea capaz de transformar texto natural a código
#* morse y viceversa.
#* - Debe detectar automáticamente de qué tipo se trata y realizar
#*   la conversión.
#* - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#*   o símbolos y dos espacios entre palabras "  ".
#* - El alfabeto morse soportado será el mostrado en
#*   https://es.wikipedia.org/wiki/Código_morse.
#*/

def comprobarTipo(texto):
    
    textoPreparado = texto
    lista = texto.split()
    if lista[0][0] in 'abcefghijklmnopqrtsuvwxyz':    # El primer indice se refire a la primera palabra, el primer elemento 
        return 'Natural'                                # de la lista. El segundo indice, a la primera letra del elemento.
    else:
        return 'Morse'
    
    
def convertirTexto():
    texto = input('Introduzca un texto:')
    
    if comprobarTipo(texto) == 'Natural':
        lista = texto.split()
        for elemento in lista:
            for letra in elemento:
                if letra == 'a':
                    print('. -',end='  ')
                elif letra == 'b':
                    print('- ...',end='  ')
                elif letra == 'c':
                    print('- . - .',end='  ')
                elif letra == 'ch':
                    print('- - - -',end='  ')
                elif letra == 'd':
                    print('- ..',end='  ')
                elif letra == 'e':
                    print('.',end='  ')
                elif letra == 'f':
                    print('.. - .',end='  ')
                elif letra == 'g':
                    print('- - .',end='  ')
                elif letra == 'h':
                    print('....',end='  ')
                elif letra == 'i':
                    print('..',end='  ')
                elif letra == 'j':
                    print('. - - -',end='  ')
                elif letra == 'k':
                    print('- . -',end='  ')
                elif letra == 'l':
                    print('. - ..',end='  ')
                elif letra == 'm':
                    print('- -',end='  ')
                elif letra == 'n':
                    print('- .',end='  ')
                elif letra == 'o':
                    print('- - -',end='  ')
                elif letra == 'p':
                    print('. - - .',end='  ')
                elif letra == 'q':
                    print('- - . -',end='  ')
                elif letra == 'r':
                    print('. - .',end='  ')
                elif letra == 's':
                    print('...',end='  ')
                elif letra == 't':
                    print('-',end='  ')
                elif letra == 'u':
                    print('.. -',end='  ')
                elif letra == 'v':
                    print('... -',end='  ')
                elif letra == 'w':
                    print('. - -',end='  ')
                elif letra == 'x':
                    print('- .. -',end='  ')
                elif letra == 'y':
                    print('- . - -',end='  ')
                elif letra == 'z':
                    print('- - ..',end='  ')
                elif letra == ' ':
                    print('//',end='  ')  # Cuidado, / es un caracter de escape.
                elif letra == '  ':
                    print('////',end='  ')
                
    elif comprobarTipo(texto) == 'Morse':
         lista = texto.split('  ')
         for letra in lista:
            if letra == '. -':
                print('a',end='')
            elif letra == '- ...':
                print('b',end='')
            elif letra == '- . - .':
                print('c',end='')
            elif letra == '- - - -':
                print('ch',end='')
            elif letra == '- ..':
                print('d',end='')
            elif letra == '.':
                print('e',end='')
            elif letra == '.. - .':
                print('f',end='')
            elif letra == '- - .':
                print('g',end='')
            elif letra == '....':
                print('h',end='')
            elif letra == '..':
                print('i',end='')
            elif letra == '. - - -':
                print('j',end='')
            elif letra == '- . -':
                print('k',end='')
            elif letra == '. - ..':
                print('l',end='')
            elif letra == '- -':
                print('m',end='')
            elif letra == '- .':
                print('n',end='')
            elif letra == '- - -':
                print('o',end='')
            elif letra == '. - - .':
                print('p',end='')
            elif letra == '- - . -':
                print('q',end='')
            elif letra == '. - .':
                print('r',end='')
            elif letra == '...':
                print('s',end='')
            elif letra == '-':
                print('t',end='')
            elif letra == '.. -':
                print('u',end='')
            elif letra == '... -':
                print('v',end='')
            elif letra == '. - -':
                print('w',end='')
            elif letra == '- .. -':
                print('x',end='')
            elif letra == '- . - -':
                print('y',end='')
            elif letra == '- - ..':
                print('z',end='')
            elif letra == '//':
                print(' ',end='')  # Cuidado, / es un caracter de escape.
            elif letra == '////':
                print('  ',end='')
            elif letra == '. - . - . -':
                print('.',end='')
                
                

if __name__ == '__main__':
  convertirTexto()