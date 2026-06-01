/*Ejercicio: Clasificación de clima

Estás haciendo una app que recibe el clima actual como texto:

"soleado" → mostrar: "Hace calor, usá ropa liviana "
"lluvioso" → mostrar: "Llevá paraguas "
"nublado" → mostrar: "El día está gris "
"nevando" → mostrar: "Hace mucho frío "

 Si el texto no coincide con ninguno →
mostrar: "Clima desconocido" */


let clima= "soleado";

switch(clima) {
    case "soleado":
        console.log("hace calor, usa ropa liviana");
        break;
    case "lluvioso":
        console.log("lleva paraguas");
        break;
    case "nublado":
        console.log("el dia esta gris");
        break;
    case "nevando":
        console.log("hace mucho pio");
        break;
    default:
        console.log("clima desconocido");
} 
