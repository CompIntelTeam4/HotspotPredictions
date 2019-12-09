function next30() {
	
	$.post("index.php",
	
	  function(result)
	  {
		alert(result);
	  });
   
}

function customPrediction(){
	
	var data = document.getElementById("data").value;
	var algorithm = document.getElementById("algorithm").value;

	$.post("index.php",
	{
	data: data
	algorithm: algorithm
	},

	function(result)
	{
	alert(result);
	});
}

