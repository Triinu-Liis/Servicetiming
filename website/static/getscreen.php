<?php
$mysqli = new mysqli("servername", "username", "password", "dbname");
if($mysqli->connect_error) {
  exit('Could not connect');
}

$sql = "SELECT user_id, driver, co_driver, service_IN, service_OUT, service_time, margin_time
FROM screens WHERE user_id = ?";

$stmt = $mysqli->prepare($sql);
$stmt->bind_param("s", $_GET['q']);
$stmt->execute();
$stmt->store_result();
$stmt->bind_result($id, $dname, $cname, $in, $out, $stime, $mtime);
$stmt->fetch();
$stmt->close();

echo "<table>";
echo "<tr>";
echo "<th>UserId</th>";
echo "<td>" . $id . "</td>";
echo "<th>Driver</th>";
echo "<td>" . $dname . "</td>";
echo "<th>Co-driver</th>";
echo "<td>" . $cname . "</td>";
echo "<th>ServiceIN</th>";
echo "<td>" . $in . "</td>";
echo "<th>ServiceOUT</th>";
echo "<td>" . $out . "</td>";
echo "<th>ServiceTime</th>";
echo "<td>" . $stime . "</td>";
echo "<th>MarginTime</th>";
echo "<td>" . $mtime . "</td>";
echo "</tr>";
echo "</table>";
?>