#!/bin/bash

run_tests() {
    for ((i=0; i<=100000; i++))
    do
        output_file="test_results_$i.txt"
        echo "Running test $i"
        gcc -o main test_MRG.c MRG32k3a.c -ltestu01 && ./main > "$output_file"
    done
}

run_tests
