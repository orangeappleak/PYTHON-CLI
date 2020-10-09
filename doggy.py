import click
import time
import random
from passlib.context import CryptContext
from commands.uc import pow_sub_com

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=1000
)

@click.group(name="Basic_utilities",help="DOG͎̾GͧY͇",invoke_without_command=True)
@click.option("--username","-u",default="no username entered")
@click.option("--password",prompt=True,confirmation_prompt=True)
@click.pass_context
def main_commands(ctx,username,password):
    click.echo("the entered username is %s" % username)
    with click.progressbar([1, 2, 3]) as bar:
        for x in bar:
            time.sleep(x)
    click.echo('Encrypted password to %s' % pwd_context.encrypt(password))

    pass

@main_commands.command(name="info",help="Provides basic info about the CLI application")
def info():
    time.sleep(1)
    click.secho("HEY THERE,",fg="red")
    time.sleep(2)
    click.secho("I am doggy your coding companion,",fg="magenta",bg="white")
    time.sleep(1.5)
    click.secho("You can make your coding life easier \b and simpler by making use of my powerful commands. LIKEEEEEE....",fg="magenta",bg="white")
    time.sleep(1.3)
    click.secho("----> You can create GITHUB repos or push changes to your GITHUB repo in just one command",fg="black",bg="magenta")
    time.sleep(1.5)
    click.secho("----> You can set shortcuts for all your workspaces as well as your code editors, so you dont have to go through all the clicking and searching for your folders.",fg="red",bg="white")
    time.sleep(1.5)
    click.secho("----> You can also make diff profiles based on your workflow and set passwords for each profile",fg="white",bg="red")
    time.sleep(2)
    click.secho("AND MUCH MUCH MORE, SO WHAT ARE YOU WAITING FOR GET CODING.....",fg="magenta")
    time.sleep(2)

main_commands.add_command(pow_sub_com)