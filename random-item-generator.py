import csv
import random

with open('spreadsheet.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    items = {}
    counter = 1

    for line in csv_reader:
        items[counter] = line[0]
        counter += 1
    
    print(items[random.randint(1,len(items))])