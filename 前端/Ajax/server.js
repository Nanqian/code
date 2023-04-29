//1. 引入express
const express = require('express');

//2. 创建应用对象
const app = express();

//3.创建路由规则
// request 是对请求报文的封装
// response 是对响应报文的封装
app.get('/', (request, response) => {
  //设置响应头  设置允许跨域
  response.setHeader('Access-Control-Allow-Origin', '*');
  //设置响应体
  response.send('HELLO AJAX');
});

//可以接收任意类型的请求
app.all('/server', (request, response) => {
  //设置响应头  设置允许跨域
  response.setHeader('Access-Control-Allow-Origin', '*');
  //响应头
  response.setHeader('Access-Control-Allow-Headers', '*');
  //设置响应体
  response.send('HELLO AJAX POST');
});

//JSON响应
app.all('/json-server', (request, response) => {
  response.setHeader('Access-Control-Allow-Origin', '*');
  response.setHeader('Access-Control-Allow-Headers', '*');
  const data = {
    name: 'nanian',
  };
  //设置响应体
  //send只能接收字符串参数，需先对对象进行字符串转换
  let str = JSON.stringify(data);
  response.send(str);
});

//针对ie缓存问题
app.all('/ie', (request, response) => {
  response.setHeader('Access-Control-Allow-Origin', '*');
  response.send('HELLO IE -3');
});

//延时响应
app.all('/delay', (request, response) => {
  response.setHeader('Access-Control-Allow-Origin', '*');
  setTimeout(() => {
    response.send('延时响应');
  }, 3000);
});

//axios 服务
app.all('/axios-server', (request, response) => {
  response.setHeader('Access-Control-Allow-Origin', '*');
  response.setHeader('Access-Control-Allow-Headers', '*');
  const data = { name: '南浅' };
  response.send(JSON.stringify(data));
});

//fetch 服务
app.all('/fetch-server', (request, response) => {
  response.setHeader('Access-Control-Allow-Origin', '*');
  response.setHeader('Access-Control-Allow-Headers', '*');
  const data = { name: '南浅' };
  response.send(JSON.stringify(data));
});

//jsonp 服务
app.all('/jsonp-server', (request, response) => {
  // response.send('console.log("hello jsonp")');
  const data = {
    name: 'nanqian',
  };
  //将数据转化成字符串
  let str = JSON.stringify(data);
  //返回结果
  response.end(`handle(${str})`);
});

//检测用户名是否存在
app.all('/check-username', (require, response) => {
  const data = {
    exist: 1,
    msg: '用户名已经存在',
  };
  let str = JSON.stringify(data);
  response.end(`handle(${str})`);
});

//4. 监听端口启动服务
app.listen(8000, () => {
  console.log('服务已经启动，8000 端口监听中....');
});
