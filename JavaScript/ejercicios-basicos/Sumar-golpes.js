/*
Ejercicio: Sumar golpes en un entrenamiento

Un personaje está entrenando y realiza golpes.

El personaje realiza golpes mientras no haya hecho 10 golpes.
Cada golpe tiene una potencia (la podés simular con un número fijo o variable).

Debés usar:
Un contador para contar cuántos golpes hizo.
Un acumulador para sumar la potencia total.
Usar un while para repetir hasta llegar a 10 golpes.

Al final, mostrar:
Total de golpes realizados
Potencia total acumulada


La potencia puede ser fija (por ejemplo 5 en cada golpe).

Ejemplo de salida

Golpe 1 - potencia 5
Golpe 2 - potencia 5
...
Golpe 10 - potencia 5

Total de golpes: 10
Potencia acumulada: 50


Pista
Contador → empieza en 0 y suma 1 en cada vuelta.
Acumulador → suma la potencia en cada iteración.
Condición del while → contador < 10. */

let potencia = 10;
let contador = 0;
let acumulador = 0;

while(contador < 10) {
    contador++;
    acumulador = acumulador + potencia;
    console.log("golpe:" + contador + "-" + "potencia:" + acumulador );
}

console.log("golpes total:" + contador + "-" + "potencia total:" + acumulador);