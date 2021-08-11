const tp = require('./procesador-plantillas.js');
var template = 'Mi mes favorito es {{mes}},  pero no me gustan los dias {{dia}} o el año {{año}}';
console.log(typeof tp.TemplateProcessor);
console.log(`\nImprimiendo plantilla...\n ${template}\n`);

var dateTemplate = new tp.TemplateProcessor(template);

var dictionary1 = { mes: 'Julio', dia: '13', año: '2020' };
console.log(`\nProbando diccionario 1: \n`);
console.log(dictionary1);
var str1 = dateTemplate.fillIn(dictionary1);
console.log(`\n${str1}`);
// console.log(str === 'Mi mes favorito es Julio,  pero no me gustan los dias 13 o el año 2020');

var dictionary2 = { mes: 'Junio', dia: '08', año: '1998', cualquierItem: 'No aparecerá' };
console.log(`\nProbando diccionario 2: \n`);
console.log(dictionary2);
var str2 = dateTemplate.fillIn(dictionary2);
console.log(`\n${str2}`);
