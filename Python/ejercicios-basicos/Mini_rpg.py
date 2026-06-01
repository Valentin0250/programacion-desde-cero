"""
EJERCICIO INTEGRADOR: “Mini RPG de combate por turnos”

Vas a crear un pequeño juego de consola donde el jugador pelea contra un enemigo.

La idea es simular un combate tipo RPG clásico.

El jugador tiene que derrotar a un enemigo en combate por turnos.

Cada uno tiene:

vida (HP)
ataque
defensa

El jugador puede elegir acciones:

atacar
curarse
rendirse

El enemigo ataca automáticamente.

REQUISITOS

1. Variables y tipos de datos

vida jugador (int)
vida enemigo (int)
nombre jugador (string)
daño (int)
booleano de juego activo

2. Entrada y salida

input() para nombre del jugador
print() para mostrar estado del combate

3. Random

daño aleatorio del jugador
daño aleatorio del enemigo

4. Condicionales
si vida <= 0 → gana o pierde
si elige opción inválida

5. El juego sigue mientras ambos tengan vida > 0

6. funciones
atacar()
curar()
estado_juego()

7. listas
lista de acciones del jugador
historial de ataques
"""

import time
import os   
import random

# CONFIGURACIONES BASICAS DEL JUEGO     
VIDA_MAXIMA = 100
DANIO_HUEVO = 5
VELOCIDAD_TEXTO = 0.1
#FUNCIONES

def imprimirTexto( texto, velocidad = VELOCIDAD_TEXTO) :
    for caracter in texto:
        print(caracter, end="", flush=True)
        time.sleep(velocidad)
        
def aplicarDaño (vida , daño) :
    vida = max (vida - daño , 0)
    return vida

def curarHeroe (vida , curar) :
    vida = min (vida + curar , VIDA_MAXIMA)
    return vida

def resultadoProbalidad33 () :

    accion = random.randint ( 1 , 3 )

    if accion <= 2 :
       return True
    else :
       return False

def eventoHuevo () :

    posibilidad = random.randint ( 1 , 100 )
    
    if posibilidad <= 30 :
        return True
    else :
        return False

def nombrarHeroe () :
    while(True) :
        try:
            heroe = str(input("Nombrar al heroe: "))
            return heroe
        except ValueError :
            print("Error")

def elegirOpciones () :
    while(True) :
        try:
            numero = int(input("Elegi una de las opciones para combatir: "))
            return numero
        except ValueError :
            print("Error, vuelva a intentar")

def imprimirMensajesDeAccion (opcion , nombre, curar, vidaHeroe) :
    match (opcion) :
        case 1 :
            nombre
        case 2 :
            print(f"{nombre} a usado curar, se a curado {curar}. Vida total: {vidaHeroe}")
        case 3 :
            print("Te has retirado...")
        case _ :
            print("Error, vuelva a intentar")

def imprimirMensajesDeAtaque (eleccion , nombre , daño1 , daño2, vidaEnemigo, variable) :
    match (eleccion) :
        case 1 :
            print(f"Ataque de {nombre} acertado, aplico {daño1} al enemigo. Vida del enemigo: {vidaEnemigo} ")
        case 2 :
            if variable == True :
                print(f"Ataque con probabilidad de {nombre} acertado, aplico {daño2} al enemigo. Vida del enemigo: {vidaEnemigo}")
            else :
                print(f"El ataque de {nombre} a fallado... Vida del enemigo: {vidaEnemigo}")

def imprimirOpcionesDeAccion (vida, nombre , vida2) :
    print(f"Vida de {nombre}: {vida}")
    print(f"Vida del enemigo: {vida2}")
    print("Atacar: 1")
    print("Curarse: 2")
    print("Rendirse: 3")

def imprimirOpcionesDeAtaque () :
    print("1 : Ataque normal")
    print("2 : Ataque con probabilidades")
    print("3 : Volver menu anterior")

def listarMovimientos (array) :
    for i , movimiento in enumerate (array) :
        print(f"{i} : {movimiento}")

def separarTurnos () :
    for i in range (0, 100) :
        print("-", end="")
    print("")

