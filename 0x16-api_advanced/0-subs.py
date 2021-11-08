#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers """
import requests
headers = {'user-agent': 'linux:taiebchaabini.tech:v1\
 (by /u/taiebchaabini)'}


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    url = 'https://api.reddit.com/r/' + subreddit + '/about'
    response = requests.get(url,
                            headers=headers)
    try:
        data = response.json()
        data = data['data']['subscribers']
    except:
        data = 0
    return data
