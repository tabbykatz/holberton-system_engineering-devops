#!/usr/bin/python3
''' get hot posts  '''
import requests

url = 'https://www.reddit.com/r/{}/hot.json'


def top_ten(subreddit):
    '''get top_ten '''
    header = {'user-agent': 'tabbykatz-app1'}
    r = requests.get(url.format(subreddit), headers=header)
    if r.status_code != 200:
        print("None")
        return
    children = r.json().get('data', {}).get('children', [])
    if not children:
        print("None")
        return
    for item in children[0:10]:
        print(item.get('data', {}).get('title', ''))
