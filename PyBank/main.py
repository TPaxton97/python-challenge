import csv

from statistics import mean

#Open budget_data and determine no. of months in analysis
with open('PyBank\\Resources\\budget_data.csv', mode= 'r') as file:
    csvFile = csv.reader(file)
    next(csvFile, None)
    totalMonths = sum(1 for line in file)

#Determine total net profit within timeframe
with open('PyBank\\Resources\\budget_data.csv', mode= 'r') as file:
    csvFile = csv.reader(file)
    total = 0
    next(csvFile, None)
    for lines in csvFile:
        total += int(lines[1])

#Determine average change of profit/loss in timeframe, 
#greatest increase and greatest decrease with corresponding months  
with open('PyBank\\Resources\\budget_data.csv', mode= 'r') as file:
    csvFile = csv.reader(file)
    profitLossesList = []
    profitChangeList = []
    monthChangeList = []
    next(csvFile, None)
    for line in csvFile:
        profitLossesList.append(int(line[1]))
        monthChangeList.append(line[0])
    monthChangeList.pop(0)
    
    profitChangeList= [profitLossesList[elem+1] - profitLossesList[elem] 
                            for elem in range(len(profitLossesList)-1)]
    averageChange = mean(profitChangeList)

greatestIncrease = max(profitChangeList)
greatestIncreaseIndex = profitChangeList.index(greatestIncrease)
greatestIncreaseMonth = monthChangeList[greatestIncreaseIndex]

greatestDecrease = min(profitChangeList)
greatestDecreaseIndex = profitChangeList.index(greatestDecrease)
greatestDecreaseMonth = monthChangeList[greatestDecreaseIndex]

#Export text file with Financial Analysis
financialAnalysis = open('PyBank\\Analysis\\financial_analysis.txt', 'w')
L = ["Financial Analysis: \n" ,
    "--------------------------------------- \n",
    'Total months: ', str(totalMonths), "\n",
    'Total: $', str(total), "\n",
    'Average Change: $', str(averageChange), "\n",
    'Greatest Increase in Profits: ', str(greatestIncreaseMonth), "($", str(greatestIncrease), ") \n",
    'Greatest Decrease in Profits: ', str(greatestDecreaseMonth), "($", str(greatestDecrease), ")"]
financialAnalysis.writelines(L)
financialAnalysis.close()

#open and read Financial Analysis
financialAnalysis = open('PyBank\\Analysis\\financial_analysis.txt', 'r')
print(financialAnalysis.read())
        

