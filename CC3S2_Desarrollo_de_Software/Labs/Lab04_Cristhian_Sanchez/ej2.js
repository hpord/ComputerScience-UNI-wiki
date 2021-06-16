const pizzas = [
    {
        name: 'Napolitana',
        toppings: ['cheese', 'sauce', 'pepperoni   '],
        crust: 'deep dish',
        serves: 2
    },
    {
        name: 'American  ',
        toppings: ['cheese', 'two hams', 'pepperoni'],
        crust: 'deep dish',
        serves: 2
    },
    {
        name: 'Hawain    ',
        toppings: ['cheese', 'sauce', 'pineapple   '],
        crust: 'deep dish',
        serves: 3
    },
    {
        name: 'Mix       ',
        toppings: ['cheese', 'sauce', 'ham', 'bacon   '],
        crust: 'deep dish',
        serves: 2
    },
    {
        name: 'National  ',
        toppings: ['cheese', 'sauce', 'bacon', 'garlic'],
        crust: 'deep dish',
        serves: 1
    },
];

console.log("Imprimiendo datos de las pizzas");
console.log("\nName\t\tToppings\t\tCrust  \tServes\n");

var values_total = [];
var keys = Object.keys(pizzas[0]);
for (var i = 0; i < pizzas.length; i++){
    var values = Object.keys(pizzas[i]).map(function(key){
        return pizzas[i][key];
    });
    values_total.push(values);
}


for (var i = 0; i < values_total.length; i++) {
    for (var j = 0; j < values_total[0].length; j++) {
        process.stdout.write(values_total[i][j] + "  ");
    
    }
    process.stdout.write("\n");
    
}
