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
        ],
        "where": {
            "shnumber": {
                "$eq": ""
            }
        }
    }
};

app.engine('mustache', mustacheExpress());
app.set('view engine', 'mustache');
app.set('views', __dirname + '/views');

app.use(express.static('public'));	

app.get('/query', function (req, res) {

    var response = {
        shnumber:req.query.shnumber,
        pincode:req.query.pincode
    };

    body.args.where.shnumber.$eq = response.shnumber;

    requestOptions.body = JSON.stringify(body);

    fetchAction(url, requestOptions)
        .then(function(response) {
        return response.json();
    })
    .then(function(result) {
        if (result.length <= 0) {
            res.sendFile( __dirname + "/" + "error.html" );
        } else {
            
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
                state: result[0].state,
                yield: result[0].yield,
                flood: result[0].flood,
                cyclone: result[0].cyclone,
                userimage: result[0].userimage
            });
        }
       
    })
    .catch(function(error) {
        console.log('Request Failed:' + error);
    });


})

var server = app.listen(8080, function(){
    //var host = server.address().address
    var port = server.address().port;
    console.log("Example express app at port: %s", port);
})
