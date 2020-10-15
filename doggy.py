import click
import time
import random
from commands.uc import user_commands
from file_operations import create_profile,set_active_profile,get_current_profile,display_profiles
import json

class active_user(object):
    def __init__(self,user_profile):
        self.user_profile = user_profile

@click.group(name="Basic_utilities",help="DOG͎̾GͧY͇",invoke_without_command=True)
@click.option("--userprof","-up",help="set the active user profile")
@click.option("--username","-un")
@click.option("--profilename","-pn")
@click.pass_context
def main_commands(ctx,userprof,username,profilename):
    ctx.obj = active_user(userprof)
    if(userprof != None):
        set_active_profile(userprof)
    if(username and profilename != None):
        create_profile(profilename,username)
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

@main_commands.command(name="currprof",help="Displays the current user profile chosen")
@click.pass_obj
def currprof(ctx):
    get_current_profile()

@main_commands.command(name="display",help="Displays all the user profiles")
def display():
    try:
        display_profiles()
    except:
        print("There are no user profiles available DUMBO, add some users and then ill display them.")




main_commands.add_command(user_commands)