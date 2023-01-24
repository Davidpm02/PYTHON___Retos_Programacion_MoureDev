#/*
#* Enunciado: Este es un reto especial por Halloween.
#* Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
#* o Trato" y un listado (array) de personas con las siguientes propiedades:
#* - Nombre de la niña o niño
#* - Edad
#* - Altura en centímetros
#*
#* Si las personas han pedido truco, el programa retornará sustos (aleatorios)
#* siguiendo estos criterios:
#* - Un susto por cada 2 letras del nombre por persona
#* - Dos sustos por cada edad que sea un número par
#* - Tres sustos por cada 100 cm de altura entre todas las personas
#* - Sustos: 🎃 👻 💀 🕷 🕸 🦇
#*
#* Si las personas han pedido trato, el programa retornará dulces (aleatorios)
#* siguiendo estos criterios:
#* - Un dulce por cada letra de nombre
#* - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
#* - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
#* - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
#*/



import random
import time



class Persona():
    """Clase que prmite crear instancias de personas, las cuales formaran los grupos de amigos.
    
    Atributos:
        - nombre
        - edad
        - altura
    """
    
    def __init__(self,nombre,edad,altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura    # Debe ser un entero con la altura en centimetros.
        
    def __str__(self):
        return '{}, que tiene {} años y mide {} centimetros.'
    


def comprobarAccion(accion):
    """Funcion parametrizada que evalua el argumento pasado y retorna un resultado en funcion del mismo.
    
    Parametros:
        - accion: string que representa el tipo de juego al que jugara el grupo de amigos.
    """
    
    accionFormateada = accion.lower()
    if accionFormateada == 'truco':
        return True             # La funcion retornara True en caso de que la accion sea 'Truco'
    
    elif accionFormateada == 'trato':
        return False            # La funcion retornara False en caso de que la accion sea 'False'


def comprobarAlturas(listaPersonas):
    """Funcion parametrizada que evalua el argumento pasado y retorna un resultado en funcion del mismo.
    
    Parametros:
        - listaPersonas: recibe la lista de amigos, para actualizar una variable propia de la funcion en base a 
        la altura de las personas de la lista.
    """
    
    contadorCentimetros = 0
    for persona in listaPersonas:
        contadorCentimetros += persona.altura
        
    return contadorCentimetros

def comprobarLetrasNombres(listaPersonas):
    """Funcion parametrizada que evalua el argumento pasado y retorna un resultado en funcion del mismo.
    
    Parametros:
        - listaPersonas: recibe la lista de amigos, para actualizar una variable propia de la funcion en base a 
        al nombre de las personas de la lista.
    """
    
    contadorLetras = 0
    for persona in listaPersonas:
        contadorLetras += len(persona.nombre)
    
    return contadorLetras


def comprobarEdades(listaPersonas):
    """Funcion parametrizada que evalua el argumento pasado y retorna un resultado en funcion del mismo.
    
    Parametros:
        - listaPersonas: recibe la lista de amigos, para actualizar una variable propia de la funcion en base a 
        le edad de las personas de la lista.
    """
    
    listaEdades = []
    
    for persona in listaPersonas:
        listaEdades.append(persona.edad)
        
    return listaEdades






def sustos(listaPersonas):
    """Funcion parametrizada que evalua el argumento pasado y devuelve un string con los sustos correspondientes a las personas
       de la lista recibida.
    """
    
    #* - Un susto por cada 2 letras del nombre por persona
    #* - Dos sustos por cada edad que sea un número par
    #* - Tres sustos por cada 100 cm de altura entre todas las personas
    tiposSustos = '🎃 👻 💀 🕷 🕸 🦇'
    
    sustosDevueltos = []  # Inicializo una lista a la que se la iran añadiendo sustos segun se cumplan los criterios pedidos.
    
    sustosPorLetras = 0
    letrasTotales = comprobarLetrasNombres(listaPersonas)
    while letrasTotales < 2:
        letrasTotales -=2
        sustosPorLetras +=1
        
        
    sustosPorEdades = 0
    listaEdades = comprobarEdades(listaPersonas)
    for edad in listaEdades:
        if edad % 2 == 0:
            sustosPorEdades +=2    # Si la edad de un niño o niña es par, se le sumaran dos sustos al susto final.
        else:
            continue
        
        
    sustosPorAltura = 0
    centimetrosTotales = comprobarAlturas(listaPersonas)
   
    while centimetrosTotales >= 100:  # Mientras que el contador de centimetros totales sume un total de 100 centimetros o mas,
        centimetrosTotales -=100      # se le restaran 100 centimetros al contador, y se le sumaran 3 sustos al contador de sustos.
        sustosPorAltura +=3
        
        
    contadorSustos = sustosPorLetras + sustosPorEdades + sustosPorAltura    # Sumamos el total de sustos que tenemos


    for susto in range(contadorSustos):
        
        sustosDevueltos.append(random.choice(tiposSustos))    # Añadimos sustos aleatoriamente a la lista de sustos segun el numero
                                                              # total de sustos que hayamos obtenido.
    
    
    
    for susto in sustosDevueltos:    # Finalmente, se imprimiran todos los sustos de la lista con un espacio de separacion.
        print(susto,end= ' ')






def tratos(listaPersonas):
    """Funcion parametrizada que evalua el argumento pasado y devuelve un string con los caramelos correspondientes a las personas
       de la lista recibida.
    """
    #* - Un dulce por cada letra de nombre
    #* - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
    #* - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
    
    tiposDeTratos = '🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩'
    
    tratosDevueltos = []




    tratosPorLetra = 0
    letrasTotales = comprobarLetrasNombres(listaPersonas)
    while letrasTotales <= 1:
        letrasTotales -=1
        tratosPorLetra +=1
        
        
    tratosPorEdades = 0
    for persona in listaPersonas:
        for numAnios in range(1,persona.edad):
            if persona.edad >= 10:
                tratosPorEdades +=3
            else:
                if numAnios == 3 or numAnios == 6 or numAnios == 9:
                    tratosPorEdades +=1
                    
    
    tratosPorAltura = 0
    for persona in listaPersonas:
        for centimetros in range(1,persona.altura):
            if persona.altura >= 150:
                tratosPorAltura +=3
            else:
                if centimetros == 50 or centimetros == 100:
                    tratosPorAltura +=1
                    
    
    contadorTratosTotales = tratosPorLetra + tratosPorEdades + tratosPorAltura
    
    for trato in range(contadorTratosTotales):
        
        tratosDevueltos.append(random.choice(tiposDeTratos))
        
    for trato in tratosDevueltos:
        print(trato, end=' ')
        
        
    
    
    

def truco_o_trato(accion,listaPersonas):
    """Funcion parametrizada que evalua el argumento pasado y devuelve una serie de mensajes con infromacion de las personas
       de la lista recibida.
       
       Parametros
       - accion: string que representa el tipo de juego al que jugara el grupo de amigos. 
       - listaPersonas: lista con las personas que forman el grupo de amigos.
    """
    
    print('Hoy es Halloween!')
    time.sleep(2)
    print('Un grupo de amigos sale a la calle a jugar a Truco o Trato.')
    time.sleep(2)
    
    print('El grupo tiene {} miembros:'.format(len(listaPersonas)))
    time.sleep(1)
    for persona in listaPersonas:
        print('> {}, de {} años.'.format(persona.nombre,
                                         persona.edad))
        time.sleep(1)
            
    tipoAccion = comprobarAccion(accion) # true = truco, false = trato
    
    
    if tipoAccion == True:
        print()
        print('El grupo de amigos ha decidido hacer Truco!')
        time.sleep(1)
        print('El grupo ha recibido los siguiente sustos:')
        sustos(listaPersonas)
        
    elif tipoAccion == False:
    
        print('El grupo de amigos ha decidido hacer Truco!')
        time.sleep(1)
        print('El grupo ha recibido los siguientes caramelos:')
        tratos(listaPersonas)


if __name__ == '__main__':
    
    persona1 = Persona('David',6,123)
    persona2 = Persona('Carlos',8,145)
    persona3 = Persona('Gabriel',5,120)
    persona4 = Persona('Macarena',2,87)
    
    listaAmigos = [persona1,persona2,persona3,persona4]
    
    juego = 'truco'
    
    truco_o_trato(juego,listaAmigos)