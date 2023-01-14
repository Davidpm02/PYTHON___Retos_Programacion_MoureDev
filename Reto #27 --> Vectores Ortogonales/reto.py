#/*
#* Crea un programa que determine si dos vectores son ortogonales.
#* - Los dos array deben tener la misma longitud.
#* - Cada vector se podría representar como un array. Ejemplo: [1, -2]
#*/

def ortogonal(vector1,vector2):
    """Funcion con dos parametros que representan cada uno un array con las coordenadas de un vector.
       La funcion se encarga de calcular un producto escalar entre estos dos vectores pasados como argumentos a la funcion
       y retornar un resultado u otro en funcion de si el producto es igual a 0 o no.
    """
    
    producto_escalar = vector1[0]*vector2[0] + vector1[1]*vector2[1]
    
    if producto_escalar == 0:
        return 'Los vectores dados son ortogonales.'
    elif producto_escalar != 0:
        return 'Los vectores dados no son ortogonales.'


if __name__ == '__main__':
    vector1 = [1,2]
    vector2 = [2,-1]
    print(ortogonal(vector1,vector2))