#/*
#* Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales
#* a Sauron contra otras bondadosas que no quieren que el mal reine
#* sobre sus tierras.
#* Cada raza tiene asociado un "valor" entre 1 y 5:
#* - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
#*   Númenóreanos (4), Elfos (5)
#* - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
#*   Huargos (3), Trolls (5)
#* Crea un programa que calcule el resultado de la batalla entre
#* los 2 tipos de ejércitos:
#* - El resultado puede ser que gane el bien, el mal, o exista un empate.
#*   Dependiendo de la suma del valor del ejército y el número de integrantes.
#* - Cada ejército puede estar compuesto por un número de integrantes variable
#*   de cada raza.
#* - Tienes total libertad para modelar los datos del ejercicio.
#* Ej: 1 Peloso pierde contra 1 Orco
#*     2 Pelosos empatan contra 1 Orco
#*     3 Pelosos ganan a 1 Orco
#*/


class RazasBondadosas():
    def __init__(self,nombre,valor):
        self.nombre = nombre
        self.valor = valor
        
    def __str__(self):
        return 'Raza bondadosa {} --> Valor: {}'.format(self.nombre,
                                                        self.valor)
        
class RazasMalvadas():
    def __init__(self,nombre,valor):
        self.nombre = nombre
        self.valor = valor
        
    def __str__(self):
        return 'Raza malvada {} --> Valor: {}'.format(self.nombre,
                                                      self.valor)


# Tras crear las clases de personajes, creo las instancias y las almaceno en una lista por cada tipo de personaje.

Pelosos = RazasBondadosas(nombre='Pelosos',
                          valor=1)
Surenios_buenos = RazasBondadosas(nombre='Sureños buenos',
                                  valor=2)
Enanos = RazasBondadosas(nombre='Enanos',
                         valor = 3)
Numenoreanos = RazasBondadosas(nombre='Númenóreanos',
                               valor = 4)
Elfos = RazasBondadosas(nombre='Elfos',
                        valor = 5)


razasBondadosas = [Pelosos,Surenios_buenos,Enanos,Numenoreanos,Elfos]



Surenios_malos = RazasMalvadas(nombre='Sureños malos',
                               valor=2)
Orcos = RazasMalvadas(nombre='Orcos',
                      valor=2)
Goblins = RazasMalvadas(nombre='Goblins',
                        valor = 2)
Huargos = RazasMalvadas(nombre='Huargos',
                               valor = 3)
Trolls = RazasMalvadas(nombre='Trolls',
                        valor = 5)


razasMalvadas = [Surenios_malos,Orcos,Goblins,Huargos,Trolls]


