<?php 

$command = escapeshellcmd('python3 testing.py');
$output = shell_exec($command);
echo $output;

?>