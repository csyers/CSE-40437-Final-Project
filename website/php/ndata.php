<?php

$new_term = $_GET["new_term"];

//exec('cd ../../scripts', $output, $return_val)

exec('../../scripts/full_stack_old.sh '.$new_term.' 2017-04-27 2017-05-01', $output,$return_val);

//echo json_encode($return_val);

echo '../../scripts/full_stack_old.sh '.$new_term.' 2017-04-27 2017-05-01'

?>
