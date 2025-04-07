#!/bin/bash

while IFS=',' read -r col1 col2 col3; do  # Assuming 3 columns
  echo "Col1: $col1, Col2: $col2, Col3: $col3"
done < data.csv