import os
import json

file = open(file = 'data/webstack.json', mode = 'r', encoding = 'utf-8')

groups = json.loads(file.read())

if os.path.exists("webstack.md"):
    os.remove("webstack.md")

f = open(file = 'webstack.md', mode = 'a', encoding = 'utf-8')

for group in groups:
    f.write("## " + group['taxonomy'] + "\n\n")

    if 'links' in group:
        f.write("|網站|說明|\n")
        f.write("|--|--|\n")
        for site in group['links']:
            f.write("|[" + site['title'] + "](" + site['url'] + ")|" + site['description'] + "|\n")
        f.write("\n")
    
    if 'list' in group:
        for terms in group['list']:
            f.write("### " + terms['term'] + "\n\n")
            f.write("|網站|說明|\n")
            f.write("|--|--|\n")
            for site in terms['links']:
                f.write("|[" + site['title'] + "](" + site['url'] + ")|" + site['description'] + "|\n")
            f.write("\n")
f.close()
