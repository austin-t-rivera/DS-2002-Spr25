#!/bin/bash

while IFS= read -r line; do
  echo "$line" | tr '[:upper:]' '[:lower:]' # Example: convert to lowercase
done