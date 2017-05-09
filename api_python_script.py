#!/usr/bin/env python

import json
import requests

def get_json(url):
    response = requests.get(url)
    commits = response.json()

    i = 0

    for commit in commits:
        i+=1
        print("id = {}, message = {}, date = {}, name = {} author id = {}".format(
        commit.get('sha'),
        commit.get('commit').get('message'),
        commit.get('commit').get('author').get('date'),
        commit.get('commit').get('author').get('name'),
        commit.get('author').get('id')))
        print(i)
        if i == 10:
            break


url= "https://api.github.com/repos/holbertonschool/Betty/commits"
get_json(url)
