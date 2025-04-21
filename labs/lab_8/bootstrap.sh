#!/bin/bash

yum update -y

yum install -y git python 3

python 3 -m pip install -upgrade pip
python 3 -m pip install boto3 pandas requests 


