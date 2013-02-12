
$(window).load(function(){

var template = _.template($('#icones').html());

$('#bar-icones').html(template());
});
