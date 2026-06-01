/*Ejercicio: Día de la semana

Estás haciendo un programa que recibe un número del 1 al 7 y debe mostrar por terminal qué día de la semana es.

1 → Lunes
2 → Martes
3 → Miércoles
4 → Jueves
5 → Viernes
6 → Sábado
7 → Domingo

Si el número no está entre 1 y 7 → mostrar: "Día inválido" */  //switch case break default

let dia = 10

switch (dia) {
    case 1:
        console.log("lunes");
        break;
    case 2:
        console.log("martes");
        break;
    case 3:
        console.log("miercoles");
        break;
    case 4:
        console.log("jueves");
        break;
    case 5:
        console.log("viernes");
        break;
    case 6:
        console.log("sabado");
        break;
    case 7:
        console.log("domingo");
        break;
    default:
        console.log("dia invalido")
} 