# Import Dependencies
import os
import csv

# Specify Filepath
csv_path = os.path.join("budget_data.csv")
output_path = os.path.join("output.txt")

# Define Starting Variables
total_months = 0
net_pl = 0
total_months_two = 0
first_iteration = True
previous_pl = 0
current_pl = 0
difference_pl = 0
difference_pl_list = []
avg_change = 0
greatest_increase_date = 0
greatest_increase_amount = 0
greatest_decrease_date = 0
greatest_decrease_amount = 0

# Open CSV Reader
with open(csv_path,newline = '') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader,None)
# Loop through each row to count total months
    for row in csv_reader:
        total_months += 1
        net_pl += int(row[1])
# If-Statement starts calculations on the second iteration. The first iteration has nothing to subtract from
        if first_iteration:
            first_iteration = False
        else:
            current_pl = int(row[1])
            difference_pl = current_pl - previous_pl
            difference_pl_list.append(difference_pl)
# If-Statement to find greatest increase and decrease in profit/losses
            if difference_pl > greatest_increase_amount:
                greatest_increase_amount = difference_pl
                greatest_increase_date = row[0]
            elif difference_pl < greatest_decrease_amount:
                greatest_decrease_amount = difference_pl
                greatest_decrease_date = row[0]
            else:
                pass
        previous_pl = int(row[1])
# Calculates Average Change
avg_change = int(sum(difference_pl_list) / (total_months-1))

# Generate Output
output_data = (
        f"\nFinancial Analysis"
        f"\n------------------"
        f"\nTotal Months: {total_months}"
        f"\nTotal: ${net_pl}"
        f"\nAverage Change: ${avg_change}"
        f"\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})"
        f"\nGreatest Decrease in Profits: {greatest_decrease_date} $({greatest_decrease_amount})"
        )
print(output_data)

# Exports output to text file
with open(output_path,"w",newline = '') as txt_output_file:
	txt_output_file.write(output_data)