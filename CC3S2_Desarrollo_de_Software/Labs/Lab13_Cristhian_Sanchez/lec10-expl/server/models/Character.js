/**
 *In Mongoose, it’s a normal practice to put each model 
 in its own file. So we will create a Character.js
 
 */
const mongoose = require('mongoose');
const Schema = mongoose.Schema;


const characterSchema = new Schema({
  name: {type: String, unique:true},
  specials: Array,
  ultimate: String
});

module.exports = mongoose.model('Character', characterSchema);