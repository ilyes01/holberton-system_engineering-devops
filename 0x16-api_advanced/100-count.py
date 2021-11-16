#!/usr/bin/python3
""" emchyyyy plzzzzzzzzzzzzzzzz """
import requests


def count_words(subreedit, word_list, after="", d={}, check=0):
    """Returns top 10 posts """
    if check == 0:
        for j in range(len(word_list)):
            word_list[j] = word_list[j].lower()
    d = dict.fromkeys(word_list)
    url = 'https://www.reddit.com'
    query_string = 'r/{}/hot.json'.format(subreedit)
    s1 = "Mozilla/5.0 (Linux; Android 11; Pixel 2;"
    s2 = "DuplexWeb-Google/1.0) AppleWebKit/537.36"
    s3 = "(KHTML, like Gecko) Chrome/86.0.4240.193 Mobile Safari/537.36"
    agent = s1 + s2 + s3
    headers = {'User-agent': agent}
    params = {'after': after}
    r = requests.get(
        '{}/{}'.format(url, query_string),
        allow_redirects=False,
        headers=headers,
        params=params
        )
    if r.status_code == 403 or r.status_code == 404:
        return
    data = r.json()
    after = data.get('data').get('after')
    posts = data.get('data').get('children')
    for post in posts:
        title = post.get('data').get('title')
        title_list = title.split(' ')
        for j in range(len(title_list)):
            title_list[j] = title_list[j].lower()
        # (title_list)
        # (word_list)
        for word in title_list:
            if word in word_list:
                if d[word] is None:
                    d[word] = 1
                else:
                    d[word] += 1
    if after:
        return count_words(subreedit, word_list, after, d, 1)
    print(d)
    return d

if __name__ == '__main___':
    count_words(subreedit)
