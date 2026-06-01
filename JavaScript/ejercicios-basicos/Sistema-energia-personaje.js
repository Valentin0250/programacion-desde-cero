/*
Ejercicio: Sistema de energía de un personaje

Estás programando la lógica de energía de un personaje en un juego.

1.El personaje empieza con 100 de energía.

2.Cada acción consume:
    Ataque → 15 energía
    Correr → 10 energía
    Defender → 5 energía

3.La ejecución continúa mientras la energía sea mayor a 0.
4.En cada iteración simulá una acción (podés fijarla manualmente con un número, por ejemplo 1 = atacar, 2 = correr, 3 = defender).
5.Mostrá la energía restante después de cada acción.
7.Cuando la energía llegue a 0 o menos, mostrar: "El personaje está agotado".

Pistas

Controlá que la energía no baje de 0 (opcional, pero suma puntos).
Podés contar cuántas acciones hizo el jugador.

Ejemplo de flujo:

Acción: atacar → energía: 85
Acción: correr → energía: 75
Acción: defender → energía: 70
...
El personaje está agotado */

let energia = 100;
let accion = 1;

while ( energia > 0 ) {
    if (accion == 1) {
        energia = energia - 15 // acumulador
        accion = 2
        if ( energia < 0) {
            energia = 0
        }
        console.log("accion: atacar"+ accion +"→"+ "energia:"+energia); 
    }

    else if (accion == 2) {
        energia = energia - 10
        accion = 3
        if ( energia < 0) {
            energia = 0
        }
        console.log("accion: correr"+ accion +"→"+ "energia:"+energia); 
    }

    else if (accion == 3) {
        energia = energia - 5
        accion = 1
        if ( energia < 0) {
            energia = 0
        }
        console.log("accion: defender"+ accion +"→"+ "energia:"+energia); 
    }
}
console.log("el personaje esta agotado"); 