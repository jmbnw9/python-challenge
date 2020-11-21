import os
import csv

# Path to the dataset in resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

#create import lists for data
Row_count = []
Net_total = []

# Import and read the csv file
with open(csvpath,"r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        Row_count.append(str(row[0]))
        Net_total.append(int(row[1]))

# Find the total number of months
total_months = len(Row_count)

# Find the net total of profit/losses over entire period
net_profit_loss= 0

for x in Net_total:
    net_profit_loss = net_profit_loss + x

# Calculate the changes of the profit/losses over the entire period
average_monthly_change = []
previous_month_amount = 0

for x in range(len(Net_total)):
    if x == 0:
        previous_month_amount = Net_total[x]
    else:
        monthly_change = Net_total[x] - previous_month_amount
        average_monthly_change.append(monthly_change)
        previous_month_amount = Net_total[x]

#Print the average of the changes of the profit/losses

length = len(average_monthly_change)
total = sum(average_monthly_change)
profit_loss_average = total / length
print(profit_loss_average)

# Find the greatest increase & decrease in dataset
month_greatest_increase = ''
amount_greatest_increase = 0
month_greatest_decrease = ''
amount_greatest_decrease = 0

for x in range(len(average_monthly_change)):
    if average_monthly_change[x] > amount_greatest_increase:
        amount_greatest_increase = average_monthly_change[x]
        month_greatest_increase = Row_count[x+1]
    elif average_monthly_change[x] < amount_greatest_decrease:
        amount_greatest_decrease = average_monthly_change[x]
        month_greatest_decrease = Row_count[x+1]

#Print all the results to terminal
print(f"Financial Analysis")
print(f"------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${profit_loss_average}")
print(f"Greatest Increase in Profits: {month_greatest_increase} for (${amount_greatest_increase})")
print(f"Greatest Decrease in Profits: {month_greatest_decrease} for (${amount_greatest_decrease})")

output_file = os.path.join("Results.txt")

with open(output_file, "w", newline= "") as datafile:

    datafile.write("Financial Analysis\n")
    datafile.write("------------------\n")
    datafile.write(f"Total Months: {total_months}\n")
    datafile.write(f"Total: ${net_profit_loss}\n")
    datafile.write(f"Average Change: ${profit_loss_average}\n")
    datafile.write(f"Greatest Increase in Profits: {month_greatest_increase} for (${amount_greatest_increase})\n")
    datafile.write(f"Greatest Decrease in Profits: {month_greatest_decrease} for (${amount_greatest_decrease})\n")
   









