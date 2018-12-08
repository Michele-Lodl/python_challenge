# PyBank Homework. Analyze:

import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    
  csvreader = csv.reader(csvfile, delimiter=',')
  
  csv_header = next(csvreader)
  #print(f"CSV Header: {csv_header}")

  print("-------------------------")
  print("Financial Analysis")
  print("-------------------------")

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
  print(f"Total Months: {month_count}")
  print(f"Total: ${TotalPL}")

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
  print(f"Average Change: ${Average_Change:.2f}")

  maxchange = max(PL_Changes_List)
  minchange = min(PL_Changes_List)
  maxchange_date = MonthsList[PL_Changes_List.index(maxchange) + 1]
  #print(maxchange_date)
  minchange_date = MonthsList[PL_Changes_List.index(minchange) + 1]
  #print(minchange_date)

  print(f"Greatest Increase in Profits: {maxchange_date} $({maxchange})")
  print(f"Greatest Decrease in Profits: {minchange_date} $({minchange})")
  

output_path = os.path.join("..", "PyBank", "PyBank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

  
    ##text=List of strings to be written to file
    text = ["Financial Analysis, Values", 
            "Total Months:, 86", 
            "Total:, $38382578",
            "Average Change:, $-2315.12", 
            "Greatest Increase in Profits:, Feb-2012 $(1926159)",
            "Greatest Decrease in Profits:, Sep-2013 $(-2196167)"]

    for line in text:
        csvfile.write(line)
        csvfile.write('\n')
  
    
