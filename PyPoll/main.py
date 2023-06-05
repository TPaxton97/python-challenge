import csv

#Open election_data, set variables for, 
#and count up the values for each candidate and total votes cast
with open('PyPoll\\Resources\\election_data.csv', mode= 'r') as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    totalVotes = 0
    CCSVotes = 0
    DDVotes = 0
    RADVotes = 0
    winner = ""
    for line in csvFile:
        if line[2] == str("Charles Casper Stockham"):
            CCSVotes = CCSVotes + 1
            totalVotes = totalVotes + 1
        elif line[2] == str("Diana DeGette"):
            DDVotes = DDVotes + 1
            totalVotes = totalVotes + 1
        else:
            RADVotes = RADVotes + 1
            totalVotes = totalVotes + 1
    
    #Determine winner         
    if CCSVotes > DDVotes and CCSVotes > RADVotes:
        winner = "Charles Casper Stockham"
    if DDVotes > CCSVotes and DDVotes > RADVotes:
        winner = "Diana DeGette"
    if RADVotes > CCSVotes and RADVotes > DDVotes:
        winner = "Raymon Anthony Doane"
    
    #Export text file with Election Results
electionResults = open("PyPoll\\Analysis\\election_results.text", 'w')
L = ["Election Results: \n",
    "--------------------------------------- \n",       
    'Total votes: ', str(totalVotes), "\n",
    "--------------------------------------- \n",       
    "Charles Casper Stockham: ", str("{:.3%}".format(CCSVotes/totalVotes)), "(", str(CCSVotes), ")", "\n",
    "Diana DeGette: ", str("{:.3%}".format(DDVotes/totalVotes)), "(", str(DDVotes), ")", "\n",
    "Raymon Anthony Doane: ", str("{:.3%}".format(RADVotes/totalVotes)), "(", str(RADVotes), ")", "\n",
    "--------------------------------------- \n",    
    "Winner: ", str(winner), "\n",
    "---------------------------------------"]
electionResults.writelines(L)

#open and read Election Results
electionResults = open("PyPoll\\Analysis\\election_results.text", 'r')
print(electionResults.read())


