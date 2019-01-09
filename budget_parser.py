import re
import subprocess

pattern = re.compile(r'"(.*?),(.*?)"', flags=re.DOTALL)

f = open("PerPupilAllExpenditures.csv", "rt")

data = f.read()

all_num = []

found = re.findall(pattern, data)

if found:

    for each in found:

        no_comma = each[0] + each[1] + "|"
        all_num.append(no_comma)

    # Extract the headers
    header_info = subprocess.getoutput('less PerPupilAllExpenditures.csv | head -1 | cut -d "," -f 2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21')
    headers = header_info.split(',')
    
    # Extract the school district from the csv
    info = subprocess.getoutput('less PerPupilAllExpenditures.csv | cut -d "," -f 2')
    districts = info.split('\n')
    
    # counter - starting at 1 to avoid header
    j = 1

    # print header
    for each in headers:
        print(each + "|", end="")
    print()

    # Print comma stripped budget as pipe delimited

    # Trying and except because of out of bounds
    # issues that need to be circumvented

    try:
        for i in range(0, len(all_num)-18, 17):
            print(districts[j] + "|", end="")
            print(all_num[i], end="")
            print(all_num[i+1], end="")
            print(all_num[i+2], end="")
            print(all_num[i+3], end="")
            print(all_num[i+4], end="")
            print(all_num[i+5], end="")
            print(all_num[i+6], end="")
            print(all_num[i+7], end="")
            print(all_num[i+8], end="")
            print(all_num[i+9], end="")
            print(all_num[i+10], end="")
            print(all_num[i+11], end="")
            print(all_num[i+12], end="")
            print(all_num[i+13], end="")
            print(all_num[i+14], end="")
            print(all_num[i+15], end="")
            print(all_num[i+16], end="")
            print(all_num[i+17])
            j = j + 1

    except:
        j = 0
        
f.close()
