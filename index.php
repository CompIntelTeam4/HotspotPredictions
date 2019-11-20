
<?php 

    
    //Executing python file in php
    echo "h <br>";
    #$python = shell_exec('"C:\Users\Lucian Murdock\AppData\Local\Programs\Python\Python37\python.exe" test.py 2>&1');
    $python = shell_exec('"D:\Python34\python.exe" test.py 2>&1');
    $python_result = json_decode($python);
    foreach ($python_result as $item) {
        echo $item."<BR>";
    }
    echo "<br> end"
    

    /*
    $string = file_get_contents("shortGeo.json");
    $string_decode = json_decode($string,true);
    //echo $string;
    echo $string_decode['data']['features'][0]['geometry']['type'];

    */

?>