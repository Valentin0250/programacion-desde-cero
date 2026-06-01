/*
Ejercicio: Sistema de experiencia y subida de nivel

Un personaje gana experiencia al derrotar enemigos.

Reglas:

El personaje empieza en:
Nivel = 1
Experiencia = 0

En cada iteración (enemigo derrotado):

1. Gana experiencia según el tipo de enemigo:
 Tipo 1 → +10 exp
 Tipo 2 → +20 exp
 Tipo 3 → +30 exp
2. El tipo de enemigo rota: 1 → 2 → 3 → 1...
3. Cada vez que la experiencia llega a 50 o más: Sube de nivel
4. La experiencia se reinicia a 0
5. El programa debe ejecutarse hasta que el personaje llegue a nivel 5.

Ejemplo de salida por consola:

Enemigo 1 (tipo 1) - exp +10 - total exp 10
Enemigo 2 (tipo 2) - exp +20 - total exp 30
Enemigo 3 (tipo 3) - exp +30 - total exp 60
Subiste a nivel 2
...
Nivel final: 5
Enemigos derrotados: X */

let nivel = 1;
let experiencia = 0;
let tipo = 1;
let acumulador = 0;
let contador = 0;

while ( nivel < 5 ) {
    
    if( tipo == 1 ) {
        tipo = 2;
        experiencia = experiencia + 10;
        contador++;
    }

    else if ( tipo == 2 ) {
        tipo = 3;
        experiencia = experiencia + 20;
        contador++;
    }

    else if ( tipo == 3) {
        tipo = 1;
        experiencia = experiencia + 30;
        contador++;
    }

    acumulador = acumulador + experiencia;
    
    console.log("Enemigo" , tipo , "(tipo"+tipo+")" , "-" , "exp" , "+"+experiencia , "-" , "total exp" , acumulador);

    if (experiencia >= 50) { 
        nivel = nivel + 1;
        experiencia = 0;
    }  

} //Enemigo 1 (tipo 1) - exp +10 - total exp 10

console.log("Nivel final:" , nivel);
console.log("Enemigos derrotados:" , contador);