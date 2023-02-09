#/*
#* ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
#* 24 días, 24 regalos sorpresa relacionados con desarrollo de software,
#* ciencia y tecnología desde el 1 de diciembre.
#*
#* Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
#* lo siguiente:
#* - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
#*   de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
#* - Si la fecha es anterior: Cuánto queda para que comience el calendario.
#* - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
#*
#* Notas:
#* - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
#*   y finaliza a las 23:59:59.
#* - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
#*   y segundos.
#* - 🎁 Cada persona que aporte su solución entrará en un nuevo sorteo
#*   del calendario de aDEViento hasta el día de su corrección
#*   (sorteo exclusivo para quien entregue su solución).
#*/


import datetime
import time

def calendarioaDEViento(fecha):
    """Funcion parametrizada que interactua con el usuario e imprime un regalo correspondiente al dia del calendario representado por el parametro.
    
       Parametros
           - fecha: parametro de tipo datetime.date que representa una fecha cualquiera.
           
    """
    inicioCalendario = datetime.date(2022,12,1)
    finCalendario = datetime.date(2022,12,25)
    
    if fecha < inicioCalendario:
        resultado = inicioCalendario - fecha
        anios = resultado.years
        meses = resultado.months
        dias = resultado.days
        if anios == 0:
            return '''El calendario de aDEViento 2022 todavía no ha comenzado.
                    El calendario de aDEViento 2022 comenzará en {} meses y {} dias.'''.format(meses,dias)
        elif meses == 0:
            return '''El calendario de aDEViento 2022 todavía no ha comenzado.
                    El calendario de aDEViento 2022 comenzará en {} años y {} dias.'''.format(anios,dias)
        elif dias == 0:
            return '''El calendario de aDEViento 2022 todavía no ha comenzado.
                    El calendario de aDEViento 2022 comenzará en {} años y {} meses.'''.format(anios,meses)
        elif anios == 0 and meses == 0:
            return '''El calendario de aDEViento 2022 todavía no ha comenzado.
                    El calendario de aDEViento 2022 comenzará en {} dias.'''.format(dias)
    
    elif fecha > finCalendario:
        resultado = fecha - finCalendario
        anios = resultado.years
        meses = resultado.months
        dias = resultado.days
        if anios == 0:
            return '''El calendario de aDEViento 2022 ya ha acabado.
                    El calendario de aDEViento 2022 acabo hace {} meses y {} dias.'''.format(meses,dias)
        elif meses == 0:
            return '''El calendario de aDEViento 2022 ya ha acabado.
                    El calendario de aDEViento 2022 acabo hace {} años y {} dias.'''.format(anios,dias)
        elif dias == 0:
            return '''El calendario de aDEViento 2022 ya ha acabado.
                    El calendario de aDEViento 2022 acabo hace {} años y {} meses.'''.format(anios,meses)
        elif anios == 0 and meses == 0:
            return '''El calendario de aDEViento 2022 ya ha acabado.
                    El calendario de aDEViento 2022 acabo hace {} dias.'''.format(dias)        
    elif fecha == inicioCalendario:
            print('Enhorabuena! El dia {} del {} del {} corresponde al inicio del calendario de aDEViento 2022. Los premios de hoy son:'.format(fecha.day,
                                                                                                                                                fecha.month,
                                                                                                                                                fecha.year))
            time.sleep(3)
            print('2 Libros “El programador pragmático” de David Thomas y Andrew Hunt.')
            time.sleep(2)
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                    1. SI
                                    2. NO
                                '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado 1 Libro “El programador pragmático” de David Thomas y Andrew Hunt.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
    elif fecha == finCalendario:
         print('Enhorabuena! El dia {} del {} del {} corresponde al último día del calendario de aDEViento 2022. El premio de hoy es:'.format(fecha.day,
                                                                                                                                                 fecha.month,
                                                                                                                                                 fecha.year))
         time.sleep(3)
         print('Elegir el libro de programación que quieras!')
         time.sleep(2)
         eleccion = int(input('''Los libros a elegir son:
                                 1. "Código Limpio. Manual de estilo para el desarrollo de software" de Robert C. Martin.
                                 2. "Patrones de diseño" de Erich Gamma.
                                 3. “El programador pragmático” de David Thomas y Andrew Hunt.
                                 4. No elegir ninguno.'''))
         if eleccion == 1:
             time.sleep(2)
             print('Has ganado 1 Libro "Código Limpio. Manual de estilo para el desarrollo de software" de Robert C. Martin.')
         elif eleccion == 2:
             time.sleep(2)
             print('Has ganado 1 Libro "Patrones de diseño" de Erich Gamma.')
         elif eleccion == 3:
             time.sleep(2)
             print('Has ganado 1 Libro “El programador pragmático” de David Thomas y Andrew Hunt.')
         elif eleccion == 4:
             time.sleep(2)
             print("No has elegido ninguno de los regalos de hoy.")
         
    elif fecha > inicioCalendario and fecha < finCalendario:
        if fecha.day == 2:
            print('Enhorabuena! El premio de hoy es el videojuego multiplataforma “while True: learn()” de Luden.io.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado 1 copia del videojuego multiplataforma “while True: learn()” de Luden.io.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                 
        elif fecha.day == 3:
            print('Enhorabuena! El premio de hoy es un curso "Aprende Javascript ES9, HTML, CSS3 y NodeJS desde cero” de Nicolás Schürmann.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado 1 un curso "Aprende Javascript ES9, HTML, CSS3 y NodeJS desde cero” de Nicolás Schürmann.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
        
        elif fecha.day == 4:
            print('Enhorabuena! El premio de hoy es un curso "Patrones de Diseño en JavaScript y TypeScript” de Héctor de León.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado 1 un curso "Patrones de Diseño en JavaScript y TypeScript” de Héctor de León.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
        
        elif fecha.day == 5:
            print('Enhorabuena! El premio de hoy es un Pack de libros "Aprende Python en un fin de semana” de Alfredo Moreno Muñoz y Sheila Córcoles Córcoles.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado Pack de libros "Aprende Python en un fin de semana” de Alfredo Moreno Muñoz y Sheila Córcoles Córcoles.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 6:
            print('Enhorabuena! El premio de hoy es un curso "Desarrollo de Apps iOS con Swift” de Juan Villalvazo y Brais Moure.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un curso "Desarrollo de Apps iOS con Swift” de Juan Villalvazo y Brais Moure.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
        
        elif fecha.day == 7:
            print('Enhorabuena! El premio de hoy es una Licencia de 6 meses para "Popsy: Crea tu web como un Notion” .')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado una Licencias de 6 meses para "Popsy: Crea tu web como un Notion”.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 8:
            print('Enhorabuena! El premio de hoy es un libro "Aprendiendo JavaScript desde cero” de Carlos Azaustre.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un libro "Aprendiendo JavaScript desde cero” de Carlos Azaustre.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 9:
            print('Enhorabuena! El premio de hoy es un curso de "Android con Jetpack Compose desde cero” de Aris Guimerá.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un curso de "Android con Jetpack Compose desde cero” de Aris Guimerá.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 10:
            print('Enhorabuena! El premio de hoy es un libro "Inteligencia matemática/Apocalipsis matemático" de Eduardo Sáenz de Cabezón.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un libro  "Inteligencia matemática/Apocalipsis matemático" de Eduardo Sáenz de Cabezón.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 11:
            print('Enhorabuena! El premio de hoy es un curso "Flutter: Tu guía completa de desarrollo para iOS y Android" de Fernando Herrera.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un curso "Flutter: Tu guía completa de desarrollo para iOS y Android" de Fernando Herrera.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 12:
            print('Enhorabuena! El premio de hoy es un libro "¿Qué puede salir mal?” de Sandra Ortonobes Lara (La Hiperactina) .')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un libro "¿Qué puede salir mal?” de Sandra Ortonobes Lara (La Hiperactina).')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 13:
            print('Enhorabuena! El premio de hoy es una Masterclass "Figma para developers” de Carmen Ansio.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado una Masterclass "Figma para developers” de Carmen Ansio.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 14:
            print('Enhorabuena! El premio de hoy es un "Dominio .dev" durante 10 años gracias a nuestro patrocinador INWX.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un "Dominio .dev" durante 10 años gracias a nuestro patrocinador INWX.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 15:
            print('Enhorabuena! El premio de hoy es un acceso de 3 meses a "Todos los cursos de Mastermind” .')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un acceso de 3 meses a "Todos los cursos de Mastermind” .')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 16:
            print('Enhorabuena! El premio de hoy son 2 Libros "El bosón de Higgs no te va a hacer la cama" y "¿Qué hace un bosón como tú en un Big Bang como este?” de Javier Santaolalla.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado 2 Libros "El bosón de Higgs no te va a hacer la cama" y "¿Qué hace un bosón como tú en un Big Bang como este?” de Javier Santaolalla.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 17:
            print('Enhorabuena! El premio de hoy es una Camiseta "I u{2665} CODE”.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado una Camiseta "I u{2665} CODE”.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 18:
            print('Enhorabuena! El premio de hoy es un acceso a "Hack4u", la academia de hacking y ciberseguridad de S4vitar.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un acceso a "Hack4u", la academia de hacking y ciberseguridad de S4vitar.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 19:
            print('Enhorabuena! El premio de hoy es un libro "Código Sostenible: Cómo desarrollar Software fácil de mantener” de Carlos Blé.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un libro "Código Sostenible: Cómo desarrollar Software fácil de mantener” de Carlos Blé.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 20:
            print('Enhorabuena! El premio de hoy es un "Bootcamp online de programación" (a tu elección) de GeeksHubs Academy.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un "Bootcamp online de programación" (a tu elección) de GeeksHubs Academy.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 21:
            print('Enhorabuena! El premio de hoy es un libro "La artesanía del código limpio" de Robert C. Martin.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un libro "La artesanía del código limpio" de Robert C. Martin.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 22:
            print('Enhorabuena! El premio de hoy es un acceso Accesos a "Todos los cursos de Codely.com" gracias a nuestro patrocinador CODELY.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un acceso a "Todos los cursos de Codely.com" gracias a nuestro patrocinador CODELY.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
        elif fecha.day == 23:
            print('Enhorabuena! El premio de hoy es un libro "Hábitos atómicos: cambios pequeños, resultados extraordinarios" de James Clear.')
            eleccion = int(input('''Quieres aceptar el regalo del día de hoy?
                                        1. SI
                                        2. NO
                                    '''))
            if eleccion == 1:
                time.sleep(2)
                print('Has ganado un libro "Hábitos atómicos: cambios pequeños, resultados extraordinarios" de James Clear.')
            elif eleccion == 2:
                time.sleep(2)
                print('No has aceptado el regalo del dia de hoy.')
                
    
if __name__ == '__main__':
    fecha = datetime.date(2022,12,24)
    calendarioaDEViento(fecha)