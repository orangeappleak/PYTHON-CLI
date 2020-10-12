import click
import json
import time
from file_operations import create_profile
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
        open("user_profiles.json","w").close()
        with click.progressbar([0.1, 1, 0.5, 0.8],label="Clearing all the userprofiles....") as bar:
            for x in bar:
                time.sleep(x)
        click.secho("All the userprofiles have been burnt to ashes, HA HA HA",fg="magenta",bg="yellow")





        
