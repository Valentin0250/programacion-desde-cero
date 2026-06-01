/*
1. Declarar dos variables:
 edad
 tieneEntrada (true o false)

2.Usar condicionales if para verificar lo siguiente:
    Si la persona tiene entrada y es mayor o igual a 18, puede pasar.
    Si tiene entrada pero es menor de 18, no puede pasar.
    Si no tiene entrada, no puede pasar sin importar la edad.

💡 Ejemplo de valores:
let edad = 20;
let tieneEntrada = true;

Mostrar en consola uno de estos mensajes:

"Puede ingresar al evento"
"No puede ingresar por ser menor de edad"
"No puede ingresar porque no tiene entrada" */


let edad = 20;
let tieneEntrada = true;
if ( edad >=18 && tieneEntrada ) {
    console.log("pasa pibe")
} else if ( edad < 18 && tieneEntrada ) {
    console.log("nou nou sos wachin")
} else  {
    console.log("no podes amigo")
}

let edad = 16;
let tieneEntrada = true;

if(!tieneEntrada){
    console.log("No puede ingresar porque no tiene entrada");
}
if(edad < 18){
    console.log("No puede ingresar por ser menor de edad")
}
else{
    console.log("Puede ingresar al evento")
}
