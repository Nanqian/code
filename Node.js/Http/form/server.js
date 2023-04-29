let http = require('http');
let fs = require('fs');
let server = http.createServer(function (req, res) {
  if (req.url == '/login') {
    switch (req.method) {
      case 'GET':
        fs.createReadStream('login.html').pipe(res);
        break;
      case 'POST':
        res.end('hello');
        break;
      default:
        console.log('other request');
    }
  } else {
    res.writeHead(302, {
      Location: '/login',
    });
    res.end();
  }
  res.end();
});

server.listen(3000);
