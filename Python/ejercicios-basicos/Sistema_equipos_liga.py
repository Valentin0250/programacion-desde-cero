"""
Ejercicio: Sistema de equipos en una liga de deportes electrónicos

Creá un programa para administrar equipos dentro de una liga de eSports.

Cada equipo debe tener:

    Nombre del equipo
    Capitán
    Cantidad de jugadores
    Nivel del equipo (1-10)
    Puntos de torneo
    Dinero del equipo
    Ciudad base
    Si el equipo está activo o eliminado

El programa debe permitir:

Crear equipos.
Mostrar todos los equipos.
Buscar un equipo por nombre.
Mostrar únicamente los equipos activos.
Mostrar únicamente los equipos eliminados.
Cambiar el estado de un equipo.
Subir el nivel de un equipo.
Agregar jugadores.
Expulsar jugadores.
Mostrar el equipo con más jugadores.
Mostrar el equipo con más dinero.
Mostrar el equipo con más puntos de torneo.
Calcular el promedio de jugadores entre todos los equipos.
Contar cuántos equipos hay por ciudad.
Eliminar equipos.
Ordenar equipos por nivel.
Ordenar equipos por puntos de torneo.
Mostrar el dinero total entre todos los equipos.
19 Salir mediante un menú.

Extras  nivel avanzado:

Evitar nombres repetidos.
Crear partidas entre equipos y actualizar puntos.
Robar dinero entre equipos (por apuestas o multas).
Crear ranking global por puntos.
Permitir alianzas temporales entre equipos.
Agregar fecha de creación del equipo.
Mostrar estadísticas generales:
  Equipo más poderoso (nivel + puntos)
  Equipo más rico
  Equipo con más jugadores
  Agregar sistema de experiencia para jugadores dentro del equipo.
  Limitar cantidad máxima de jugadores por equipo.
  Crear equipos según categoría:
   FPS
   MOBA
   Battle Royale
   Estrategia
"""

import os
import random
import time 
from datetime import datetime, date
# date.today() fecha actual
# datetime.now() fecha y hora actual

programaActivo = True

VELOCIDAD_TEXTO = 0.01
MAX_NIVEL= 10
MAX_PUNTOS= 500
MAX_DINERO= 500
MAX_JUGADORES= 200
APUESTA= 50
PUNTAJE= 50
MAPAS_FPS= 20
MAPAS_MOBA= 3
MAPAS_BATTLE_ROYALE= 1
MAPAS_ESTRATEGIA= 10

def tipearTexto( texto, velocidad = VELOCIDAD_TEXTO) :
    for caracter in texto:
        print(caracter, end="", flush=True)
        time.sleep(velocidad)
    print()

def agregarEquipo(equipos): #1
    categorias= ["fps","moba","battle royale","estrategia"]
    tipearTexto("Ahora se le pediran datos para poder crear a su equipo.")
    datos = pedirDatos(equipos, categorias)
    equipos.append(datos)

def mostrarTodosLosEquipos (equipos): #2
    tipearTexto("Estos son todos los equipos.")
    for i, equipo in enumerate(equipos, 1):
        tipearTexto(f"\nEquipo - {i}:")
        mostrarEquipoEnPantalla(equipo)
            
def mostrarEquipoEnPantalla(equipo):
    for i, keys in enumerate(equipo, 0):
        tipearTexto(f"{i+1}- {keys}: {equipo[keys]}")

def buscarEquipo (equipos): #3

    tipearTexto("Ponga el nombre correctamente y le aparecera el equipo.")
    nombreUsuario = input("Poner nombre del equipo a buscar: ")

    validar = True
    for equipo in equipos:
        if equipo["nombre"] == nombreUsuario:
            tipearTexto(f"Se ha encontrado.")
            validar = False
            mostrarEquipoEnPantalla(equipo)
            break

    if validar:
        tipearTexto(f"No se ha encontrado ningun equipo llamado {nombreUsuario}")
    
def ordenarEquiposEstado(equipos, key):
    validar = True
    for equipo in equipos:
        if equipo["estado"] == key:
            validar = False
            tipearTexto(f"Equipo: {equipo['nombre']} - Estado: {equipo['estado']}")
    if validar:
        tipearTexto(f"Parece ser que no hay ningun equipo {key}")

