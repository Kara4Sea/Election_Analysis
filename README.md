# Election Analysis 
An analysis of election results using Python
## Overview of Election Audit
The purpose of this election audit analysis is to further insight on the congressional vote by adding information about voting by county to the candidate results. Specifically, adding information regarding the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest voter turnout.
## Election-Audit Results

### Image below reflects all candidate and county results as discussed in bullet points:
![Election_results_image](https://user-images.githubusercontent.com/110419577/192631471-46f0001d-9a59-46f2-8769-92cc11b6230c.png)


* **How many votes were cast in this congressional election?**   
A total of 369,711 votes were cast in the congressional election.

* **Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**  
Denver County saw the largest turnout of votes at 306,055 votes, making up 82.8% of the total votes. Jefferson county had 38,855 votes, making up 8% of the total votes. Lastly, Arapahoe had 24,801 votes, making up 6.7% of the total votes.
* **Which county had the largest number of votes?**  
The county with the largest voter turnout was Denver. Denver county saw a total of 306,055 votes, which made up 82.8% of the turnout.
* **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**  
Diana DeGette, the winner of the election, received a total of 272,892 votes, which made up 73.8% of the total votes. Charles Casper Stockham received 85,213 votes, making up 23.0% of the total votes. Raymon Anthony Doane received 11,606 votes, making up 3.1% of the total votes.
* **Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**  
Diana DeGette won the election. She received a total of 272,892 votes, which made up 73.8% of the total votes.
## Election-Audit Summary
### Script Performance
This election-audit script proved to be useful in determining the outcome of the election. It calculated the total votes, breakdown by county of number of votes, breakdown by county by percentage of votes, breakdown of candidate by number of votes, breakdown of candidate by percentage of votes. It also detailed the county with the largest turnout, along with the winning candidate, their winning vote count and winning percentage count. I believe this script can be reutilized for future elections to make the process of determining the winner and the county with largest turnout more efficient.

### Script Reutilization
To reutilize, it would be best to use a csv file with similar formatting when creating a path to import the data. This would ensure the report is relating the correct values to the correct variables. Code used to create a path to import data is as follows. This would need to be updated to reflect the new election's csv file to pull data from.

`file_to_load = os.path.join("resources", "election_results.csv")`

We would also want to create a new file to save to, so that we can keep the original intact. Code used to create a path to export data is as follows. This would need to be updated to reflect a new txt file to save data for the new election.

`file_to_save = os.path.join("analysis", "election_analysis.txt")`

It seems likely the csv file formatting for a new election's data would be different. If this is the case, we would need to update the script where we extract the candidate name and county name to assign the proper column number. For example, if the candidate name is in a row other than 2, and the county name is in a row other than 1. We would need to change the assigned rows in the code below.

        `# Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]`
