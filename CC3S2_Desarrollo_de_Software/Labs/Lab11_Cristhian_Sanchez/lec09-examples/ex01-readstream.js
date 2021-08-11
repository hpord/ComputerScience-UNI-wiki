//Read data from the stream
//Create input.txt file:

//Create main.js file, as follows:

var fs = require("fs");
var data = '';

// Crear un stream de lectura
var readerStream = fs.createReadStream('input.txt');

// Utilizar codificación utf8
readerStream.setEncoding('UTF8');

// Manejo de eventos de transmisión -> datos, finalización y error
readerStream.on('data', function(chunk) {
   data += chunk;
});

readerStream.on('end',function(){
   console.log(data);
});

readerStream.on('error', function(err){
   console.log(err.stack);
});

console.log("Ejecución terminada ");

//$ node ex01-readstream.js 


