const matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8, 9]];

//var merged = [].concat.apply([], matrix);

var merged = matrix.reduce(function(a, b){
    return a.concat(b);
}, []);

console.log("Imprimiendo matriz..\n");
console.log(matrix);

console.log("\nImprimiendo matriz aplanada...\n");
console.log(merged);