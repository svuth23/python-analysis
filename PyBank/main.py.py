import os
import csv
print("Financial Analysis")
print("--------------------------")
csvpath = os.path.join("C:\\Users\\swapn\\OneDrive\\Desktop\\Starter_Code (2)\\Starter_Code\\PyBank\\Resources\\budget_data.csv")

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    #to print header row below code
    #print(f"CSV Header: {csv_header}")

#calculate the total months and total profit/losses
    for row in csvreader:
        total_months += 1
        profit_loss = int(row[1])
        total_profit_loss += profit_loss

        # Calculate the profit/loss change
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

            # Check for the greatest increase and greatest decrease
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")



# Define the file path for the output text file
output_file = os.path.join("C:\\Users\\swapn\\\OneDrive\\Desktop\\Starter_Code (2)\\Starter_Code\\PyBank","analysis","financial_analysis.txt")

# Write the results to the text file
with open(output_file, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------\n")
    textfile.write(f"CSV Header: {csv_header}\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total Profit/Loss: ${total_profit_loss}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
print(f"Results written to {output_file}")
