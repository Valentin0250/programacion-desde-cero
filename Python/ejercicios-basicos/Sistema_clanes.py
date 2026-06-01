"""
Ejercicio: Sistema de clanes de un MMORPG

Creá un programa para administrar clanes dentro de un videojuego online.

Cada clan debe tener:

    nombre del clan
    líder
    cantidad de miembros
    nivel del clan
    puntos de guerra
    oro del clan
    región
    si el clan está activo o disuelto

El programa debe permitir:

1.Crear clanes.
2.Mostrar todos los clanes.
3.Buscar un clan por nombre.
4.Mostrar únicamente los clanes activos.
4.Mostrar únicamente los clanes disueltos.
5.Cambiar el estado de un clan.
6.Subir el nivel de un clan.
7.Agregar miembros.
8.Expulsar miembros.
9.Mostrar el clan con más miembros.
10.Mostrar el clan con más oro.
11.Mostrar el clan con mayor nivel.
12.Calcular el promedio de miembros entre todos los clanes.
13.Contar cuántos clanes hay por región.
14.Eliminar clanes.
15.Ordenar clanes por nivel.
16.Ordenar clanes por puntos de guerra.
17.Mostrar el oro total entre todos los clanes.
18.Salir mediante un menú.
"""

import os

def agregarClan(clanes, datos): #1
    clanes.append(datos) 

def mostrarClanes(clanes): #2
    for i ,clan in enumerate (clanes, 0):
        print(f"{i+1}- \nNombre del clan: {clan["nombre"]} \nLider: {clan["lider"]} \nCantidad de miembros: {clan["miembros"]} \nNivel del clan: {clan["nivel"]} \nPuntos de guerra: {clan["puntos"]} \nOro del clan: {clan["oro"]} \nRegion: {clan["region"]} \nEstado: {clan["estado"]}") 

def buscarClanPorNombre(clanes, nombre): #3
    validar = True
    for clan in clanes:
        if clan["nombre"] == nombre:
            validar = False
            print(f"Se encontro el clan : {clan["nombre"]}")
    if validar == True:
        print(f"No se a encontrado un clan con el nombre: {nombre}")

def mostrarClanesActivos(clanes): #4
    for clan in clanes:
        if clan["estado"] == "activo":
            print(f"{clan["nombre"]} - {clan["estado"]}")
    
def mostrarClanesDisueltos(clanes): #5
    for clan in clanes:
        if clan["estado"] == "disuelto":
            print(f"{clan["nombre"]} - {clan["estado"]}")

def cambiarEstadoClan(clanes, nombre): #6
    for clan in clanes:
        if clan["nombre"] == nombre:
            if clan["estado"] == "activo":
                clan["estado"] = "disuelto"
                print(f"{clan["nombre"]} - {clan["estado"]}")
            else:
                clan["estado"] = "activo"
                print(f"{clan["nombre"]} - {clan["estado"]}")

def subirNivelClan(clanes,nombre): #7
    for clan in clanes:
        if clan["nombre"] == nombre:
            clan["nivel"] += 1
            print(f"Clan: {clan["nombre"]} - Nivel: {clan["nivel"]}")

def agregarMiembros(clanes,nombre, numero): #8
    for clan in clanes:
        if clan["nombre"] == nombre:
            clan["miembros"] += numero
            if clan["miembros"] > 200:
                clan["miembros"] = 200
            print(f"Clan: {clan["nombre"]} - Miembros: {clan["miembros"]}")

def expulsarMiembros(clanes,nombre, numero): #9
    for clan in clanes:
        if clan["nombre"] == nombre:
            clan["miembros"] -= numero
            if clan["miembros"] < 0:
                clan["miembros"] = 1
            print(f"Clan: {clan["nombre"]} - Miembros: {clan["miembros"]}")

def mostrarClanMultitud(clanes): #10
    multitud = 0
    nombre = ""
    for clan in clanes:
        if multitud == 0:
            multitud = clan["miembros"]
            nombre = clan["nombre"]
        if multitud < clan["miembros"]:
            multitud = clan["miembros"]
            nombre = clan["nombre"]
    print(f"Clan: {nombre} - Miembros: {multitud}")

