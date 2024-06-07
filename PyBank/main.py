import os
import csv

# --------------------------------------------------------------------------------------

# Path to collect data from this project's Resources folder
budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Path to finanaical analysis results file
financial_analysis_txt = os.path.join("PyBank", "analysis", "financial_analysis.txt")

# --------------------------------------------------------------------------------------

# Intermediate data store for financial analysis results
results = {
    "num_months":           0,
    "net_profit_loss":      0.0,
    "prev_profit_loss":     0.0,
    "net_change":           0.0,
    "average_change":       0.0,

    "greatest_increase":    0.0,
    "greatest_decrease":    0.0,
    "greatest_increase_date":   None,
    "greatest_decrease_date":   None
}

# --------------------------------------------------------------------------------------

# Function that calculates the financial analysis on a per-row (monthly) basis
def analyse_datarow(datarow, results):
    # Interpret / retrieve data values
    date = datarow[0]
    this_month_profit_loss = float(datarow[1])
    # Count the number of months (each datarow is monthly)
    results['num_months'] += 1
    # Update the net profit/loss total
    results['net_profit_loss'] += this_month_profit_loss

    # Keep track of changes to net profit/loss by month
    if results['num_months'] == 1:
        results['prev_profit_loss'] = 0.0
    else:
        # Determine month-on-month profit/loss change, and update the average change to date
        change = this_month_profit_loss - results['prev_profit_loss']
        results['net_change'] += change
        results['average_change'] = results['net_change'] / (results['num_months']-1)
        # Track greatest increase value & date
        if (results['greatest_increase'] < change):
            results['greatest_increase_date'] = date
            results['greatest_increase'] = change
        # Track greatest decrease value & date
        if (results['greatest_decrease'] > change):
            results['greatest_decrease_date'] = date
            results['greatest_decrease'] = change

    # Update the reference value for calculating the next change
    results['prev_profit_loss'] = this_month_profit_loss

# --------------------------------------------------------------------------------------

# Read in and process the CSV data file
with open(budget_data_csv, 'r') as csvfile:

    # Parse the data fields based on comma delimiters
    csvreader = csv.reader(csvfile, delimiter=',')

    # Consume (skip) the data file header row
    header = next(csvreader)

    # Iterate over the data
    for datarow in csvreader:
        analyse_datarow(datarow, results)

    # Close the file handle
    csvfile.close()


# --------------------------------------------------------------------------------------

# Format then output financial analysis results

str_total_months = f"Total months: {results['num_months']}"
str_total = f"Total: ${results['net_profit_loss']:.0f}"
str_average_change = f"Average Change: ${results['average_change']:.2f}"
str_greatest_increase_details = f"Greatest Increase in Profits: {results['greatest_increase_date']} (${results['greatest_increase']:.0f})"
str_greatest_decrease_details = f"Greatest Decrease in Profits: {results['greatest_decrease_date']} (${results['greatest_decrease']:.0f})"

# Output to the console...

print("Financial Analysis")
print("----------------------------")
print(str_total_months + "\n")
print(str_total + "\n")
print(str_average_change + "\n")
print(str_greatest_increase_details + "\n")
print(str_greatest_decrease_details + "\n")

# ..and to a file.

with open(financial_analysis_txt, 'w') as txtfile:
    # Output results header
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    # Output results statistics
    txtfile.write(str_total_months + "\n\n")
    txtfile.write(str_total + "\n\n")
    txtfile.write(str_average_change + "\n\n")
    txtfile.write(str_greatest_increase_details + "\n\n")
    txtfile.write(str_greatest_decrease_details + "\n\n")
    # Close the file handle
    txtfile.close()

# --------------------------------------------------------------------------------------