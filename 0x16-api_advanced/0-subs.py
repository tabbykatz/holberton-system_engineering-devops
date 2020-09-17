#!/usr/bin/python3
''' get subs '''
import requests

url = 'https://www.reddit.com/r/{}/about.json'


def number_of_subscribers(subreddit):
    '''get subscribers'''
    header = {'user-agent': 'tabbykatz-app0'}
    r = requests.get(url.format(subreddit), headers=header)
    if r.status_code != 200:
        return 0
    return r.json().get("data", {}).get("subscribers", 0)
