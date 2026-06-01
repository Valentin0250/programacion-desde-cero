"""
Ejercicio: Gestión de biblioteca

Creá un programa para administrar una pequeña biblioteca.

Cada libro debe tener:

    título
    autor
    año de publicación
    cantidad de páginas
    si está disponible o prestado

El programa debe permitir:

1.Agregar varios libros.
2.Mostrar todos los libros cargados.
3.Buscar un libro por título.
4.Mostrar únicamente los libros disponibles.
5.Mostrar únicamente los libros prestados.
6.Cambiar el estado de un libro (de disponible a prestado o viceversa).
7.Mostrar cuál es el libro con más páginas.
8.Calcular el promedio de páginas entre todos los libros.
9.Contar cuántos libros hay de un autor específico.
10.Permitir salir del programa mediante un menú.

EXTRAS:

1.Evitar títulos repetidos.
2.Permitir eliminar libros.
3.Mostrar los libros ordenados por año.
4.Guardar los datos aunque el programa siga ejecutándose varias veces dentro del menú.
"""

import os

programaActivo = True

def numeroUsuario () :
    while (True) :
        try:
            numero = int(input("Elegi una de las opciones del menu: "))
            return numero
        except ValueError :
            print("Error")

def nombreLibro (mensaje) :
    while(True) :
        try:
            libro = str(input(mensaje))
            return libro
        except ValueError :
            print("Error")

def agregarLibro (biblioteca) : #1
    print("Ahora se le pedira datos del libro...")
    libro = datosDelLibroAgregar()
    biblioteca.append(libro)

def eliminarLibro (biblioteca) :
    print("Eliminar libro de nuestra coleccion: ")
    borrar = nombreLibro("Nombre del libro a eliminar: ")
    for libro in biblioteca :
        if libro["titulo"] == borrar :
            biblioteca.remove(libro)
            print(f"Se elimino con exito el libro {borrar}")
            break
    if not libro["titulo"] == borrar:
        print(f"No se a poodido encontrar el libro {borrar}, para eliminar")

def mostrarlibros (biblioteca) :
    print("Mostrando todo nuestro catalogo de los "'mejores'" libros de la biblioteca: ")
    for i , libro in enumerate (biblioteca , 0) :
        print(f"Libro {i+1} -")
        mostrarLibroEnPantalla(libro)

def mostrarLibroEnPantalla(equipo):
    for i, keys in enumerate(equipo, 0):
        print(f"{i+1}- {keys}: {equipo[keys]}")

def buscarLibro (biblioteca) :
    print("Buscando el libro, una vez encontrado se mostrara los detalles del libro")
    libroBuscado = nombreLibro("Poner el nombre del libro: ")
    x = True
    for libro in biblioteca :
        if libroBuscado in libro["titulo"] :
            print(f"Libro encontrado con exito:" , libroBuscado)
            mostrarLibroEnPantalla(libro)
            x = False
            break
    
    if x:
        print("No se a encontrado ese libro")

def cambiarEstadoDeLibro (biblioteca) :
    print("Libro listo para partir/volver: ")
    nombre = nombreLibro("Poner el libro a cambiar de estado: ")
    for libro in biblioteca :
        if not nombre == libro["titulo"] :
            continue
        else :
            if  libro["estado"] == "prestado" : # libro = prestado
                libro["estado"] = "disponible"
                print(libro["titulo"] , libro["estado"])
            else :
                libro["estado"] = "prestado"  # libro = disponible
                print(libro["titulo"] , libro["estado"])
        
def ordenarMaquinaImprimir(biblioteca, key):
    for i , libro in enumerate (biblioteca, 0):
        if libro["estado"] == key :
            print(i+1 , "-" , libro["titulo"] , "-" , libro["estado"])


def imprimirLinbrosPrestados (biblioteca) :
    print("Estos estan en prestamos, tenemos muchos clientes... pocos libros cof cof..")
    ordenarMaquinaImprimir(biblioteca, "prestado")

