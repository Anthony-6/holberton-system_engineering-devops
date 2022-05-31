#!/usr/bin/python3
"""function that return the top 10 post from a subreddit"""


import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit."""
    req = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "anthony_6_"},
                       allow_redirects=False)
    if req.status_code >= 300:
        return 0
    else:
        for information in req.json().get("data").get("children"):
            print(information.get("data").get("title"))
