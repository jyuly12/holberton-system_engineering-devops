#!/usr/bin/python3
"""
This module defines the "number_of_subscribers" function
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function obtain queries the Reddit API and returns the number
    of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Ana'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)