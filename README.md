# Develop Wagtail Wordpress Import

This is a development setup for the Wagtail Wordpress Import plugin. [Wagtail Wordpress Import](https://github.com/torchbox/wagtail-wordpress-import) is a package for Wagtail CMS to import WordPress blog content from an XML file.

## Requirements

- [Docker](https://www.docker.com/products/docker-desktop)
- A few python packages in requirements-dev.txt for local commands `pip install -r requirements-dev.txt`

## Installation

Run the following commands to install the developer setup.

```bash
# clone this repo
git clone https://github.com/nickmoreton/wwi-docker-develop

# change to the wwi-docker-develop directory
cd wwi-docker-develop

# install everything and run a test import
./setup.sh
```

Once you have followed the above steps, you will be able to access the

- Wagtail admin interface at <http://localhost:8000/admin>
- WordPress admin interface at  <http://localhost:8080/wp-admin>

### Fabric Commands

To manage the docker containers.

#### List the available fabric commands

```bash
fab -l
```

All Commands

General

- `build`           Build the wagtail docker container
- `destroy`         Destroy the docker containers. THIS WILL ALSO REMOVE - THE DATABASES
- `init`            Install WordPress CLI and import the XML theme - fixures with media files (run this second)
- `start`           Start the docker containers
- `startbuild`      Build & Start the docker containers
- `stop`            Stop the docker containers

Wordpress

- `permalinks`      Change the WordPress permalink structure to /%postname%/
- `run-import`      Run the import to Wagtail
- `theme`           Install a WordPress theme and switch to it
- `theme-delete`    Un-install a WordPress theme by name
- `theme-install`   Install a WordPress theme by name
- `wpexport`        Export the WordPress data to an XML file
- `wprestart`       Restart the WordPress container
- `wpstart`         Start the WordPress container
- `wpstop`          Stop the WordPress container

Wagtail Wordpress Import / Django

- `sh`                  Open a bash shell in the docker development container
- `run-import`          Run the import to Wagtail
- `run-tests`           Run the tests for the Wagtail WordPress Impoter
- `run-delete`          Delete all the imported pages. Optionally delete the images and documents
- `run-del-documents`   Delete all the imported documents
- `run-del-images`      Delete all the imported images

After and initial setup running `./setup.sh` the follwoing fab commands are the most useful.

- start
- run-tests
- run-import (this will import the XML data again and only update existing pages)
- run-delete (run with the args `--images` and/or `--documents`)
- run-del-documents
- run-del-images

## Useful to know

It can take a while for the WordPress site to be available at <http://localhost:8080> Once running you should see the WordPress site populated with dummy blog posts and pages all with images and text content.

Using the fab commands you can swap out the WordPress theme and install a new one and export the XML data to a file. When you use that data file as the import source for your development the images and documents will be available locally via the runnning WordPress site. This is useful for develpment and testing the importer without having to download media etc. from a remote site.

You can login to the WordPress site at <http://localhost:8080/wp-admin> using the preset username/password of `admin/password`. If you want to change these login details look at the `env.example` file.

You can work with the WordPress site files: un-comment the lines indicated in the `docker/docker-compose-wordpress.yml` file. In theory, but not tested, you could add your own WordPress site files to the `./wordpress` directory so you can work with your own data and media files.

### Export the WordPress xml data

Although this is done during setup you can run it again.

Run `fab wpexport`. An XML file named `export.xml` will be saved to the XML folder.
