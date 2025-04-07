#!/usr/bin/env python3

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

sum_nums = num1 + num2

print(f"The sum is: {sum_nums}") # Standard output
with open("sum.txt", "w") as f: # Redirecting to file
    f.write(f"The sum is: {sum_nums}\n")