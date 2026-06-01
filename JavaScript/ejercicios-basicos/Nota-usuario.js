/* Ejercicio:
Pedile al usuario una nota (del 0 al 10) y mostrá un mensaje según el valor.

Condiciones:

Si la nota es mayor o igual a 7 → "Aprobado"
Si la nota es menor a 7 pero mayor o igual a 4 → "Recuperación"
Si la nota es menor a 4 → "Desaprobado"
*/

let nota = 10;
let mostrar;
if ( nota >= 7 ) {
    mostrar = "Aprobado";
}
if ( nota < 7 && nota >= 4 ) {
    mostrar = "Recuperacion";
}
if ( nota < 4 ) {
    mostrar = "Desaprobado";
}
console.log( "mostrar" + mostrar);