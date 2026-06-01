/*
Ejercicio: Número invertido

Escribí un programa que al ingresarle un número entero positivo, muestre por consola ese mismo número pero invertido.

Entrada:
1234

Salida:
4321

Pistas:
El último dígito de un número se puede obtener con la operación matemática % 10. 
*/

let numero = 1234;
let numinvertido = 0;
let ultimo;

console.log("numero de entrada:" + numero);
while (numero >= 1) {
    ultimo = numero % 10;
    numero = (numero - ultimo) / 10;
    numinvertido = numinvertido * 10 + ultimo;
}
console.log("numero de salida:"+ numinvertido);  
