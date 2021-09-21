var flag = 0;
var start;
var millis;
setInterval(function(){
	var a = document.getElementsByClassName("zzgSd");
	if(a[0] != null)
	{
		var b = a[0].querySelector("span").getInnerHTML()
		if((b == 'typing…' || b == 'online') && flag == 0)
		{
			var d = new Date();
			var h = addZero(d.getHours());
			var m = addZero(d.getMinutes());
			// var s = addZero(d.getSeconds());
			console.log("started online from: " + h + ":" + m);
			start = Date.now();
			flag = 1;
		}
		else if((b == 'typing…' || b == 'online') && flag == 1)
		{
			console.log();
		}
		// else if(flag == 1)
		// {
		// 	millis = Date.now() - start;
		// 	console.log("online for: " + Math.floor(millis / 1000));
		// 	flag = 0;
		// }
	}
	else if(!(a[0]) && flag)
	{
		millis = Date.now() - start;
		console.log("online for: " + Math.floor(millis / 1000) + "seconds");
		flag = 0;
	}
}, 1000);

function addZero(i) {
	if (i < 10) {
	  i = "0" + i;
	}
	return i;
  }
  