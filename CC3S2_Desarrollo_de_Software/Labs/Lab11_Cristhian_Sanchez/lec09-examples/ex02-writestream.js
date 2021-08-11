//Write stream
//Create main.js file, as follows:

var fs = require("fs");
var data = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero';

// Crear un stream para escritura y escribirla en el archivo output.txt
var writerStream = fs.createWriteStream('output.txt');

// Usar la codificación utf8 para escribir los datos
writerStream.write(data,'UTF8');

// marca el final del archivo
writerStream.end();

// Manejo de eventos de transmisión -> datos, finalización y error
writerStream.on('finish', function() {
    console.log("La escritura está completa");
});

writerStream.on('error', function(err){
   console.log(err.stack);
});

console.log("Ejecucion completada");

// En el progerama data se escribira en el archivo de salida output.txt.
//El resultado de la ejecucion sera:

//$ node ex02-writestream.js

//output.txt con el contenodp de la variable data:
//$ cat output.txt 

