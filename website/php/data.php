<?php

$file = $_GET["product"];

exec('python ../../results/compile.py ../../results/'.$file.' sentiment', $output, $return_val);

print json_encode($output);

?>