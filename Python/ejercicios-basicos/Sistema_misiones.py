"""
Ejercicio: Sistema de misiones (quests) de un videojuego

Creá un programa que administre las misiones de un RPG.

Cada misión debe tener:

    nombre
    descripción
    dificultad
    recompensa en oro
    experiencia otorgada
    estado (pendiente, en progreso, completada)
    NPC que entrega la misión

El programa debe permitir:

1.Agregar misiones.
2.Mostrar todas las misiones.
3.Buscar una misión por nombre.
4.Mostrar solo las misiones pendientes.
5.Mostrar solo las misiones completadas.
6.Cambiar el estado de una misión.
7.Mostrar la misión con mayor recompensa.
8.Calcular la experiencia total de todas las misiones.
9.Contar cuántas misiones hay de una dificultad específica.
10.Eliminar misiones.
11.Ordenar misiones por recompensa.
12.Ordenar misiones por dificultad.
13.Mostrar cuántas misiones dio cada NPC.
14.Salir mediante un menú.
"""

import os

programaActivo = True

MAX_EXPERIENCIA= 100
MAX_ORO= 10000

def agregarMision (misiones):
    dificultad = ["dificil", "normal" , "facil"]
    estado = ["pendiente" , "en progreso" , "completada"]
    print("Ahora se le pedira unos datos para la mision.")
    mision= datosPedir(dificultad, estado)
    misiones.append(mision)

def mostrarMisiones (misiones):
    print("Estas son todas nuestras misiones de momento.")
    for i , mision in enumerate (misiones, 0):
        print(f"Mision - {i+1} : ")
        mostrarObjetoEnPantalla(mision)

def mostrarObjetoEnPantalla(equipo):
    for i, keys in enumerate(equipo, 0):
        print(f"{i+1}- {keys}: {equipo[keys]}")

def buscarPorNombre (misiones):
    print("Poniendo el nombre aparecera la mision con sus datos.")
    nombre = input("Nombre del objeto a buscar: ")
    variable = True
    for mision in misiones:
        if mision["nombre"] == nombre:
            variable = False
            print(f"{nombre} se a encontrado")
            mostrarObjetoEnPantalla(mision)
            break
    if variable:
        print(f"{nombre} no se a podido encontrar")

def imprimirMisiones(misiones, estado):
    for mision in misiones:
        if mision["estado"] == estado:
            mostrarObjetoEnPantalla(mision)

def mostrarMisionesPendiente (misiones):
    print("Mostrando todas nuestras misiones pendientes.")
    imprimirMisiones(misiones,"pendiente")

def mostrarMisionesEnProgreso (misiones):
    print("Mostrando todas nuestras misiones en progreso.")
    imprimirMisiones(misiones,"en progreso")

def mostrarMisionesCompleta (misiones):
    print("Mostrando todas nuestras misiones completadas.")
    imprimirMisiones(misiones,"completada")

def cambiarEstadoMision(misiones):
    print("Cambiando estado de la mision (pendiente/en progreso/completada) <3.")
    estado = ["pendiente" , "en progreso" , "completada"]
    nombre = input("Nombre de mision: ")
    estadoVariable = validar(estado, "Estado de mision que pasa a estar: ")
    valor = True
    for mision in misiones:
        if mision["nombre"] == nombre:
          valor = False
          mision["estado"] = estadoVariable
          print(f"Mision {nombre} cambio el estado: {estadoVariable}")
    if valor:
        print(f"No se encontro una mision con el nombre {nombre}")

def mostrarMisionMayorRecompensa(misiones):
    print("Esta es nuestra mision con mayor recompensa.")
    expGuardar = 0
    nomGuardar = ""
    for mision in misiones:
        if expGuardar == 0:
            expGuardar = mision["experiencia"]
            nomGuardar = mision["nombre"]
        if expGuardar < mision["experiencia"]:
            expGuardar = mision["experiencia"]
            nomGuardar = mision["nombre"]
    print(f"{nomGuardar} - experiencia: {expGuardar}")

def sumarExpTotal (misiones):
    print("Suma de la experiencia de todas nuestas misiones.")
    sumaFinal= 0
    for mision in misiones:
        sumaFinal += mision["experiencia"]
    print(f"Experiencia total: {sumaFinal}")

def mostrarMisionPorDificultad(misiones):
    print("Poner la dificultad que deseas ver (dificil/normal/facil).")
    dificultad = ["dificil", "normal" , "facil"]
    nombre = validar(dificultad, "Dificultad: ")
    for mision in misiones:
        if mision["dificultad"] == nombre:
            print(f"{mision['nombre']} - {mision['dificultad']}")
        
def eliminarMisiones (misiones):
    print("Una vez eliminada, la mision no volvera.")
    nombre = input("Nombre de mision a eliminar: ")
    valor = True 
    for mision in misiones:
        if mision["nombre"] == nombre:
            valor = False
            misiones.remove(mision)
            print(f"Se a eliminado correctamente la mision {nombre}")
    if valor:
        print(f"No se econtro una mision llamada {nombre}")

