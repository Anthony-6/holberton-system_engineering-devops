#!/usr/bin/python3
"""function that return the top 10 post from a subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    function that queries recursively the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit."""
    req = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "anthony_6_"},
                       allow_redirects=False)
    if req.status_code >= 300:
        print("None")
        return
    else:
        for information in req.json().get("data").get("children"):
            hot_list.append(information.get("title"))
    if not req.json().get("data").get("after"):
        return hot_list
    return recurse(subreddit, hot_list)
