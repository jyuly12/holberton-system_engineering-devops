#!/usr/bin/python3
"""
This module defines the "recurse" function
"""
import requests


after = ""


def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    """
    global after
    header = {"User-Agent": "Holberton"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url = url + "?after=" + after
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code != 200:
        return None
    after = r.json().get("after", "")
    for i in r.json().get("data", None).get("children", None):
        hot_list.append(i.get("data", None).get("title", None))
    if after:
        return recurse(subreddit, hot_list)
    return hot_list
