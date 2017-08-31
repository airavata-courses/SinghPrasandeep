var express = require('express');
var router = express.Router();

/* GET greeting. */
router.get('/sayhello', function(req, res, next) {
  res.json({msg: 'Hello Docker from Express Node!'});
});

module.exports = router;
