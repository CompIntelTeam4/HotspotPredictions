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
$ssl_ca = 'D:\\\\home\\ssl\\BaltimoreCyberTrustRoot.crt.pem"';
mysqli_ssl_set($connection,null,null,$ssl_ca,null,null);

//Make the actual connection
if(!mysqli_real_connect($connection,$servername,$username,$password,$myDB)) {
    //Stop and report error if connection uncesseful 
    die("Connect error: " . mysqli_connect_error());
}
echo "Connection Successful";


$date = new DateTime();
$date->setTimeZone(new DateTimeZone("US/Central"));
$date->sub(new DateInterval('P1D'));
echo "Current time: " . $date->format('Y-m-d') . "<br>";
$yesterday = $date->format('Y-m-d');
//$tz = $date->getTimezone();
//echo $tz->getName() . "<br>";


$file_name = "D:\\\\home\\site\\wwwroot\\Data\\Crime_data\\tempData\\crime_wGrid_" . $yesterday . ".csv";
echo $file_name;

/*
$incident_num = '8_11';
$lat = 36.2;
$long = -86.0;
$grid = 3500;

echo $incident_num . ", Lat: " . $lat . ", Long: " . $long . ", grid #: " . $grid . "<br>";
//parse the date into an array by / to get the values out
//Proper Format YYYY-MM-DD HH:MM-SS
$dateFormatted = '2100' . "-" . '11' . "-" . '14' . " " . '00:00' . ":00";
$sql = "INSERT INTO `incidents` (`primary_key`,`incident_occured`,`latitude`,`longitude`,`grid` ) VALUES ('$incident_num','$dateFormatted','$lat','$long','$grid');";
if ($connection->query($sql) === TRUE) {
    echo "Record created successfully<br>";
} else {
    echo "Error: " . $sql . "<br>" . $connection->error;
}
*/




$row = 0;
if (($handle = fopen($file_name, "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {

        //Skip over the header row
        if ($row == 0) {
            $row++;
            continue;
        }

        //Print the number of columns of data for each row
        //$num = count($data);
        echo "On row: " . $row . ", ";
        $row++;


        //These indicies are different then working with a csv downloaded straight from data.nashville
        //When using the API the columns are arranged differently and the incident_occured is already 
        //put into SQL datetime format
        //primary_incident_num (0), incident_occured(7), offense_nibrs(13), latitude (25), longitude (26), grid (31)
        $incident_num = $data[0];
        $lat = $data[25];
        $long = $data[26];
        $grid = $data[31];
        $date = $data[7];


        //Need to add offense nibrs to sql statement
        echo $incident_num . ", Date: " . $date . ", Lat: " . $lat . ", Long: " . $long . ", grid #: " . $grid . "<br>";
    
        
        $sql = "INSERT INTO `incidents` (`primary_key`,`incident_occured`,`latitude`,`longitude`,`grid`,`offense_type` ) VALUES ('$incident_num','$date','$lat','$long','$grid','assault');";
        if ($connection->query($sql) === TRUE) {
            echo "Record created successfully<br>";
        } else {
            echo "Error: " . $sql . "<br>" . $connection->error;
        }
    }
    fclose($handle);
}
echo "Added: " . $row . "'s";
?>