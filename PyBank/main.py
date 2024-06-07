import os
import csv

# --------------------------------------------------------------------------------------

# Path to collect data from this project's Resources folder
budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

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

# Function that calculates & outputs financial analysis per row in the data file
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


# --------------------------------------------------------------------------------------

# Output financial analysis results

print(f"{results['num_months']}")
print(f"{results['net_profit_loss']}")
print(f"{results['average_change']}")
print(f"Greatest increase {results['greatest_increase_date']} {results['greatest_increase']} ")
print(f"Greatest decrease {results['greatest_decrease_date']} {results['greatest_decrease']} ")