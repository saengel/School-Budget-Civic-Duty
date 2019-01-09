# Sarah Engel
# January, 2018
# Professor Broder
# Linux Programming and Scripting

# QUESTION: Is there a relationship between school district funding increases and percent young voter participation increases in the state of Ohio?

# Note: PerPupilExpenditures.xlsx.aspx had to be manually downloaded as a csv since the .aspx prevented us from modifying it any other way (as did district_size_2004.csv)

all: graph.pdf

clean:
	rm rawVoterData/raw04_1_22.txt rawVoterData/raw04_23_44.txt rawVoterData/raw04_45_66.txt rawVoterData/raw04_67_88.txt rawVoterData/raw08_1_22.txt rawVoterData/raw08_23_44.txt rawVoterData/raw08_45_66.txt rawVoterData/raw08_67_88.txt election2008_18or19.txt election2004_18or19.txt 2004_DistrictVotes.txt 2008_DistrictVotes.txt clean_PerPupilExpenditures.txt 2000_budget.txt 2004_budget.txt budget_increase_per_dist.txt percent_voters_by_dist.txt twelfthGradeDistSize.txt final_data.txt graph.pdf

# Raw Voter Data By DISTRICT 
# Reduced into files with the DOB, City school district and
# whether or not they participated in the 2004 election
rawVoterData/raw04_1_22.txt: OhioStateVoterFiles/SWVF_1_22.txt.gz
	zcat OhioStateVoterFiles/SWVF_1_22.txt.gz | cut -d "," -f 8,30,56 > rawVoterData/raw04_1_22.txt

rawVoterData/raw04_23_44.txt: OhioStateVoterFiles/SWVF_23_44.txt.gz
	zcat OhioStateVoterFiles/SWVF_23_44.txt.gz | cut -d "," -f 8,30,56 > rawVoterData/raw04_23_44.txt

rawVoterData/raw04_45_66.txt: OhioStateVoterFiles/SWVF_45_66.txt.gz
	zcat OhioStateVoterFiles/SWVF_45_66.txt.gz | cut -d "," -f 8,30,56 > rawVoterData/raw04_45_66.txt

rawVoterData/raw04_67_88.txt: OhioStateVoterFiles/SWVF_67_88.txt.gz
	zcat OhioStateVoterFiles/SWVF_67_88.txt.gz | cut -d "," -f 8,30,56 > rawVoterData/raw04_67_88.txt

# Repeating the same process for the 2008 election
rawVoterData/raw08_1_22.txt: OhioStateVoterFiles/SWVF_1_22.txt.gz
	zcat OhioStateVoterFiles/SWVF_1_22.txt.gz | cut -d "," -f 8,30,71 > rawVoterData/raw08_1_22.txt

rawVoterData/raw08_23_44.txt: OhioStateVoterFiles/SWVF_23_44.txt.gz
	zcat OhioStateVoterFiles/SWVF_23_44.txt.gz | cut -d "," -f 8,30,71 > rawVoterData/raw08_23_44.txt

rawVoterData/raw08_45_66.txt: OhioStateVoterFiles/SWVF_45_66.txt.gz
	zcat OhioStateVoterFiles/SWVF_45_66.txt.gz | cut -d "," -f 8,30,71 > rawVoterData/raw08_45_66.txt

rawVoterData/raw08_67_88.txt: OhioStateVoterFiles/SWVF_67_88.txt.gz
	zcat OhioStateVoterFiles/SWVF_67_88.txt.gz | cut -d "," -f 8,30,71 > rawVoterData/raw08_67_88.txt

