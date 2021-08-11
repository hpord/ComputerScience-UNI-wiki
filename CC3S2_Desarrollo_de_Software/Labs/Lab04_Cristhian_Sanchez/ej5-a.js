const arr = [1, 2, 3, 4, 5];

var funcMap = x =>{
    return x**2;
}

var funcSum = (a, b) => {
    return a + b;
}


const sumPower = arr.map(funcMap).reduce(funcSum);

console.log("\nEn el arreglo..");
console.log(arr);
console.log("\nEl resultado de la suma de cuadrados es " + sumPower + "\n");