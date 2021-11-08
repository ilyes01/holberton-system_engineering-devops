#!/usr/bin/python3
"""
subs
"""
import requests
from sys import argv
"""
function number
"""


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        req = requests.get(url, headers={'User-agent': 'fedi'})
        subs = req.json()
        return subs.get('data').get('subscribers')
    except AttributeError:
        return 0
