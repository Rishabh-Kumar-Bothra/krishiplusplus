var express = require('express');
var fetchAction =  require('node-fetch');
var mustacheExpress = require('mustache-express');

var app = express();

var url = "https://data.combatant32.hasura-app.io/v1/query";
var requestOptions = {
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
            "*"
        ]
    }
};

app.engine('mustache', mustacheExpress());
app.set('view engine', 'mustache');
app.set('views', __dirname + '/views');

app.use(express.static('public'));	

/*app.get('/', function(req, res){
	res.sendFile( __dirname + "/" + "index.html" );
})*/

app.get('/query', function (req, res) {

    response = {
        shnumber:req.query.shnumber,
        pincode:req.query.pincode
    };
  
    requestOptions.body = JSON.stringify(body);

    fetchAction(url, requestOptions)
        .then(function(response) {
        return response.json();
    })
    .then(function(result) {
        var shnum = result[0].shnumber;
        
        if (shnum == response.shnumber) {
            res.render('index', {
                name: result[0].name,
                crop: result[0].crop,
                variety: result[0].variety,
                intercrop: result[0].intercrop,
                sowingPeriod: result[0].sowingPeriod,
                landprep: result[0].landprep,
                seedrate: result[0].seedrate,
                spacing: result[0].spacing,
                fertilizer: result[0].fertilizer,
                yield: result[0].yield
            });
        }

    })
    .catch(function(error) {
        console.log('Request Failed:' + error);
    });


})

var server = app.listen(8081, function(){
    //var host = server.address().address
    var port = server.address().port;
    console.log("Example express app at port: %s", port);
})
