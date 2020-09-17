#!/usr/bin/python3
''' Get hot posts '''
import pprint
import requests

url = 'http://reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[], after=None):
    ''' Get hot posts '''
    headers = {'User-agent': 'tabbykatz-app2'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "DONE":
            params['after'] = after
        else:
            return hot_list
    response = requests.get(url.format(subreddit),
                            headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'DONE')
    if not after:
        after = "DONE"
    hot_list = hot_list + [item.get('data', {}).get('title')
                           for item in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
