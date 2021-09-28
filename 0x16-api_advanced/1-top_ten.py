#!/usr/bin/python3
"""
This node defines the "top_ten" function
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    header = {"User-Agent": "Holberton"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:

        for item in response.json().get("data", None).get("children", None):
            print(item.get("data", None).get("title", None))
    else:
        print(None)
        return
