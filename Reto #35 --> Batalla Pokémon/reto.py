#/*
#* Enunciado: Crea un programa que calcule el daño de un ataque durante
#* una batalla Pokémon.
#* - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
#* - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
#* - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
#*   (buscar su efectividad)
#* - El programa recibe los siguientes parámetros:
#*  - Tipo del Pokémon atacante.
#*  - Tipo del Pokémon defensor.
#*  - Ataque: Entre 1 y 100.
#*  - Defensa: Entre 1 y 100.
#*/


def efectividad(tipo1,tipo2):
    """Funcion parametrizada que retorna un resultado numerico en funcion de la relacion existente entre los dos parametros."""
    
    if tipo1 == 'Agua' and tipo2 == 'Fuego':
        return 2
    elif tipo1 == 'Agua' and tipo2 == 'Planta':
        return 0.5
    elif tipo1 == 'Agua' and tipo2 == 'Agua':
        return 1
    elif tipo1 == 'Agua' and tipo2 == 'Electrico':
        return 0.5
    elif tipo1 == 'Fuego' and tipo2 == 'Fuego':
        return 1
    elif tipo1 == 'Fuego' and tipo2 == 'Planta':
        return 2
    elif tipo1 == 'Fuego' and tipo2 == 'Agua':
        return 0.5
    elif tipo1 == 'Fuego' and tipo2 == 'Electrico':
        return 1
    elif tipo1 == 'Planta' and tipo2 == 'Fuego':
        return 0.5
    elif tipo1 == 'Planta' and tipo2 == 'Planta':
        return 1
    elif tipo1 == 'Planta' and tipo2 == 'Agua':
        return 2
    elif tipo1 == 'Planta' and tipo2 == 'Electrico':
        return 0.5
    elif tipo1 == 'Electrico' and tipo2 == 'Fuego':
        return 1
    elif tipo1 == 'Electrico' and tipo2 == 'Planta':
        return 1
    elif tipo1 == 'Electrico' and tipo2 == 'Agua':
        return 2
    elif tipo1 == 'Electrico' and tipo2 == 'Electrico':
        return 1
            
            
            
def batalla(tipo1,tipo2,ataque,defensa):
    
    try:
        assert (0 < ataque <= 100) and (0 < defensa <= 100)
        danioInflingido = 50 * (ataque/defensa) * efectividad(tipo1,tipo2)
        danioRedondeado = round(danioInflingido,2)   # Redondeamos el dano inflingido a dos decimales.
        
        return 'El Pokémon de tipo {} ha inflingido {} puntos de daño al Pokémon de tipo {}.'.format(tipo1,
                                                                                                     danioRedondeado,
                                                                                                     tipo2)
    except AssertionError:
        print('Las estadisticas de los Pokemon no son validas.')
        return 


if __name__ == '__main__':
    print(batalla('Agua','Planta',63,55))
    
    
