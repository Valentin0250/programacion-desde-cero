/*
jercicio: Semáforo

Crear un programa que simule el comportamiento de un semáforo.

Una variable llamada color que puede tener estos valores:

"rojo"
"amarillo"
"verde"

Condiciones:
Si el color es rojo → mostrar: "Detenerse"
Si es amarillo → mostrar: "Precaución"
Si es verde → mostrar: "Avanzar" */

let color = "verde";
let mostrar;
if (color === "rojo") {
    mostrar = "Detenerse";
}
if ( color === "amarillo" ) {
    mostrar = "Precaucion";
}
if ( color === "verde" ) {
    mostrar = "Avanzar";
}
console.log ("mostrar:" + mostrar);