def mostrarClanOro(clanes): #11
    oro = 0
    nombre = ""
    for clan in clanes:
        if oro == 0:
            oro = clan["oro"]
            nombre = clan["nombre"]
        if oro < clan["oro"]:
            oro = clan["oro"]
            nombre = clan["nombre"]
    print(f"Clan: {nombre} - Oro del clan: {oro}")

def mostrarClanNivel(clanes): #12
    nivel = 0
    nombre = ""
    for clan in clanes:
        if nivel == 0:
            nivel = clan["nivel"]
            nombre = clan["nombre"]
        if nivel < clan["nivel"]:
            nivel = clan["nivel"]
            nombre = clan["nombre"]
    print(f"Clan: {nombre} - Nivel del clan: {nivel}")

def calcularPromedioMiembros(clanes): #13
    acumulador = 0
    divisor = 0
    for i, clan in  enumerate (clanes,1):
        acumulador += clan["miembros"]
        divisor = i
    
    resultado = acumulador / divisor
    print(f"Promedio de miembros de los clanes: {resultado}")

def calcularClanesPorRegion(clanes, nombre): #14
    for clan in clanes:
        if clan["region"] == nombre:
            print(f"Clan: {clan["nombre"]} - Region: {clan["region"]}")

def eliminarClanes(clanes, nombre): #15
    for clan in clanes:
        if clan["nombre"] == nombre:
            clanes.remove(clan)
            print(f"Clan {nombre} se a eliminado")

def ordenarPorNivel(clanes): #16
    copia = clanes.copy()
    resultado = []

    while(copia):
        nivel = 0

        for clan in copia:
            if nivel < clan["nivel"]:
                nivel = clan["nivel"]

        for clan in copia:
            if nivel == clan["nivel"]:
                resultado.append(clan)
                copia.remove(clan)
                break
    
    for clan in resultado:
        print(f"Clan: {clan["nombre"]} - Nivel: {clan["nivel"]}")
    
def OrdenarPorPuntosGuerra(clanes): #17
    copia = clanes.copy()
    resultado = []

    while(copia):
        puntos = 0

        for clan in copia:
            if puntos < clan["puntos"]:
                puntos = clan["puntos"]

        for clan in copia:
            if puntos == clan["puntos"]:
                resultado.append(clan)
                copia.remove(clan)
                break
    
    for clan in resultado:
        print(f"Clan: {clan["nombre"]} - Puntos de guerra: {clan["puntos"]}")

def mostrarOroTotal(clanes): #18
    oro = 0
    for clan in clanes:
        oro += clan["oro"]
    print(f"Oro total de todos los clanes: {oro}")

          
def validarNum (mensaje,numeroMaximo):

    while(True):
        try:
            numero = int(input(mensaje))
            if numero >= 0 and numero <=numeroMaximo:
                return numero
            else:
                print("Error, vuelva a intentar")
        except ValueError:
            print("Error, vuelva a intentar")

def perdirDatos():
    nombre = input("Nombre del clan: ")
    lider = input("Nombre del lider del clan: ")
    miembros = validarNum("Numero de miembros(max 200) del clan: ", 200)
    nivel = validarNum("Nivel(max 100) del clan: ", 100)
    puntos = validarNum("Cantidad de puntos(max 10000) del clan: ", 10000)
    oro = validarNum("Cantidad de oro(max 10000) del clan: ", 10000)
    region = input("Region del clan: ")
    estado = "activo"

    hola = {
        "nombre":nombre,
        "lider":lider,
        "miembros":miembros,
        "nivel":nivel,
        "puntos":puntos,
        "oro":oro,
        "region":region,
        "estado":estado
    }
    return hola

def pedirTexto(mensaje):
    while(True):
        try:
            texto=input(mensaje)
            return texto
        except ValueError:
            print("Error, vuelva a intentar")

def pedirNum(mensaje):
    while(True):
        try:
            numero=int(input(mensaje))
            return numero
        except ValueError:
            print("Error, vuelva a intentar")

