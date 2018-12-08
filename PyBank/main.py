# PyBank Homework. Analyze:

import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:

    
  csvreader = csv.reader(csvfile, delimiter=',')
  # HELP: don't really get next and what is happening here. 
  csv_header = next(csvreader)
  print(f"CSV Header: {csv_header}")

  # The total net amount of "Profit/Losses" over the entire period
  # The total net amount of "Proft/Losses" over the entire period

  MonthsList = []
  TotalPL = 0
  ProfitLossList = []
  PL_Changes_List=[]
  PL_Changes_Sum= 0
  for row in csvreader:
    Date = str(row[0])
    MonthsList.append(Date)

    Months_Profit_Losses = int(row[1])
     #print(row[1])
    ProfitLossList.append(Months_Profit_Losses)
    TotalPL = TotalPL + Months_Profit_Losses

  month_count = (len(MonthsList))
  print(month_count)
  print(TotalPL)

  #print(PL_Changes_Sum)

  #The average change in "Profit/Losses" between months over the entire period
  PL_Changes_List=[]
  PL_Changes_Sum= 0
  for i in range(1,month_count):
    change = int(ProfitLossList[i])-int(ProfitLossList[i-1])
    PL_Changes_List.append(change)
    PL_Changes_Sum = PL_Changes_Sum + change
  #print(PL_Changes_Sum)

  Average_Change = PL_Changes_Sum/len(PL_Changes_List)
  print(f"The average change is {Average_Change} dollars.")

  maxchange = max(PL_Changes_List)
  minchange = min(PL_Changes_List)
  maxchange_date = MonthsList[PL_Changes_List.index(maxchange) + 1]
  #print(maxchange_date)
  minchange_date = MonthsList[PL_Changes_List.index(minchange) + 1]
  #print(minchange_date)

  print(f"The greatest increase in profits totaled {maxchange} dollars on {maxchange_date}.")
  print(f"The steepest decrease in profits totaled {minchange} dollars on {minchange_date}.")
  

print("The End")

# DONE.The total number of months included in the dataset
# DONE.The total net amount of "Proft/Losses" over the entire period
# DONE. The average change in "Profit/Losses" between months over the entire period
# DONE. The greatest increase in profits (date and amount) over the entire period
# DONE. The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# something about both scripts working on both files. 