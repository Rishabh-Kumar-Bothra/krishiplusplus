var express = require('express');
var app = express();

app.use(express.static('public'));	

app.get('/', function(req, res){
	res.sendFile( __dirname + "/" + "index.html" );
})

app.get('/query', function (req, res) {
   // Prepare output in JSON format
   response = {
      shnumber:req.query.shnumber,
      pincode:req.query.pincode
   };
   console.log(response);
   res.end(JSON.stringify(response.pincode));
})

var server = app.listen(8080, function(){
	var host = server.address().address
   var port = server.address().port
	console.log("Example express app at http://%s:%s", host, port);
})
