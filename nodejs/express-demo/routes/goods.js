var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

/* GET users listing. */
router.get('/age', function(req, res, next) {
  res.send('我的年龄是18');
});

module.exports = router;
