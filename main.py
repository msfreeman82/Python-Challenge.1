import os

import csv


#lists of variables


# retreiving the path to the file to work on 
csv_file = os.path.join("PyBank", "Resources", "budget_data.csv")
total_months = 1
total_net= 0
average_1 = 0
# read the file into csv_read
with open(csv_file, 'r') as csv_read:
    csv_read_1 = csv.reader
    header = next(csv_read_1)
    firstrow=next(csv_read_1)
    total_net = total_net + int(firstrow[1])
    previous_net = total_net

# Add total Months
    for row in csv_read_1:
        total_months = total_months + 1

 # retreiving the net total amoun of profit/losses
        total_net = total_net + int(row[1])
        netchange = int(row[1]) - previous_net
        previous_net = int(row[1])

# retreiving the average
        sum((total_months)/len(int(total_net)))

        print(sum)


# Test your function with the following:

               


