"""
Ejercicio: “Gestor de inventario de un juego”

Crear un pequeño sistema de inventario para un juego de rol.

Requisitos
1. Crear una lista que almacene los objetos del inventario.
2. Crear funciones para:
> agregar_objeto(inventario, objeto) → añade un objeto a la lista.
> eliminar_objeto(inventario, objeto) → elimina un objeto de la lista si existe.
> mostrar_inventario(inventario) → imprime todos los objetos con índice.
> buscar_objeto(inventario, objeto) → devuelve True si el objeto está, False si no.
3. Probar las funciones con varios objetos, como "Espada", "Poción", "Escudo".
4. Usar al menos una función con parámetros por defecto, por ejemplo la funcion agregar_objeto podría agregar un objeto "Curita" si no se pasa ningún objeto.
"""
import os
 
def agregar_objeto ( inventario , x ) :
    if (x) :
        inventario.append(x)
    else :
        inventario.append("Curita")

def eliminar_objetos ( inventario , x ) :
    inventario.remove( x )

def mostrar_inventario (inventario) :
    for i in range ( 0 , len(inventario) , 1) :
        print(i , ":" + inventario[i] )

def buscar_objeto ( inventario , x ) :
    if x in inventario :
        print("True")
    else :
        print("False")


def opciones_elegir () :
    while (True) :
        try:
            mensaje = int(input("Numero para ingresar a las opciones del inventario:"))
            return mensaje
        except ValueError:
            print("Error")


def mostrarMenuInicial () :
    print("Opciones:")
    print("1: Agregar un objeto al inventario")
    print("2: Eliminar un objeto del inventario")
    print("3: Investigar inventario")
    print("4: Comprobar objeto dentro del inventario")
    print("5: Salir")

def validarNumeroEntero ( mensaje = "Ingrese numero entero: " ) :
    while(True) :
        try :
            numeroEntero = int(input(mensaje))
            return numeroEntero
        except ValueError :
            print("Error, vuelva a intentar")

def pedirEntradaDeDatos ( opc ) :

    objeto = ""

    match ( opc ) :
            case ( 1 ) :
                objeto = input("objeto agregable: ")
            case ( 2 ) :
                objeto = input("Eliminar objeto del inventario: ")
            case ( 3 ) :
                print("Inventario completo:")
            case ( 4 ) :
                objeto = input("Buscar objeto en inventario: ")
            case ( 5 ) :
                print("Saliendo...")
            case _ :
                print(input("Error, vuelva a intentar"))

    return objeto

def juego_siglo_xxi () :

    array = [ "Espada" , "Pocion" , "Escudo" ]

    while(True) :

        #muestra las opciones del menu
        mostrarMenuInicial ()

        #valida y guarda la opcion del usuario
        opcion = validarNumeroEntero ("Ingrese un numero correspondiente del menu: ")

        #clean to terminal
        os.system('cls')

        #pide la entrada de datos segun la opcion del usuario
        objeto = pedirEntradaDeDatos ( opcion )

        match ( opcion ) :
            case ( 1 ) :
                agregar_objeto ( array , objeto )
            case ( 2 ) :
                eliminar_objetos( array , objeto )
            case ( 3 ) :
                mostrar_inventario(array)
            case ( 4 ) :
                buscar_objeto( array , objeto )
            case ( 5 ) :
                break

        input("Enter para volver...")

        os.system('cls')
