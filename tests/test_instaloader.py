import instaloader

USER_NAME = "cilantro_guy74298"
PASSWORD = "jablarious39the1goat477"

def get_profiles(username="", password=""): 

    loader = instaloader.Instaloader()

    try: 
        loader.login(username, password) # sign into account
    except instaloader.BadCredentialsException as creds:
        print(f"WHAT THE HELL IS HAPPENING: {creds}")
    except instaloader.BadResponseException as badResp: 
        print(f"\nThe following error occurred: {badResp}\n")
    except instaloader.TwoFactorAuthRequiredException as MFA:
        print(f"\nThe following error has occurred: {MFA}")
    except instaloader.LoginException as login: 
        print(f"\nThe following error has occurred: {login}")

    profile = instaloader.Profile.from_username(context=loader.context, username=username)
    following = profile.get_followees()
    return following

# print(get_profiles(USER_NAME, PASSWORD))
loading = instaloader.Instaloader()
try: 
    loading.login(USER_NAME, PASSWORD)
except instaloader.BadCredentialsException as creds: 
    print(f"WHAT THE HELL IS HAPPENING: {creds}")

