import click
import json
import time
from doggy.file_operations import create_profile,display_profiles,deleteallprofiles,add_shortcut
import colorama

@click.group(name="usersett",help="Manage your userprofile settings or add new profiles",invoke_without_command=True)
@click.option('--profilename',"-pn",type=click.STRING)
@click.option("--username","-un",type=click.STRING)
@click.pass_context
def user_commands(ctx,profilename,username):
    if(profilename != None):
        create_profile(profilename,username)
    pass


@user_commands.command(name="newprof",help="creates a new user profile")
@click.argument('name')
@click.argument('username')
def newProfile(name,username):
    create_profile(name,username)
    

@user_commands.command(name="deleteprofiles",help="deletes all the userdata")
def deleteprofiles():
    if(click.confirm("Are you sure you want to delete all the user_profiles?")):
        with click.progressbar([0.1, 1, 0.5, 0.8],label="Clearing all the userprofiles....") as bar:
            for x in bar:
                time.sleep(x)
        deleteallprofiles()
        click.secho("All the userprofiles have been burnt to ashes, HA HA HA",fg="magenta",bg="yellow")

@user_commands.command(name="display",help="Displays all the user profiles")
def display():
    display_profiles()

@user_commands.command(name="shortcuts",help="add new apllication/file shortcuts to your profile")
@click.option('--shortcut','-sc',required=True,prompt='enter the shortcut (shortcut can be anything you want, like v for vscode or at for atom etc.)')
@click.option('--path','-p',required=True,prompt="path for the file or apllication")
@click.option('--userprofile','-up',required=True,help="the userprofile to add the shortcuts",prompt="the userprofile to add the shortcuts")
def shortcuts(shortcut, path,userprofile):
    click.secho("shortcut is:"+shortcut+"\n path is "+path,fg="red",bg="yellow")
    add_shortcut(path, shortcut, userprofile)




        