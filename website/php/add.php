<?php

$new_term = $_GET["new_term"];

exec('python ../project/web_test.py', $output,$return_val);

echo json_encode($output);

?>