#/*
#* Enunciado: Crea una función que sea capaz de detectar y retornar todos los
#* handles de un texto usando solamente Expresiones Regulares.
#* Debes crear una expresión regular para cada caso:
#* - Handle usuario: Los que comienzan por "@"
#* - Handle hashtag: Los que comienzan por "#"
#* - Handle web: Los que comienzan por "www.", "http://", "https://" 
#*   y finalizan con un dominio (.com, .es...)
#*/


import re

usuario = '@'  
hashtag = '#'
esquema1 = 'www.'
esquema2 = 'http://'
esquema3 = 'https://'
dominio1 = '.com'
dominio2 = '.es'

def handles():
    """Funcion sin parametros que imprime por pantalla un mensaje con el tipo de handle que contiene el texto que introduzca el 
       usuario por pantalla.
       """
    texto = input('Escriba un texto cualquiera...')
    
    coincidenciasUsuario = re.search(usuario,texto)
    coincidenciasHashtag = re.search(hashtag,texto)
    
    coincidenciasWeb1 = re.search(esquema1,texto)
    coincidenciasWeb2 = re.search(esquema2,texto)
    coincidenciasWeb3 = re.search(esquema3,texto)
    coincidenciasWeb4 = re.search(dominio1,texto)
    coincidenciasWeb5 = re.search(dominio2,texto)
    
    if coincidenciasUsuario:
        print('El texto contiene un handle de Usuario')
    elif coincidenciasHashtag:
        print('El texto contiene un handle de Hashtag')
    elif (coincidenciasWeb1 or coincidenciasWeb2 or coincidenciasWeb3) and (coincidenciasWeb4 or coincidenciasWeb5) :
        print('El texto contiene un handle de Web')
    else:
        print('El texto no introducido no contiene ningun handle definido...')
    
if __name__ == '__main__':
    handles()