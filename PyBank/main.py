# PyBank Homework. Analyze:

#read_cvs.py class
# First we'll import the os module. The os module means that we can create file paths across operating systems. 
# This module is especially important if you want to make your programs platform-independent. os figures out which sysytem on and runs based on that
# i.e. it allows the program to be written such that it will run on Linux as well as Windows without any problems and without requiring changes
import os

# Module (aka toolbox that has a tool) for reading CSV files
import csv

#HELP. do wn directory? The path join starts from where this file that I am typing in is located 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Using class Method 2: Improved Reading using CSV module
# "with this file path open this file as a csv"
# using newline to accomate reading across all os' some interpret them differently

# ML FYI, this was what was in class. mine did not run when I had new line: with open(csvpath, newline='') as csvfile:
with open(csvpath) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Best practice to check to see if reader worked by printing. Will know by seeing "cvs.reader object at...blah, blah, blah. Then # out. 
    # print(csvreader)

    # Read the header row first (skip this step if there is no header. Print it the header after the hard coded text CSV header.)
    # HELP: don't really get next and what is happening here. 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    # Look for each row of data. Do something if the desired call is found; do somethign else if not
    # Read each row of data , iteratate over something 
    

    # The total net amount of "Profit/Losses" over the entire period
    MonthsList = []
    TotalPL = 0
    ProfitLossList = []

    for row in csvreader:
      #This tells the computer to look at the first column for the variable I called "Date"
      #Trying to create a list with the months 
      Date = str(row[0])
      MonthsList.append(Date)

      #This tells the computer to look at the second column for the variable I called "Months_Profit_Losses" and casted as an integer 
      Months_Profit_Losses = int(row[1])
      # print(row[1])
      ProfitLossList.append(Months_Profit_Losses)
      TotalPL = TotalPL + Months_Profit_Losses

    #This is me attempting to find the changes MoM for profit/loss
    #need to tell it to look at two variables from row 1 and 2 in the second column 

    month_count = (len(MonthsList))
    print(month_count)
    print(TotalPL)


    PL_Changes_List=[]
    PL_Changes_Sum= 0
    for i in range(1,len(ProfitLossList)):
      change = int(ProfitLossList[i])-int(ProfitLossList[i-1])
      PL_Changes_List.append(change)
      PL_Changes_Sum = PL_Changes_Sum + change
    #print(PL_Changes_Sum)
    Average_Change = PL_Changes_Sum/len(PL_Changes_List)
    print(Average_Change)

    print("The End")
    # DONE.The total number of months included in the dataset
    # DONE.The total net amount of "Proft/Losses" over the entire period
    # DONE. The average change in "Profit/Losses" between months over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
    # In addition, your final script should both print the analysis to the terminal and export a text file with the results.
    # WIP - both analysis to terminal? How do I know the book closed?