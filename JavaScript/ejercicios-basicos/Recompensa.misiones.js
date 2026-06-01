/* Ejercicio: Sistema de recompensas por misiones

Un jugador completa 12 misiones.

Consigna: Usá+ un for para recorrer las 12 misiones.

En cada misión:

1.Si el número de misión es:
    Par → gana 20 monedas
    Impar → gana 10 monedas

2.Además: Cada misión múltiplo de 5 → gana 50 monedas extra


3.Mostrar en cada iteración:
    Número de misión
    Monedas ganadas en esa misión
Al final mostrar:Total de monedas acumuladas

Ejemplo de salida por consola:

Misión 1 - monedas 10
Misión 2 - monedas 20
...
Misión 5 - monedas 60   (10 o 20 + 50 extra)

Total de monedas: XXX

Pistas:

Para saber si un numero es par:
i % 2 === 0
Para saber si un numero es múltiplo de 5:
i % 5 === 0 */


let monedas = 0;
let acumulacion = 0;

for ( let i = 1 ; i <= 12 ; i++ ) {
 // aca verifica si es par o impar
    if( i % 2 === 0 ) { 
        monedas = 20;
    }
    else {
        monedas = 10;
    }

    if( i % 5 === 0) {
        monedas = monedas + 50;
    }

    if ( i % 2 === 0 && i % 5 === 0 ) {
        monedas = 50 + 20;
    }

    else if ( i % 2 === 0 ) {
        monedas = 20;
    }

    else if ( i > 0 && i % 5 === 0 ) {
        monedas = 10 + 50;
    }
    else {
        monedas = 10;
    }
    
    acumulacion = acumulacion + monedas;
    console.log("Mision" , i , "-" ,"monedas" , monedas);
}
console.log("Total de monedas:" , acumulacion); 
