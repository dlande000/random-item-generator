import csv
import random

def random_item_generator (file_path):
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        items = {}
        counter = 1

        for line in csv_reader:
            items[counter] = line[0]
            counter += 1
        
        print(items[random.randint(1,len(items))])

random_item_generator('spreadsheet.csv')