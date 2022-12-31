#/*
#* Escribe una función que calcule si un número dado es un número de Armstrong
#* (o también llamado narcisista).
#* Si no conoces qué es un número de Armstrong, debes buscar información 
#* al respecto.
#*/

def armstrong(num):
    listaResultados = []
    for item in str(num):
        listaResultados.append(int(item) ** len(str(num)))
    
    resultado = 0
    for item in listaResultados:
        resultado += item
    
    if resultado == num:
        return True
    else:
        return False
    

if __name__ == '__main__':
    print(armstrong(8208))