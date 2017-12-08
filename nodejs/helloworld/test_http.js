var http = require("http");
var url = require("url");

var server = http.createServer(function (req, res) {

    if (req.url == "/favicon.ico") {
        return;
    }

    //url.parse()可以将一个完整的URL地址，分为很多部分：
    //host、port、pathname、path、query
    var pathname = url.parse(req.url).pathname;
    //url.parse()如果第二个参数是true，那么就可以将所有的查询变为对象
    //就可以直接打点得到这个参数
    var query = url.parse(req.url, true).query;
    //直接打点得到这个参数

    var jsStruser = JSON.stringify( {name:"zhangsan",desc:"haha",sex:"false",age:"18" } );
    var notify = {
        "type": 3,
        "nickname": "梦梦[默131519804]",
        "avatar": "http://devimg.365yf.com/avatar/103878/fa36eeff9b68b6c533fe.jpg",
        "uid": "131519804",
        "created_at": 1511918046,
        "title": "新访客通知",
        "desc": "新访客通知",
        "expire_at": 1511918166,
        "notify_no": "visitor_1511918046",
        "receiver_uid": null,
        "sound": 1,
        "vibrate": 1,
        "light": 1,
        "total_unaccepted_num": 1,
        "id": 103878,
        "age": 21,
        "province": "上海",
        "distance": "10公里",
        "push_type": "transimission"
    };
    var jsStrnotify = JSON.stringify(notify);
    // var jsStr = JSON.stringify( {name:true,desc:19,sex:"false",age:"18" } );

    if (pathname.indexOf("user") >= 0) {
        console.log(jsStruser);
        res.writeHead(200, {"Content-Type": "text/plain;charset=UTF8"})
        res.write(jsStruser);
    }

    if (pathname.indexOf("notify") >= 0) {
        console.log(jsStrnotify);
        res.writeHead(200, {"Content-Type": "text/plain;charset=UTF8"})
        res.write(jsStrnotify);
    }
    res.end();
});

server.listen(3000, "192.168.39.124");
