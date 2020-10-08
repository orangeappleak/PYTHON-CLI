import click
import os
import subprocess
import sys

@click.group()
def cli():
    pass
@cli.command()
def hel():
    for x in range(5):
        click.echo("Hello DUMBO")

@cli.command()
@click.option('--name',default="you are an idiot",help = "greets the user.")
def name(name):
    click.echo("Hello Idiot, OH shit my bad. HELLO " + name)
