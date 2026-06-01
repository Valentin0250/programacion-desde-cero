/*
Ejercicio: Sistema de energía y monedas

Un jugador juega 20 rondas.

Consigna:

El jugador empieza con:

5 de energía
0 monedas

Usá un for para recorrer las 20 rondas.

En cada ronda:
1.Si la ronda es:
    Par → gana 15 monedas
    Impar → gana 5 monedas
Si la ronda es múltiplo de 3 → pierde 2 de energía
(pero sí gana monedas normalmente)
Si la ronda es múltiplo de 5 → recupera 1 de energía
4.El juego termina antes si: La energía llega a 0

Ejemplo de salida:
Ronda 1 - ganaste 5 monedas
Ronda 2 - ganaste 15 monedas
Ronda 3 - ganaste 5 monedas y perdiste 2 de energía (energía: 3)
Ronda 5 - ganaste 5 monedas y recuperaste 1 de energía (energía: 4)
...

Juego terminado
Monedas totales: XXX
Energía restante: X */

let monedas = 0;
let energia = 5;
let rondas = 20;

for ( let i = 1 ; i <= rondas ; i++ ) {

    let mensaje = "Ronda " + i + " - ";

    // ¿TIENE ENERGIA?
    if ( energia <= 0 ) {
        break;
    }

    //¿LA RONDA ES PAR O IMPAR?
    if ( i % 2 == 0 ) {
        monedas = monedas + 15;
        mensaje = mensaje + "ganaste 15 monedas"
    }else {
        monedas = monedas + 5;
        mensaje = mensaje + "ganaste 5 monedas"
    }

    // ¿ES MULTIPLO DE 3?
    if ( i % 3 == 0 ) {
        energia = energia - 2;
        mensaje = mensaje + " - perdiste 2 de energia" + "(energia:" + energia + ")";
    }

    // ¿ES MULTIPLO DE 5?
    if ( i % 5 == 0 ) {
        energia = energia + 1;
        mensaje = mensaje + " - recuperaste 1 de energia" + "(energia:" + energia + ")";
    }

    console.log(mensaje)
}
console.log("juego terminado");
console.log("monedas totales:" , monedas);
console.log("energia restantes:" , energia);