from github import Github
import time
import sys

#Open keyfile
with open("GHKey.txt", "r") as keyfile:
    access_token = keyfile.read().replace('\n','')

results = open("search_results.txt", "a")

print("Enter keyword:")
keyword = raw_input(">>> ")

#Instantiate Github instance
g = Github(access_token)

#Get authenticated user
user = g.get_user()

#Generate list of orgs
org_paginated_list = user.get_orgs()
org_list = []
print "Please select which org to scan"

#Display list of orgs
counter = 0
for org in org_paginated_list:
    print "{}) {}".format(counter,org.name)
    org_list.append(org)
    counter +=1
action = raw_input(">>> ")
#print org_list[0]
try:
    org = org_list[int(action)]
except:
    exit()
print("You have selected {}".format(org))

#Page through members
counter = 0
members = org.get_members()

with open("evilkey.txt", "r") as keyfile:
    access_token = keyfile.read().replace('\n','')

g = Github(access_token)
countera=0
repo_list = []
repo_query = ""
for user in members:
    #Page through member's public repos
    for repo in user.get_repos():
        countera+=1
        #Search each repo for keyword
        repo_query+=" repo:"
        repo_query+=str(repo.full_name)
        if countera >100:
            countera = 0
            repo_list.append(repo_query[1:])
            repo_query=""
            print len(repo_list)
repo_list.append(repo_query)
print repo_list
print len(repo_list)
for query in repo_list:
    for item in g.search_code("{} {}".format(keyword, query)):
        time.sleep(1)
        print item.html_url
        results.write(item.html_url)
        results.write("\n")
    time.sleep(30)
