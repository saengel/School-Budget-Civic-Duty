#! /usr/bin/env python3

file2000 = open("2000_budget.txt", "rt")
file2004 = open("2004_budget.txt","rt")

# Read the first line (which is the header)
line_00 = file2000.readline()
line_04 = file2004.readline()

# Read the second and third line (which is the first info row)
line_00 = file2000.readline()
line_04 = file2004.readline()

line_00 = file2000.readline()
line_04 = file2004.readline()

print("line_00 is....")
print(line_00)

# Dictionary with the key being the county
# and the value being the percent 2004/2000
percent_increase = {}

while line_00 and line_04:
    fields00 = line_00.split("|")
    fields04 = line_04.split("|")

    print(fields00)
    
    dist00 = fields00[0]
    budget00 = int(fields00[1])

    dist04 = fields04[0]
    budget04 = int(fields04[1])
    
    # check the two districts are the same
    if dist00 and dist04 and dist00 == dist04:
        percent_increase[dist00] = (budget04/budget00)
        
    # Progress on to the next line
    line_00 = file2000.readline()
    line_04 = file2004.readline()


# Print
for each in percent_increase:
    print(each + "|" + str(percent_increase[each]))
file2000.close()
file2004.close()
