#! /usr/bin/env python3


# HAVING ISSUES - NOT GETTING ALL OF THE COUNTIES!
# 
# Open files of raw number of 18 or 19 year old
# voters in each school district
file2004 = open("2004_DistrictVotes.txt", "rt")
file2008 = open("2008_DistrictVotes.txt", "rt")

# Dictionary with the key being the county
# and the value being the percent 2008/2004
percent_increase = {}

# Make initial dictionary just with
# 2008 values

# Read the first line of 2008                                           
line_08 = file2008.readline()
while line_08:
    fields08 = line_08.split("|")
    
    dist08 = fields08[0]
    numVoters08 = fields08[1]

    # Escaping the blank school district
    if dist08:
        percent_increase[dist08] = numVoters08

    line_08 = file2008.readline()


# Now average in the 2004 raw nums
line_04 = file2004.readline()

while line_04:
    fields04 = line_04.split("|")

    dist04 = fields04[0]
    numVoters04 = fields04[1]

    # if the district isn't blank and exists in
    # the dictionary already
    if dist04 and dist04 in percent_increase:

        # Divide the contents of the dictionary
        # at that point by the 04 raw data
        raw08 = int(percent_increase[dist04])
        raw04 = int(numVoters04)
        percentage = (raw08/raw04)

        # Replace value at that point with the percentage
        percent_increase[dist04] = percentage

    line_04 = file2004.readline()

# Debugging
# print("DEBUG:")
# print(percent_increase)

# Print results
for each in percent_increase:
    
    percent = str(percent_increase[each]).rstrip()
    print(each + "|" + percent)

file2004.close()
file2008.close()
    
