var buf = new Buffer(26);

for(var i = 0;i<26;i++){
	buf[i] = i+97
}

console.log(buf.toString(undefined,0,5));
console.log(buf.toString("utf8",0,5));



var buf = new Buffer('www.runoob.com');
var json = buf.toJSON();//字符串buffer才可以调用  toJSON()

console.log(json);