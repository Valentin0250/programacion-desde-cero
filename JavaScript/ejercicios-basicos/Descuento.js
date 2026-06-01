/*
Crear un programa que determine si una persona tiene descuento en una compra.

edad
esEstudiante (true o false)
totalCompra (número)

Si el cliente es menor de 18 → tiene 20% de descuento
Si es estudiante → tiene 10% de descuento
Si la compra es mayor a $10.000 → tiene 15% de descuento
Si cumple más de una condición, solo se aplica el mayor descuento */

let edad = 99;
let esEstudiante = false;
let totalcompra = 88;
let descuento = 0;

if ( edad <18 ) {
    descuento = 20;
}
if ( totalcompra > 10000 && descuento < 15 ) {
    descuento = 15;
}
if ( esEstudiante && descuento < 10 ) {
   descuento = 10;
}
console.log("descuento de :"+ descuento);