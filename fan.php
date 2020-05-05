<html>
<head>
<meta http-equiv="refresh" content="1">
</head>
<body>
<title>Project</title>
<style type="text/css">
h1{
	padding-left: 300px;
}
form{
	padding-left: 550px;
}
#on{
	position: absolute;
	top: 100px;
	width: 70px;
	height: 50px;
}
#off{
	position: absolute;
	top: 200px;
	width: 70px;
	height: 50px;
}

</style>
<h1> Home Automation By Priyanka Saini </h1>
<?php
$file = "temp_file.txt";
$handle = fopen($file,'r');
$contents = fread($handle,filesize($file));
fclose($handle);
?>
<div>
	<br>
	<br>
	<br>
	<br>
	<label><font size="4">The current temperature of the system is </font></label>
	<label><font size="30">	<?php echo $contents; ?></font></label>
</div>

<form action = "index.php" method = "POST">
<input type = "submit" name ="on" id="on" value = "Turn On">
<input type = "submit" name ="off" id="off" value = "Turn Off">
</form>
</body>
</html>
