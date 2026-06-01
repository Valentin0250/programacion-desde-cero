"""
Ejercicio: Sistema de personajes de un RPG

Creá un programa para administrar los personajes de un videojuego RPG.

Cada personaje debe tener:

    nombre
    clase (guerrero, mago, arquero, etc.)
    nivel
    vida
    mana
    ataque
    defensa
    oro
    si está vivo o derrotado

El programa debe permitir:

1.Agregar personajes.
2.Mostrar todos los personajes.
3.Buscar un personaje por nombre.
4.Mostrar únicamente los personajes vivos.
5.Mostrar únicamente los personajes derrotados.
6.Subir de nivel a un personaje.
7.Cambiar el estado de un personaje (vivo/derrotado).
8.Mostrar el personaje con mayor nivel.
9.Mostrar el personaje con más ataque.
10.Calcular el promedio de nivel.
11.Contar cuántos personajes hay de una clase específica.
12.Eliminar personajes.
13.Ordenar personajes por nivel.
14.Ordenar personajes por ataque.
15.Mostrar el oro total de todos los personajes.
16.Salir mediante un menú.
"""

import os

MAX_NIVEL = 100
MAX_VIDA = 100
MAX_MANA = 100
MAX_ATAQUE = 20
MAX_DEFENSA = 15
MAX_ORO = 1000

def agregarPersonajes (personajes, clase): #1
    pj = datosPedir(clase)
    personajes.append(pj)

def datosPedir (lista):
    nombre = input("Nombre de personaje: ")
    clase = validar(lista, "Elegir clase del personaje(guerrero, mago, arquero): ")
    nivel = validarNum ("Elegir nivel del personaje(max 100): ", MAX_NIVEL)
    vida = validarNum ("Elegir la cantidad de vida(max 1000): ", MAX_VIDA )
    mana = validarNum ("Elegir cantidad de mana(max 700): ", MAX_MANA)
    ataque = validarNum("Elegir cantidad de daño de ataque(max 200): ", MAX_ATAQUE)
    defensa = validarNum("Elegir cantidad de defensa(max 100): ", MAX_DEFENSA)
    oro = validarNum("Elegir cantidad de oro que posee(max10000): ", MAX_ORO)
    estado = "vivo"

    guardar = {
        "nombre":nombre,
        "clase":clase,
        "nivel":nivel,
        "vida":vida,
        "mana":mana,
        "ataque":ataque,
        "defensa":defensa,
        "oro":oro,
        "estado":estado
    }
    return guardar

def mostrarPersonajes(personajes): #2
    for i, pj in enumerate (personajes, 0):
        print(f"Mision - {i+1} : ")
        mostrarObjetoEnPantalla(pj)

def mostrarObjetoEnPantalla(equipo):
    for i, keys in enumerate(equipo, 0):
        print(f"{i+1}- {keys}: {equipo[keys]}")

def buscarPersonaje(personajes): #3
    nombre = input("Nombre del personaje buscado: ")
    verdad = True
    for pj in personajes:
        if pj["nombre"] == nombre:
            verdad = False
            print("Personaje encontrado")
            mostrarObjetoEnPantalla(pj)
    if verdad:
        print("Personaje no encontrado")

def mostrarPersonajesEstado(personajes, estado):
     for pj in personajes:
        if pj["estado"] == estado :
            print(f"Personaje: {pj['nombre']} - Estado: {pj['estado']}")

def mostrarPersonajesVivos(personajes): #4
    mostrarPersonajesEstado(personajes, "vivo")

def mostrarPersonajesDerrotados(personajes): #5
    mostrarPersonajesEstado(personajes, "derrotado")

def subirNivelPersonaje(personajes, nombre): #6
    for pj in personajes:
        if pj["nombre"] == nombre:
            pj["nivel"] = pj["nivel"] + 1
            if pj["nivel"] > 100:
                pj["nivel"] = 100
            print(f"Nuevo nivel: {pj["nombre"]} level {pj["nivel"]}")

def cambiarEstadoPersonaje(personajes, nombre): #7
    for pj in personajes:
        if pj["nombre"] == nombre:
            if pj["estado"] == "vivo":
                pj["estado"] = "derrotado"
            else:
                pj["estado"] = "vivo"
            print(f"{pj["nombre"]} - estado: {pj["estado"]}")

def mostrarMayorNivel(personajes): #8
    level = 0
    name = ""
    for pj in personajes:
        if level == 0:
            level = pj["nivel"]
            name = pj["nombre"]
        if level < pj["nivel"]:
            level = pj["nivel"]
            name = pj["nombre"]
    print(f"Personaje con mas nivel: {name} - level: {level}")

def mostrarMayorAtaque(personajes): #9
    atack = 0
    name = ""
    for pj in personajes:
        if atack == 0:
            atack = pj["ataque"]
            name = pj["nombre"]
        if atack < pj["ataque"] :
            atack = pj["ataque"]
            name = pj["nombre"]
    print(f"Personaje con el ataque mas fuerte: {name} - ataque: {atack}")

