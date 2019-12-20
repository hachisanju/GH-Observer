with open ("results.txt") as file:
    content = file.readlines()

content = [x.strip() for x in content]
final_list = []
for line in content:
    subsections = line.split('/blob/')
    if subsections[0] not in final_list:
        final_list.append(subsections[0])
for line in final_list:
    print line
