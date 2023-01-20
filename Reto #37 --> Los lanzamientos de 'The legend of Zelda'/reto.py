#/*
#* Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! 
#* Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
#* Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
#* "The Legend of Zelda" de la historia?
#* Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
#* que tú selecciones.
#* - Debes buscar cada uno de los títulos y su día de lanzamiento 
#*   (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
#*/



class OrdenError(Exception):
    pass




from datetime import timedelta,datetime

formato_fecha = "%Y-%m-%d"

class JuegoZelda():
    """Clase que representa cada uno de los juegos que vamos a crear y utilizar para el funcionamiento de nuestro programa.
    
        Atributos:
        - nombre: nombre del juego en cuestion.
        - lanzamiento: fecha en formato '%Y-%m-%d' , que representa el dia en el que el juego salio al mercado.
    """
    def __init__(self,nombre,lanzamiento):
        self.nombre = nombre
        self.lanzamiento = lanzamiento
    
    def __str__(self):
        return '{} lanzado en {}'.format(self.nombre,
                                         self.lanzamiento)
        
        
        
        
        

juegoZelda1 = JuegoZelda(nombre='The Legend of Zelda',
                         lanzamiento= datetime.strptime('1986-10-10',formato_fecha) ) 

juegoZelda2 = JuegoZelda(nombre='Zelda II: The Adventure of Link',
                         lanzamiento= datetime.strptime('1987-5-20',formato_fecha) ) 

juegoZelda3 = JuegoZelda(nombre='The Legend of Zelda: A Link to the Past',
                         lanzamiento= datetime.strptime('1991-11-27',formato_fecha) ) 

juegoZelda4 = JuegoZelda(nombre="The Legend of Zelda: Link's Awakening",
                         lanzamiento= datetime.strptime('1993-8-14',formato_fecha) ) 

juegoZelda5 = JuegoZelda(nombre='The Legend of Zelda BS',
                         lanzamiento= datetime.strptime('1995-10-10',formato_fecha) ) 

juegoZelda6 = JuegoZelda(nombre='The Legend of Zelda: Ocarina of Time',
                         lanzamiento= datetime.strptime('1998-7-20',formato_fecha) ) 

juegoZelda7 = JuegoZelda(nombre="The Legend of Zelda: Majora's Mask",
                         lanzamiento= datetime.strptime('2000-11-25',formato_fecha) ) 

juegoZelda8 = JuegoZelda(nombre='The Legend of Zelda: Oracle of Seasons',
                         lanzamiento= datetime.strptime('2001-10-24',formato_fecha) ) 

juegoZelda9 = JuegoZelda(nombre='The Legend of Zelda: Four Swords',
                         lanzamiento= datetime.strptime('2002-5-7',formato_fecha) ) 

juegoZelda10 = JuegoZelda(nombre='The Legend of Zelda: The Wind Waker',
                         lanzamiento= datetime.strptime('2002-10-10',formato_fecha) )

listaJuegosZelda = [juegoZelda1,
                    juegoZelda2,
                    juegoZelda3,
                    juegoZelda4,
                    juegoZelda5,
                    juegoZelda6,
                    juegoZelda7,
                    juegoZelda8,
                    juegoZelda9,
                    juegoZelda10]


def comprobarFecha():
    """Funcion sin parametros que solicita al usuario dos juegos de una lista de juegos, y devuelve por pantalla el tiempo transcurrido entre dichos juegos
       en años y días.
    """
    
    
    comprobacion1 = int(input("""Seleccione el primer juego:
                                    1 - The Legend of Zelda
                                    2 - Zelda II: The Adventure of Link
                                    3 - The Legend of Zelda: A Link to the Past
                                    4 - The Legend of Zelda: Link's Awakening
                                    5 - The Legend of Zelda BS
                                    6 - The Legend of Zelda: Ocarina of Time
                                    7 - The Legend of Zelda: Majora's Mask
                                    8 - The Legend of Zelda: Oracle of Seasons
                                    9 - The Legend of Zelda: Four Swords
                                    10 - The Legend of Zelda: The Wind Waker
                                    """))
    juego1Comprobacion = listaJuegosZelda[comprobacion1-1]
    
    comprobacion2 = int(input("""Seleccione el segundo juego:
                                    1 - The Legend of Zelda
                                    2 - Zelda II: The Adventure of Link
                                    3 - The Legend of Zelda: A Link to the Past
                                    4 - The Legend of Zelda: Link's Awakening
                                    5 - The Legend of Zelda BS
                                    6 - The Legend of Zelda: Ocarina of Time
                                    7 - The Legend of Zelda: Majora's Mask
                                    8 - The Legend of Zelda: Oracle of Seasons
                                    9 - The Legend of Zelda: Four Swords
                                    10 - The Legend of Zelda: The Wind Waker
                                    """))
    juego2Comprobacion = listaJuegosZelda[comprobacion2 - 1]
    
    try:
        assert (comprobacion1 != comprobacion2)
        if comprobacion1 < comprobacion2:
            
            distanciaTemporal = juego2Comprobacion.lanzamiento - juego1Comprobacion.lanzamiento
            resultado_final = distanciaTemporal.days
            anios = 0
            
            while resultado_final > 365:
                if resultado_final > 365:
                    resultado_final -= 365
                    anios +=1
            
            if anios > 0:
                return 'La distancia temporal entre el lanzamiento de "{}" y el de "{}" es de {} años y {} días.'.format(juego1Comprobacion.nombre,
                                                                                                                    juego2Comprobacion.nombre,
                                                                                                                    anios,
                                                                                                                    resultado_final)
            else:
                return 'La distancia temporal entre el lanzamiento de "{}" y el de "{}" es de {} días.'.format(juego1Comprobacion.nombre,
                                                                                                            juego2Comprobacion.nombre,                        
                                                                                                            resultado_final)
        
        elif comprobacion1 > comprobacion2:
            
            distanciaTemporal = juego1Comprobacion.lanzamiento - juego2Comprobacion.lanzamiento
            resultado_final = distanciaTemporal.days
            anios = 0
            
            while resultado_final > 365:
                if resultado_final > 365:
                    resultado_final -= 365
                    anios +=1
            
            if anios > 0:
                return 'La distancia temporal entre el lanzamiento de "{}" y el de "{}" es de {} años y {} días.'.format(juego1Comprobacion.nombre,
                                                                                                                    juego2Comprobacion.nombre,
                                                                                                                    anios,
                                                                                                                    resultado_final)
            else:
                return 'La distancia temporal entre el lanzamiento de "{}" y el de "{}" es de {} días.'.format(juego1Comprobacion.nombre,
                                                                                                            juego2Comprobacion.nombre,                        
                                                                                                            resultado_final)
        
            
    except AssertionError:
        print('Se ha seleccionado el mismo juego para los dos casos.')
        return 'Por favor, seleccione dos juegos distintos.'
    except OrdenError:
        print('Por favor, el segundo juego elegido debe ser el mas reciente.')
        return 'Intentelo de nuevo.'


if __name__ == '__main__':
    
   print(comprobarFecha())