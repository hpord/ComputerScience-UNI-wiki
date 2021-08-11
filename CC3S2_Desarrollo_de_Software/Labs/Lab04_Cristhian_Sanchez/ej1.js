const numbers = [1, 2, 3, 4, 5, 6, 7, 8,
    9, 10, 11, 12, 13, 14, 15, 16, 17];

const filterPair = arr => {
    const filtered = arr.filter(el => el % 2 === 0);
    return filtered;
};

const isPrime = n => {
    if (n === 1) {
        return false;
    } else if (n === 2) {
        return true;
    } else {
        for (let x = 2; x < n; x++) {
            if (n % x === 0) {
                return false;
            }
        }
        return true;
    };
};

const filterPrime = arr => {
    const filtered = arr.filter(el => isPrime(el));
    return filtered;
};

const filterMultiples = arr => {
    const filtered = arr.filter(el => (el % 3 === 0) && (el !== 0));
    return filtered;
};


console.log("Imprimiendo números pares..");
console.log(filterPair(numbers));

console.log("\n\nImprimiendo números primos...");
console.log(filterPrime(numbers));

console.log("\n\nImprimiendo múltiplos de 3");
console.log(filterMultiples(numbers));