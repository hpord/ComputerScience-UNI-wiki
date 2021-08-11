const mongoose = require('mongoose');

/* 
En Mongoose, es una práctica normal poner cada modelo
en su propio archivo. Entonces previamente crearemos 
un archivo /server/models/Character.js */

const Character = require('./models/Character');

var dotenv = require('dotenv');

dotenv.config();

//const url = 'mongodb://127.0.0.1:27017/street-fighters'
// defina en un archivo ".env" en la raiz de su proyecto
// la constante DB_CONNECTION="<su cadena de conexion a la BD
// street-fighters >"
var  url =process.env.DB_CONNECTION;

mongoose.connect(url, { useNewUrlParser: true });
/* 
Para comprobar si la conexión se ha realizado correctamente, 
podemos utilizar el evento 'open'. Para comprobar si la conexión falló,
usamos el evento  'error'.
*/

const db = mongoose.connection;
db.once('open', _ => {
  console.log('Database connected:', url);
});

db.on('error', err => {
  console.error('connection error:', err);
});

/*
Digamos que quiere crear un personaje llamado Ryu.
Ryu tiene un movimiento  llamado "Shinku Hadoken".
Para crear Ryu, use new, seguido de su modelo.
En este caso,  new Character.
*/

/**
 * new Character crea el personaje en la memoria.
  * Aún no se ha guardado en la base de datos.
  * Para guardar en la base de datos, puede ejecutar el método save.
 */

  async function runCode() {
    var ryu = new Character({
      name: 'Ryu',
      ultimate: 'Shinku Hadoken'
    });
  
    var doc = await ryu.save()
    console.log(doc);

    // * otro caracter *

    const ken = new Character({
        name: 'Ken',
        ultimate: 'Guren Enjinkyaku'
      });
      
      doc = await ken.save();
      console.log(doc);

  }
  
  async function runCleanCode(){
        /*para limpiar la coleccion Character */
        await Character.deleteMany({}, (err)=>{
          if(!err) {console.log("La Coleccion Character fue Borrada !");} 
          console.log(err);
         });
  }

    async function runUpdateCode(){

/*    Digamos que Ryu tiene tres movimientos especiales:
      Hadoken, Shoryuken, Tatsumaki Senpukyaku
      Queremos agregar estos movimientos especiales a la base de datos. 
      Primero, necesitamos actualizar nuestro  Schema Character. 
      agregando specials : Array 

      const characterSchema = new Schema({
          name: {type: String, unique:true},
          specials: Array,
          ultimate: String
      });

      */

        var ryu = await Character.findOne({ name: 'Ryu' });
        ryu.specials = [
        'Hadoken',
        'Shoryuken',
        'Tatsumaki Senpukyaku'
        ];

        var doc = await ryu.save();
        console.log(ryu.specials);
    }

    /**para insertar en la coleccion  caracteres */
      //runCode().catch(error => { console.error(error) });

    /**para actualizar la coleccion caracteres */
     runUpdateCode().catch(error => { console.error(error) });

        /**para eliminar  la coleccion  caracteres */
    //   runCleanCode().catch(error => { console.error(error) });
