
import random 

adjective1 = [
    "Key",
    "Top",
    "Main",
    "Chief",
    "Assistant to",
    "Advisor to",
    "Personal Assistant to",
    "Part Time",
    ""
    ]

adjective2 = [
    "Senior",
    "Junior",
    "Regional",
    "Country",
    "Associate",
    "Head",
    "Super",
    "Local",
    "Global",
    "Assistant",
    "Independent",
    "Fulltime",
    "Division",
    "National",
    "Creative",
    "Dedicated",
    "Operations",
    "Improvement",
    "Area",
    "Licenced",
    "Retail",
    "Office",
    "Industrial"
    ]

adjective3 = [
    "Development",
    "Technical",
    "Business",
    "Financial",
    "IT",
    "Project",
    "Cost",
    "Managing",
    "Commercial",
    "Procurement",
    "Cleaning",
    "Team",
    "Real Estate",
    "Sales",
    "Property",
    "Asset",
    "Facility",
    "Cashflow",
    "Creative",
    "Operation",
    "Letting",
    "Enterprise",
    "Corporate",
    "Accounting",
    "Green Building",
    "Construction",
    "Marketing",
    "Investment",
    "Customer",
    "Support",
    "Feedback",
    "Reconciliation",
    "Volume Rebates",
    "Sales Support",
    "Master",
    "Safety",
    "Process",
    "Research",
    "Leasing",
    "Strategy",
    "Planning",
    "Due Dilligence",
    "Loan",
    "Risk",
    "Valuations",
    "Insurance",
    "Debt",
    "Portfolio",
    "Acquisitions",
    "Performance"
    ]

position = [
    "Director",
    "Manager",
    "Administrator",
    "Architect",
    "Representative",
    "Specialist",
    "Boss",
    "President",
    "Vice-president",
    "Partner",
    "Leader",
    "Co-ordinator",
    "Engineer",
    "Officer",
    "Analyst",
    "Consultant",
    "Advisor",
    "Estimator",
    "Professional",
    "Supervisor",
    "Messenger",
    "Executive",
    "Agent",
    "Appraiser",
    "Economist",
    "Controller",
    "Counsel",
    "Underwriter"
    ]

def print_job_title():
    adj1 = random.randrange(len(adjective1))
    adj2 = random.randrange(len(adjective2))
    adj3 = random.randrange(len(adjective3))
    pos = random.randrange(len(position))
    jobtitle = ""
    if adjective1[adj1] != "":
        jobtitle += adjective1[adj1] + " "
    if adjective2[adj2] != "":
        jobtitle += adjective2[adj2] + " "
    if adjective3[adj3] != "":
        jobtitle += adjective3[adj3] + " "
    if position[pos] != "":
        jobtitle += position[pos]        
    print("Your new job title:")
    print(jobtitle)

resp = ""
while resp.lower() != "q":
    print_job_title()
    resp = input("\nPress ENTER to generate new job title, or type 'q' to quit: ")
    print("")