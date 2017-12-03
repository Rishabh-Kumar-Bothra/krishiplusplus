var express = require('express');
var app = express();
var fetchAction =  require('node-fetch');

var url = "https://data.combatant32.hasura-app.io/v1/query";

app.use(express.static('public'));	

app.get('/', function(req, res){
	res.sendFile( __dirname + "/" + "index.html" );
})

ar requestOptions = {
    "method": "POST",
    "headers": {
        "Content-Type": "application/json"
    }
};

var body = {
    "type": "select",
    "args": {
        "table": "krishiplusplus",
        "columns": [
            "shnumber"
        ]
    }
};

app.get('/query', function (req, res) {
   // Prepare output in JSON format
   response = {
      shnumber:req.query.shnumber,
      pincode:req.query.pincode
   };
   res.sendFile( __dirname + "/" + "index1.html" );
   console.log(response);
   res.end(JSON.stringify(response.pincode));
	
   requestOptions.body = JSON.stringify(body);

fetchAction(url, requestOptions)
.then(function(response) {
	return response.json();
})
.then(function(result) {
	console.log(first);
})
.catch(function(error) {
	console.log('Request Failed:' + error);
});

})

var server = app.listen(8080, function(){
	var host = server.address().address
   var port = server.address().port
	console.log("Example express app at http://%s:%s", host, port);
})
