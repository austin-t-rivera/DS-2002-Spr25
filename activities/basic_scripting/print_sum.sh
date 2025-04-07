#!/bin/bash

num1=$1
num2=$2

sum=$((num1 + num2))

echo "The sum is: $sum"  # Standard output
echo "The sum is: $sum" > sum.txt # Redirecting to file