var express = require('express')
var app = express()
var fs=require('fs');
const port = 3000


app.get('/', (req, res) => {
  res.send('Hello World 2! - desde el -ej 2 ')
});

app.get('/object/:objid', (req, res) => {
  var dbFile = "./server/DB"+ req.params.objid;
  fs.readFile(dbFile, function(err,contents){
    if(err){
      res.status(500).send(err.message);
      
    } else{
      var obj=JSON.parse(contents); // JSON.parse acepta Buffers
      obj.date=new Date();
      console.log(obj);
      res.set('Content-type', 'application/json');
      res.status(200).send(JSON.stringify(obj));
    }
  });
})

//Puerto 
app.listen(port, () => {
  console.log(`Aplicacion de Ejemplo escuchando en  http://localhost:${port}`)
})