def ordenarMisionPorRecompensas (misiones):
    print("Ordenado por recompensa.")
    copia = misiones.copy()
    listaOrdenada = []
    
    while(copia):
        valor = 0

        for mision in copia:
            if valor < mision["recompensa en oro"]:
                valor = mision["recompensa en oro"]

        for mision in copia:
            if valor == mision["recompensa en oro"]:
                listaOrdenada.append(mision)
                break
        copia.remove(mision)
    mostrarMisiones(listaOrdenada)
                
def ordenarMisionPorDificultad (misiones):
    print("De la mas dificiles a las mas faciles.")
    for mision in misiones:
        if mision["dificultad"] == "dificil":
            print(f"{mision['nombre']} - {mision['dificultad']}")
    for mision in misiones:
        if mision["dificultad"] == "normal":
            print(f"{mision['nombre']} - {mision['dificultad']}")
    for mision in misiones:
        if mision["dificultad"] == "facil":
            print(f"{mision['nombre']}- {mision['dificultad']}")

def mostrarMisionesNpc (misiones):
    print("Poner nombre del npc que buscamos.")
    npc = 0
    nombre = input("Npc: ")
    valor = True
    for mision in misiones:
        if mision["npc"] == nombre:
            valor = False
            npc += 1
    if valor:
        print(f"No se a econtrado ningun npc con el nombre {nombre}")
    else:
        print(f"Npc: {nombre} - misiones: {npc}")

def validar(array,mensaje):

    while(True):
        volver = input(mensaje)

        if volver in array:
            return volver
        else:
            print("Error, ingrese un valor valido")
            input()

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

def datosPedir (array, array2):
    nombre = input("Nombre de mision: ")
    descripcion = input("Descripcion: ")
    dificultad = validar(array, "Difilcultad(dificil/normal/facil): ")
    recompensaEnOro = validarNum (f"Recompensa en oro(max {MAX_ORO}): ", MAX_ORO)
    experiencia = validarNum (f"Experiencia(max {MAX_EXPERIENCIA}): " , MAX_EXPERIENCIA)
    estado = validar(array2, "Estado(pendiente, en progreso, completada): ")
    npc =input("Nombre de npc: ")

    diccionario = {
        "nombre": nombre,
        "descripcion": descripcion,
        "dificultad": dificultad,
        "recompensa en oro": recompensaEnOro,
        "experiencia": experiencia,
        "estado": estado,
        "npc": npc
    }
    return diccionario

def numUsuario(mensaje):
    while(True):
        try:
            volver = int(input(mensaje))
            return volver
        except ValueError:
            print("Error, vuelva a intentar")

        
def menUsuario(mensaje):
    while(True):
        try:
            volver =input(mensaje)
            return volver
        except ValueError:
            print("Error, vuelva a intentar")

def imprimirTextoInicial():

    texto = [
    ("Agregar misiones" , agregarMision),
    ("Mostrar tolas las misiones" , mostrarMisiones),
    ("Buscar mision por nombre" , buscarPorNombre),
    ("Mostrar misiones pendientes" , mostrarMisionesPendiente),
    ("Mostrar misiones en progreso" , mostrarMisionesEnProgreso),
    ("Mostrar misiones completadas" , mostrarMisionesCompleta),
    ("Cambiar estado de una mision" , cambiarEstadoMision),
    ("Mostrar mision con mayor recompensa" , mostrarMisionMayorRecompensa),
    ("Experiencia total de todas las misiones" , sumarExpTotal),
    ("Mostrar cuantas misiones hay por dificultad especifica" , mostrarMisionPorDificultad),
    ("Eliminar misiones" , eliminarMisiones),
    ("Misiones ordenadas por recompensas" , ordenarMisionPorRecompensas),
    ("Misiones ordenadas por dificultad" , ordenarMisionPorDificultad),
    ("Mostrar cuantas misiones dio un npc especifico" , mostrarMisionesNpc),
    ("Salir" , salir)
    ]
    return texto

def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pedirNumUsuario(array):
    numero = validarNum("Ingrese un numero: ", len(array) )
    return numero

def crearDiccionario(array):
    diccionarios = []

    for i, tupla in enumerate(array, 0):
        diccionarios.append({"nombre":tupla[0]}),
        diccionarios[i]["funcion"] = tupla[1]
        
    return diccionarios

def mostrarMenu (menu) :

    for i , nombre in enumerate (menu , 1):
        print(f"{i}: {nombre['nombre']}")

def ejecutarMenu (menu, equipos) :
    opcion = pedirNumUsuario(menu)
    opcion = opcion -1
    menu[opcion]["funcion"](equipos)

def salir(equipos):
    print("Saliendo...")
    global programaActivo
    programaActivo = False

        
def ejecutarProgramaPriincipal ():

    misiones=[]

    while(programaActivo):

        limpiarPantalla()

        disccionario = crearDiccionario(imprimirTextoInicial())
        mostrarMenu(disccionario)
        ejecutarMenu(disccionario, misiones)
        input()

if __name__=="__main__" :
    ejecutarProgramaPriincipal()