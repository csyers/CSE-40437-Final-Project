<?php

$new_term = $_GET["new_term"];

exec('python ../../scripts/web_test.py '.$new_term, $output,$return_val);

echo json_encode($output);

?>