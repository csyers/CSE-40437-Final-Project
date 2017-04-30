<?php

$file = $_GET["product"];

exec('python ../../results/compile.py '.$file, $output, $return_val);

echo $return_val;

?>