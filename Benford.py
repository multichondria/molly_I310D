# File: Benford.py
# Student: Molly Du
# UT EID: md46223
# Course Name: CS303E
# 
# Date: 04/05/2024
# Description of Program: verify Benford's law using population data for select Texas counties

# import libraries
import os.path

# accept name for file given by user & validate if no file of that name exists
def validateFileName():

    newFileName = input("Enter a filename: ").strip()
    if '.txt' not in newFileName:
        newFileName += '.txt'
    if not os.path.isfile(newFileName):
        print("File does not exist")
        return None
    return newFileName

def findPopulationValues(newFileName):
    infile = open(newFileName, "r")
    populationValuesFound = set()
    line = infile.readline()
    while line:
        if '#' not in line:
            items = line.split('&')
            populationValuesFound.add(items[6])
            populationValuesFound.add(items[7])
        line = infile.readline()
    infile.close()
    return populationValuesFound

def countUniqueValues(valuesSet):
    leadingDigits = { '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0 }
    for item in valuesSet:
        leadingDigits[item[0]] += 1
    return leadingDigits

def writeValuesDict(outfile, dictionary, total):
    for key in dictionary:
        percentage = round((dictionary[key]/total)*100, 1)
        outfile.write(format(str(key), "<8s"))
        outfile.write(format(str(dictionary[key]), "<8s"))
        outfile.write(str(percentage) + "\n")

def countCounties(newFileName):
    infile = open(newFileName, "r")
    countiesFound = set()
    line = infile.readline()
    while line:
        if '#' not in line:
            items = line.split('&')
            countiesFound.add(items[1])
        line = infile.readline()
    infile.close()
    return len(countiesFound)
    
def main():
    newFileName = validateFileName()
    if newFileName:
        uniquePopValues = findPopulationValues(newFileName)
        
        outfile = open("benford.txt", "w")
        outfile.write("Total number of counties: " + str(countCounties(newFileName)) + "\n")
        outfile.write("Unique population counts: " + str(len(uniquePopValues)) + "\n")
        outfile.write("First digit frequency distributions:\n")
        outfile.write("Digit\tCount\tPercentage\n")
        
        writeValuesDict(outfile, countUniqueValues(uniquePopValues), len(uniquePopValues))

        outfile.close()

        print("Output written to benford.txt")

                                                     
main()        
