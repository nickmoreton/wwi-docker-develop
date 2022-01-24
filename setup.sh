#!/bin/bash

set -e

# Set up the environment variables
## Set the path to the directory where the package is located
WWIPACKAGE_PATH=wagtail-wordpress-import

## Copy the environment variables to .env and append the IP address of the host machine
cp env.example .env
echo "" >> .env
echo HOST_IP=$(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | head -1 | awk '{ print $2 }') >> .env

if [ ! -d "wagtail-wordpress-import" ]; then
    git clone https://github.com/torchbox/wagtail-wordpress-import.git
else
    echo "Using existing wagtai-wordpress-import."
fi

fab build
fab start
fab run-tests
fab init
fab run-import

# NOTES
# all
# ```bash
# ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'
# ```

# first
# ```bash
# ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | head -1 | awk '{ print $2 }'
# ```