def mostrarEquiposActivos(equipos): #4
    tipearTexto("Estos son todos los equipos activos de momento.")
    ordenarEquiposEstado(equipos, "activo")

def mostrarEquiposEliminados(equipos): #5
    tipearTexto("Estos son todos los equipos eliminados de momento.")
    ordenarEquiposEstado(equipos, "eliminado")
    

def cambiarEstado(equipos): #6

    tipearTexto("Poner correctamente el nombre del equipo a cambiar de estado(activo/eliminado).")
    nombreUsuario = input("Poner nombre del equipo a cambiar de estado: ")

    for equipo in equipos:
        if equipo["nombre"] == nombreUsuario:
            if equipo["estado"] == "activo":
                equipo["estado"] = "eliminado"
                tipearTexto(f"Equipo: {equipo['nombre']} - Estado anterior: activo - Estado actual: {equipo['estado']}")
                break
            if equipo["estado"] == "eliminado":
                equipo["estado"] = "activo"
                tipearTexto(f"Equipo: {equipo['nombre']} - Estado anterior: eliminado - Estado actual: {equipo['estado']}")
                break

def subirNivelEquipo(equipos): #7

    tipearTexto(f"Subira de un punto de nivel y el maximo es {MAX_NIVEL}.")
    nombreUsuario = input("Poner nombre del equipo a subir de nivel: ")

    for equipo in equipos:
        if equipo["nombre"] == nombreUsuario:
            equipo["nivel"] += 1
            if equipo["nivel"] > MAX_NIVEL:
                equipo["nivel"] = MAX_NIVEL
            tipearTexto(f"Equipo: {equipo['nombre']} - Nivel: {equipo['nivel']}")

def agregarJugadores(equipos): #8

    tipearTexto("Poner la cantidad de jugadores que quieras agregar y al equipo que sera.")
    nombreUsuario = input("Poner nombre del equipo que sumara jugadores: ")
    numeroUsuario = validarNum("Cantidad de jugadores a sumar: ", MAX_JUGADORES)

    validar = True
    for equipo in equipos:
        if equipo["nombre"] == nombreUsuario:
            validar = False
            equipo["jugadores"] += numeroUsuario
            equipo["jugadores"] = min(equipo["jugadores"], MAX_JUGADORES)
            tipearTexto(f"Equipo: {equipo['nombre']} - Jugadores: {equipo['jugadores']}")
    if validar:
        tipearTexto(f"No se encontrado a {nombreUsuario} para agregar jugadores")

def expulsarJugadores(equipos): #9

    tipearTexto("Poner la cantidad de jugadores que quieras eliminar y al equipo que sera.")
    nombreUsuario = input("Poner nombre del equipo que sumara jugadores: ")
    numeroUsuario = validarNum("Cantidad de jugadores a sumar: ", MAX_JUGADORES)
    validar = True
    for equipo in equipos:
        if equipo["nombre"] == nombreUsuario:
            validar = False
            equipo["jugadores"] -= numeroUsuario
            equipo["jugadores"] = max(equipo["jugadores"] , 0)
            tipearTexto(f"Equipo: {equipo['nombre']} - Jugadores: {equipo['jugadores']}")
    if validar:
        tipearTexto(f"No se encuentra ha {nombreUsuario} para expulsar jugadores")

def ordenarEquipos(equipos, key, mensaje):
    
    variable = 0
    nombre = ""
    for equipo in equipos:
        if variable == 0:
            variable = equipo[key]
            nombre = equipo["nombre"]
        if variable < equipo[key]:
            variable = equipo[key]
            nombre = equipo["nombre"]
    tipearTexto(f"Equipo: {nombre} - {mensaje}: {variable}")


def mostrarEquipoJugadores(equipos): # 10

    tipearTexto("Este es el equipo que mas mueve gente.")
    ordenarEquipos(equipos, "jugadores" , "Cantidad de Jugadores")

def mostrarEquipoDinero(equipos): #11

    tipearTexto("Una buena economia nunca viene mal.")
    ordenarEquipos(equipos, "dinero" , "Dinero del equipo")

