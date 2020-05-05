<?php
$file = "saini.txt";
$handle = fopen($file,'w+');
if (isset($_POST['on']))
{
$onstring = "on";
fwrite($handle,$onstring);
fclose($handle);
header('Location: fan.html');
$var = 'on';
}
else if(isset($_POST['off']))
{
$offstring = "off";
fwrite($handle, $offstring);
fclose($handle);
header('Location: fan.html');
$var = 'off';
}


?>