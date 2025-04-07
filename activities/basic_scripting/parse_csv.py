#!/usr/bin/env python3
import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      try:
        col1, col2, col3 = row #unpacking the list
        print(f"Col1: {col1}, Col2: {col2}, Col3: {col3}")
      except ValueError:
        print(f"Skipping row due to error: {row}")