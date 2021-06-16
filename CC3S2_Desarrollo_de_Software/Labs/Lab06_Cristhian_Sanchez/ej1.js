const each = (array, func) => {
    array.forEach(numero => func(numero));
}

const doble = (numero) => {
    console.log(numero * 2);
}

const cuadrado = (numero) => {
    console.log(numero ** 2);
}

const raizCuadrada = (numero) => {
    console.log(numero ** 0.5);
}

const array = [1, 2, 3, 4, 5, 6];

console.log(array);

console.log("\nImprimiendo dobles..");
each(array, doble);

console.log("\nImprimiendo cuadrados..");
each(array, cuadrado);

console.log("\nImprimiendo raíces cuadradas..");
each(array, raizCuadrada);