def imprimirLibrosDisponibles (biblioteca) :
    print("Estos son TODOS nuestros libros a disposicion: ")
    ordenarMaquinaImprimir(biblioteca, "disponible")

def mostrarLibroMasLargo (biblioteca) :
    print("Ante usted el libro mas largo de nuestra coleccion: ")
    maximoHojas = 0 #bandera
    tituloGuardar = ""
    for libro in biblioteca :
        if maximoHojas == 0 :
            maximoHojas = libro["cantidad de paginas"]
            tituloGuardar = libro["titulo"]
        elif maximoHojas < libro["cantidad de paginas"] :
            maximoHojas = libro["cantidad de paginas"]
            tituloGuardar = libro["titulo"]

    print("Titulo:" , tituloGuardar , "Longitud: " , maximoHojas)

def sumarPromedioDePaginas (biblioteca) :
    print("Cantidad de paginas de los libros: ")
    paginasTotal = 0
    for libro in biblioteca :
        paginasTotal += libro["cantidad de paginas"]
    print(str(paginasTotal))

def informarCantidadDeUnMismoAutor (biblioteca) :
    print("Autores y sus libros...") 
    autor = nombreLibro("Nombre del autor ha buscar: ")
    cantidad = 0
    for libro in biblioteca :
        if libro["autor"] == autor:
            cantidad += 1
    print(autor, ":" , str(cantidad))

def datosDelLibroAgregar ():
    titulo = input("titulo del libro: ")
    autor = input("Autor del libro: ")
    año = input("Año de publicacion: ")
    longitud = int(input("Cantidad de paginas: "))
    estado = "disponible"

    libroUsuario = {
        "titulo":titulo,
        "autor":autor,
        "año de publicacion":año,
        "cantidad de paginas":longitud,
        "estado":estado
    }
    return libroUsuario

def salir(biblioteca):
    print("Nos vemos, vuelva pronto...")
    global programaActivo
    programaActivo = False

def fantasma(biblioteca):
    print("Error, vuelva ha intentar")

def validarNum (mensaje,numeroMaximo):

    while(True):
        try:
            numero = int(input(mensaje))
            if numero >= 0 and numero <=numeroMaximo:
                return numero
            else:
                print("Error, vuelva ha intentar")
        except ValueError:
            print("Error, vuelva ha intentar")

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
        print(f"{i}: {nombre["nombre"]}")
        if i == 11:
            break

def ejecutarMenu (menu, equipos) :
    opcion = pedirNumUsuario(menu)
    opcion = opcion -1
    menu[opcion]["funcion"](equipos)

def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def programaPrincipal ():

    biblioteca = []

    textos = [
        ("Agregar libro a la biblioteca", agregarLibro),
        ("Mostrar todos los libros" , mostrarlibros),
        ("Buscar libro por su titulo" , buscarLibro),
        ("Mostrar libros disponibles" , imprimirLibrosDisponibles),
        ("Mostrar libros prestados" , imprimirLinbrosPrestados),
        ("Cambiar estado de libros" , cambiarEstadoDeLibro),
        ("Mostrar libro con mas paginas" , mostrarLibroMasLargo),
        ("Calcular promedio de hojas de todos los libros" , sumarPromedioDePaginas),
        ("Cantidad de libros por autor en especifico" , informarCantidadDeUnMismoAutor),
        ("Eliminar libro" , eliminarLibro),
        ("Salir" , salir),
        ("" , fantasma)
    ]

    print("Bienvenido a la biblioteca, mantenga la voz baja...")

    while (programaActivo) :

        limpiarPantalla()

        diccionario = crearDiccionario(textos)
        mostrarMenu(diccionario)
        ejecutarMenu(diccionario, biblioteca)
        input()

if __name__=="__main__" :
    programaPrincipal()