def mostrarEquipoPuntos(equipos): #12

    tipearTexto("Un equipo respetado por todos.")
    ordenarEquipos(equipos, "puntos" , "Puntos de guerra")

def mostrarPromedioDeJugadores(equipos): #13

    tipearTexto("Promedio de jugadores.")

    suma= 0
    for i , equipo in enumerate(equipos, 1):
        suma += equipo["jugadores"]
        divisor = i
    resultado = suma // divisor
    tipearTexto(str(resultado))

def contarEquiposPorCiudad(equipos): #14

    tipearTexto("Poniendo el nombre correcto de la ciudad, aparece los equipos que comparten la misma ciudad.")
    nombreUsuario = input("Poner nombre de la ciudad: ")

    validar = True
    for equipo in equipos:
        validar = False
        if equipo["ciudad"] == nombreUsuario:
            tipearTexto(f"Equipo: {equipo["nombre"]} - Ciudad: {equipo["ciudad"]}")
    if validar:
        tipearTexto(f"No se ha encontrado ningun equipo en la ciudad {nombreUsuario}")

def eliminarEquipo(equipos): #15

    tipearTexto("Es el fin...")
    nombreUsuario = input("Poner nombre del equipo a eliminar: ")

    validar = True
    for equipo in equipos:
        if equipo["nombre"] == nombreUsuario:
            validar = False
            equipos.remove(equipo)
            tipearTexto(f"Se ha borrado correctamente el equipo {nombreUsuario}")
    if validar:
        tipearTexto(f"No se ha podido eliminar, ya que no se encuentra ningun equipo llamado {nombreUsuario}")

def ordenarEquiposNivel(equipos): #16

    tipearTexto("Respeten los levels.")
    organizado = ordenar(equipos, "nivel")
    mostrarTodosLosEquipos(organizado)

def ordenar(equipos, key):
    
    copia = equipos.copy()
    organizado = []

    while(copia):
        puntos = 0

        for equipo in copia:
            if puntos < equipo[key]:
                puntos = equipo[key]

        for equipo in copia:
            if puntos == equipo[key]:
                organizado.append(equipo)
                break
        copia.remove(equipo)
    return organizado

def ordenarEquiposPuntos(equipos): #17

    tipearTexto("Esto es una batalla sin fin.")
    organizado = ordenar(equipos, "puntos")
    mostrarTodosLosEquipos(organizado)

def MostrarOroTotal(equipos): #18
    
    tipearTexto("Una buena suma.")
    
    oro = 0
    for equipo in equipos:
        oro += equipo["dinero"]
    tipearTexto(str(oro))
       
def validarNum (mensaje,numeroMaximo):

    while(True):
        try:
            numero = int(input(mensaje))
            if numero >= 0 and numero <=numeroMaximo:
                return numero
            else:
                tipearTexto("Error, vuelva ha intentar")
        except ValueError:
            tipearTexto("Error, vuelva ha intentar")

def validarNombre(array, mensaje):
    nombres=[]
    for nombre in array:
            nombres.append(nombre["nombre"])
    
    while(True):
        nombreUsuario = input(mensaje)
        if nombreUsuario in nombres:
            tipearTexto("Ese nombre ya es usado, intente con otro")
        else:
            return nombreUsuario
        
def validar(array,mensaje):

    while(True):
        rareza = input(mensaje)

        if rareza in array:
            return rareza
        else:
            tipearTexto("Error, ingrese un valor valido")
            input()

def pedirDatos(equipos, categorias):
    nombre= validarNombre(equipos, "Poner del nombre su equipo: ")
    capitan= input("Nombre del capitan: ")
    categoria= validar(categorias, "Categoria(fps, moba, battle royale, estrategia) del equipo: ")
    jugadores= validarNum(f"Cantidad de jugadores(max {MAX_JUGADORES}) del equipo: ", MAX_JUGADORES)
    nivel= validarNum(f"Nivel(max {MAX_NIVEL}) del equipo: ", MAX_NIVEL)
    puntos= validarNum(f"Puntos(max {MAX_PUNTOS}) de torneo del equipo: ", MAX_PUNTOS)
    dinero= validarNum(f"Cantidad de dinero(max {MAX_DINERO}) del equipo: ", MAX_DINERO)
    ciudad= input("Nombre de la ciudad base: ")
    fecha= datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    hola = {
        "nombre":nombre,
        "capitan":capitan,
        "categoria":categoria,
        "jugadores":jugadores,
        "nivel":nivel,
        "puntos":puntos,
        "dinero":dinero,
        "ciudad":ciudad,
        "estado":"activo",
        "fecha":fecha
    }
    return hola

