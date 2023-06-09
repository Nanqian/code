let fs = require('fs');
let data = '';

// 创建可读流
let readerStream = fs.createReadStream('./input.txt');

// 设置编码为 utf8。
readerStream.setEncoding('UTF8');

// 处理流事件 --> data, end, and error
readerStream.on('data', function (chunk) {
  data += chunk;
});

readerStream.on('end', function () {
  console.log(data);
});

readerStream.on('error', function () {
  console.warn('error');
});

console.log('程序执行完毕');
