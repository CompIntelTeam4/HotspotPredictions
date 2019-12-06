<?php

//$yesterday = date('Y-m-d', strtotime(' -1 day'));


$date = new DateTime();
$date->setTimeZone(new DateTimeZone("US/Central"));
$date->sub(new DateInterval('P1D'));
echo "Current time: " . $date->format('Y-m-d') . "<br>";

$tz = $date->getTimezone();
echo $tz->getName() . "<br>";


?>