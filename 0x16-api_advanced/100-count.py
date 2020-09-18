#!/usr/bin/python3
''' Get hot posts '''
import pprint
import re
import requests

url = 'http://reddit.com/r/{}/hot.json'


def count_words(subreddit, word_list, hot_list=[], after=None):
    ''' Get hot posts '''
    header = {'User-agent': 'tabbykatz-app3'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "DONE":
            params['after'] = after
        else:
            return print_it(word_list, hot_list)

    response = requests.get(url.format(subreddit),
                            headers=header, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'DONE')
    if not after:
        after = "DONE"
    hot_list = hot_list + [item.get('data', {}).get('title')
                           for item in data.get('children', [])]
    return count_words(subreddit, word_list, hot_list, after)


def print_it(word_list, hot_list):
    ''' we are printing this time '''
    # print(hot_list)
    # print(word_list)
    count = {}
    for word in word_list:
        count[word] = 0
    for title in hot_list:
        for word in word_list:
            count[word] = count[word] +\
             len(re.findall(r'(?:^| ){}(?:$| )'.format(word), title, re.I))
            # findall(thing, where, ignore case)

    count = {k: v for k, v in count.items() if v > 0}
    words = sorted(list(count.keys()))
    for word in sorted(words,
                       reverse=True, key=lambda k: count[k]):
        # sorted( thing, descending, by count)
        print("{}: {}".format(word, count[word]))
