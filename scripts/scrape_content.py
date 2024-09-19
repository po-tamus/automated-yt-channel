import instaloader #pip install instaloader
from instalooter.looters import InstaLooter, ProfileLooter #pip install instalooter
from instalooter.cli.login import login
import datetime 
import logging

def get_profiles(username="", password=""): 

    loader = instaloader.Instaloader(max_connection_attempts=3)

    try: 
        loader.login(username, password) # sign into account
    except instaloader.BadResponseException as badResp: 
        print(f"\nThe following error occurred: {badResp}\n")
    except instaloader.TwoFactorAuthRequiredException as MFA:
        print(f"\nThe following error has occurred: {MFA}")
    except instaloader.LoginException as login: 
        print(f"\nThe following error has occurred: {login}")

    profile = instaloader.Profile.from_username(context=loader, username=username)
    following = profile.get_followees()
    return following

def scrapeContent(username="", password="", output_folder=""):
    
    try: 
        following = get_profiles()
    except: 
        return None

    for profile in following:

        # looter can be based on hashtags, posts, profiles
        looter = ProfileLooter(username=profile)

        # error handling
        try: 
            pass
        except: 
            pass



if __name__ == "__main__": 
    scrapeContent()