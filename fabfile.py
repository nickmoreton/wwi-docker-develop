import os
import secrets
import subprocess
from shlex import quote

from dotenv import load_dotenv
from invoke import run as local
from invoke.tasks import task
from rich import print

load_dotenv()


user = os.environ.get("ADMIN_USER")
password = os.environ.get("ADMIN_PASSWORD")
email = os.environ.get("ADMIN_EMAIL")
host_ip = os.environ.get("HOST_IP")

""" accept these values or set your own"""
WORDPRESS_USER = user
WORDPRESS_PASSWORD = password
WORDPRESS_ADMIN_EMAIL = email
WORDPRESS_HOST = host_ip + ":8080"

WAGTAIL_USER = user
WAGTAIL_PASSWORD = password
WAGTAIL_ADMIN_EMAIL = email
WAGTAIL_HOST = host_ip + ":8000"

""" COMMON TASKS """


@task
def build(ctx):
    """Build Wagtail docker container"""
    local("docker-compose build")


@task
def start(ctx):
    """
    Start the docker containers
    """
    load_dotenv(".env")
    url = os.environ.get("url")

    local("docker-compose up -d")

    wagtaildocker_exec("python example/manage.py migrate")
    wagtaildocker_exec(
        f"python example/manage.py init_wagtail {WAGTAIL_USER} {WAGTAIL_PASSWORD} {WAGTAIL_ADMIN_EMAIL}"
    )

    print("[bold green]WordPress is starting[/bold green]...")
    print(
        "[bold red]Wait a minute or two for the WordPress container to start before running any further commands...[/bold red]"
    )
    print("-------------------------------------------------------")
    print("[bold]WordPress is installed.[/bold]")
    print("-------------------------------------------------------")
    print(f"You can check that WordPress is running at http://{WORDPRESS_HOST}")
    print("-------------------------------------------------------")
    print("[bold]Wagtail is installed.[/bold]")
    print("-------------------------------------------------------")
    print(f"You can check that Wagtail is running at http://{WAGTAIL_HOST}")
    print("-------------------------------------------------------")
    print(
        "[bold]Now run [yellow]fab init[/yellow] to install the WordPress initial test data[/bold]"
    )


@task
def startbuild(ctx):
    """
    Build & Start the docker containers
    """
    local("docker-compose up -d --build")


@task
def build(ctx):
    """
    Build the wagtail docker container
    """
    local("docker-compose build")


@task
def stop(ctx):
    """
    Stop the docker containers
    """
    local("docker-compose down")


@task
def destroy(ctx):
    """
    Destroy the docker containers. THIS WILL ALSO REMOVE THE DATABASES
    """
    local("docker-compose down -v --remove-orphans")


"""WAGTAIL TASKS"""


def wagtaildocker_exec(cmd, service="wagtail"):
    return local(f"docker-compose exec -T {quote(service)} bash -c {quote(cmd)}")


@task
def sh(c):
    """Open a bash shell in the docker development container"""
    subprocess.run(["docker-compose", "exec", "wagtail", "bash"])


"""WORDPRESS TASKS"""


def wpdocker_exec(cmd, service="wordpress"):
    return local(f"docker-compose exec -T {quote(service)} bash -c {quote(cmd)}")


