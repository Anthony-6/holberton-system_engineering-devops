#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    unction that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit."""

    req = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "anthony_6_"},
                       allow_redirects=False)
    if req.status_code >= 300:
        return 0
    else:
        return(req.json().get('data').get('subscribers'))
