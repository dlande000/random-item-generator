import csv
import random
import time

def random_item_generator ():
    print("Enter a file path including the .csv extension:")
    file_path = raw_input()

    if (file_path[-3:] != "csv"):
        print("Please select a .csv file.")
        time.sleep(.5)
        random_item_generator()
    else:
        generate_title(file_path)
    
def generate_title (file_path, items = {}):
    if len(items) == 0:
        counter = 1
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                if len(line) == 1:
                    items[counter] = line[0]
                else:
                    items[counter] = line
                counter += 1

    print(items[random.randint(1,len(items))])
    time.sleep(.5)
    print("Generate new title? (Y/N)")
    answer = raw_input().lower()

    if answer == "n":
        return
    elif answer == "y":
        generate_title(file_path, items)
    else:
        print("Please use Y for Yes or N for No.")

random_item_generator()