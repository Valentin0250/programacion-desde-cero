"""
Ejercicio: Adivinar la contraseña secreta

Descripción:

1.El programa genera una contraseña numérica aleatoria de 3 dígitos (por ejemplo: 527).

2.El usuario debe intentar adivinar la contraseña completa.
3.Cada vez que el usuario hace un intento:
    El programa le dice cuántos dígitos son correctos y están en la posición correcta.
    Y cuántos dígitos son correctos pero están en posición incorrecta.

4.El juego termina cuando el usuario adivina exactamente la contraseña.
5.Al final, el programa muestra cuántos intentos necesitó.

Requisitos:

Crear una función para generar la contraseña aleatoria de 3 dígitos.
Crear una función para pedir el intento del usuario y validar que:
Sea un número de 3 dígitos.
Crear una función para comparar el intento con la contraseña y devolver:
Cantidad de dígitos correctos en posición correcta.
Cantidad de dígitos correctos en posición incorrecta.
Usar un while para repetir hasta que el usuario acierte.
"""

import random

def numeroRandom () :
    return random.randint( 100 , 999 )

def adivinadorInteractivo () :
    while (True) :
        try:
            mensaje = int(input("Ingrese un numero con tres digitos:"))
            return  mensaje

        except ValueError :
            print("Error, ingrese un numero de tres digitos ej: 333")

def desguezar ( numAdivinador , numeroMisterioso) :

    numAdivinador3 = 0
    numAdivinador2 = 0
    numAdivinador1 = 0

    numAdivinador3 = numAdivinador % 10
    numAdivinador = (numAdivinador - numAdivinador3) / 10

    numAdivinador2 = numAdivinador % 10
    numAdivinador = (numAdivinador - numAdivinador2) / 10
    
    numAdivinador1 = numAdivinador

    numeroMisterioso3 = 0
    numeroMisterioso2 = 0
    numeroMisterioso1 = 0

    numeroMisterioso3 = numeroMisterioso % 10
    numeroMisterioso = (numeroMisterioso - numeroMisterioso3) / 10

    numeroMisterioso2 = numeroMisterioso % 10
    numeroMisterioso = (numeroMisterioso - numeroMisterioso2) / 10
    
    numeroMisterioso1 = numeroMisterioso

    listilla = [ numeroMisterioso3 , numeroMisterioso2 , numeroMisterioso1 , numAdivinador3 , numAdivinador2 , numAdivinador1]
    return listilla

def comparar ( numAdivinador , numeroMisterioso ) :

    if ( numAdivinador == numeroMisterioso ) :
        print("Felicidades adivinaste, te ganaste una palmadita")
        return True

    lista = desguezar (numAdivinador , numeroMisterioso)

    if( lista[5] == lista[2] ) :
        print("El primer numero es correcto")
    elif( lista[5] == lista[1] ) :
        print("El primer numero es correcto, pero posicion incorrecta")
    elif( lista[5] == lista[0]) :
        print("El primer numero es correcto, pero en posicion incorrecta")
    else :
        print("EL primer numero no es correcto")
       

    if( lista[4] == lista[1] ) :
        print("El segundo numero es correcto")
    elif( lista[4] == lista[2] ) :
        print("El segundo numero es correcto, pero en posicion incorrecta")
    elif( lista[4] == lista[0] ) :
        print("El segundo numero es correcto, pero en posicion incorrecta")
    else :
        print("El segundo numero no es correcto")


    if( lista[3] == lista[0]) :
        print("El tercer numero es correcto")
    elif( lista[3] == lista[2] ) :
        print("El tercer numero es correcto, pero posicion incorecta")
    elif( lista[3] == lista[1] ) :
        print("El tercer numero es correcto, pero posicion incorrecta")
    else :
        print("El tercer numero no es correcto")

    return False
   
def juegoDelSiglo () :
    numeroGenerado = numeroRandom ()
    numeroDeIntentos = 0

    while (True) :
        adivinador = adivinadorInteractivo ()
        numeroDeIntentos += 1
        print("----------------------------------------------------------------------------")
        if comparar ( adivinador , numeroGenerado ) :
            print("Intentos realizados:" , numeroDeIntentos , "<3")
            break

    input("Aprete enter para salir...     no se olvide sus cosas...")

juegoDelSiglo()