import csv
import random

def random_item_generator ():
    print("Enter a file path:")
    file_path = raw_input()

    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        items = {}
        counter = 1

        for line in csv_reader:
            items[counter] = line[0]
            counter += 1
        
        print(items[random.randint(1,len(items))])

random_item_generator()