def batalla():
    numeroPersonajes = int(input('''Seleccione el numero de personajes por equipo:
                           - 1.
                           - 2.
                           - 3.
                           '''))
    
    if numeroPersonajes == 1:
        
        
        
        pBueno = int(input("""Seleccione el personaje del equipo de Razas Bondadosas:
                           1. Peloso (v = 1)
                           2. Sureño buenos(v = 2)
                           3. Enano (v = 3)
                           4. Númenóreano (v = 4)
                           5. Elfo (v = 5)
                           """))
        equipoBueno = []
        equipoBueno.append(razasBondadosas[pBueno - 1]) # Hay 5 personajes en cada lista, empezando desde el 0 hasta el 4
        
        valorEquipoBueno = 0 
        
        for personaje in equipoBueno:
            valorEquipoBueno += personaje.valor
            
            
        # ---------------------------------------------------- #
        
        
        
        pMalvado = int(input("""Seleccione el personaje del equipo de Razas Malvadas:
                             1. Sureños malvado (v = 2)
                             2. Orco (v = 2)
                             3. Goblin (v = 2)
                             4. Huargo (v = 3)
                             5. Troll (v = 5)
                             """))
        equipoMalvado = []
        equipoMalvado.append(razasMalvadas[pMalvado - 1])

        
        valorEquipoMalvado = 0 
        
        for personaje in equipoMalvado:
            valorEquipoMalvado += personaje.valor
            
        
        resultado = valorEquipoBueno - valorEquipoMalvado
        
        if resultado > 0:
            return 'Equipo de Razas Bondadosas gana vs Equipo de Razas Malvadas.'
        
        elif resultado < 0:
            return 'Equipo de Razas Malvadas gana vs Equipo de Razas Bondadosas.'
        
        elif resultado == 0:
            return 'Equipo de Razas Bondadosas y Equipo de Razas Malvadas han quedado EMPATE.'




    elif numeroPersonajes == 2:
        
        
        
        
        pBueno1 = int(input("""Seleccione el primer personaje del equipo de Razas Bondadosas:
                           1. Peloso (v = 1)
                           2. Sureño buenos(v = 2)
                           3. Enano (v = 3)
                           4. Númenóreano (v = 4)
                           5. Elfo (v = 5)
                           """))
        equipoBueno = []
        equipoBueno.append(razasBondadosas[pBueno1 - 1]) # Hay 5 personajes en cada lista, empezando desde el 0 hasta el 4
        
        pBueno2 = int(input("""Seleccione el segundo personaje del equipo de Razas Bondadosas:
                           1. Peloso (v = 1)
                           2. Sureño buenos(v = 2)
                           3. Enano (v = 3)
                           4. Númenóreano (v = 4)
                           5. Elfo (v = 5)
                           """))
        equipoBueno.append(razasBondadosas[pBueno2 - 1]) # Hay 5 personajes en cada lista, empezando desde el 0 hasta el 
        
        
        valorEquipoBueno = 0 
        
        for personaje in equipoBueno:
            valorEquipoBueno += personaje.valor
            
            
        # ---------------------------------------------------- #
        
        
        pMalvado1 = int(input("""Seleccione el primer personaje del equipo de Razas Malvadas:
                             1. Sureños malvado (v = 2)
                             2. Orco (v = 2)
                             3. Goblin (v = 2)
                             4. Huargo (v = 3)
                             5. Troll (v = 5)
                             """))
        equipoMalvado = []
        equipoMalvado.append(razasMalvadas[pMalvado1 - 1])
        
        pMalvado2 = int(input("""Seleccione el segundo personaje del equipo de Razas Malvadas:
                             1. Sureños malvado (v = 2)
                             2. Orco (v = 2)
                             3. Goblin (v = 2)
                             4. Huargo (v = 3)
                             5. Troll (v = 5)
                             """))
        equipoMalvado.append(razasMalvadas[pMalvado2 - 1])

        
        valorEquipoMalvado = 0 
        
        for personaje in equipoMalvado:
            valorEquipoMalvado += personaje.valor
            
        resultado = valorEquipoBueno - valorEquipoMalvado
        
        if resultado > 0:
            return 'Equipo de Razas Bondadosas gana vs Equipo de Razas Malvadas.'
        
        elif resultado < 0:
            return 'Equipo de Razas Malvadas gana vs Equipo de Razas Bondadosas.'
        
        elif resultado == 0:
            return 'Equipo de Razas Bondadosas y Equipo de Razas Malvadas han quedado EMPATE.'
        
        
        
    elif numeroPersonajes == 3:
        
        
        
        pBueno1 = int(input("""Seleccione el primer personaje del equipo de Razas Bondadosas:
                           1. Peloso (v = 1)
                           2. Sureño buenos(v = 2)
                           3. Enano (v = 3)
                           4. Númenóreano (v = 4)
                           5. Elfo (v = 5)
                           """))
        equipoBueno = []
        equipoBueno.append(razasBondadosas[pBueno1 - 1]) # Hay 5 personajes en cada lista, empezando desde el 0 hasta el 4
        
        pBueno2 = int(input("""Seleccione el segundo personaje del equipo de Razas Bondadosas:
                           1. Peloso (v = 1)
                           2. Sureño buenos(v = 2)
                           3. Enano (v = 3)
                           4. Númenóreano (v = 4)
                           5. Elfo (v = 5)
                           """))
        equipoBueno.append(razasBondadosas[pBueno2 - 1]) # Hay 5 personajes en cada lista, empezando desde el 0 hasta el 
        
        pBueno3 = int(input("""Seleccione el tercer personaje del equipo de Razas Bondadosas:
                           1. Peloso (v = 1)
                           2. Sureño buenos(v = 2)
                           3. Enano (v = 3)
                           4. Númenóreano (v = 4)
                           5. Elfo (v = 5)
                           """))
        equipoBueno.append(razasBondadosas[pBueno3 - 1]) # Hay 5 personajes en cada lista, empezando desde el 0 hasta el 
        
        valorEquipoBueno = 0 
        
        for personaje in equipoBueno:
            valorEquipoBueno += personaje.valor
            
        
        # ---------------------------------------------------- #
        
        
        pMalvado1 = int(input("""Seleccione el primer personaje del equipo de Razas Malvadas:
                             1. Sureños malvado (v = 2)
                             2. Orco (v = 2)
                             3. Goblin (v = 2)
                             4. Huargo (v = 3)
                             5. Troll (v = 5)
                             """))
        equipoMalvado = []
        equipoMalvado.append(razasMalvadas[pMalvado1 - 1])
        
        pMalvado2 = int(input("""Seleccione el segundo personaje del equipo de Razas Malvadas:
                             1. Sureños malvado (v = 2)
                             2. Orco (v = 2)
                             3. Goblin (v = 2)
                             4. Huargo (v = 3)
                             5. Troll (v = 5)
                             """))
        equipoMalvado.append(razasMalvadas[pMalvado2 - 1])
        
        pMalvado3 = int(input("""Seleccione el tercer personaje del equipo de Razas Malvadas:
                             1. Sureños malvado (v = 2)
                             2. Orco (v = 2)
                             3. Goblin (v = 2)
                             4. Huargo (v = 3)
                             5. Troll (v = 5)
                             """))
        equipoMalvado.append(razasMalvadas[pMalvado3 - 1])

        
        valorEquipoMalvado = 0 
        
        for personaje in equipoMalvado:
            valorEquipoMalvado += personaje.valor
            
        resultado = valorEquipoBueno - valorEquipoMalvado
        
        if resultado > 0:
            return 'Equipo de Razas Bondadosas gana vs Equipo de Razas Malvadas.'
        
        elif resultado < 0:
            return 'Equipo de Razas Malvadas gana vs Equipo de Razas Bondadosas.'
        
        elif resultado == 0:
            return 'Equipo de Razas Bondadosas y Equipo de Razas Malvadas han quedado EMPATE.'
            
        
        

if __name__ == '__main__':
    print(batalla())
        

