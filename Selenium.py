#Names: Waleed I, Wenbo W, Ashi M
#BAX422 A5
#Date: Feb. 15th, 2022

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time
import json

AUTH = "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"
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}


# Getting the first 100 contributors from the Apache Hadoop Repository
url = "https://api.github.com/repos/apache/hadoop/contributors?per_page=100"
res = requests.get(url, headers=headers)
contributors = json.loads(res.content)


for contributor in contributors: # Getting the total number of repositories and the total number of contributions of a user and printing it
    login = contributor['login']
    user_url = contributor['html_url']
    
    profile_page = requests.get(user_url, headers=headers)
    profile_page_content = profile_page.content
    
    soup = BeautifulSoup(profile_page_content, "html.parser")
    
    num_repos = soup.find("span", class_ = "Counter").text
    
    year_box = soup.find("ul", class_ = "filter-list small")
    years = year_box.find_all("li")
    
    total_contributions = 0
    
    for year in years:
        time.sleep(2)
        year_link = "https://www.github.com" + year.find("a")['href']
        year_page = requests.get(year_link, headers=headers)
        
        year_page_soup = BeautifulSoup(year_page.content, "html.parser")
        total = year_page_soup.find('h2', class_ = 'f4 text-normal mb-2')
        total_contributions += int(total.text.split()[0].replace(',', ''))
        
    print("Username:", login)
    print("Total Number of Repos:", num_repos)
    print("Total Contributions:", total_contributions)
    print()



# Accessing the commits endpoint for the repository Apche/Hadoop and print the difference betweent first and 100th commit timestamp
url = "https://api.github.com/repos/apache/hadoop/commits?page="
res = requests.get(url + str(1), headers=headers)
first_commit = res.json()[0]
res = requests.get(url + str(4), headers=headers)
one_hundreth_commit = res.json()[9]

first_commit = datetime.strptime(first_commit['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')
one_hundreth_commit = datetime.strptime(one_hundreth_commit['commit']['committer']['date'], '%Y-%m-%dT%H:%M:%SZ')

print("Difference between last and 100th commit:", (first_commit-one_hundreth_commit).total_seconds(), "seconds")