def calcularPromedioNivel(personajes): #10
    promedio = []
    dividir = 0
    suma =0
    for i, pj in  enumerate (personajes,1):
        promedio.append(pj["nivel"])
        dividir = i
    for num in promedio:
        suma += num
    print(suma // dividir)

def calcularPersonajesPorClaseEspecifica(personajes,nombre): #11
    for pj in personajes:
        if pj["clase"] == nombre:
            print(f"{pj["nombre"]} - {pj["clase"]}")

def eliminarPersonajes(personajes, nombre): #12
    for pj in personajes:
        if pj["nombre"] == nombre:
            personajes.remove(pj)
            print(f"Personaje {nombre}, eliminado con exito")

def mostrarPersonajesPorNivel(personajes): #13
    copia = personajes.copy()
    personajesPorLevel = []

    while (copia):
        nivel = 0

        for pj in copia:
            if nivel < pj["nivel"]:
                nivel = pj["nivel"]

        for pj in copia:
            if nivel == pj["nivel"]:
                personajesPorLevel.append(pj)
                copia.remove(pj)
                break
    return personajesPorLevel

def mostrarPersonajesPorAtaque(personajes): #14
    copia = personajes.copy()
    personajesPorAtaque = []

    while (copia):
        ataque = 0

        for pj in copia:
            if ataque < pj["ataque"]:
                ataque = pj["ataque"]

        for pj in copia:
            if ataque == pj["ataque"]:
                personajesPorAtaque.append(pj)
                copia.remove(pj)
                break
    return personajesPorAtaque

def ayudaOrdenar(lista, mensaje):
    for pj in lista:
        print(f"{pj["nombre"]} - {mensaje}: {pj[mensaje]}")

def mostrarOroTotal(personajes):  #15
    oro = 0
    for pj in personajes:
        oro += pj["oro"]
    print(f"Oro total de los personajes: {oro}")

def pedirDatoUsuario(mensaje):
    while(True):
        try:
            dato= input(mensaje)
            return dato
        except ValueError:
            print("Error, vuelva a intentar")


def pedirNumeroUsuario(mensaje):
    while(True):
        try:
            dato= int(input(mensaje))
            return dato
        except ValueError:
            print("Error, vuelva a intentar")

def validar(array,mensaje):

    while(True):
        dato = input(mensaje)

        if dato in array:
            return dato
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

def imprimirTextoInicial():

    texto = [
    ("Agregar un personaje",),
    ("Mostrar todos los personajes",),
    ("Buscar personaje",),
    ("Mostrar personajes vivos",),
    ("Mostrar personajes derrotados",),
    ("Subir de nivel a un personaje",),
    ("Cambiar de estado a un personaje",),
    ("Personaje con mayor nivel",),
    ("Personaje con mayor ataque",),
    ("Mostrar el promedio de nivel",),
    ("Personajes por clases",),
    ("Eliminar personaje",),
    ("Personajes por nivel",),
    ("Personajes por ataque",),
    ("Oro total de los personajes",),
    ("Salir",)
    ]

def imprimirTextoOpciones(opciones):
    match(opciones):
        case 1:
            print("Ahora se le pedira datos para poder crear a su personaje.")
        case 2:
            print("Aca estan todos los personajes que tenemos por ahora.")
        case 3:
            print("Poniendo el nombre del personaje aparecera si lo encontro o no.")
        case 4:
            print("Estos son todos nuestros personajes vivos")
        case 5:
            print("Estos son los personajes caidos")
        case 6:
            print("Se subira de 1 nivel, cuando llegue a 100 no subira mas.")
        case 7:
            print("No se para que usarias esto con un personaje vivo... pero para uno derrotado esta bien.")
        case 8:
            print("Nuestro personaje de la mas alta calidad.")
        case 9:
            print("Pega como trompada de burro.")
        case 10:
            print("Un promedio curioso.")
        case 11:
            print("Poner una de las clases y aparecen nuestros mejores(unicos) peleadores.")
        case 12:
            print("Te recordaremos.")
        case 13:
            print("Hay que esforzarse mas.")
        case 14:
            print("El primero intimida, el ultimo no tanto.")
        case 15:
            print("Mucho oro y nada en que gastar")
        case 16:
            print("Saliendo...")
        case _ :
            print("Error")

def ejecucionPrincipalPrograma():
    personajes = []
    clase = ["guerrero" , "mago" , "arquero"]

    while (True):

        os.system("cls")

        imprimirTextoInicial()

        opciones = pedirNumeroUsuario("Seleccionar deacuerdo a las opciones: ")

        os.system("cls")

        imprimirTextoOpciones(opciones)

        match(opciones):
            case 1:
                pj = datosPedir(clase)
                agregarPersonajes(personajes, pj)
            case 2:
                mostrarPersonajes(personajes)
            case 3:
                nombre = pedirDatoUsuario("Poner el nombre del personaje que buscamos: ")
                buscarPersonaje(personajes, nombre)
            case 4:
                mostrarPersonajesVivos(personajes)
            case 5:
                mostrarPersonajesDerrotados(personajes)
            case 6:
                nombre = pedirDatoUsuario("Poner el nombre del personaje que subira su nivel: ")
                subirNivelPersonaje(personajes, nombre)
            case 7:
                nombre = pedirDatoUsuario("Nombre del personaje a cambiar de estado: ")
                cambiarEstadoPersonaje(personajes, nombre)
            case 8:
                mostrarMayorNivel(personajes)
            case 9:
                mostrarMayorAtaque(personajes)
            case 10:
                calcularPromedioNivel(personajes)
            case 11:
                nombre = validar(clase, "Poner nombre de la clase que mostraremos: ")
                calcularPersonajesPorClaseEspecifica(personajes, nombre)
            case 12:
                nombre = pedirDatoUsuario("Se aproxima el fin para: ")
                eliminarPersonajes(personajes, nombre)
            case 13:
                nivel = mostrarPersonajesPorNivel(personajes)
                ayudaOrdenar(nivel, "nivel")
            case 14:
                ataque = mostrarPersonajesPorAtaque(personajes)
                ayudaOrdenar(ataque, "ataque")
            case 15:
                mostrarOroTotal(personajes)
            case 16:
                break
        input()

if __name__=="__main__" :
    ejecucionPrincipalPrograma()