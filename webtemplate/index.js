function next30() {
	
	$.post("index.php",
	
	  function(result)
	  {
		alert(result);
	  });
   
}

function customPrediction(){
	
	var data = document.getElementById("data").value;
	var alogrithm = document.getElementById("alogrithm").value;

	$.post("index.php",
	{
	data: data
	alogrithm: alogrithm
	},

	function(result)
	{
	alert(result);
	});
}

