#!/bin/bash

set -e

# Copy the environment variables to .env and append the IP address of the
# Wordpress and Wagtail running containers

if [ ! -f ".env" ]
then
    cp env.example .env
    echo WAGTAIL_WORDPRESS_IMPORTER_SOURCE_DOMAIN=http://$(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | head -1 | awk '{ print $2 }'):8080>>.env
    echo BASE_URL=http://$(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | head -1 | awk '{ print $2 }'):8000>>.env
fi

if [ ! -d "wagtail-wordpress-import" ]
then
    git clone https://github.com/torchbox/wagtail-wordpress-import
    git checkout develop
else
    echo "Using existing wagtai-wordpress-import."
fi

fab build
fab start
fab run-tests
fab init
fab run-import
