/*
Ejercicio: Recolección de monedas

Un personaje está explorando un mapa y va recolectando monedas.

El personaje encuentra monedas hasta haber pasado por 8 zonas.
En cada zona encuentra una cantidad fija de monedas (por ejemplo 3).

Utilizar:

Un contador para contar las zonas recorridas.
Un acumulador para sumar las monedas recolectadas.
Usar un while para repetir el proceso hasta recorrer las 8 zonas.

Al final mostrar:
Cuántas zonas recorrió
Cuántas monedas recolectó en total

La cantidad de monedas por zona puede ser fija.

Ejemplo de salida:

Zona 1 - monedas 3
Zona 2 - monedas 3
...
Zona 8 - monedas 3

Zonas recorridas: 8
Monedas totales: 24

Pista:

Contador empieza en 0 y llega hasta 8.
Acumulador suma 3 en cada vuelta. */


let monedas = 3;
let acumulador = 0; // monedasss
let contador = 0; // zonas

while ( contador < 8 ) {
    contador++;
    acumulador = acumulador + monedas;
    console.log( "zonas:" + contador + "-" + "monedas:" + acumulador);
}

console.log( "zonas recorridas:" + contador ); // seperar, no sobre explotar
console.log( "monedas recolectadas:" + acumulador ); 
