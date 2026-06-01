/*
Ejercicio: Menú de opciones (tipo cajero / app)

Estás programando un menú simple. El usuario elige una opción con un número:

1 → "Ver saldo"
2 → "Depositar dinero"
3 → "Retirar dinero"
4 → "Salir"

Según la opción elegida, mostrar un mensaje por consola.

Si ingresa un número que no existe → mostrar:
"Opción inválida" */

let opcion = 5;

switch (opcion) {
    case 1:
        console.log("ver saldo");
        break;
    case 2:
        console.log("depositar dinero");
        break;
    case 3:
        console.log("retirar dinero");
        break;
    case 4:
        console.log("salir");
        break;
    default:
        console.log("opcion invalida")
}