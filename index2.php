<?php


//Azure database credentials
$servername = "crimewebsitedatabase.mysql.database.azure.com";
$username = "lmurdock12";
$password = "TheCloudtest2019";
$myDB = "date_test";
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



$row = 1;
if (($handle = fopen("assault_crime_data_2016_wGrid.csv", "r")) !== FALSE) {
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
        
        
        $sql = "INSERT INTO `date` (`incident_occured`) VALUES ('$dateFormatted');";

        if ($connection->query($sql) === TRUE) {
            echo "Record created successfully<br>";
        } else {
            echo "Error: " . $sql . "<br>" . $connection->error;
        }


        //echo $month . " + " . $day . " + " . $year . "<br>";



    }
    fclose($handle);
}
?>