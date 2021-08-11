var express = require('express')
var app = express()
const port = 5000

app.use(function (req, res, next) {

    // current timestamp in milliseconds
    let ts = Date.now();

    let date_ob = new Date(ts);
    let date = date_ob.getDate();
    let month = date_ob.getMonth() + 1;
    let year = date_ob.getFullYear();

    // prints date & time in YYYY-MM-DD format
    console.log(year + "-" + month + "-" + date);

    next()
})

//middleware
app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/user/:id', function (req, res) {
    res.send('user ' + req.params.id)
})

app.use(express.json()) // for parsing application/json
app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded

/* 
curl -X POST -H "Content-Type: application/json" \
    -d '{"name": "Pedro", "email": "pedr@example.com"}' \
    http://localhost:5000/profile
*/

app.post('/profile', function (req, res, next) {
  console.log(req.body)
  res.json(req.body)
})



//Puerto 
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
