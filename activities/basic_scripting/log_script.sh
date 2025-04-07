#!/bin/bash

log_file="my_script.log"

log_message() {
  timestamp=$(date +"%Y-%m-%d %H:%M:%S")
  echo "[$timestamp] $1" >> "$log_file"
}

log_message "Script started."

# My logic
log_message "Sleeping for 5 seconds..."  # Log the sleep action
sleep 5  # Pause for 5 seconds

log_message "Resuming after sleep." # Log after the sleep

log_message "Data processing complete."