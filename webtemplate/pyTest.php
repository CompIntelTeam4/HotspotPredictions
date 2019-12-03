<?php 




//Executing python file in php

echo "h <br>";
$python = shell_exec('"C:\Users\Lucian Murdock\AppData\Local\Programs\Python\Python37\python.exe" testing.py 2>&1');
$python_result = json_decode($python);
foreach ($python_result as $item) {
    echo $item."<BR>";
}
echo "<br> end"

////////////////////////////////////////////////////


?>