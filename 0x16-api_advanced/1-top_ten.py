#!/usr/bin/python3
""" Queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit. """

import requests
headers = {"User-Agent": "ubuntu:hbtn:v1.0 (by /u/piroli_)"}


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        for children in request.json().get("data").get("children"):
            print(children.get("data").get("title"))

    else:
        print(None)

