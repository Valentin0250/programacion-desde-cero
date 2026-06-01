"""
Ejercicio: Tienda de golosinas (Python)

Una tienda registra sus ventas durante 10 días.

Crear un menú interactivo de usuario con las siguientes opciones:

1.Registrar condiciones iniciales
número de unidades de galletitas
número de unidades de chocolates
plata inicial
vuelva al menú principal

2.Ejecutar programa
ejecuta el programa
espera que el usuario lea los resultados
vuelva al menú principal
3.Salir de programa
El usuario sale del programa


Reglas de venta por día:

Galletitas

    Días impares → se venden 3
    Días pares → se venden 5

Chocolates

    Días múltiplos de 3 → se venden 4
    Resto de los días → se venden 2

Precios
    Galletitas: $50
    Chocolates: $80

Descuentos especiales: Días múltiplos de 5 → 20% de descuento en todas las ventas del día.

Reposición:
Días múltiplos de 4 → llegan 6 galletitas y 3 chocolates

Condición de corte:

El programa se detiene si el stock de cualquier producto llega a 0 o menos.

Salida esperada (ejemplo):

Día 1 - vendiste 3 galletitas y 2 chocolates, ganaste $260 (stock: 37 galletitas, 28 chocolates)
Día 5 - vendiste 5 galletitas y 2 chocolates con descuento, ganaste $336 (stock: 32 galletitas, 26 chocolates)
Día 8 - vendiste 5 galletitas y 2 chocolates y recibiste reposición (stock: 31 galletitas, 27 chocolates)
...
Sistema finalizado
Ingresos totales: $XXXX
Stock restante: XX galletitas, XX chocolates
"""

import os

stock_galletitas = 0
stock_chocolates = 0
cantidad_plata = 0
opcion = 0
total = 0

while True :
    os.system('cls')
    print("Tienda de golosinas")
    print("1 - Registro de stock")
    print("2 - Mostrar de ventas")
    print("3 - Salir")

    while True :
        try:
            opcion = int(input("Ponga un numero respecto a las opciones: "))
            if opcion > 0 and opcion < 4 :
                break
        except ValueError:
            print("Error, numero incorrecto")

    match opcion :
        case 1 :
            os.system('cls')
            print("Regristo de condiciones iniciales")
            while True :
                try:
                    if stock_galletitas == 0 :
                        stock_galletitas = int(input("Cantidad de galletitas: "))
                    if stock_chocolates == 0 :
                        stock_chocolates = int(input("Cantidad de chocolates: "))
                    if cantidad_plata == 0 :
                        cantidad_plata = int(input("Cantidad de plata inicial: "))
                    break
                except ValueError:
                    print("Error, numero incorrecto")
        case 2 :
            os.system('cls')
            print("Ejecutar programa")
            for i in range ( 1 , 11 , 1) :

                ganancia_dia = 0
                precio_galletitas = 50
                precio_chocolates = 80
                galletitas_vendidas = 0
                chocolates_vendidos = 0

                if stock_chocolates <= 0 or stock_galletitas <= 0 :

                    print("Sistema finalizado")
                    print("Ingresos totales:" , total + cantidad_plata)
                    print("Stock restante:" , stock_galletitas , "galletitas," , stock_chocolates , "chocolates")
                    input("presione enter para volver al menu...")
                    break
                
                if i % 4 == 0 :
                    stock_galletitas += 6
                    stock_chocolates += 3
                    print("Reposicion de stock +6 galletitas y +3 chocolates")

                if i % 5 == 0 :
                    precio_galletitas -= precio_galletitas * 20 // 100
                    precio_chocolates -= precio_chocolates * 20 // 100
                
                if i % 2 == 0 :
                    galletitas_vendidas = min( 5 , stock_galletitas )
                    stock_galletitas -= galletitas_vendidas
                    ganancia_dia = precio_galletitas * galletitas_vendidas
                else :
                    galletitas_vendidas = min( 3 , stock_galletitas )
                    stock_galletitas -= galletitas_vendidas
                    ganancia_dia = precio_galletitas * galletitas_vendidas
            

                if i % 3 == 0 :
                    chocolates_vendidos = min( 4 , stock_chocolates )
                    stock_chocolates -= chocolates_vendidos
                    ganancia_dia = precio_chocolates * chocolates_vendidos
                else :
                    chocolates_vendidos = min( 2 , stock_chocolates )
                    stock_chocolates -= chocolates_vendidos
                    ganancia_dia = precio_chocolates * chocolates_vendidos

                total += ganancia_dia

                print("Dia" , i , "-" , "vendiste" , galletitas_vendidas , "galletitas y", chocolates_vendidos , "chocolates, ganaste $" , ganancia_dia , "(stock:" , stock_galletitas , "galletitas," , stock_chocolates , "chocolates)") 

        case 3 :
            os.system('cls')
            print("Salir de programa...")
            break