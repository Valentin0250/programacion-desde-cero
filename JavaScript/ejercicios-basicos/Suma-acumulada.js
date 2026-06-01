/*
Ejercicio: Suma acumulada hasta superar un límite

Escribí un programa que:

Empiece con una suma en 0
Vaya sumando números consecutivos empezando desde 1 (1, 2, 3, 4, …)
Se detenga cuando la suma sea mayor o igual a 50  
*/

let suma= 0;
let i= 1;

while ( suma <= 50 ) {
    suma = suma + i;
    console.log( "suma:",suma);
    i++; // contador
} 