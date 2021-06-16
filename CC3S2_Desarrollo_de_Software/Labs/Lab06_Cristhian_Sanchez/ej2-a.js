const reject = (array, func) => {
	console.log(
		array.filter(function(n) {
			return !func(n);
		})
	);
};

const moduloDos = (numero) => {
	return numero % 2 === 0;
};

const mayorDeDos = (numero) => {
	return numero > 2;
};

const array = [ 1, 2, 3, 4, 5, 6 ];

console.log(array);

console.log('\nImprimiendo elementos que no son mayores a 2..');
reject(array, mayorDeDos);

console.log('\nImprimiendo elementos que no son módulo 2..');
reject(array, moduloDos);
