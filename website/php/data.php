<?php

$file = $_GET["product"].'.csv';

exec('python ../../results/compile.py '.$file, $output, $return_val);

echo $output;

?>