#!/bin/bash

# wrapper for comparing check results with expected results (check_expected_output.txt)
# Usage: bash test.sh

cd ../src/compatibility && bash check.sh > ../../test/temp_test_check_output.txt
cd ../../test
DIFF=$(sdiff -s test_check_output.txt temp_test_check_output.txt)
EXITCODE=$?
if [ $EXITCODE != 0 ]
then
    echo 'Expected output: Output:'
    echo $DIFF
    echo 'Failure. Compatibility check output not as expected.'
    exit 1
else
    echo 'Compatibility check output as expected.'
fi
rm temp_test_check_output.txt