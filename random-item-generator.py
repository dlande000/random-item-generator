import csv
import random

print("Enter a file path:")
file_path = raw_input()

with open(file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    items = {}
    counter = 1

    for line in csv_reader:
        if len(line) == 1:
            items[counter] = line[0]
        else:
            items[counter] = line
        counter += 1
    
    print(items[random.randint(1,len(items))])