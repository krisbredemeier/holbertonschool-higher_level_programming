#!/usr/bin/env python

import json
import requests

def get_json(url):
    response = requests.get(url)
    commits = response.json()

    for commit in commits:
        print("id = {}, message = {}, date = {}, name = {}".format(
        commit.get('sha'),
        commit.get('commit').get('message'),
        commit.get('commit').get('author').get('date'),
        commit.get('commit').get('author').get('name')))

url= "https://api.github.com/repos/holbertonschool/Betty/commits"
get_json(url)