@task
def init(c):
    """
    Install WordPress CLI and import the XML theme fixures with media files (run this second)
    """
    load_dotenv(".env")
    url = os.environ.get("url")
    local("mkdir -p xml")

    wpdocker_exec(
        "curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar"
    )
    wpdocker_exec("chmod +x wp-cli.phar")
    wpdocker_exec("mkdir -p /xml")
    wpdocker_exec(
        "curl https://raw.githubusercontent.com/WPTT/theme-unit-test/master/themeunittestdata.wordpress.xml -o /xml/import.xml"
    )
    wpdocker_exec(
        f"php wp-cli.phar core install --allow-root --url={WORDPRESS_HOST} --title=WordPress --admin_user={WORDPRESS_USER} --admin_password={WORDPRESS_PASSWORD} --admin_email={WORDPRESS_ADMIN_EMAIL}"
    )
    wpdocker_exec(
        "php wp-cli.phar plugin install wordpress-importer --activate --allow-root"
    )
    wpdocker_exec(
        "php wp-cli.phar import /xml/import.xml --authors=create --allow-root"
    )
    print("-------------------------------------------------------")
    print("[bold]WordPress is installed.[/bold]")
    print("-------------------------------------------------------")
    print(
        f"You can view the WordPress site at http://{WORDPRESS_HOST} \nand you can login at http://{WORDPRESS_HOST}/wp-admin/ \nUsername: {WORDPRESS_USER} Password: {WORDPRESS_PASSWORD}"
    )
    print("-------------------------------------------------------")
    print(
        f"You can view the Wagtail site at http://{WAGTAIL_HOST} \nand you can login at http://{WAGTAIL_HOST}/admin/ \nUsername: {WAGTAIL_USER} Password: {WAGTAIL_PASSWORD}"
    )
    print("-------------------------------------------------------")
    print("[bold green]Creating the export file for the XML fixtures.[/bold green]")
    wpexport(c)


@task
def wpexport(c):
    """
    Export the WordPress data to an XML file
    """
    wpdocker_exec(
        f"php wp-cli.phar export --allow-root --dir=/xml --filename_format=export.xml --user={WORDPRESS_USER}"
    )


@task
def theme(c, name="twentytwentyone"):
    """
    Install a WordPress theme and switch to it
    """
    wpdocker_exec(f"php wp-cli.phar theme activate {name} --allow-root")


@task
def theme_install(c, name="twentytwentyone"):
    """
    Install a WordPress theme by name
    """
    wpdocker_exec(f"php wp-cli.phar theme install {name} --allow-root")


@task
def theme_delete(c, name="twentytwentyone"):
    """
    Un-install a WordPress theme by name
    """
    wpdocker_exec(f"php wp-cli.phar theme delete {name} --allow-root")


@task
def permalinks(c):
    """
    Change the WordPress permalink structure to /%postname%/
    """
    wpdocker_exec("php wp-cli.phar rewrite structure /%postname%/ --allow-root")


@task
def wpstart(c):
    """
    Start the WordPress container
    """
    local("docker-compose up -d wordpress")


@task
def wpstop(c):
    """
    Stop the WordPress container
    """
    local("docker-compose stop wordpress")


@task
def wprestart(c):
    """
    Restart the WordPress container
    """
    local("docker-compose restart wordpress")


def wtdocker_exec(cmd, service="wagtail"):
    return local(f"docker-compose exec -T {quote(service)} bash -c {quote(cmd)}")


@task
def run_tests(c):
    """
    Run the tests for the Wagtail WordPress Impoter
    """
    wtdocker_exec("cd /app/wagtail-wordpress-import && python testmanage.py test")


@task
def run_import(c, file_name="export.xml", app="pages", model="PostPage"):
    """
    Run the import to Wagtail
    """
    wtdocker_exec(f"python /app/example/manage.py import_xml xml/{file_name} 3 -a {app} -m {model}")


@task
def run_delete(c, app="pages", model="PostPage", images=False, documents=False):
    """
    Delete all the imported pages. Optionally delete the images and documents
    """
    wtdocker_exec(f"python /app/example/manage.py delete_imported_pages {app} {model}")
    if images:
        wtdocker_exec(f"python /app/example/manage.py delete_images")
    if documents:
        wtdocker_exec(f"python /app/example/manage.py delete_documents")


@task
def run_del_images(c):
    """
    Delete all the imported images
    """
    wtdocker_exec("python /app/example/manage.py delete_images")


@task
def run_del_documents(c):
    """
    Delete all the imported documents
    """
    wtdocker_exec("python /app/example/manage.py delete_documents")
