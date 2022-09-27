# Election Analysis 
An analysis of election results using Python
## Overview of Election Audit
The purpose of this election audit analysis is to further insight on the congressional vote by adding information about voting by county to the canddidate results. Specically, adding information regarding the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest voter turnout.
## Election-Audit Results

### Image below relfects all candidate and county results  
![Election_results_image](https://user-images.githubusercontent.com/110419577/192631471-46f0001d-9a59-46f2-8769-92cc11b6230c.png)


* **How many votes were cast in this congressional election?**   
A total of 369,711 votes were cast in the congretional election.

* **Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**  
Denver county saw the largest turnout of votes at 306,055 votes, making up 82.8% of the total votes. Jefferson county had 38,855 votes, making up 8% of the total votes. Lastly, Arapahoe had 24,801 votes, making up 6.7% of the total votes.
* **Which county had the largest number of votes?**  
The county with the largest voter turnout was Denver. Denver county saw a total of 306,055 votes, which made up 82.8% of the turnout.
* **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**  
Diana DeGette, the winner of the election, received a total of 272,892 votes, which made up 73.8% of the total votes. Charles Casper Stockham received 85,213 votes, making up 23.0% of the total votes. Raymon Anthony Doane recived 11,606 votes, making up 3.1% of the total votes.
* **Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**  
Diana DeGette won the election. She received a total of 272,892 votes, which made up 73.8% of the total votes.
## Election-Audit Summary
This election-audit script proved to be useful in determining the outcome of the election. It calculated the total votes, breakdown by county of number of votes, breakdown by county by percentage of votes, breakdown of candidate by number of votes, breakdown of candidate by percentage of votes. It also detailed the County with the largest turnout, along with the winning candide along with their winning vote coun and winning percentage count. I believe this script can be reutilized for future election to make the process of determining the winner and the county with largest turnout more efficient.

To reutilize, we would require a csv file with similar formatting to use when adding a variable to load file from a path and ensure this is updated on each line needed. We would also want to creat a new file to save to so that we can keep the original intact, and ensure that this is updated on each line needed. If the formating looks different on a future csv file, we would need to update the script where we extract the candidate name and county name to the proper column number.
