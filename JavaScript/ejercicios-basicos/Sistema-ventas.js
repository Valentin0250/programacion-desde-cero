/*
Ejercicio: Sistema de ventas y stock

Una tienda registra sus ventas durante 15 días.

Consigna:

La tienda empieza con:

50 productos en stock
$0 de ingresos

Usá un for para recorrer los 15 días.

En cada día:

1.Si el día es:
    Par → vende 4 productos
    Impar → vende 2 productos
2.Cada producto vale: $100
3.Si el día es múltiplo de 3:
 Hay descuento → cada producto vale $80
4.Si el día es múltiplo de 5:
    Llega reposición → suma 10 productos al stock

El sistema se detiene si: El stock llega a 0 o menos

Ejemplo de salida:
Día 1 - vendiste 2 productos, ganaste $200 (stock: 48)
Día 2 - vendiste 4 productos, ganaste $400 (stock: 44)
Día 3 - vendiste 2 productos con descuento, ganaste $160 (stock: 42)
Día 5 - vendiste 2 productos y recibiste reposición (stock: 50)

...

Sistema finalizado
Ingresos totales: $XXXX
Stock restante: XX */

let productos = 50;
let ingresos = 0;

for ( let i = 1 ; i <= 15 ; i++ ) {

    let mensaje= `Dia ${i} -`;
    let vendido = 0;
    let ganancia= 0;
    let precio= 0;

/// si no hay stock se detiene
    if ( productos <= 0 ) {
        break;
    }

    if ( i % 3 == 0 ) {
        precio = 80;
    }else {
        precio = 100;
    }

/// si es par entra en el if, si es umpar entra en el else
    if ( i % 2 == 0 ) {
        vendido = 4;
        productos -= vendido;
        ganancia = vendido * precio; 
    }else {
        vendido = 2;
        productos -= vendido;
        ganancia = vendido * precio;
    }

    mensaje += `vendiste ${vendido} productos, ganaste $${ganancia} (stock: ${productos})`;

    if ( i % 5 == 0 ) {
        productos += 10;
        mensaje += `y recibiste reposicion (stock:`+ productos +`)`;
    }
    
    ingresos = ingresos + ganancia;

    console.log( mensaje );
}
console.log(`Sistema finalizado`);
console.log(`Ingresos totales:` + ingresos);
console.log(`Stock restantes:` + productos); 
