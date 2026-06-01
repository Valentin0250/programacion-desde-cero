"""
Ejercicio: Inventario de un videojuego

Creá un programa que simule el inventario de un personaje en un videojuego.

Cada objeto del inventario debe tener:

    nombre
    tipo de objeto (arma, armadura, poción, material, etc.)
    rareza
    valor en oro
    cantidad
    si está equipado o no

El programa debe permitir:

1.Agregar objetos al inventario.
2.Mostrar todos los objetos.
3.Buscar un objeto por nombre.
4.Mostrar únicamente las armas.
5.Mostrar únicamente los objetos equipados.
6.Equipar o desequipar un objeto.
7.Mostrar el objeto más valioso.
8.Calcular el valor total del inventario.
9.Contar cuántos objetos hay de una rareza específica.
10.Salir del programa mediante un menú.
"""

import os

programaActivo = True

MAX_VALOR= 1000
MAX_CANTIDAD= 10

def numeroUsuario () :
    while(True):
        try:
            numero = int(input(""))
            return numero
        except ValueError:
            print("Error, vuelva a intentar")

def textoUsuario () :
    while(True):
        try:
            texto = str(input(""))
            return texto
        except ValueError:
            print("Error, vuelva a intentar")

def agregarObjeto (inventario) :
    rarezaOpciones = ["legendario", "raro", "normal"]
    tipoOpciones = ["arma","proteccion","pocion","basura"]
    print("Se le pedira datos del objeto agregar.")
    objeto = pedirDatosUsuario(tipoOpciones,rarezaOpciones, inventario)
    inventario.append(objeto)

def eliminarObjeto (inventario) :
    print("Una vez eliminado no vuelve mas, podes crear uno 'igual'.")
    nombre = input("Nombre del objeto a eliminar: ")
    validar= True
    for objeto in inventario:
        if objeto["nombre"] == nombre:
            validar= False
            inventario.remove(objeto)
            print("Descartado")
    if validar:
        print(f"No se encontrado ningun objeto llamado {nombre} para eliminar")

def mostrarObjetos (inventario) :
    print("Todos los objetos del inventario: ")
    for i, objeto in enumerate (inventario, 0):
        print(f"\nEquipo - {i+1}:")
        mostrarObjetoEnPantalla(objeto)
           
def mostrarObjetoEnPantalla(equipo):
    for i, keys in enumerate(equipo, 0):
        print(f"{i+1}- {keys}: {equipo[keys]}")

def buscarPorNombre (inventario) :
    print("Una vez encontrado aparecera con sus datos. ")
    nombre = input("Nombre del objeto a buscar: ")
    valor = True
    for objeto in inventario :
        if objeto["nombre"] == nombre :
            valor = False
            print("Objeto encontrado.")
            mostrarObjetoEnPantalla(objeto)
            break
    if valor:
        print("Objeto no encontrado en el menu")

def mostrarObjeto(inventario,tipo, estado):
    valor = True
    for objeto in inventario :
        if objeto[tipo] == estado :
            valor = False
            mostrarObjetoEnPantalla(objeto)
    if valor:
        print(f"No se encontrado nada de tipo '{estado}'")

def mostrarArmas (inventario) :
    print("Todas las armas del menu: ")
    mostrarObjeto(inventario,"tipo de objeto", "arma")

def mostrarObjetosEquipados (inventario) :
    print("Objeto equipados: ")
    mostrarObjeto(inventario,"estado", "equipado")

def cambiarEstadoObjeto (inventario) :
    print("Los estados a cambiar son equipados y desequipados. ")
    nombre = input("Nombre del objeto de estado a cambiar: ")
    valor = True
    for objeto in inventario:
        if objeto["nombre"] == nombre:
            valor = False 
            if objeto["estado"] == "equipado" :
                objeto["estado"] = "desequipado"
                print(objeto["nombre"] , "-" , objeto["estado"])
            else:
                objeto["estado"] = "equipado"
                print(objeto["nombre"] , "-" , objeto["estado"])
    if valor:
        print("No se a encontrado el objeto a des/equipar")

