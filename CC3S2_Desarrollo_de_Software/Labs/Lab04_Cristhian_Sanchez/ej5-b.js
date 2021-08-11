const arr = [2, 22, 1, -2, 23, -4];

var funcMap = x =>{
    if (x >= 0) {
        return 1; 
    } else {
        return 0;
    }
     
}

var funcSum = (a, b) => {
    return a + b;
}


const possitivesCounted = arr.map(funcMap).reduce(funcSum);

console.log("\nEn el arreglo..");
console.log(arr);
console.log("\nHay " + possitivesCounted + " positivos\n");