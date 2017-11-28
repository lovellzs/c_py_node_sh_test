var http = require("http");
var url = require("url");

var server = http.createServer(function(req,res){

    if(req.url == "/favicon.ico"){
        return;
    }

	//url.parse()可以将一个完整的URL地址，分为很多部分：
	//host、port、pathname、path、query
	var pathname = url.parse(req.url).pathname;
	//url.parse()如果第二个参数是true，那么就可以将所有的查询变为对象
	//就可以直接打点得到这个参数
	var query = url.parse(req.url,true).query;
	//直接打点得到这个参数

    var jsStr = JSON.stringify( {name:"zhangsan",desc:"haha",sex:"false",age:"18" } );

	// var jsStr = JSON.stringify( {name:true,desc:19,sex:"false",age:"18" } );

	console.log(jsStr);
	if(pathname.indexOf("user") >=0 ){
        res.writeHead(200,{"Content-Type":"text/plain;charset=UTF8"})
        res.write( jsStr );
	}
	res.end();
});

server.listen(3000,"192.168.39.124");
