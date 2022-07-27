# Run this to get the repositories info and the imports
import string
import pandas as pd
import math
from github import Github
import os
from pprint import pprint
import requests
import csv


# Makes the csv
def createCSV(repoInfo):
    data = []
    for repo in repoInfo:
        repoName = repo
        for commit in repoInfo[repo]:
            commits = []
            commits.append(repoName)
            commits.append(commit["forks"])
            commits.append(commit["additions"])
            commits.append(commit["deletions"])
            commits.append(commit["total"])
            commits.append(commit["message"])
            data.append(commits)

    header = ['Repository', 'Forks', 'additions', 'Deletions', 'Total', 'Messages']

    with open('MainDataset5.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerows(data)


repos_info = pd.read_csv("repositories.csv")

# Run this to get the owner and repos form each repos (it's just for the owner mainly)
reposURLs = repos_info["url"]
reposSlicedURLs = []
for reposURL in reposURLs:
    reposSlicedURLs.append(reposURL[29:])
slicedInfo = {}


token = os.getenv('GITHUB_TOKEN', 'YOUR GHP TOKEN HERE') # Generate a ghp token from Github and paste it here.
repoInfo = {}

i = 0
for slice in reposSlicedURLs:

    ownerRepos = slice.split("/")
    owner = ownerRepos[0]
    repo = ownerRepos[1]
    if i < 856:
        i+=1
        continue
    # else:
    #     print(ownerRepos)
    #     break

    else:
        try:
            # To get the number of forks
            query_url = f"https://api.github.com/repos/{owner}/{repo}"
            params = {
                "state": "open",
            }
            headers = {'Authorization': f'token {token}'}
            fork = requests.get(query_url, headers=headers, params=params)
            # To get the info of the commits
            query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
            r = requests.get(query_url, headers=headers, params=params)
            commitsInfo = []
            for author in r.json():
                commitStats = {"total": 0, "additions": 0, "deletions": 0, "message": "", "forks": fork.json()["forks_count"]}
                sha = author["url"]
                query_url = sha
                commit = requests.get(query_url, headers=headers, params=params)
                #         for spesCommit in commit.json():
                totalS = commit.json()["stats"]["total"]
                additionS = commit.json()["stats"]["additions"]
                deletionS = commit.json()["stats"]["deletions"]
                messageS = commit.json()["commit"]["message"]
                commitStats["total"] = totalS
                commitStats["additions"] = additionS
                commitStats["deletions"] = deletionS
                commitStats["message"] = messageS
                commitsInfo.append(commitStats)
            i = i + 1
            repoInfo[repo] = commitsInfo
            pprint(i)
            if i > 1000:
                break
        except:
            pprint('error at repo')
            createCSV(repoInfo)
            continue
    createCSV(repoInfo)




# Makes the dict with the stats of the the repos
# token = os.getenv('GITHUB_TOKEN', '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')
# repoInfo = {}
# i = 0
# for owner in slicedInfo:
#     owner = owner
#     repo = slicedInfo[owner]
#     #To get the number of forks
#     query_url = f"https://api.github.com/repos/{owner}/{repo}"
#     params = {
#         "state": "open",
#     }
#     headers = {'Authorization': f'token {token}'}
#     fork = requests.get(query_url, headers=headers, params=params)
#     #To get the info of the commits
#     query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
#     r = requests.get(query_url, headers=headers, params=params)
#     commitsInfo = []
#     for author in r.json():
#         commitStats = {"total": 0, "additions": 0, "deletions": 0, "message": "", "forks": fork.json()["forks_count"]}
#         sha = author["url"]
#         query_url = sha
#         commit = requests.get(query_url, headers=headers, params=params)
# #         for spesCommit in commit.json():
#         totalS = commit.json()["stats"]["total"]
#         additionS = commit.json()["stats"]["additions"]
#         deletionS = commit.json()["stats"]["deletions"]
#         messageS = commit.json()["commit"]["message"]
#         commitStats["total"] = totalS
#         commitStats["additions"] = additionS
#         commitStats["deletions"] = deletionS
#         commitStats["message"] = messageS
#         commitsInfo.append(commitStats)
#     i = i + 1
#     repoInfo[repo] = commitsInfo
#     pprint(i)
#     if i > 1000:
#         break

# owner = slicedInfo[205]
# repo = slicedInfo[205]
# #To get the number of forks
# query_url = f"https://api.github.com/repos/{owner}/{repo}"
# params = {
#     "state": "open",
# }
# headers = {'Authorization': f'token {token}'}
# fork = requests.get(query_url, headers=headers, params=params)
# #To get the info of the commits
# query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
# r = requests.get(query_url, headers=headers, params=params)
# commitsInfo = []
# for author in r.json():
#     commitStats = {"total": 0, "additions": 0, "deletions": 0, "message": "", "forks": fork.json()["forks_count"]}
#     sha = author["url"]
#     query_url = sha
#     commit = requests.get(query_url, headers=headers, params=params)
# #         for spesCommit in commit.json():
#     totalS = commit.json()["stats"]["total"]
#     additionS = commit.json()["stats"]["additions"]
#     deletionS = commit.json()["stats"]["deletions"]
#     messageS = commit.json()["commit"]["message"]
#     commitStats["total"] = totalS
#     commitStats["additions"] = additionS
#     commitStats["deletions"] = deletionS
#     commitStats["message"] = messageS
#     commitsInfo.append(commitStats)
# i = i + 1
# repoInfo[repo] = commitsInfo
#