def textoInicial():
    print("1: Crear clanes")
    print("2: Mostrar todos los clanes")
    print("3: Buscar clan por nombre")
    print("4: Mostrar clanes activos")
    print("5: Mostrar clanes disueltos")
    print("6: Cambiar el estado de un clan")
    print("7: Subir de nivel a un clan")
    print("8: Agregar miembros")
    print("9: Expulsar miembros")
    print("10: Mostrar clan con mas gante")
    print("11: Mostrar al clan mas rico")
    print("12: Mostrar el clan con mas nivel")
    print("13: Promedio de miembros de los clanes")
    print("14: Clanes por regiones")
    print("15: Eliminar clanes")
    print("16: Ordenar clanes por nivel")
    print("17: Ordenar clanes por puntos de guerra")
    print("18: Mostrar oro total entre clanes")
    print("19: Salir")

def textoOpciones(opciones):
    match(opciones):
        case 1:
            print("Ahora se le pedira datos para poder crear un clan.")
        case 2:
            print("Estos son todos los clanes que tenemos registrados.")
        case 3:
            print("Tendra que poner el nombre del que buscamos.")
        case 4:
            print("Estos mantienen vivo el juego.")
        case 5:
            print("Ya volveran... siempre vuelven.")
        case 6:
            print("A revivir a los muertos o a enterrar a los vivos.")
        case 7:
            print("Si el clan ya alcanzo el nivel 100, queda en 100.")
        case 8:
            print("Camaradas nuevos para la aventura.")
        case 9:
            print("No todo dura para siempre.")
        case 10:
            print("Es el boquita de los clanes.")
        case 11:
            print("Pusieron la tarjeta.")
        case 12:
            print("Cuidado con estos.")
        case 13:
            print("Promedio de miembro entre clanes.")
        case 14:
            print("Estan todos ubicados en puntos estrategicos.")
        case 15:
            print("A desaparecer parasitos.")
        case 16:
            print("Los tops globales.")
        case 17:
            print("Son todos unos grandes guerreros.")
        case 18:
            print("Si tan solo se llevaran todos bien.")
        case 19:
            print("Saliendo...")

def ejecucionPrincipal ():
    clanes = []

    while(True):
        os.system("cls")

        textoInicial()

        opciones = pedirNum("Eligir segun las opciones: ")

        os.system("cls")

        textoOpciones(opciones)

        match(opciones):
            case 1:
                clan = perdirDatos()
                agregarClan(clanes, clan)
            case 2:
                mostrarClanes(clanes)
            case 3:
                nombre = pedirTexto("Nombre del clan: ")
                buscarClanPorNombre(clanes, nombre)
            case 4:
                mostrarClanesActivos(clanes)
            case 5:
                mostrarClanesDisueltos(clanes)
            case 6:
                nombre = pedirTexto("Nombre del clan: ")
                cambiarEstadoClan(clanes, nombre)
            case 7:
                nombre = pedirTexto("Nombre del clan: ")
                subirNivelClan(clanes, nombre)
            case 8:
                nombre = pedirTexto("Nombre del clan: ")
                numero = pedirNum("Numero de miembros(max 200):")
                agregarMiembros(clanes, nombre, numero)
            case 9:
                nombre = pedirTexto("Nombre del clan: ")
                numero = pedirNum("Numero de miembros a eliminar:")
                expulsarMiembros(clanes, nombre, numero)
            case 10:
                mostrarClanMultitud(clanes)
            case 11:
                mostrarClanOro(clanes)
            case 12:
                mostrarClanNivel(clanes)
            case 13:
                calcularPromedioMiembros(clanes)
            case 14:
                nombre = pedirTexto("Nombre de la region: ")
                calcularClanesPorRegion(clanes, nombre)
            case 15:
                nombre = pedirTexto("Nombre del clan a eliminar: ")
                eliminarClanes(clanes, nombre)
            case 16:
                ordenarPorNivel(clanes)
            case 17:
                OrdenarPorPuntosGuerra(clanes)
            case 18:
                mostrarOroTotal(clanes)
            case 19:
                break
        input()


if __name__=="__main__" :
    ejecucionPrincipal()