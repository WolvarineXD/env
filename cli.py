import os
import click
import subprocess
import sys

BASE_ENV_DIR = os.path.expanduser("~/.envs")  # Store environments in a common location

if not os.path.exists(BASE_ENV_DIR):
    os.makedirs(BASE_ENV_DIR)

@click.group()
def cli():
    """Environment Management CLI"""
    pass

@cli.command()
@click.argument("env_name")
def create(env_name):
    """Create a new virtual environment"""
    env_path = os.path.join(BASE_ENV_DIR, env_name)
    if os.path.exists(env_path):
        click.echo(f"Environment '{env_name}' already exists.")
        return
    subprocess.run([sys.executable, "-m", "venv", env_path])
    click.echo(f"Environment '{env_name}' created at {env_path}.")

@cli.command()
@click.argument("env_name")
def activate(env_name):
    """Print activation command for an environment"""
    env_path = os.path.join(BASE_ENV_DIR, env_name)
    if not os.path.exists(env_path):
        click.echo(f"Environment '{env_name}' does not exist.")
        return
    activation_script = os.path.join(env_path, "Scripts" if os.name == "nt" else "bin", "activate")
    click.echo(f"Run this command to activate: source {activation_script}" if os.name != "nt" else activation_script)

@cli.command()
def list():
    """List all environments"""
    envs = os.listdir(BASE_ENV_DIR)
    if not envs:
        click.echo("No environments found.")
        return
    click.echo("Available Environments:")
    for env in envs:
        click.echo(f"- {env}")

@cli.command()
@click.argument("env_name")
def delete(env_name):
    """Delete a virtual environment"""
    env_path = os.path.join(BASE_ENV_DIR, env_name)
    if not os.path.exists(env_path):
        click.echo(f"Environment '{env_name}' does not exist.")
        return
    subprocess.run(["rm", "-rf", env_path] if os.name != "nt" else ["rmdir", "/s", "/q", env_path], shell=True)
    click.echo(f"Environment '{env_name}' deleted.")

if __name__ == "__main__":
    cli()
