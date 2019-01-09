#! /usr/bin/env/python3
import re

# Import the file of budget increase percentages
f_budget = open("budget_increase_per_dist.txt", "rt")

# Load budget into a dictionary
# with the non-blank reformatted district as a key
# and the percentage as the data

budget = {}

budget_line = f_budget.readline()
while budget_line:
    parts = budget_line.split("|")

    # print(parts)
    
    # checking for blank
    if parts[0] != "":
        dist = "\"" + parts[0].upper() + "\""
        try: increase = parts[1]
        except: increase = 0
        
        budget[dist] = increase

    budget_line = f_budget.readline()

# Open twelfthGradeDistSize.txt                                 
# if field[1] on comma delimeter matches      
# existing district     
# then regex the number and make an int
# and add to dictionary
enroll = {}

symbol_pat = re.compile(r'([0-9]+)')

f_size = open("twelfthGradeDistSize.txt", "rt")
line_size = f_size.readline() # Skipping extra headers
line_size = f_size.readline()
line_size = f_size.readline()
line_size = f_size.readline()
line_size = f_size.readline()

while line_size:
    fields = line_size.split(",")
    district = "\"" + fields[0].upper() + "\""

    # Regex to find the number
    found = re.findall(symbol_pat, fields[1])

    if found:
        dist_size = int(found[0])
        enroll[district] = dist_size

    line_size = f_size.readline()

f_size.close()

# print(enroll)

# Open the file of the voter percentage increases
# will be my baseline for counties because in the voter
# files they record fewer school districts (as opposed
# to DOE produced district-by-district expenditures
# which will be scrupulous on the counties
f_voters = open("percent_voters_by_dist.txt", "rt")

# Load the first line from baseline voter file
line_voters = f_voters.readline()
inc = 1

# setting up
print("District" + "|" + "% Voter Increase" + "|" + "% Budget increase" + "|" + "12th Grade Dist Enrollment 2004-5")

# going by the lines in voters
while line_voters:
    
    fields = line_voters.split("|")

    # Make sure district isn't blank
    if fields[0] != "":
        district = fields[0].rstrip()
        voter_increase = fields[1].rstrip()

    # Now see if the district exists in budget
    # and if it does, save the budget
    # increase to a variable as well

    #if district in budget:
    #    print(district, budget[district])
    #else:
    #    print(district + " not in budget")
    #    
    #if district in enroll:
    #    print(district, enroll[district])
    #else:
    #    print(district + " not in enroll")

    
    if district in budget and district in enroll:
        budget_increase = budget[district].rstrip()
        enrollment = str(enroll[district])
        print(district + "|" + voter_increase + "|" + budget_increase + "|" + enrollment)
        
    # Incrementing external while loop
    line_voters = f_voters.readline()

    
f_budget.close()
f_voters.close()


