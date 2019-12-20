from github import Github

with open("GHKey.txt", "r") as keyfile:
    access_token = keyfile.read().replace('\n','')
g = Github(access_token)

user = g.get_user()
org_paginated_list = user.get_orgs()
org_list = []
print "Please select which org to scan"

counter = 0
for org in org_paginated_list:
    print "{}) {}".format(counter,org)
    org_list.append(org)
    counter +=1
action = raw_input(">>> ")
print org_list[0]
try:
    org = org_list[int(action)]
except:
    exit()
print("You have selected {}".format(org))
