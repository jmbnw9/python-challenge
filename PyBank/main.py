import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

#find total number of months included in datset
    row_count = sum(1 for row in csvreader)
#find total profit/losses
    net_total = sum(1 for row in csvreader)


print ("Financial Analysis")
print ("-------------------------")
print (f"Total Months : {row_count}")
print (f"Total : {net_total}")