# Creating a composite file grepping on birthdays (had to be born in either 89 or 90 to be 18 or 19
# in the 2008 general election) of raw voter data reduced to only the young voters
election2008_18or19.txt: rawVoterData/raw08_1_22.txt rawVoterData/raw08_23_44.txt rawVoterData/raw08_45_66.txt rawVoterData/raw08_67_88.txt
	cat rawVoterData/raw08_1_22.txt | grep -e "1989-" -e "1990-"> election2008_18or19.txt
	cat rawVoterData/raw08_23_44.txt | grep -e "1989-" -e "1990-">> election2008_18or19.txt
	cat rawVoterData/raw08_45_66.txt | grep -e "1989-" -e "1990-">> election2008_18or19.txt
	cat rawVoterData/raw08_67_88.txt | grep -e "1989-" -e "1990-">> election2008_18or19.txt

# Creating a composite file grepping on birthdays (had to be born in either 85 or 86 to be 18 or 19     
# in the 2004 general election) of raw voter data reduced to only the young voters  
election2004_18or19.txt: rawVoterData/raw04_1_22.txt rawVoterData/raw04_23_44.txt rawVoterData/raw04_45_66.txt rawVoterData/raw04_67_88.txt
	cat rawVoterData/raw04_1_22.txt | grep -e "1985-" -e "1986-"> election2004_18or19.txt
	cat rawVoterData/raw04_23_44.txt | grep -e "1985-" -e "1986-">> election2004_18or19.txt
	cat rawVoterData/raw04_45_66.txt | grep -e "1985-" -e "1986-">> election2004_18or19.txt
	cat rawVoterData/raw04_67_88.txt | grep -e "1985-" -e "1986-">> election2004_18or19.txt

# Use a python script to produce a pipe-delimited file by school district
# with a raw total number of young voters in 2004
2004_DistrictVotes.txt: election2004_18or19.txt
	python3 ./2004_DistrictVotes.py > 2004_DistrictVotes.txt

# Use a python script to produce a pipe-delimited file by school district                                                           
# with a raw total number of young voters in 2004   
2008_DistrictVotes.txt: election2008_18or19.txt
	python3 ./2008_DistrictVotes.py > 2008_DistrictVotes.txt

# Data cleansing the PerPupilAllExpenditures.csv because it's a comma delimited file with commas
# inside the numeric field as well, so I cannot parse the data. So, this Python script
# uses regexes to clean the csv removing the commas from the numeric field. 
clean_PerPupilExpenditures.txt: PerPupilAllExpenditures.csv
	python3 budget_parser.py > clean_PerPupilExpenditures.txt

# Then, on the clean data, extract a file of just the 2000 fiscal year
# spending by district
2000_budget.txt: clean_PerPupilExpenditures.txt
	cat clean_PerPupilExpenditures.txt | cut -d "|" -f 1,7 > 2000_budget.txt

# Then, on the clean data, extract a file of just the 2000 fiscal year                                                              
# spending by district  
2004_budget.txt: clean_PerPupilExpenditures.txt
	cat clean_PerPupilExpenditures.txt | cut -d "|" -f 1,11 > 2004_budget.txt

# Then, created a Python script to emit a pipe delimited file of the proportionate spending increase
# of FiscalYear2004/FiscalYear2000
budget_increase_per_district.txt: 2000_budget.txt 2004_budget.txt
	python3 budget_percent_increase.py > budget_increase_per_dist.txt

# Then, created a Python script to emit a pipe delimited file of the proportionate young voter increase                    
# of RawVoters2008/VoterCount2004 by district 
percent_voters_by_dist.txt: 2004_DistrictVotes.txt 2008_DistrictVotes.txt
	python3 percent_dist_votes.py > percent_voters_by_dist.txt

# School district sizes for graph
twelfthGradeDistSize.txt: district_size_2004.csv
	cat district_size_2004.csv | cut -d "," -f 3,18 > twelfthGradeDistSize.txt

# Final data - with only the overlapping counties
final_data.txt: percent_voters_by_dist.txt budget_increase_per_district.txt twelfthGradeDistSize.txt
	python3 final_percentages.py > final_data.txt

# Using the final data to generate a graph in matplotlib
graph.pdf: final_data.txt
	python3 graph.py > graph.pdf
