"""
Ejercicio: Juego de adivinar el número

Descripción:

1.El programa genera un número aleatorio entre 1 y 50.
2.El usuario tiene que adivinar el número.
3.Cada vez que el usuario hace un intento, el programa le dice si el número es más alto o más bajo que su intento.
4.Cuando el usuario acierta, el programa le dice cuántos intentos le tomó.
"""

import random

def generarNum1a50 ( ) :
    return random.randint( 1 , 50 )

def validarNum ():
    while ( True ) :
        try :
            intento = int(input("Igresar numero valido: "))
            return intento
        except ValueError :
            print("Error, ponga un numero entero")

def compararNum ( numero , numeroMisterioso ) :
    if numero < numeroMisterioso :
        print("Es mas grande que el numero dado")
    elif numero > numeroMisterioso :
        print("Es mas chico que el numero dado")
    else :
        print("Correcto, es el mismo numero dado")

def ejecutarJuego () :
    numeroGenerado = generarNum1a50 ()
    numeroDeIntentos = 0

    while (True) :
            numeroAdivinador = validarNum ()
            compararNum( numeroAdivinador , numeroGenerado )
            numeroDeIntentos += 1
            if numeroAdivinador == numeroGenerado :
                print("Intentos: " , numeroDeIntentos)
                break
ejecutarJuego ()