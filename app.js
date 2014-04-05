
var express = require('express');
var app = express();
//var connect = require('connect');

    console.log("Servidor iniciado com sucesso!!!");

app.configure(function(){
    app.set('views', __dirname + '/views');
    app.set('view engine', 'jade');
    app.set('view options', {pretty: false, layout: false});
    app.use(express.static(__dirname + '/static'));
    app.use(express.urlencoded());
    app.use(express.json());
    app.use(express.methodOverride());
});


app.get('/', function(req, res){
    res.render('index', {title: "Home"});
});

app.get('/projetos', function(req, res){
   res.render('projetos', {title: "Projetos"});
});

app.get('/about', function(req, res){
    res.render('about', {title: "Sobre"});
});

app.get('/contato', function(req, res){
    res.render('contato', {title: "Contato"});
});

app.get('/blog', function(req, res){
    res.render('blog', {title: "Blog"});
});

app.listen(3000);
