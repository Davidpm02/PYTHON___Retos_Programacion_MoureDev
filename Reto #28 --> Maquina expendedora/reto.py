#/*
#* Simula el funcionamiento de una máquina expendedora creando una operación
#* que reciba dinero (array de monedas) y un número que indique la selección
#* del producto.
#* - El programa retornará el nombre del producto y un array con el dinero
#*   de vuelta (con el menor número de monedas).
#* - Si el dinero es insuficiente o el número de producto no existe,
#*   deberá indicarse con un mensaje y retornar todas las monedas.
#* - Si no hay dinero de vuelta, el array se retornará vacío.
#* - Para que resulte más simple, trabajaremos en céntimos con monedas
#*   de 5, 10, 50, 100 y 200.
#* - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
#*/

import time


class BotellaAgua():
    nombre = 'Botella de Agua'
    precio = 80
    nProducto = 1
    
class BolsaPatatas():
    nombre = 'Bolsa de Patatas'
    precio = 120
    nProducto = 2
    
class Golosina():
    nombre = 'Golosina'
    precio = 100
    nProducto = 3



def maquinaExpendedora(listaMonedas):
    """Funcion parametrizada que actua como maquina expendedora.
    Parametros:
        - listaMonedas: es una lista de enteros que el usuario debe pasar como argumento al momento de invocar la funcion.
        En funcion de los enteros que compongan la lista, y del producto que haya seleccionado para comprar, la funcion tomara
        un camino u otro, imprimiendo por pantalla un resultado u otro.
    """
    monedasPermitidas = [5,10,50,100,200]
    botellaAgua = BotellaAgua()
    bolsaPatatas = BolsaPatatas()
    golosina = Golosina()
    
    for moneda in listaMonedas:
            if moneda in monedasPermitidas:
                continue
            else:
                print('Se ha introducido una moneda no permitida(de {} centimos). Las monedas de centimos permitidas son: 5,10,50,100 y 200.'.format(moneda))
                return 
    
    
    
    try:
        producto = int(input("""Seleccione el producto que desee:
                    1. Botella de agua
                    2. Bolsa de patatas
                    3. Golosina
                    """))
        assert producto > 0 and producto < 4
        
        total_dinero_introducido = sum(listaMonedas)
        
        if producto == 1:
            if botellaAgua.precio > total_dinero_introducido:
                print('No has introducido el importe total necesario del producto. Se te devolvera el dinero introducido.')
                time.sleep(1)
                print('Se te han devuelto {} centimos.'.format(total_dinero_introducido))
                return
   
            elif botellaAgua.precio == total_dinero_introducido:
                print('Producto seleccionado: {}'.format(botellaAgua.nombre))
                print('Entregando su producto...')
                time.sleep(3)
                print('Disfruta tu {}!'.format(botellaAgua.nombre))
                return 
            
            elif botellaAgua.precio < total_dinero_introducido:
                print('Producto seleccionado: {}'.format(botellaAgua.nombre))
                print('Entregando su producto...')
                time.sleep(3)
                print('Disfruta tu {}!'.format(botellaAgua.precio))
                dineroSobrante = total_dinero_introducido - botellaAgua.precio
                print('Te han sobrado {} centimos.'.format(dineroSobrante))
                return

        elif producto == 2:
            if bolsaPatatas.precio > total_dinero_introducido:
                print('No has introducido el importe total necesario del producto. Se te devolvera el dinero introducido.')
                time.sleep(1)
                print('Se te han devuelto {} centimos.'.format(total_dinero_introducido))
                return
   
            elif bolsaPatatas.precio == total_dinero_introducido:
                print('Producto seleccionado: {}'.format(bolsaPatatas.nombre))
                print('Entregando su producto...')
                time.sleep(3)
                print('Disfruta tu {}!'.format(bolsaPatatas.nombre))
                return 
            
            elif bolsaPatatas.precio < total_dinero_introducido:
                print('Producto seleccionado: {}'.format(bolsaPatatas.nombre))
                print('Entregando su producto...')
                time.sleep(3)
                print('Disfruta tu {}!'.format(bolsaPatatas.nombre))
                dineroSobrante = total_dinero_introducido - bolsaPatatas.precio
                print('Te han sobrado {} centimos.'.format(dineroSobrante))
                return
        elif producto == 3:
            if golosina.precio > total_dinero_introducido:
                print('No has introducido el importe total necesario del producto. Se te devolvera el dinero introducido.')
                time.sleep(1)
                print('Se te han devuelto {} centimos.'.format(total_dinero_introducido))
                return
   
            elif golosina.precio == total_dinero_introducido:
                print('Producto seleccionado: {}'.format(golosina.nombre))
                print('Entregando su producto...')
                time.sleep(3)
                print('Disfruta tu {}!'.format(golosina.nombre))
                return 
            
            elif golosina.precio < total_dinero_introducido:
                print('Producto seleccionado: {}'.format(golosina.nombre))
                print('Entregando su producto...')
                time.sleep(3)
                print('Disfruta tu {}!'.format(golosina.nombre))
                dineroSobrante = total_dinero_introducido - golosina.precio
                print('Te han sobrado {} centimos.'.format(dineroSobrante))
                return
            
            
            
            
            
    except AssertionError:
        print('El producto seleccionado no existe en la maquina.')
        print('Por favor, seleccione un producto valido.')
    
        
        
    
    
if __name__ == '__main__':
    maquinaExpendedora([10,100])
    
    
