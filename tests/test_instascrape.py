from instascrape import *

URL = "https://www.instagram.com/google/"

def scrape_test(url): 
    google = Profile(url)
    google.scrape()
    print(google.followers)

scrape_test(URL)
