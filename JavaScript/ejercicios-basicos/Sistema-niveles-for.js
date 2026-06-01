/*
Ejercicio: Sistema de puntos por niveles

Un personaje juega 10 rondas y gana puntos.

Consigna: Usá un bucle for para recorrer 10 rondas.

En cada ronda:
1.Si la ronda es:
    1 a 3 → gana 10 puntos
    4 a 7 → gana 20 puntos
    8 a 10 → gana 30 puntos

2.Mostrar en cada vuelta:
    Número de ronda
    Puntos ganados

Al final mostrar:
    Total de puntos acumulados

Ejemplo de salida por consola:

Ronda 1 - puntos 10
Ronda 2 - puntos 10
...
Ronda 8 - puntos 30

Total de puntos: XXX */

let puntos = 0;
let acumulados = 0; 

for( let i = 1 ; i <= 10 ; i++) {

    if ( i < 4 ) {
        puntos = 10;
    }

    else if ( i < 8 ) {
        puntos = 20;
    }

    else if ( i <= 10 ) {
        puntos = 30;
    } 

    acumulados = acumulados + puntos;

    console.log("Ronda" , i , "-" , "puntos" , puntos);

}
console.log("Total de puntos:" , acumulados);