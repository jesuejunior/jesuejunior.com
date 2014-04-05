
var express = require('express');
var app = express();

    console.log("Servidor iniciado com sucesso!!!");

app.configure(function(){
    app.set('views', __dirname + '/views');
    app.set('view engine', 'jade');
    app.set('view options', {pretty: false, layout: false});
    app.use(express.static(__dirname + '/static'));
    app.use(express.bodyParser());
    app.use(express.methodOverride());
});


app.get('/', function(req, res){
    res.render('index');
});

app.get('/projetos', function(req, res){
   res.render('projetos');
});

app.listen(3000);
