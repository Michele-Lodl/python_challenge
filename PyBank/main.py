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
  #MonthsList = []
  #TotalPL = 0
  #ProfitLossList = []
  
  month_counter = 0 
  Total_PL = 0
  PL_Changes_List=[]
  PL_Changes_Sum= 0
  for row in csvreader:
    month_counter += 1
    Total_PL += int(row[1])
    Test_Second_Row_PL_Value= int((row + 1)[1])
    print(Test_Second_Row_PL_Value)
    #change = int((row + 1)[1])) - int(row[1])
    #PL_Changes_List.append(change)

    #Date = str(row[0])
    #MonthsList.append(Date)
    #Months_Profit_Losses = int(row[1])
    # print(row[1])
    #ProfitLossList.append(Months_Profit_Losses)
    #TotalPL = TotalPL + Months_Profit_Losses
    
    #Month_Value = int(row[1])
    #for i in range(1,month_counter):
      #Total_PL = Month_Value 
      #Total_PL =+ Month_Value + Month_Value[i+1]
      #Total_PL += int(row[1])

  #month_count = (len(MonthsList))
  #print(month_count)

  #New prints
  print(month_counter)
  print(Total_PL)
  #print(PL_Changes_Sum)

  #The average change in "Profit/Losses" between months over the entire period
 # PL_Changes_List=[]
  #PL_Changes_Sum= 0
  #for i in range(1,len(month_counter):
    #change = int(ProfitLossList[i])-int(ProfitLossList[i-1])
    #PL_Changes_List.append(change)
    #PL_Changes_Sum = PL_Changes_Sum + change
  #print(PL_Changes_Sum)

  #Average_Change = PL_Changes_Sum/len(PL_Changes_List)
  #print(f"The average change is {Average_Change} dollars.")

  #maxchange = max(PL_Changes_List)
  #minchange = min(PL_Changes_List)
  #maxchange_date = MonthsList[PL_Changes_List.index(maxchange) + 1]
  #print(maxchange_date)
  #minchange_date = MonthsList[PL_Changes_List.index(minchange) + 1]
  #print(minchange_date)

  #print(f"The greatest increase in profits totaled {maxchange} dollars on {maxchange_date}.")
  #print(f"The steepest decrease in profits totaled {minchange} dollars on {minchange_date}.")
  

print("The End")

# DONE.The total number of months included in the dataset
# DONE.The total net amount of "Proft/Losses" over the entire period
# DONE. The average change in "Profit/Losses" between months over the entire period
# DONE. The greatest increase in profits (date and amount) over the entire period
# DONE. The greatest decrease in losses (date and amount) over the entire period
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# something about both scripts working on both files. 