let timerId = setInterval(function () {
    console.log("HI!");
}, 1000);

setTimeout(function () {
    clearTimeout(timerId);
}, 3000);