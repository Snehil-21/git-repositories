# import libraries
import requests
from bs4 import BeautifulSoup

# input username from user
username = input('Enter the username: ')

# function to scrape data out of the html of the website


def getUser():
    # define the url to scrape
    url = 'https://github.com/'+username+'?tab=repositories'

    # GET request pn the URL
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    # if GET request is successful
    if res.status_code == 200:
        # extract content out of the response
        received_load = res.content
        # beautify the HTML content
        payload = BeautifulSoup(received_load, 'html.parser')
        # extract the name of the user
        name = payload.select("h1.vcard-names span")[0].text.strip()
        # extract the repositories
        repos = payload.select("li.public div div h3")
        # print name and then repositories of the requested user
        print('Name: '+name)
        for repo in repos:
            print(repo.a.text.strip(), end=' --> ')
            print('https://github.com' + repo.a.attrs['href'], end='\n\n')
    # if there is any error
    else:
        print('An Error Occured! Please check if the username is correct or there might be some other problem at the moment. Please try again later!')


# call function to scrape profile
getUser()
