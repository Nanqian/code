let http = require('http');
let server = http.createServer(function (req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('<html><body><h1>HELLO NODE!</h1><body></html>');
});

server.listen(3000);
