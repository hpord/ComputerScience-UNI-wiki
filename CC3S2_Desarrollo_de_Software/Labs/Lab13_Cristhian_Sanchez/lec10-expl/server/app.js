// instalar express nodemon y con
//  npm install express --save
// npm install --save-dev nodemon , 
//correr con: nodemon ./server/app.js
var express = require('express')
var app = express()
const port = 3000

app.use(function (req, res, next) {
    // Tiempo actual en milisegundos
    let ts = Date.now();
    let date_ob = new Date(ts);
    let date = date_ob.getDate();
    let month = date_ob.getMonth() + 1;
    let year = date_ob.getFullYear();

    // Imprime la fecha en el formato DD-MM-YYYY 
    console.log(date  + "-" + month + "-" + year );
    next()
})

//middleware
app.get('/', (req, res) => {
  res.send('Hello World! - desde el middleware ')
})

//Puerto 
app.listen(port, () => {
  console.log(`Aplicacion de Ejemplo escuchando en  http://localhost:${port}`)
})