def pedirNumUsuario(array):
    numero = validarNum("Ingrese un numero: ", len(array) )
    return numero

def imprimirTextoArray(array):
    for mensaje in array:
        tipearTexto(mensaje)

def validarNombreParaJuegos(array, mensaje,equipo1):

    nombres=[]
    for nombre in array:
            nombres.append(nombre["nombre"])
    
    if equipo1 in nombres:
        nombres.remove(equipo1)

    while(True):
        nombreUsuario = input(mensaje)
        if nombreUsuario == equipo1:
            tipearTexto("Ese equipo ya esta siendo usado")
        elif not nombreUsuario in nombres:
            tipearTexto("Ese equipo no existe")
        elif nombreUsuario in nombres:
            return nombreUsuario
        
        if nombreUsuario == "break":
            tipearTexto("Volviendo al menu...")
            return nombreUsuario

def pedirNumRandom(equipos, equipo1, equipo2, numero):
    while(True):
        numero1 = random.randint( 0 , numero)
        numero2 = random.randint( 0 , numero )
        if numero1 != numero2:
            sumarPuntos(equipos,numero1, numero2, equipo1, equipo2)
            break

def sumarPuntos(equipos,numero1, numero2, equipo1, equipo2):
    if numero1 > numero2:
        for equipo in equipos:
            if equipo1 == equipo["nombre"]:
                equipo["puntos"] += PUNTAJE
                equipo["puntos"] = min(equipo["puntos"] , MAX_PUNTOS)
                tipearTexto(f"Ha ganado {equipo1} {numero1} a {numero2},conseguiendo {PUNTAJE} puntos. Puntos de guerra: {equipo['puntos']}")
                break
    if numero2 > numero1:
        for equipo in equipos:
            if equipo2 == equipo["nombre"]:
                equipo["puntos"] += PUNTAJE
                equipo["puntos"] = max(equipo["puntos"] , MAX_PUNTOS)
                tipearTexto(f"Ha ganado {equipo2} {numero2} a {numero1},conseguiendo {PUNTAJE} puntos. Puntos de guerra: {equipo['puntos']}")
                break

def jugarPartidas(equipos):

    categorias= ["fps","moba","battle royale","estrategia"]

    tipearTexto(f"Se hace una simulacion de juego donde el ganador se lleva {PUNTAJE} puntos de guerra, los juegos a simular son: \n(fps, moba, battle royale, estrategia).\nEn caso de querer volver podes escribir 'break' para poder salir.")

    if not equipos:
        tipearTexto("No hay equipos para jugar de momento...")
        return

    juego = validar(categorias, "Elegir el juego para la partida: ")
    equipo1 = validarNombreParaJuegos(equipos, "Elegir al primer equipo que jugara: " , "")
    if equipo1 == "break":
        return
    equipo2 = validarNombreParaJuegos(equipos, "Elegir al segundo equipo que jugara: " , equipo1)
    if equipo2 == "break":
        return

    match(juego):
        case "fps":
            pedirNumRandom(equipos, equipo1, equipo2, MAPAS_FPS)
        case "moba":
            pedirNumRandom(equipos, equipo1, equipo2, MAPAS_MOBA)
        case "battle royale":
            pedirNumRandom(equipos, equipo1, equipo2, MAPAS_BATTLE_ROYALE)
        case "estrategia":
            pedirNumRandom(equipos, equipo1, equipo2, MAPAS_ESTRATEGIA)

