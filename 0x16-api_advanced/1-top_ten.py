#!/usr/bin/python3
""" function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit. """
import json
import requests
headers = {'user-agent': 'linux:taiebchaabini.tech:v1\
 (by /u/taiebchaabini)'}


def top_ten(subreddit):
    """ function that queries the Reddit API. """
    url = 'https://api.reddit.com/r/' + subreddit
    response = requests.get(url,
                            headers=headers)
    try:
        data = response.json()
    except:
        print("None")
        return
    if (str(response.status_code) == '404'):
        print("None")
        return
    for i in range(0, 10):
        try:
            print(data['data']['children'][i]['data']['title'])
        except:
            pass
