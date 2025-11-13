# Zachary Narcotta
# November 13, 2025 [start]
# November XX, 2025 [finish]
# COS226: Fall 2025
# hash.py
# [Hash Something Out] HW

import csv
CSV_FILE_NAME = "MOCK_DATA.csv"

# holds all of the different information related to data
class DataItem:
    def __init__(self, line):
        self.movieName = line[0]
        self.genre = line[1]
        self.releaseDate = line[2]
        self.director = line[3]
        revenue = line[4].split("$")
        self.revenue = float(revenue[1])
        self.rating = float(line[5])
        self.duration = int(line[6]) # in minutes
        self.production = line[7]
        self.quote = line[8]

class HashTable:
    pass

    # recommend: "handleCollision" function

def main():
    counter = 0
    try:
        with open(CSV_FILE_NAME, "r", newline = "", encoding = "utf8") as csvFile:
            reader = csv.reader(csvFile)
            for line in reader:
                if(counter == 0):
                    counter += 1
                    continue
                
                # length should be 9
                if(len(line) != 9):
                    print(f"{line} length is invalid! {len(line)} [should be 9]")
                    return
                
                # ensure every element in the line exists
                for element in line:
                    if(element == None):
                        print(f"{line} has an empty field!")
                        return
                dataItem = DataItem(line)
                print(line)
                # create DataItem from line
                # feed the appropriate field into hash function to get a 'key'
                # key % len(hashTable)
                # attempt to insert DataItem into hash table
                # handle collisions
                counter += 1
    except FileNotFoundError as ex:
        print(f"File does not exist in main!\nException: {ex}")
    except Exception as ex:
        print(f"Unknown exception in main!\nException: {ex}")

if(__name__ == "__main__"):
    main()