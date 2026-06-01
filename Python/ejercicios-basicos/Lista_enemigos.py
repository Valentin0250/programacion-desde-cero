"""
Ejercicio: “Lista de enemigos”

Vas a crear un sistema simple para manejar enemigos en un juego.

Requisitos

1. Crear una lista que almacene los enemigos como strings, por ejemplo "Goblin", "Orco", "Dragón".

2. Crear funciones para:
> agregar_enemigo(lista, enemigo="Slime") → añade un enemigo; si no se pasa, añade "Slime" por defecto.
> eliminar_enemigo(lista, enemigo) → elimina al enemigo de la lista si existe.
> mostrar_enemigos(lista) → muestra todos los enemigos con su índice.
> buscar_enemigo(lista, enemigo) → devuelve True si el enemigo está, False si no.

3. Probar las funciones agregando, eliminando y buscando enemigos.
"""

import os

def agregarEnemigo ( lista , enemigo ) :
    if ( enemigo ) :
        lista.append(enemigo)
    else :
        lista.append("Slime")

def eleminarEnemigo ( lista , enemigo ) :
    lista.remove( enemigo )

def imprimirEnemigos ( lista ) :
    for i in range ( 0 , len(lista) , 1 ) :
        print(i ,":" + lista[i])

def buscarEnemigo ( lista , enemigo ) :
    if enemigo in lista :
        print("True")
    else :
        print("False")

def recibirDatosUsuarios (mensaje = "Ingrese un numero entero: ") :
    while (True) :
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error, vuelva a intentar")

def mostrarOpcionesDelMenu () :
    print("Bienvenido a la lista de enemigos")
    print("1: Agrega un enemigo a la lista")
    print("2: Elemina a un enemigo de la lista")
    print("3: Ver lista de enemigo")
    print("4: Mostrar si el enemigo esta en la lista")
    print("5: salir")

def listarEpicamente ( opc ) :

    objeto = ""

    match( opc ) :
        case ( 1 ):
            objeto = input("Agregar a un enemigo a la lista: ")
        case ( 2 ):
            objeto = input("Eliminar a un enemigo de la lista: ")
        case ( 3 ):
            print("Lista de enemigo completa: ")
        case ( 4 ):
            objeto = input("Buscar enemigo por nombre: ")
        case ( 5 ):
            print("Saliendo...")
        case _ :
            print("Error, vuelva intentar...")
    
    return objeto

def ejecutarJuego_3 () :

    array = [ "Goblin" , "Orco" , "Dragon" ]

    while( True ):
        
        mostrarOpcionesDelMenu ()

        dato = recibirDatosUsuarios ("Poner numero deacuerdo a las opciones: ")

        os.system('cls')

        objeto = listarEpicamente (dato)

        match (dato) :
            case ( 1 ):
                agregarEnemigo(array , objeto) 
            case ( 2 ):
                eleminarEnemigo(array , objeto)
            case ( 3 ):
                imprimirEnemigos (array)
            case ( 4 ):
                buscarEnemigo (array , objeto)
            case ( 5 ):
                break
        input("Enter para volver atras")

        os.system('cls')

ejecutarJuego_3 ()