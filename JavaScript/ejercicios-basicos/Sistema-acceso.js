/* Ejercicio: Sistema de acceso a una misión especial

Estás programando un juego donde el jugador quiere acceder a una misión especial. Hay varias condiciones:

Si tiene más de 1000 puntos y 5 o más vidas → accede directamente
Si tiene más de 1000 puntos pero menos de 5 vidas → accede, pero con penalización
Si tiene entre 500 y 1000 puntos (inclusive) y al menos 3 vidas → acceso limitado
En cualquier otro caso → no puede acceder

Consigna:
Mostrar por consola uno de estos mensajes según corresponda:

"Acceso total a la misión"
"Acceso con penalización"
"Acceso limitado"
"Acceso denegado" */

let puntos = 700;
let vidas = 2;
//let mostrar;

if ( puntos > 1000 && vidas >= 5) {                   // console.log( mostrar + "\n")
   // mostrar= "Acceso total a la misión";
    console.log ("Acceso total a la misión");
}

else if ( puntos > 1000 && vidas < 5) {
   // mostrar= "Acceso con penalizacion";
    console.log("Acceso con penalizacion");
}

else if ( puntos >= 500 && puntos <= 1000 && vidas >= 3 ) {
   // mostrar= "Acceso limitado";
   console.log("Acceso limitado");
}
else {
   // mostrar= "Acceso denegado";
   console.log("Acceso denegado");
} 
