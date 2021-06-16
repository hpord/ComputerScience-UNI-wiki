// flujo del Pipeline
 
// Generalmentre se usa para obtener data y transferirla  de un stream a otro stream.

//En este ejemplo queremos escribir un archivo 
// con el contenido de otro archivo.

// creamos un input.txt con un texto de ejemplo


var fs = require("fs");

var readerStream = fs.createReadStream('input.txt');

var writerStream = fs.createWriteStream('output2.txt');


// Leer el contenido del archivo input.txt 
// escribir el contenido en el archivo output.txt
readerStream.pipe(writerStream);

console.log("Ejecucion del programa terminado ");

//El resultado de la ejecucion sera:

//$ node ex03-Pipelinestream.js

// ver el contenido dee output.txt file:

//$ cat output.txt 

