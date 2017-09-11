var express = require('express');
var router = express.Router();
var amqp = require('amqplib/callback_api');

/* GET greeting. */
router.get('/sayhello', function(req, res, next) {
	// console.log("Request contains :"+req)
	var query = require('url').parse(req.url,true).query;
	var msg_r = "Message Sent!  ------------->"+query.text;
	amqp.connect('amqp://localhost', function(err, conn) {
	conn.createChannel(function(err, ch) {
    		var q = 'hello';
    		//msg_r = 'Hello RabbitMQ World from Node!';
	    	ch.assertQueue(q, {durable: false});
    		// Note: on Node 6 Buffer.from(msg) should be used
   			ch.sendToQueue(q, new Buffer(msg_r));
    		console.log(" [x] Sent %s", msg_r);
			res.json({msg : msg_r});
		//return msg_r;
  		});
	});
});

module.exports = router;
