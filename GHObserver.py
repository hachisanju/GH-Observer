from github import Github
import time

#Open keyfile
with open("GHKey.txt", "r") as keyfile:
    access_token = keyfile.read().replace('\n','')

results = open("search_results.txt", "a")

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
print org_list[0]
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

for user in members:
    #Page through member's public repos
    for repo in user.get_repos():
        counter +=1
        if counter > 10:
            counter = 0
            time.sleep(90)
        else:
            time.sleep(1)
        #Search each repo for keyword
        for item in g.search_code("mobiquity repo:{}".format(repo.full_name)):
            print item.html_url
            results.write(item.html_url)
            results.write("\n")
