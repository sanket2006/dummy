console.log("hello buddy....")
var http=require(http)
createserver(function (req,res) {
	// body...
	res.end("we are on serveer nbro..")
}).listen(8080)