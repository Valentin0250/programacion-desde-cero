/*
Ejercicio: Combate contra enemigos

Un personaje entra en combate contra enemigos uno por uno.

Reglas del juego:

El personaje tiene 100 puntos de vida.
Enfrenta enemigos mientras su vida sea mayor a 0.
Cada enemigo hace un daño diferente según su tipo:
Tipo 1 → 10 de daño
Tipo 2 → 15 de daño
Tipo 3 → 20 de daño

El tipo de enemigo va cambiando en cada iteración:
1, luego 2, luego 3, y vuelve a 1 (ciclo).

Utilizar:
Un contador para contar cuántos enemigos enfrentó.
Un acumulador para sumar el daño total recibido.
Un while para repetir mientras la vida sea > 0.

if / else if para decidir el daño según el tipo de enemigo.
Si la vida baja de 0, se corta el combate.

Reglas importantes:
El tipo de enemigo se controla con una variable que va rotando.

Ejemplo de salida:

Enemigo 1 (tipo 1) - daño 10 - vida 90
Enemigo 2 (tipo 2) - daño 15 - vida 75
Enemigo 3 (tipo 3) - daño 20 - vida 55
Enemigo 4 (tipo 1) - daño 10 - vida 45
...
El personaje fue derrotado
Enemigos enfrentados: X
Daño total recibido: Y


Pistas:

Vida empieza en 100.
Tipo de enemigo puede ser una variable que va cambiando así:
1 → 2 → 3 → 1 → 2...
Usá if / else if para aplicar el daño.
Acumulador = suma de daño total.
Contador = enemigos enfrentados. */

let vida = 100;  // pj                            // if else while
let acumulador = 0; // daño recibido
let contador = 0; // enemigos
let tipo = 1;
let daño = 0;

while ( vida > 0) {

    if (tipo == 1) {  // == SI = NO, DENTRO DE UNA CONDICIONAL
        vida = vida - 10;
        tipo = 2;
        contador++;
        daño = 10;
    }
    else if (tipo == 2) {
        vida = vida - 15;
        tipo = 3;
        contador++;
        daño = 15;
    }
    else if (tipo == 3) {
        vida = vida - 20;
        tipo = 1;
        contador++;
        daño = 20; //Enemigo 4 (tipo 1) - daño 10 - vida 45
    }
    acumulador = (acumulador + daño);
    console.log("enemigo" ,  tipo , "(tipo" + tipo +")" , "-" , "daño" , daño , "-" , "vida" , vida);
}

console.log("personaje derrotado");
console.log("enemigos derrotados:" + contador);
console.log("daño recibido :" + acumulador); 
