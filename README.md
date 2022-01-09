# Develop Wagtail Wordpress Import

## Set Up

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/nickmoreton/wwi-docker-develop)

Gitpod has everything installed that you need to get started.

## Local Development

Initial setup uses [Fabric](https://www.fabfile.org/) and [python-dotenv](https://saurabh-kumar.com/python-dotenv/) which you will need to have installed on your local machine.

[Docker](https://www.docker.com/) is also required to run the example wordpress site and needs to be started.

Run the following commands to install the required packages. Local development only.

```bash
# clone this repo
git clone https://github.com/nickmoreton/wwi-docker-develop

# change to the wwi-docker-develop directory
cd wwi-docker-develop
```

## Start Development

Run this commend to setup the package for development. This will clone the latest version of the Wagtail WordPress Import repository and set some environment variables.

```bash
./setup.sh
```

### Use docker for development

Start the containers

```bash
fab build
fab up
```

Initialise wordpress and export and xml file

```bash
fab init
```

### WordPress Fabric Commands

Use to manage the WordPress docker containers.

```bash
# list the available fabric commands
fab -l
```

Open a shell in the Wagtail container

```bash
fab sh
```

Commands

```bash
# initial setup
fab up                Start the WordPress environment (run this first)
fab init              Install WordPress and import the XML theme fixures with media files (run this second)

# access the Wagtail conteint
fab sh                Open a shell in the Wagtail container

# container management
fab wpexport          Export the WordPress data to and XML file
fab destroy         Destroy the WordPress environment containers and volumes (database will lost!)

# fab wppull            Build the WordPress environment (you can call this first but its not necessary)
# fab wprestart         Restart the WordPress environment
# fab wpstop            Stop the WordPress environment

# wordpress API commands
fab wppermalinks      Change the permalink structure to /%postname%/
fab wptheme           Install a WordPress theme and switch to it
fab wptheme-delete    Un-install a WordPress theme by name
fab wptheme-install   Install a WordPress theme by name
```

### Initialise the Wordpress container with dummy data

The commands above provide a simple way to spin up a wordpress site and download the official theme test xml file and have it installed into the wordpress site. You can also use this to  generate an XML file for you to use as the import source XML for development.

#### (Useful to know)

It can take a while for the WordPress site to be available at <http://localhost:8080> Once running you should see the WordPress site populated with dummy blog posts and pages all with images and text content.

Using the fab commands you can swap out the WordPress theme and install a new one and export the XML data to a file. When you use that data file as the import source for your development the images and documents will be available locally via the runnning WordPress site. This is useful for develpment and testing the importer without having to download media etc. from a remote site.

You can login to the WordPress site at <http://localhost:8080/wp-admin> using the preset username/password of `wwi/7SKFj8Di`. If you want to change these login details update the `fabfile.py` CONSTANTS

You can work with the WordPress site files: un-comment the lines indicated in the `docker/docker-compose-wordpress.yml` file. In theory you could add your own WordPress site files to the `./wordpress` directory so you can work with your own data and media files.

### Export the WordPress xml data

Run `fab wpexport`. An XML file will be saved to the XML folder `export.xml`. You can use this as your Wagtail WordPress Import data source and the import process will have a local domain available for downloading the media files.


all
```bash
ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'
```

first
```bash
ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | head -1 | awk '{ print $2 }'
```