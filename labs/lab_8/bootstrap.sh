#!/bin/bash

yum update -y

yum install -y git python 3 python3-pip

command -v pip3 || ln -s /usr/bin/pip3 /usr/bin/pip

python 3 -m pip install --upgrade pip
python 3 -m pip install boto3 pandas requests 


