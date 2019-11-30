<?php


//Azure database credentials
$servername = "crimewebsitedatabase.mysql.database.azure.com";
$username = "lmurdock12";
$password = "TheCloudtest2019";
$myDB = "crimes";
//Make connection instance
$connection = mysqli_init();
if(!$connection) {
    die("mysqli_init_failed");
}
//Esatablish SSL with the connection instance
$ssl_ca = 'C:\xampp\phpMyAdmin\ssl\BaltimoreCyberTrustRoot.crt.pem';
mysqli_ssl_set($connection,null,null,$ssl_ca,null,null);

//Make the actual connection
if(!mysqli_real_connect($connection,$servername,$username,$password,$myDB)) {
    //Stop and report error if connection uncesseful 
    die("Connect error: " . mysqli_connect_error());
}
echo "Connection Successful";


$files = array('assault_crime_data_2016_wGrid.csv','assault_crime_data_2017_wGrid.csv','assault_crime_data_2018_wGrid.csv','assault_crime_data_2019_wGrid.csv');

foreach ($files as $file) {
    echo $file . "<br>";


    #$file_path = "C:\\\\Users\\Lucian Murdock\\Desktop\\Computational_Intelligence\\Crime_prediction\\Data\\Crime_data\\tempData\\" . $file;
    $file_path = $file;
    //echo $file_path;



    $row = 1;
    if (($handle = fopen($file_path, "r")) !== FALSE) {
        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {

            //Skip over the header row
            if ($row == 1) {
                $row++;
                continue;
            }

            if($row%50==0) {
                echo "Processing file: " . $file . ", on row: " . $row . "<br>";
                //break;
            }

            //Print the number of columns of data for each row
            //$num = count($data);
            //echo "On row: " . $row . ", ";
            $row++;

            //Incident occured is stored in column 7 (using 0 as starting index)
            //echo $data[7] . "<br>";


            $incident_num = $data[0];
            //28 29 31
            $lat = $data[28];
            $long = $data[29];
            $grid = $data[31];

            $offense_num = $data[16];


            //echo $incident_num . ", Lat: " . $lat . ", Long: " . $long . ", grid #: " . $grid . ", offense #: ". $offense_num . "<br>";

            //parse the date into an array by / to get the values out
            $date = explode("/",$data[7]);

            //Get the month and day
            $month = $date[0];
            $day = $date[1];
            //Parse the date again to split up the year and time by " "
            $date = explode(" ",$date[2]);
            $year = $date[0];
            $time = $date[1];

            //Proper Format YYYY-MM-DD HH:MM-SS

            $dateFormatted = $year . "-" . $month . "-" . $day . " " . $time . ":00";
            //echo "Proper format: " . $dateFormatted . "<br>";
            
            $sql = "INSERT INTO `incidents` (`primary_key`,`incident_occured`,`latitude`,`longitude`,`grid`,`offense_type` ) VALUES ('$incident_num','$dateFormatted','$lat','$long','$grid','$offense_num');";

            if ($connection->query($sql) === TRUE) {
                
                if ($row%49 == 0) {
                    echo "Record created successfully<br>";
                }
                continue;
                
            } else {
                echo "Error: " . $sql . "<br>" . $connection->error;
            }

            //echo $month . " + " . $day . " + " . $year . "<br>";
            


        }
        fclose($handle);
        
    }
    





}




/*
$incident_num = '8_11';
$lat = 36.2;
$long = -86.0;
$grid = 3500;

echo $incident_num . ", Lat: " . $lat . ", Long: " . $long . ", grid #: " . $grid . "<br>";
//parse the date into an array by / to get the values out
//Proper Format YYYY-MM-DD HH:MM-SS
$dateFormatted = '2013' . "-" . '11' . "-" . '14' . " " . '00:00' . ":00";
$sql = "INSERT INTO `incidents` (`primary_key`,`incident_occured`,`latitude`,`longitude`,`grid` ) VALUES ('$incident_num','$dateFormatted','$lat','$long','$grid');";
if ($connection->query($sql) === TRUE) {
    echo "Record created successfully<br>";
} else {
    echo "Error: " . $sql . "<br>" . $connection->error;
}*/

/*
$row = 1;
if (($handle = fopen("assult_crime_data_2018_wGrid.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {

        //Skip over the header row
        if ($row == 1) {
            $row++;
            continue;
        }

        //Print the number of columns of data for each row
        //$num = count($data);
        echo "On row: " . $row . ", ";
        $row++;

        //Incident occured is stored in column 7 (using 0 as starting index)
        //echo $data[7] . "<br>";


        $incident_num = $data[0];
        //28 29 31
        $lat = $data[28];
        $long = $data[29];
        $grid = $data[31];




        //echo $incident_num . ", Lat: " . $lat . ", Long: " . $long . ", grid #: " . $grid . "<br>";

        //parse the date into an array by / to get the values out
        $date = explode("/",$data[7]);

        //Get the month and day
        $month = $date[0];
        $day = $date[1];
        //Parse the date again to split up the year and time by " "
        $date = explode(" ",$date[2]);
        $year = $date[0];
        $time = $date[1];

        //Proper Format YYYY-MM-DD HH:MM-SS

        $dateFormatted = $year . "-" . $month . "-" . $day . " " . $time . ":00";
        //echo "Proper format: " . $dateFormatted . "<br>";
        
        $sql = "INSERT INTO `incidents` (`primary_key`,`incident_occured`,`latitude`,`longitude`,`grid`,`offense_type` ) VALUES ('$incident_num','$dateFormatted','$lat','$long','$grid','assault');";

        if ($connection->query($sql) === TRUE) {
            echo "Record created successfully<br>";
        } else {
            echo "Error: " . $sql . "<br>" . $connection->error;
        }

        //echo $month . " + " . $day . " + " . $year . "<br>";



    }
    fclose($handle);
    
}
*/


?>