def verificarGanador (vidaHeroe, vidaEnemigo, movimientos) :

    if vidaHeroe <= 0 and vidaEnemigo <= 0 :
        separarTurnos ()
        print("Lo diste todo hasta el final... te recordaremos como un heroe")
    elif vidaHeroe <= 0 :
        separarTurnos ()
        print("Perdiste...")
    elif vidaEnemigo <= 0:
        separarTurnos ()
        print("Has ganado, eres todo un heroe")

    listarMovimientos(movimientos)
    print("Muchas gracias por jugar")

def menuAtaques (eleccion, vidaEnemigo, dañoHeroe, movimientos, dañoheroe2, variable) :

    match  eleccion :
        case 1 :
            vidaEnemigo = aplicarDaño (vidaEnemigo , dañoHeroe)
            movimientos.append (f"Ataque: {dañoHeroe}")
            return vidaEnemigo
        case 2 :
            if variable == True :
                vidaEnemigo = aplicarDaño (vidaEnemigo , dañoheroe2)
                movimientos.append (f"Ataque con probabilidad: {dañoheroe2}")
                return vidaEnemigo
            else :
                movimientos.append ("Ataque fallido: 0")
                return vidaEnemigo
        case 3 :
            return vidaEnemigo

def AtaqueEnemigo (vidaHeroe, dañoEnemigo, probabilidad) :

    if probabilidad :
            vidaHeroe = aplicarDaño (vidaHeroe , dañoEnemigo)
            print(f"Te golpearon, has recibido {dañoEnemigo}, vida total del heroe: {vidaHeroe}")
            return vidaHeroe
    else :
        print(f"El enemigo a fallado su ataque, vida total del heroe: {vidaHeroe}")
        return vidaHeroe

def ataqueHuevoLetal (huevo, vidaEnemigo) :
    if  eventoHuevo() and huevo:
            vidaEnemigo = aplicarDaño( vidaEnemigo , DANIO_HUEVO )
            huevo = False
            print(f"Un heroe amigo dezconocido, le arrojo un huevo al enemigo aplica {DANIO_HUEVO} de daño. Vida del enemigo: {vidaEnemigo}")
            return vidaEnemigo
    else :
        return vidaEnemigo

def juego_4 () :

    os.system('cls')

    vidaHeroe = VIDA_MAXIMA
    vidaEnemigo = VIDA_MAXIMA
    movimientos = []
    huevo = True
    eleccion = 1

    print("Hola heroe, bienvenido al combate... no tenemos tiempo di tu nombre y preparate para LUCHAR")
    nombre = nombrarHeroe ()
    
    while (True) :

        if vidaEnemigo <= 0 or vidaHeroe <= 0 :
            verificarGanador (vidaHeroe, vidaEnemigo, movimientos)
            break

        curar = random.randint (8 , 15)
        dañoHeroe = random.randint (10 , 20)
        dañoHeroe2 = random.randint (20 , 25)
        dañoEnemigo = random.randint (10 , 20)
        probabilidadHeroe = resultadoProbalidad33 ()
        probabilidadEnemigo = resultadoProbalidad33 ()

        os.system('cls')

        imprimirOpcionesDeAccion (vidaHeroe , nombre , vidaEnemigo)

        opcion = elegirOpciones ()

        match opcion :
            case 1 :
                separarTurnos()
                imprimirOpcionesDeAtaque ()
                eleccion = elegirOpciones()
                vidaEnemigo = menuAtaques (eleccion, vidaEnemigo, dañoHeroe, movimientos, dañoHeroe2, probabilidadHeroe)
                separarTurnos()
                imprimirMensajesDeAtaque (eleccion , nombre , dañoHeroe , dañoHeroe2, vidaEnemigo, probabilidadHeroe)
                
            case 2 :
                separarTurnos()
                vidaHeroe = curarHeroe (vidaHeroe , curar)
                movimientos.append (f"Curacion: {curar}")
            case 3 :
                separarTurnos()
                movimientos.append ("Retirada")
                listarMovimientos(movimientos)
                print(f"{nombre} se a retirado...")
                break

        imprimirMensajesDeAccion (opcion, nombre, curar , vidaHeroe)

        if eleccion == 3 :
            pass
        else :
            vidaHeroe = AtaqueEnemigo (vidaHeroe, dañoEnemigo, probabilidadEnemigo)
            vidaEnemigo = ataqueHuevoLetal (huevo, vidaEnemigo)

        input("Enter para volver atras")

if __name__ == "__main__" :
    juego_4 ()



