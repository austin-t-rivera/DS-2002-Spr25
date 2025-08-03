#!/bin/bash

# Update and upgrade system packages
apt update -y
apt upgrade -y

# Install Python3
apt install -y python3

# Install git
apt install -y git

# Install jq (lightweight JSON processor)
apt install -y jq
