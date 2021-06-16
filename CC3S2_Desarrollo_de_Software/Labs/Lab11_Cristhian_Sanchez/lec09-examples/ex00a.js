//Ejemplo NodeJs leyendo un archivo
//Crear el archivo input.txt:
//Crear ex00.js file, como sigue:

var fs = require("fs"); // requiere - es una llamada a un módulo de Node
                        //fs - encapsula las llamadas de sistema  a sync()
                        //lo que graba todas las modificaciones en los buffers al
                        //sistema de archivos 
fs.readFile ('input.txt', readDoneCallback); //empezar la lectura
function readDoneCallback(error,dataBuffer){
//Convension de llamadas a funciones callback en Node:
//Primer argumento: Objeto error de JavaScript
//dataBuffer es un objeto especial de Node tipo Buffer()

//imprime: <Buffer 45 6e 20 75 6e 20 6c 75 67 61 ...
console.log(dataBuffer); //imprime: <Buffer 45 6e 20 75 6e 20 6c 75 67 61 ...
    if(!error){
        console.log("Contenideo del archivo:",dataBuffer.toString());    
    }
}
console.log(" ****************************** Ejecución terminada *****************************");
//$ node ex00a.js 


