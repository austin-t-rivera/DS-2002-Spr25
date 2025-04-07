#!/bin/bash

while IFS= read -r line; do
  value=$(echo "$line" | cut -d',' -f2)
  result=$((value * 2))
  echo "$line,$result"
done