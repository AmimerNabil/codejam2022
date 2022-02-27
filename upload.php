<?php
// $target_Path = "uploads/";
$target_Path = $target_Path.basename( $_FILES['myFile']['name'] );
move_uploaded_file( $_FILES['myFile']['tmp_name'], $target_Path );

?>