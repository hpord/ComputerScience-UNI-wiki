// la convension de manejo de errores en los callback
// la funcion callback espera recibir por lo menos un argumento
// El primer argumento, siendo un error. 
// Opcionalmente puede tener uno o mas argumentos adicionales

var myCallback = function(err, data) {
    if (err) throw err; // Chequear el error y lanzarlo si existe.
    console.log('Recibi datos: '+data); // de otro modo proceder como siempre.
  };
  
  var usingItNow = function(callback) {
    callback(null, ' get it?'); //no quiero lanzar el error, 
                               // asi que se pasa un argumento null en vez de error
  };

  var usingItNow_Error = function(callback) {
    var myError = new Error('Un error propio!');
    callback(myError, 'get it?'); // Envio el error como primer argumento.
  };

  console.log("Usando el callback:");
  usingItNow(myCallback);

  console.log("Usando el callback con error:");
  usingItNow_Error(myCallback);
  