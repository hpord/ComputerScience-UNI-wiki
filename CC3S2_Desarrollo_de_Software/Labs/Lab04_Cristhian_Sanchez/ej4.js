class Pizza {
    constructor(name, toppings, crust, serves, variant) {
        this.name = name;
        this.toppings = toppings;
        this.crust = crust;
        this.serves = serves;
        this.variant = variant;
    }
}


const pizzas = [
    [
        'Napolitana',
        ['cheese', 'sauce', 'pepperoni'],
        'deep dish',
        2
    ],
    [
        'American',
        ['cheese', 'sauce', 'pepperoni'],
        'deep dish',
        3
    ],
    [
        'Hawain',
        ['cheese', 'sauce', 'pineapple'],
        'deep dish',
        1
    ],
    [
        'Mix',
        ['cheese', 'sauce', 'ham', 'bacon'],
        'deep dish',
        2
    ],
    [
        'National  ',
        ['cheese', 'sauce', 'bacon', 'garlic'],
        'deep dish',
        1
    ],
];

console.log("Creando variante Regular...");
var regular = [];
for (var i = 0; i < pizzas.length; i++) {
    const pizzaRegular = new Pizza(
        pizzas[i][0],
        pizzas[i][1],
        pizzas[i][2], 
        pizzas[i][3],
        "regular"
    );
    regular.push(pizzaRegular);
    delete(pizzaRegular);
}

console.log(regular);

console.log("Creando variante Large...");
var large = [];
for (var i = 0; i < pizzas.length; i++) {
    const pizzaLarge = new Pizza(
        pizzas[i][0],
        pizzas[i][1],
        pizzas[i][2], 
        pizzas[i][3],
        "large"
    );
    large.push(pizzaLarge);
    delete(pizzaLarge);
}

console.log(large);

console.log("Creando variante extra-Large...");
var extraLarge = [];
for (var i = 0; i < pizzas.length; i++) {
    const pizzaExtraLarge = new Pizza(
        pizzas[i][0],
        pizzas[i][1],
        pizzas[i][2], 
        pizzas[i][3],
        "extra-large"
    );
    extraLarge.push(pizzaExtraLarge);
    delete(pizzaExtraLarge);
}

console.log(extraLarge);