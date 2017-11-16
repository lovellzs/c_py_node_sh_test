var http = require('http');
var url = require('url');
var util = require('util');
 
http.createServer(function(req, res){
    
    // res.writeHead(200, {'Content-Type': 'text/html;charset=gb2312'});

    res.writeHead(200, {'Content-Type': 'text/html;charset=utf8'});



	// 解析 url 参数
    var params = url.parse(req.url, true).query;
    res.write("网站名：" + params.name);
    res.write("\n");
    res.write("网站 URL：" + params.url);

    res.end(util.inspect(url.parse(req.url, true)));



}).listen(3000);

console.log('Server running at http://127.0.0.1:3000/');