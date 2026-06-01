/*
Ejercicio: Sistema de vidas y puntaje

Un jugador juega 15 rondas.

Consigna:
El jugador empieza con:
    3 vidas
    0 puntos

Usá un for para recorrer las 15 rondas.

En cada ronda:
1.Si la ronda es:
    Par → gana 20 puntos
    Impar → gana 10 puntos

2.Si la ronda es múltiplo de 4 → pierde 1 vida y no gana puntos
3.El juego termina antes si: Las vidas llegan a 0

Ejemplo de salida:

Ronda 1 - ganaste 10 puntos
Ronda 2 - ganaste 20 puntos
Ronda 3 - ganaste 10 puntos
Ronda 4 - perdiste una vida (vidas: 2)
...

Juego terminado
Puntos totales: XXX
Vidas restantes: X */

let vidas = 3;
let puntos = 0;
let acumulacion = 0;

for( let i = 1 ; i <= 15 ; i++ ) {

    if ( vidas == 0 ) {
     break;
    }
    console.log("Ronda:"+i);
    if ( i % 4 === 0 ) {
        vidas = vidas - 1;
       // puntos = puntos - 20;
        console.log("-" , "perdiste una vida" , "(vidas:" , vidas+")");
    }else if ( i % 2 === 0 ) {
        puntos = puntos + 20;
    }
    else {
        puntos = puntos + 10;
    }

   // acumulacion = acumulacion + puntos;

    console.log("Ronda" , i , "-" , "ganaste" , puntos , "puntos");
}
console.log("Juego terminado");
console.log("Puntos totales:" , puntos);
console.log("Vidas restantes:" , vidas); 
