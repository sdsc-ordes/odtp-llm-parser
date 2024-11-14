#!/bin/bash

# Navigate to the directory containing the tests
cd "$(dirname "$0")"

# Find all test files and run them
for test_file in $(find . -name 'test_*.sh'); do
    echo "Running $test_file"
    bash "$test_file"
done