def lanzarMoneda(equipos, equipo1, equipo2):

        for equipo in equipos:
            if equipo1 == equipo["nombre"]:
                equipo["dinero"] += APUESTA
                equipo["dinero"] = min(equipo["dinero"] , MAX_DINERO)
                tipearTexto(f"{equipo['nombre']} se llevo {APUESTA}. Dinero: {equipo['dinero']}")

        for equipo in equipos:
            if equipo2 == equipo["nombre"]:
                equipo["dinero"] -= APUESTA
                equipo["dinero"] = max(equipo["dinero"] , 0) 
                tipearTexto(f"{equipo['nombre']} ha perdido {APUESTA}, dinero: {equipo['dinero']}")

def robarDinero (equipos):

    moneda = ["cara" , "cruz"]

    if not equipos:
        tipearTexto("No hay equipos para jugar de momento...")
        return

    tipearTexto(f"Se eligira a un equipo a quien apoyar y uno a quien retar. Se jugara por {APUESTA}. Cara o cruz.\nEn caso de querer volver podes escribir 'break' para poder salir.")

    equipo1 = validarNombreParaJuegos(equipos, "Elegir equipo que apoyara para ganar: " , "")
    if equipo1 == "break":
        return
    equipo2 = validarNombreParaJuegos(equipos, "Elegir equipo que desafiaras: " , equipo1)
    if equipo2 == "break":
        return

    opcion = validar(moneda, "Elegir a cual lado de la moneda le confiaras tu futuro: ")

    lado = random.randint(0,1)
    tipearTexto(f"Salio {moneda[lado]}")
    if moneda[lado] == opcion:
        lanzarMoneda(equipos, equipo1, equipo2)
    else:
        lanzarMoneda(equipos, equipo2, equipo1)

def formarAlianzas(equipos):

    tipearTexto("Formar una alianza entre dos equipos, que sera permanente.\nEn caso de querer volver podes escribir 'break' para poder salir.")

    if not equipos:
        tipearTexto("No hay equipos para formar alianzas...")
        return

    equipo1 = validarNombreParaJuegos(equipos, "Elegir equipo que forjara una alianza: " , "")
    if equipo1 == "break":
        return
    equipo2 = validarNombreParaJuegos(equipos, "Elegir equipo que participara en la alianza: " , equipo1)
    if equipo2 == "break":
        return
    
    for equipo in equipos:
        if equipo1 == equipo["nombre"]:
            equipo["alianza"] = equipo2
        if equipo2 == equipo["nombre"]:
            equipo["alianza"] = equipo1

def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

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
    tipearTexto("Saliendo...")
    global programaActivo
    programaActivo = False

def ejecucionPrincipal():
    equipos = []
    

    textos = [
        ("Agregar equipo" , agregarEquipo),
        ("Mostrar todos los equipos" , mostrarTodosLosEquipos),
        ("Buscar equipo por nombre", buscarEquipo),
        ("Mostrar equipos activos", mostrarEquiposActivos),
        ("Mostrar equipos eliminados", mostrarEquiposEliminados),
        ("Cambiar estado de equipo", cambiarEstado),
        ("Subir de nivel de un equipo", subirNivelEquipo),
        ("Agregar jugadores a un equipo", agregarJugadores),
        ("Expulsar jugadores a un equipo", expulsarJugadores),
        ("Mostrar equipo con mas jugadores", mostrarEquipoJugadores),
        ("Mostrar equipo con mas dinero", mostrarEquipoDinero),
        ("Mostrar equipo con mas puntos de guerra",mostrarEquipoPuntos),
        ("Calculo de promedio de jugadores entre equipos", mostrarPromedioDeJugadores),
        ("Investigar cantidad de equipos por ciudad", contarEquiposPorCiudad),
        ("Eliminar un equipo", eliminarEquipo),
        ("Ordenar equipos por nivel", ordenarEquiposNivel),
        ("Ordenar equipos por puntos de guerra", ordenarEquiposPuntos),
        ("Mostrar oro total entre todos los equipos", MostrarOroTotal),
        ("Simulacion de juegos por puntos", jugarPartidas),
        ("Juego de la moneda por dinero", robarDinero),
        ("Formar alianza entre equipos", formarAlianzas),
        ("Salir", salir)
    ]

    while(programaActivo):

        limpiarPantalla()

        diccionario = crearDiccionario(textos)
        mostrarMenu(diccionario)
        ejecutarMenu(diccionario, equipos)
        input()

if __name__=="__main__" :
    ejecucionPrincipal()