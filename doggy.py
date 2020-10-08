import click
import os
import subprocess
import sys

@click.command()
@click.option('--count','-c',default = 1, help = "Number of greetings")
@click.option('--name','-n', help = "The person to greet")
@click.option('--info','-i',help = "provides the information for the tool.")
def hello(count, name):
    for x in range(count):
        click.echo("Hello %s!" % name)
def info():
    print("This is a CLI utility tool that helps you do werid things, \n it was designed and developed by the great MR.SPOCK himself(A.KARTHIK)")
