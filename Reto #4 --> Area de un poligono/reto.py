#/*
#* Crea una única función (importante que sólo sea una) que sea capaz
#* de calcular y retornar el área de un polígono.
#* - La función recibirá por parámetro sólo UN polígono a la vez.
#* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#* - Imprime el cálculo del área de un polígono de cada tipo.
#*/


# Para el siguiente reto hago uso de estructuras condicionales dentro de la funcion, para hacer que el programa
# tome una ruta u otra en funcion del poligono que escoja el usuario.

def calcularAreaPoligono(poligono):
        if poligono == 'Triangulo' or poligono == 'triangulo' or poligono == '1':
            base = float(input('Define una base para el triangulo:'))
            altura = float(input('Define una altura para el triangulo:'))
            area = (base*altura)/2
            return 'El area de tu poligono es de {} unidades cuadradas.'.format(area)
        elif poligono == 'Cuadrado' or poligono == 'cuadrado' or poligono == '2':
            lado = float(input('Define una longitud para cada lado:'))
            area = lado*lado
            return 'El area de tu poligono es de {} unidades cuadradas.'.format(area)
        elif poligono == 'Rectangulo' or poligono == 'rectangulo' or poligono == '3':
            base = float(input('Define una base para el rectangulo:'))
            altura = float(input('Define una altura para el rectangulo:'))
            area = base*altura
            return 'El area de tu poligono es de {} unidades cuadradas.'.format(area)      
        else:
            print('Debes introducir un poligono que sea valido.')   # Este mensaje saldra por pantalla en el caso de 
                                                                # el usuario no poporcione una respuesta valida.
        
        
if __name__ == '__main__':
    print('\n'*3)
    poligono = input('''Por favor, introduce el poligono del que quieras calcular su area
                                 ---- [Triangulo/ Cuadrado / Rectangulo] ---- :''')
    print(calcularAreaPoligono(poligono))
        