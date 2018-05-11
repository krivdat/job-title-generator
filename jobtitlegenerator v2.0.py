import random

adj1_fname = "adjective1.txt"
adj2_fname = "adjective2.txt"
adj3_fname = "adjective3.txt"
pos_fname = "position.txt"

with open(adj1_fname) as f:
    adjectives1 = f.readlines()

with open(adj2_fname) as f:
    adjectives2 = f.readlines()

with open(adj3_fname) as f:
    adjectives3 = f.readlines()

with open(pos_fname) as f:
    positions = f.readlines()

print(adjectives1)


def print_job_title():
    adj1 = random.randrange(len(adjectives1))
    adj2 = random.randrange(len(adjectives2))
    adj3 = random.randrange(len(adjectives3))
    pos = random.randrange(len(positions))
    jobtitle = ""
    if adjectives1[adj1] != "":
        jobtitle += adjectives1[adj1].rstrip() + " "
    if adjectives2[adj2] != "":
        jobtitle += adjectives2[adj2].rstrip() + " "
    if adjectives3[adj3] != "":
        jobtitle += adjectives3[adj3].rstrip() + " "
    if positions[pos] != "":
        jobtitle += positions[pos].rstrip()
    print("Your new job title:")
    print(jobtitle)

resp = ""
while True:
    resp = input("Press ENTER to generate new job title, or type 'q' to quit: ")
    if resp.lower() == "q":
        print("Thank you for using Job Title Generator v2.0.")
        break
    else:
        print_job_title()
        print("")
