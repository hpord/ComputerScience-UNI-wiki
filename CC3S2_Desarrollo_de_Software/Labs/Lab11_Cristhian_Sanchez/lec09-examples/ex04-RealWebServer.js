var http = require('http');
var fs = require('fs');

http.createServer(function (req, res) {

  const baseURL = (req.protocol) ? req.protocol : "http"   + '://' + req.headers.host + '/';
  const reqUrl = new URL(req.url,baseURL);
  //console.log(baseURL);
  console.log(reqUrl);
  
  var filename = "." + reqUrl.pathname;
  fs.readFile(filename, function(err, data) {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'});
      return res.end("404 Not Found :" + err.message);
    } 
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    return res.end();
  });
}).listen(8080);




