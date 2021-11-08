#!/usr/bin/python3
"""
 recursive function that queries the Reddit API and returns a list containing
 the titles of all hot articles for a given subreddit.
"""
import json
import requests
headers = {'user-agent': 'linux:taiebchaabini.tech:v1\
 (by /u/taiebchaabini)'}


def recurse(subreddit, hot_list=[], after=''):
    """
     recursive function that queries the Reddit API and returns a list
     containing the titles of all hot articles for a given subreddit.
    """
    url = 'https://api.reddit.com/r/' + subreddit + '?limit=100&after=' + after
    response = requests.get(url,
                            headers=headers)
    try:
        data = response.json()
    except:
        return None
    if (str(response.status_code) == '404'):
        return None
    dataLength = len(data['data']['children'])
    if (dataLength is 0):
        return None
    for i in range(0, dataLength):
        try:
            get_title = data['data']['children'][i]['data']['title']
            hot_list.append(get_title)
        except:
            pass
    afterVal = data['data']['after']
    if (afterVal is not None):
        return recurse(subreddit, hot_list, afterVal)
    else:
        return hot_list
