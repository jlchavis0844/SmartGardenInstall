<?php
header('Content-Type: json');
// SQL server declerations
$host = "76.94.123.147";//server IP
$port = 4910;//mySQL port
$socket = "";//not used
$user = "491user";//server username
$password = "password1";//server password
$dbname = "gardens";//removes need to have database.tableName

$data = file_get_contents('php://input');
$data = json_decode($data, true);
//var_dump($data);

$user = $data['user'];
$password = $data['password'];
$gardens = $data['Gardens'];

$sensors = array();
$gardenNames = array();
foreach $gardens as $gName => $tName{//rewrite logic goal sensors per garden
	array_push($gardens,$gName['TempNames']);
	array_push($gardens,$gName['MoistName']);
	array_push($gardenNames,$gName);
}

echo count($gardens);
var_dump($gardens);
//echo json_encode($data);


?>