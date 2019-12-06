


<?php



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
echo "Connection Successful <br>";


$sql = "SELECT * FROM incidents WHERE incident_occured >= '2018-11-27'";
$result = $connection->query($sql);

if ($result->num_rows > 0) {
    //echo count($result) . "<br>";
    echo "Got some results <br>";
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row['primary_key'] . "<br>";
    }
} else {
    "0 results";
}




?>
