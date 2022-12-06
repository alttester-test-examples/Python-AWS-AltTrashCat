#!/bin/bash

# Print how script is used and exit
function print_help_and_die() {
    echo "Usage: $0 <ios|android>"
    exit 0
}

if [[ "$#" -eq 1 ]]; then
    ENV="$1"
else
    print_help_and_die
fi

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

TEST_FILE="test-package_${ENV}.zip"

rm ${TEST_FILE}

echo "Creating test file for environment: ${ENV}"
zip -r a "${TEST_FILE}" tests/ requirements.txt 
echo "
You should now upload test file '${TEST_FILE}' to AWS Cloud"