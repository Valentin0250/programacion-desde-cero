/*
Ejercicio: Número capicúa (palíndromo)

Escribí un programa que:

Tome un número entero positivo.
Use un bucle while para invertir el número (como en el ejercicio anterior).
Compare el número original con el invertido.
Determine si es capicúa (se lee igual al derecho y al revés).

Ejemplos

121 → capicúa ✅
123 → no es capicúa ❌
1331 → capicúa ✅   */

let numero = 23;
let numero_ori = numero
let invertido = 0;
let ultimo;

while (numero > 0) {
    ult= numero % 10;
    numero = (numero - ult) / 10;
    invertido = invertido * 10 + ult;
}

if  ( invertido == numero_ori ) {
    console.log("la capi y la cua:"+ invertido); }
else if ( invertido != numero ) {
    console.log ("no es la capi y la cua"); } 