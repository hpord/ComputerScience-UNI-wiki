var all = document.getElementsByTagName('ol')[0]
            .getElementsByTagName('li');

const colored = (element) => {
    element.style.backgroundColor = "green";
}

for (var i = 0, max = all.length; i < max; i++) {
    setTimeout(colored(all[i]), 1000);
    
}
