import random
import json

with open('words.json', 'r') as f:
    data = f.read()
words = json.loads(data)

def print_job_title():
    adj1 = random.randrange(len(words['adjective1']))
    adj2 = random.randrange(len(words['adjective2']))
    adj3 = random.randrange(len(words['adjective3']))
    pos = random.randrange(len(words['position']))
    jobtitle = ""
    if words['adjective1'][adj1] != "":
        jobtitle += words['adjective1'][adj1].rstrip() + " "
    if words['adjective2'][adj2] != "":
        jobtitle += words['adjective2'][adj2].rstrip() + " "
    if words['adjective3'][adj3] != "":
        jobtitle += words['adjective3'][adj3].rstrip() + " "
    if words['position'][pos] != "":
        jobtitle += words['position'][pos].rstrip() + " "
    print("Your new job title:")
    print(jobtitle)

resp = ""
while True:
    resp = input("Press ENTER to generate new job title, or type 'q' to quit: ")
    if resp.lower() == "q":
        print("Thank you for using Job Title Generator")
        break
    else:
        print_job_title()
        print("")
