# Zachary Narcotta
# November 13, 2025 [start]
# November XX, 2025 [finish]
# COS226: Fall 2025
# hash.py
# [Hash Something Out] HW

import csv, time, math
CSV_FILE_NAME = "MOCK_DATA.csv"
HASH_TABLE_SIZE = 20000

# initialize hash tables
hashTableTitles = [None] * HASH_TABLE_SIZE
hashTableQuotes = [None] * HASH_TABLE_SIZE

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
        
    def __str__(self):
        return self.movieName

# attempts to insert dataItem into table[key], handles possible collisions
def addToTable(table, dataItem, key):
    # linear probing method
    # if(table[key] == None):
    #     table[key] = dataItem
    #     return 0
    
    # table[key] is already full ; collision!
    
    # return linearProbe(table, dataItem, key)

    # linked list method
    if(table[key] == None):
        table[key] = [dataItem]
        return 0
    
    # table[key] is already full ; collision!

    return linkedListHandling(table, dataItem, key)

# returns -1 if the item could not be inserted.
def linearProbe(table, dataItem, key):
    for i in range(key, len(table)):
        if(table[i] == None):
            table[i] = dataItem
            return 1
        
    for i in range(0, key):
        if(table[i] == None):
            table[i] = dataItem
            return 1
        
    return -1

def linkedListHandling(table, dataItem, key):
    table[key].append(dataItem)
    return 1

# converts each character in the string into its integer ASCII value
# sums them up, returns this value (modulo division applied later)
def asciiStringHash(stringData):
    total = 0
    for char in stringData:
        total += ord(char)
    return total

# multiply each key by a random number (0, 1), then multiply by the length of the table
# flooring the resulting value at the end
def multiplicationHash(table, stringData):
    k = asciiStringHash(stringData)
    a = 0.51869377 # randomly picked value where 0 < a < 1
    n = len(table)

    key = math.floor((n * ((k * a) % 1)))
    return key

# receives a key, groups key into groups of n, and sums them
def foldingHash(key, n):
    k = str(key)
    total = 0
    for i in range(0, len(k), n):
        total += int(k[i:i+n])

    return total

# iterates through a string, multiplying each character ascii value 
# by (small prime number (p) ^ num of iterations), modulo by a very large prime number (m)
def polynomialRollingHash(stringData):
    p = 53 # recommended prime for strings consisting of uppercase and lowercase characters
    m = (10**9) + 9 # commonly used large prime

    total = 0

    for i in range(len(stringData)):
        asciiVal = ord(stringData[i])
        power = p**i
        total += (asciiVal * power) % m

    return total

def midSquareHash(stringData):
    key = asciiStringHash(stringData)
    key *= key
    r = len(str(HASH_TABLE_SIZE))

    k = (key // 10) % key
    power = 1
    power = 10**r
    k = k % power

    return k

def reportTableStatistics(table, elapsed, collisionCount):
    wastedSlots = 0
    for i in range(len(table)):
        if(table[i] == None):
            wastedSlots += 1

    print(f"Wasted Space (unused slots): {wastedSlots}")
    print(f"Number of collisions during construction: {collisionCount}")
    print(f"Construction time: {elapsed:0.3f}s\n")
    return

def main():
    counter = 0
    
    # initialize collision counters
    titlesCollisions = 0
    quotesCollisions = 0

    # initialize amount of folds to use for folding hash
    foldCount = 4

    print("METHOD: MID-SQUARE HASH")
    print("COLLISION METHOD: LINKED LIST\n")
    try:
        with open(CSV_FILE_NAME, "r", newline = "", encoding = "utf8") as csvFile:
            start = time.time()
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
                
                # create DataItem from line
                movie = DataItem(line)
                
                # feed the appropriate field into hash function to get a 'key'
                # titleKey = asciiStringHash(movie.movieName)
                # hashIndex = titleKey % len(hashTableTitles)
                # titleKey = multiplicationHash(hashTableTitles, movie.movieName)
                # titleKey = foldingHash(titleKey, foldCount)
                # returnVal = addToTable(hashTableTitles, movie, hashIndex)
                # titleKey = polynomialRollingHash(movie.movieName) % len(hashTableTitles)
                # returnVal = addToTable(hashTableTitles, movie, titleKey)
                titleKey = midSquareHash(movie.movieName) % len(hashTableTitles)
                returnVal = addToTable(hashTableTitles, movie, titleKey)

                if(returnVal == -1):
                    print(f"{movie} could not be inserted into table.")
                elif(returnVal == 1): # collision happened
                    titlesCollisions += 1
                counter += 1
            end = time.time()
            elapsed = (end - start)
            print("TITLE TABLE STATISTICS")
            reportTableStatistics(hashTableTitles, elapsed, titlesCollisions)
            
        counter = 0
        with open(CSV_FILE_NAME, "r", newline = "", encoding = "utf8") as csvFile:
            start = time.time()
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
                
                # create DataItem from line
                movie = DataItem(line)
                
                # feed the appropriate field into hash function to get a 'key'
                # quoteKey = asciiStringHash(movie.quote)
                # hashIndex = quoteKey % len(hashTableQuotes)
                # quoteKey = multiplicationHash(hashTableQuotes, movie.quote)
                # quoteKey = foldingHash(quoteKey, foldCount)
                # returnVal = addToTable(hashTableQuotes, movie, hashIndex)
                # quoteKey = polynomialRollingHash(movie.quote) % len(hashTableQuotes)
                # returnVal = addToTable(hashTableQuotes, movie, quoteKey)
                quoteKey = midSquareHash(movie.quote) % len(hashTableQuotes)
                returnVal = addToTable(hashTableQuotes, movie, quoteKey)

                if(returnVal == -1):
                    print(f"{movie} could not be inserted into table.")
                elif(returnVal == 1): # collision happened
                    quotesCollisions += 1
                counter += 1
            end = time.time()
            elapsed = (end - start)
            print("QUOTE TABLE STATISTICS")
            reportTableStatistics(hashTableQuotes, elapsed, quotesCollisions)
    except FileNotFoundError as ex:
        print(f"File does not exist in main!\nException: {ex}")
    except Exception as ex:
        print(f"Unknown exception in main!\nException: {ex}")
    finally:
        return

if(__name__ == "__main__"):
    main()