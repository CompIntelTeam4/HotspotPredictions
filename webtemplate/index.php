<?php 
/*
$command = escapeshellcmd('python3 testing.py');
$output = shell_exec($command);
echo $output;


*/
//Executing python file in php



    //echo "h <br>";
    #$python = shell_exec('"C:\Users\timot\AppData\Local\Programs\Python\Python38-32\python.exe" testing.py 2>&1');
    $python = shell_exec('"C:\Users\timot\AppData\Local\Programs\Python\Python37\python.exe" 
                                  testing.py 2>&1');
    $python_result = json_decode($python);
	echo $python;
    foreach ($python_result as $item) {
        echo $item."<BR>";
    }
    echo "<br> end"

///////////////////////////////////////////////////
/*

if(isset($_REQUEST['data']))
	{
	if(isset($_REQUEST['algorithm']))
	  {
		echo "I got it! " . $_REQUEST['data'] . " " . $_REQUEST['algorithm'];
	  }
	}

*/

?>