def mostrarObjetoMayorValor (inventario):
    print("Objeto de mayor valor del inventario(una buena pasta).")
    valorGuardar = 0
    objetoGuardar = ""
    for objeto in inventario :
        if valorGuardar == 0:
            valorGuardar = objeto["valor"]
            objetoGuardar = objeto["nombre"]
        elif valorGuardar < objeto["valor"]:
            valorGuardar = objeto["valor"]
            objetoGuardar = objeto["nombre"]
    print(f"Objeto: {objetoGuardar} -  Valor: {valorGuardar}")

def sumaValorTotal (inventario):
    print("Suma del valor de todos los objetos: ")
    sumaTotal = 0
    for objeto in inventario:
        sumaTotal += objeto["valor"]
    print(f"Valor total: {sumaTotal}")

def calcularRarezas (inventario): #especificas
    print("Las rarezas pueden ser legendario, raro y normal.")
    nombre= input("Nombre de rareza a buscar: ")
    cantidad = 0
    valor = True
    for objeto in inventario:
        if objeto["rareza"] == nombre:
            valor= False
            cantidad += 1
    if valor:
        print(f"No se a encontrado ningun objeto con la rareza {nombre}")
    else:
        mostrarObjetoEnPantalla(objeto)

def validar(array,mensaje):

    while(True):
        rareza = input(mensaje)

        if rareza in array:
            return rareza
        else:
            print("Error, ingrese un valor valido")


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

def validarNombre(array, mensaje):
    nombres=[]
    for nombre in array:
            nombres.append(nombre["nombre"])
    
    while(True):
        nombreUsuario = input(mensaje)
        if nombreUsuario in nombres:
            print("Ese nombre ya es usado, intente con otro")
        else:
            return nombreUsuario

def pedirDatosUsuario (array, array2, inventario) :
    nombre = validarNombre(inventario,"Nombre: ")
    tipo = validar(array, "Tipo de objeto(arma/proteccion/pocion/basura): ")
    rareza = validar(array2, "Rareza del objeto(legendario/raro/normal): ")
    valor = validarNum(f"Valor del objeto en oro(0 a {MAX_VALOR}): " , MAX_VALOR)
    cantidad = validarNum(f"Cantidad del objeto(0 a {MAX_CANTIDAD}): " , MAX_CANTIDAD)

    objeto = {
        "nombre":nombre,
        "tipo de objeto":tipo,
        "rareza":rareza,
        "valor":valor,
        "cantidad":cantidad,
        "estado":"desequipado"
    }

    return objeto

def imprimirTextoInicial():

    texto = [
    ("Agregar objetos" , agregarObjeto),
    ("Mostrar todos los objetos" , mostrarObjetos),
    ("Buscar objeto" , buscarPorNombre),
    ("Mostrar todas las armas" , mostrarArmas),
    ("Mostrar objetos equipados" , mostrarObjetosEquipados),
    ("Cambiar estado de objetos (equipar/desequipar)" , cambiarEstadoObjeto),
    ("Mostrar objeto mas valioso" , mostrarObjetoMayorValor),
    ("Valor total de los objetos" , sumaValorTotal),
    ("Objetos por rareza a eleccion" , calcularRarezas),
    ("Descartar objeto del inventario" , eliminarObjeto),
    ("Salir" , salir)
    ]
    return texto
       
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

def salir(equipos):
    print("Saliendo...")
    global programaActivo
    programaActivo = False

def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def ejecucionPrincipal():

    inventario = []

    while(programaActivo):

        limpiarPantalla()

        diccionario = crearDiccionario(imprimirTextoInicial())
        mostrarMenu(diccionario)
        ejecutarMenu(diccionario, inventario)
        input()

        limpiarPantalla()

if __name__=="__main__" :
    ejecucionPrincipal()
