#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        value = int(line.strip().split(',')[1]) # Extracting the second field (example)
        if value > 10: # Example logic
            print(line.strip())
    except (ValueError, IndexError):
        print(f"Skipping line due to error: {line.strip()}")  # Handle potential errors