/*
Ejercicio: Sistema de alquiler de bicicletas

Un local de alquiler de bicicletas registra su actividad durante 12 días.

Consigna:

El local comienza con:
    30 bicicletas disponibles
    $0 de ingresos

En cada día:

1.Si el día es:
    Par → se alquilan 5 bicicletas
    Impar → se alquilan 3 bicicletas
2.Cada alquiler cuesta: $200
3.Si el día es múltiplo de 4: Hay promoción → cada alquiler cuesta $150
4.Si el día es múltiplo de 6: Se agregan bicicletas → suma 8 bicicletas al stock

5.El sistema se detiene si no hay bicicletas disponibles (stock ≤ 0)

Ejemplo de salida:

Día 1 - alquilaste 3 bicicletas, ganaste $600 (stock: 27)
Día 2 - alquilaste 5 bicicletas, ganaste $1000 (stock: 22)
Día 4 - alquilaste 5 bicicletas con promoción, ganaste $750 (stock: 17)
Día 6 - alquilaste 5 bicicletas y recibiste nuevas bicicletas (stock: 20)

...

Sistema finalizado
Ingresos totales: $XXXX
Bicicletas restantes: XX */

let stock = 30;
let ingresos = 0;

for ( let i = 1 ; i <= 12 ; i++ ) {

    let mensaje= `Dia ${i} -`;
    let precio= 0;
    let ganancia= 0;
    let alquilados = 0;

    if ( stock <= 0 ) {
        break;
    }

    if ( i % 4 == 0 ) {
        precio= 150;
    } else {
        precio= 200;
    }

    if ( i % 2 == 0 && stock >= 5) {
        alquilados= 5;
        stock -= alquilados;
        ganancia = alquilados * precio;
    }else {
        alquilados= 3;
        stock -= 3;
        ganancia =alquilados * precio
    }

    mensaje+= `alquilaste ${alquilados} bicicletas y ganaste $${ganancia} (stock: ${stock}) `;

    if ( i % 6 == 0 ) {
        stock += 8;
        mensaje += `, recibiste nuevas bicicletas (stock:${stock})`;
    }

    ingresos = ingresos + ganancia;

    console.log (mensaje);
}
console.log( "Sistema finalizado ");

console.log("Ingresos totales:" , ingresos);

console.log("Stock total:" , stock);