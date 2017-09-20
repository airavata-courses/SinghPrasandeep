var express = require('express');
var router = express.Router();
var amqp = require('amqplib/callback_api');

/* GET greeting. */
router.get('/sayhello', function(req, res, next) {
	// console.log("Request contains :"+req)
	var query = require('url').parse(req.url,true).query;
	var msg_r = query.text;
	amqp.connect('amqp://149.165.156.204', function(err, conn) {
	conn.createChannel(function(err, ch) {
    		var q = 'hello';
    		//msg_r = 'Hello RabbitMQ World from Node!';
	    	ch.assertQueue(q, {durable: false});
    		// Note: on Node 6 Buffer.from(msg) should be used
   			ch.sendToQueue(q, new Buffer(msg_r));
    		console.log(" [x] Sent %s", msg_r);
			res.json({msg : "Message Sent!  ------------->"+msg_r});
		//return msg_r;
  		});
	});
});


/* GET greeting. */
router.get('/receive', function(req, res, next) {
	// console.log("Request contains :"+req)
	//var query = require('url').parse(req.url,true).query;
	var msg_q = "";
	var amqp = require('amqplib/callback_api');

	amqp.connect('amqp://149.165.156.204', function(err, conn) {
  			conn.createChannel(function(err, ch) {
  				var q = 'hello';
			   	//ch.assertQueue(q, {durable: true});
    			console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", q);
   				ch.consume(q, function(msg) {
      				console.log(" [x] Received %s", msg.content.toString());
      				msg_q += msg.content.toString();
      				console.log("Printing msg_q -----------------"+msg_q);	
      				res.json({msg : "Message Received!  ------------->"+msg_q});
      				setTimeout(function() { conn.close()}, 500);
    			}, {noAck: true});
    			console.log("Printing msg_q outside-----------------"+msg_q);
    			
  			});
	});
});


module.exports = router;
