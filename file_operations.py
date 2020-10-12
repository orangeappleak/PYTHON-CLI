import os
import json
import click

def create_profile(name,username):
    try:
        if(os.path.getsize("user_profiles.json") == 0):
            with open("user_profiles.json","w") as outfile:
                with open("user_profiles.json","r") as infile:
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
        else:
            if(not check_profile(name)):
                new_user_profile = {
                    "username": username,
                    "profile_name": name,
                    "current_prof": "False"
                }
                with open("user_profiles.json","r") as infile:
                    data = json.load(infile)
                    data['user_profiles'].append(new_user_profile)
                    with open("user_profiles.json","w") as outfile:
                        json.dump(data,outfile,indent=4,sort_keys=True)
            else:
                print("username/profile_name is already registered")
    except FileNotFoundError:
        click.secho("The file was not found, creating the json file",fg="red")
        with open("user_profiles.json","a") as outfile:
                with open("user_profiles.json","r") as infile:
                    file_data = {
                        "user_profiles":[]
                    }
                    json.dump(file_data,outfile,indent=4)

def check_profile(profile_name):
    with open("user_profiles.json") as f:
        data = json.load(f)
        for userprofile_name in data['user_profiles']:
            if userprofile_name['profile_name'] == profile_name:
                return True
                break
    return False
