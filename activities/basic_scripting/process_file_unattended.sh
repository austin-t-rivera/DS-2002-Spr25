#!/bin/bash

while IFS= read -r line; do
  value=$(echo "$line" | cut -d',' -f2) # Extracting the second field (example)
  if [[ "$value" -gt 10 ]]; then # Example logic
    echo "$line"
  fi
done