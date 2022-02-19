#Names: Waleed I, Wenbo W, Ashi M
#BAX422 A5
#Date: Feb. 15th, 2022

import requests
from datetime import datetime

AUTH = "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"

# Getting the first 100 contributors from the Apache Hadoop Repository
url = "https://api.github.com/repos/apache/hadoop/contributors?page="
contributors = []

for i in range(1, 5): # we can 30 contributors in each page. So we need to go to page 4 for getting 100 contributors
    url = url + str(i)
    res = requests.get(url)
    contributors.extend(res.json())


contributors = contributors[:100] # just get the first 100 contributors

for contributor in contributors: # Getting the total number of repositories and the total number of contributions of a user and printing it
    login = contributor['login']
    headers = {
        "Authorization": f"bearer {AUTH}"
    }
    payload = {
        "query": """query {
            user(login: \"""" + login + """\"){
                name
                repositories{
                totalCount
                }
                contributionsCollection {
                contributionCalendar {
                    totalContributions
                }
                }
            }
            }"""
    }

    res = requests.post("https://api.github.com/graphql", json=payload, headers=headers)
    user_data = res.json()
    user = user_data['data']['user']
    print("Name:", user['name'])
    print("Username:", login)
    print("Total Number of Repos:", user['repositories']['totalCount'])
    print("Total Contributions:", user['contributionsCollection']['contributionCalendar']['totalContributions'])
    print()


# Accessing the commits endpoint for the repository Apche/Hadoop and print the difference betweent first and 100th commit timestamp
url = "https://api.github.com/repos/apache/hadoop/commits?page="
res = requests.get(url + str(1))
first_commit = res.json()[0]
res = requests.get(url + str(4))
one_hundreth_commit = res.json()[9]

first_commit = datetime.strptime(first_commit['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ').timestamp()
one_hundreth_commit = datetime.strptime(one_hundreth_commit['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ').timestamp()

print("Difference between last and 100th commit:", first_commit-one_hundreth_commit)

