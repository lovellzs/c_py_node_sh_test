var MongoClient = require('mongodb').MongoClient;
var express = require('express');

var router = express.Router();
var DB_CONN_STR = 'mongodb://localhost:27017/test'; //# 数据库为 test

var insertData = function(db, callback) {
    //连接到表 site
    var collection = db.collection('user');
    //插入数据
    var data = [{"name":"张三","url":"www.sz.com"},{"name":"张三","url":"www.sz.com"}];
    collection.insert(data, function(err, result) {
        if(err)
        {
            console.log('Error:'+ err);
            return;
        }
        callback(result);
    });
}

var selectData = function(db, callback) {
    //连接到表
    var collection = db.collection('user');
    //查询数据
    var whereStr = {"name":'张三'};
    collection.find(whereStr).toArray(function(err, result) {
        if(err)
        {
            console.log('Error:'+ err);
            return;
        }
        callback(result);
    });
}


/* GET users listing. */
router.get('/', function(req, res, next) {

    MongoClient.connect(DB_CONN_STR, function(err, db) {
        console.log("连接成功!");
        insertData(db, function(result) {
            console.log(result);
            db.close();
        });
    });
    res.send('========================');
});



/*     插入数据    */
router.get('/add', function(req, res, next) {

    MongoClient.connect(DB_CONN_STR, function(err, db) {
        console.log("连接成功!");
        insertData(db, function(result) {
            console.log(result);
            db.close();
            res.send('=============result===========' + result) ;
        });
    });
    // res.send('============add============');
});

/* 查询 */
router.get('/find', function(req, res, next) {

    MongoClient.connect(DB_CONN_STR, function(err, db) {
        console.log("连接成功!");
        selectData(db, function(result) {
            console.log(result);

            db.close();
            res.send('=============result===========' + JSON.stringify( result )) ;
        });
    });
    // res.send('============find============');
});


module.exports = router;