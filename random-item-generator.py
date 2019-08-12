import csv

with open('spreadsheet.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    items = {}
    counter = 1

    for line in csv_reader:
        items[counter] = line
        counter += 1
    
    print(items)