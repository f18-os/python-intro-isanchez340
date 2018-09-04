import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import string
# executing program

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCountTest.py <input text file> <output file> ")
    exit()

inputFname = sys.argv[1]
outputFname = sys.argv[2]

# make sure that input file exist
if not os.path.exists(inputFname):
    print("Input %s doesn't exist")
    exit()

if os.path.exists(outputFname):
    print("Removing previous results")
    os.remove(outputFname)

words = {}


with open(inputFname, 'r') as inputFile:
    for line in inputFile:
        # get rid of newline characters
        line = line.strip()
        # removes characters and replaces them with spaces
        line = line.replace("-", " ")
        line = line.replace("\'", " ")
        for i in string.punctuation:
            line = line.replace(i, "")
            List = list(line.split(" "))

            # replaces upper case letters with lower case
            for i in range(len(List)):
                List[i] = List[i].lower()

                # checks if word is in list and if it is, it increments count and if not adds it to list
                if len(List[i]) >= 1 and List[i][0].isalpha():
                    if not List[i] in words:
                        words[List[i]] = 1
                    else:
                        words[List[i]] += 1

    # sorts list from most to least
    SortList = {}
    for i in sorted(words):
        SortList[i] = words[i]

    # Writes sorted list to file
    fileOut = open(outputFname, "w")
    for i in SortList:
        fileOut.write(str(i) + " " + str(SortList[i]) + "\n")
    fileOut.close()
