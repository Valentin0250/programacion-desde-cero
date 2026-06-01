/*Ejercicio: Nota de un alumno

Crear un programa que evalúe la nota de un alumno.

Dato:

Una variable llamada nota (número del 0 al 10)

Condiciones:
Si la nota es menor a 4 → "Desaprobado"
Si la nota es entre 4 y 6 → "Aprobado"
Si la nota es 7 o más → "Promocionado" */

let nota = 10;
let mostrar;

if ( nota < 4) {
    mostrar= "Desaprobado";
}
if ( nota >= 4 && nota <= 6) {
    mostrar= "Aprobado";
}
if ( nota >= 7 ) {
    mostrar= "Promocionado"
}
console.log ("mostrar:" + mostrar);