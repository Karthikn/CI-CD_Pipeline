#!/bin/bash

# Run the Python script to check for changes
python3 /var/www/html/CI-CD_Pipeline/GitHub_CI.py

# If changes are detected, update the website
if [ $? -eq 0 ]; then
    /var/www/html/CI-CD_Pipeline/Website.sh
fi
