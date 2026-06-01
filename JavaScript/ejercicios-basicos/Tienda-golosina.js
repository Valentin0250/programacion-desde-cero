/*
Ejercicio: Tienda de golosinas

Una tienda registra sus ventas durante 10 días.

Condiciones iniciales:

    40 unidades de galletitas
    30 unidades de chocolates
    $0 de ingresos

Reglas de venta por día:

Galletitas:
    Días impares → se venden 3
    Días pares → se venden 5
Chocolates:
    Días múltiplos de 3 → se venden 4
    Resto de los días → se venden 2
Precios:
    Galletitas: $50
    Chocolates: $80
Descuentos especiales:
    Días múltiplos de 5 → 20% de descuento en todas las ventas
Reposición:
    Días múltiplos de 4 → llegan 6 galletitas y 3 chocolates

Condición de corte:
El sistema se detiene si el stock de cualquier producto llega a 0 o menos.

Ejemplo de salida:

Día 1 - vendiste 3 galletitas y 2 chocolates, ganaste $260 (stock: 37 galletitas, 28 chocolates)
Día 5 - vendiste 5 galletitas y 2 chocolates con descuento, ganaste $336 (stock: 32 galletitas, 26 chocolates)
Día 8 - vendiste 5 galletitas y 2 chocolates y recibiste reposición (stock: 31 galletitas, 27 chocolates)
...
Sistema finalizado
Ingresos totales: $XXXX
Stock restante: XX galletitas, XX chocolates */

let stock_galletitas = 40;
let stock_chocolates = 30;
let ingresos = 0;

for (let i = 1; i <= 10; i++ ){

  let precio_galletitas = 50;
  let precio_chocolates = 80;
  let galletitas_vendidas = 0;
  let chocolates_vendidos = 0;

  let mensaje = `Dia ${i} - `;

  //Condicion de corte sin stock de cualquier producto
  if(stock_galletitas <= 0 || stock_chocolates <= 0){
    break;
  }

  //Reintegro stock días multiplos de 4
  if(i % 4 === 0){
    stock_galletitas += 6;
    stock_chocolates += 3; 
  }

  //Calculo de precios 20% de descuento multiplos de 5
  if(i % 5 === 0){
    precio_galletitas -= precio_galletitas * 20 / 100;
    precio_chocolates -= precio_chocolates * 20 / 100;
  }

  //Si es día par o impar...
  if(i % 2 === 0){

    if(stock_galletitas < 5){
      galletitas_vendidas = stock_galletitas;
    }
    else{
      galletitas_vendidas = 5;
    }
    stock_galletitas -= galletitas_vendidas;

  }else{
    if(stock_galletitas < 3){
      galletitas_vendidas = stock_galletitas;
    }
    else{
      galletitas_vendidas = 3;
    }
    stock_galletitas -= galletitas_vendidas;
  }
  //Si es multiplo de 3 o resto de dias...
  if(i % 3 === 0){
    chocolates_vendidos = 4
    stock_chocolates -= chocolates_vendidos;
    if(stock_chocolates < 0){
      stock_chocolates = 0;
    }
  }else{
    chocolates_vendidos = 2;
    stock_chocolates -= chocolates_vendidos;
    if(stock_chocolates < 0){
      stock_chocolates = 0;
    }
  }
  let ingreso_diario = (chocolates_vendidos * precio_chocolates) + (galletitas_vendidas * precio_galletitas);
  ingresos += ingreso_diario;
  mensaje += `vendiste ${galletitas_vendidas} galletitas y ${chocolates_vendidos} chocolates, ganaste $${ingreso_diario} (stock: ${stock_galletitas} galletitas, ${stock_chocolates} chocolates)`;
  console.log(mensaje);
}
console.log("Sistema finalizado");
console.log("Ingresos totales: ", ingresos);
console.log(`Stock restante: ${stock_galletitas} galletitas, ${stock_chocolates} chocolates`);
