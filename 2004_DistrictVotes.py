#! /usr/bin/env python3

# For the 2004 .txt file, create a dictionary
# where the key is the district, and the value
# In the txt files, comma delimited
# field 1 = dob, field 2 is school district (if not empty), and field 3 is a X if they voted in the general election for that year

f = open("election2004_18or19.txt", "rt")

line = f.readline()
total = {}

while line:
    fields = line.split(",")
    dob = fields[0]
    school_district = fields[1]
    voted = fields[2]
    
    # if this person voted (aka has an X not an None)
    if voted:
        
        # tally the total number of votes so far for the
        # school_district in a dictionary
        if school_district in total:
            total[school_district] += 1
        else:
            total[school_district] = 1

    line = f.readline()

f.close()

# Print a pipe delimited file to stdout with the district and total
# young voters

for eachDist in total:
    print(eachDist + "|" + str(total[eachDist]))
