# HTTP
HTTP (hypertext transport protocol)协议「超文本传输协议」，协议详细规定了浏览器和万维网互相通信的规则。

## 请求报文
**重点是格式与参数**
```
行       POST  /s?wd=apple (参数）  HTTP/1.1
头       Host: atguigu.com
         Cookie: name=guigu
         Content-type: application/x-www-form-urlencoded
         User-Agent: chrome 83
空行
体       username-admin&password=admin

请求方式为get时请求体为空，POST方式可以不为空
```

## 响应报文
```
行        HTTP/1.1  200  OK
头        Content-Type: text/html;charset=utf-8
          Content-length: 2048
          Content-encoding: gzip
空行
体         <html>
             <head>
             </head>
             <body>
               <h1>巴拉巴拉</h1>
             </body>

           </html>
```
* 404
* 403
* 401
* 500
* 200