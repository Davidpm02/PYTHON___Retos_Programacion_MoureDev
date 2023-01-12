#/*
#* Crea un programa que calcule quien gana más partidas al piedra,
#* papel, tijera.
#* - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#* - La función recibe un listado que contiene pares, representando cada jugada.
#* - El par puede contener combinaciones de "R" (piedra), "P" (papel)
#*   o "S" (tijera).
#* - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
#*/


# piedra = 'R'
# papel = 'P'
# tijeras = 'S'

jugadaN1 = [('R','P'),('R','S'),('P','P')]

def ganador(puntosJ1,puntosJ2):
    """Funcion que evalua las puntuaciones de dos jugadores e imprime un resultado por pantalla en funcion del mismo.
       args:
       - puntosJ1 --> Representa la puntuacion del Jugador1
       - puntosJ2 --> Representa la puntuacio del Jugador2
    """
    if puntosJ1 > puntosJ2:
        print('Player 1')
    elif puntosJ2 > puntosJ2:
        print('Player 2')
    elif puntosJ1 == puntosJ2:
        print('Tie')


def comprobarGanador(jugada):
    puntosJ1 = 0
    puntosJ2 = 0
    for par in jugada:
        if par[0] == 'R' and par[1] == 'P':
            puntosJ1 +=1
        elif par[0] == 'R' and par[1] == 'R':
            continue
        elif par[0] == 'R' and par[1] == 'S':
            puntosJ2 +=1  
        elif par[0] == 'P' and par[1] == 'P':
            continue
        elif par[0] == 'P' and par[1] == 'S':
            puntosJ2 +=1
        elif par[0] == 'P' and par[1] == 'R':
            puntosJ1 +=1
        elif par[0] == 'S' and par[1] == 'S':
            continue
        elif par[0] == 'S' and par[1] == 'R':
            puntosJ2 +=1
        elif par[0] == 'S' and par[1] == 'P':
            puntosJ1 +=1
    else:                               # Cuando acabe de ejecutarse el bucle for, se invoca la funcion 'ganador()', que imprimira 
        ganador(puntosJ1,puntosJ2)      # el resultado por pantalla en funcion de las puntuaciones de los jugadores.
        
if __name__ == '__main__':
    comprobarGanador(jugadaN1)
          
        