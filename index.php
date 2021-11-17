<?php
//                        $servername="192.168.1.50";
  //                      $username="luft";
    //                    $password="luft1";
//			$database="hotel";

                        $conn = mysqli_connect("192.168.1.50", "luft","luft1", "hotel");

                        if (!$conn) {
                        die("Connection failed: " . mysqli_connect_error());
                        }
                        echo "Connected successfully";
?>
<!DOCTYPE html>
<html lang= "de">
	<head>
		<meta charset = "utf-8" />
		<meta name = "author" content = "Janin Hanisch & Lukas Beppler" />
		<meta name = "date" content = "November 2021" />
		<meta http-equiv="refresh" content="5">
		<title>Dashboard Netzlabor 1</title>
	</head>
	<body>
		<h1>Dashboard Netzlabor 1</h1>
	<h2>Uhrzeit</h2>
		<?php
			$Uhrzeit = date("H:i",$timestamp);
			echo $Uhrzeit;
		?>
	<h2>Temperatur</h2>
		<?php
			$sqlselect = "SELECT temperatur FROM LUFTQUALITAET ORDER BY Messwert DESC LIMIT 1";
			$result = mysqli_query($conn, $sqlselect);
		?>
		<p>$result</p> 
	<h2>Luftfeuchtigkeit</h2>
		<?php
                        $sqlselect = "SELECT Luftfeuchte FROM LUFTQUALITAET ORDER BY Messwert DESC LIMIT 1";
                        $result = mysqli_query($conn, $sqlselect);
                ?>
		<p>$result</p>
	<h2>Anzahl Personen im Raum</h2>
		<?php
		        $sqlselect = "SELECT COUNT(LOG_IN) FROM KONTAKT";
			$sqlselect2 = "SELECT COUNT(LOG_OUT) FROM KONTAKT WHERE LOG_OUT is not null";
                        $result = mysqli_query($conn, $sqlselect);
			$result2 = mysqli_query($conn, $sqlselect2);
			$result3 = $result-$result2
                ?>
                <p>$result3</p>

	</body>
</html>

<?php
	mysqli_close($conn);
?>

