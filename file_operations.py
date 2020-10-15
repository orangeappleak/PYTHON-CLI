import os
import json
import click

# pypi-AgEIcHlwaS5vcmcCJGQ0MTJlZjYwLWE3MTEtNDJlMi05YWZiLWZhNmM3MDRjNjQ2MQACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgCBOAVFwL7x_6M6vJ-yD3hEhjWoKyQbb0z7aKZVkykAU
absolute_path = os.path.dirname(os.path.abspath(__file__))

filename = absolute_path + "/user_profiles.json"

def create_profile(name,username):
    try:
        if(os.path.getsize(filename) == 0):
            with open(filename,"w") as outfile:
                with open(filename,"r") as infile:
                    file_data = {
                        "user_profiles":[
                            {
                                "username": username,
                                "profile_name": name,
                                "current_prof": "False"
                            }
                        ]
                    }
                    json.dump(file_data,outfile,indent=4)
                    click.secho("The new profile has been created successfully",fg='red',bg="green")

        else:
            if(not check_profile(name)):
                new_user_profile = {
                    "username": username,
                    "profile_name": name,
                    "current_prof": "False"
                }
                with open(filename,"r") as infile:
                    data = json.load(infile)
                    data['user_profiles'].append(new_user_profile)
                    with open(filename,"w") as outfile:
                        json.dump(data,outfile,indent=4,sort_keys=True)
                        click.secho("The new profile has been created successfully",fg='red',bg="green")
            else:
                click.secho("username/profile_name is already registered",err=True)
    except FileNotFoundError:
        click.secho("The file was not found, creating the json file",fg="red")
        with open(filename,"a") as outfile:
                with open(filename,"r") as infile:
                    file_data = {
                        "user_profiles":[]
                    }
                    json.dump(file_data,outfile,indent=4)

def check_profile(profile_name):
    with open(filename) as f:
        data = json.load(f)
        for userprofile_name in data['user_profiles']:
            if userprofile_name['profile_name'] == profile_name:
                return True
                break
    return False

def set_active_profile(up):
    deactivate_prof()
    with open(filename,"r") as infile:
        data = json.load(infile)
        with open(filename,"w") as outfile:
            for userprofile in data['user_profiles']:
                if userprofile['profile_name'] == up:
                    userprofile['current_prof'] = "True"
            json.dump(data,outfile,indent=4,sort_keys = True)
            click.secho("the active profile has been changed to %s" % up)
    
def deactivate_prof():
    with open(filename,"r") as infile:
        data = json.load(infile)
        with open(filename,"w") as outfile:
            for userprofile in data['user_profiles']:
                userprofile['current_prof'] = "False"
            json.dump(data,outfile,indent=4,sort_keys = True)

def get_current_profile():
    with open(filename,"r") as infile:
        data = json.load(infile)
        for userprofile in data['user_profiles']:
            if(userprofile['current_prof'] == "True"):
                click.secho("The current user profile is " + userprofile['profile_name'])

def display_profiles():
    with open(filename,"r") as infile:
        data = json.load(infile)
        click.secho("The username is the name of the person who created the user profile",fg="green",bg="blue")
        click.secho(json.dumps(data['user_profiles'],indent=2,sort_keys=False),fg='yellow')