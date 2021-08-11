var express= require('express')
var fs = require('fs');
var app= express();
var multer = require('multer');

app.use(express.json());
app.use(express.urlencoded({
    extended: true
  }));
app.use('/', express.static(__dirname + '/public'));

app.get('/', function(req, res){
  res.render('index.html');
});

var upload = multer({ dest: 'uploads/' })

app.post('/submit', upload.single('file'), function(req, res, next) {
  
    var html = fs.readFileSync(req.file.path, 'utf-8');
    
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end(html);
});
//Listening to computer's IP address
app.listen(3000);
console.log('Listening at 192.168.0.172:3000')