/*Ejercicio: ¿Puede el jugador pasar de nivel?

Imaginá que estás creando un juego donde el jugador necesita cumplir ciertas condiciones para pasar al siguiente nivel.

El jugador debe tener al menos 100 puntos
Y además debe tener 3 o más vidas
Si cumple ambas → pasa de nivel
Si no → no pasa

Informar por consola. */

let puntos = 99;
let vidas = 2;

if ( puntos >= 100 && vidas >= 3 ) {
    console.log("pasa de nivel");
}
else {
    console.log ("no pasa");
} 
