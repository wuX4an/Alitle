import click
from ali_src import ali_utils
from ali_src import conf
import os

@click.group()
def main():
    pass

@main.command()
def uninstall():
    """Uninstall ali"""
    ali_utils.uninstall()

@main.command()
def create():
    """Create a container"""
    ali_utils.create(conf.username, conf.password, conf.alpine_version)

@main.command()
def shell():
    """Enter to the container"""
    ali_utils.shell(conf.username)

@main.command()
def start():
    """Start the container"""
    ali_utils.start()

@main.command()
def stop():
    """Stop the container"""
    ali_utils.stop()

@main.command()
def status():
    """Status of the container"""
    ali_utils.status()

@main.command()
def restart():
    """Restart the container"""
    ali_utils.restart()

@main.command()
def delete():
    """Delete the container"""
    ali_utils.delete()


user = os.environ.get('USER')

if __name__ == "__main__" and user != "root":
    main()
else:
    print("Don't use it as the root user")