import pygsheets
import csv
import os
import sys

#Query function
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

#print(os.getcwd())

#Pasre list from LOCAL .CSV to list
CsvList = list(csv.reader(open('test_2.csv')))

#Parse level number and hash from .CSV
levelNoCsv = int(CsvList[1][0])
levelHashCsv = CsvList[0][0]

#Delete number and hash from list
del CsvList[0:2] 

#Convert every item to int
IntCsv = [int(j[0]) for j in CsvList]

#Authorization
gc = pygsheets.authorize(service_file="ProjectTest-82e6b523785c.json")

#Open the google spreadsheet
sh = gc.open('Level Tester')

#Select the first sheet
wks = sh.worksheet('index', 1)
wks2 = sh.worksheet('index', 2)
#Parse list from Google Sheets table
GSheetList = wks.get_col(levelNoCsv + 1, returnas='matrix')

#Define level hash
levelHashGS = GSheetList[0]
#Delete number and hash from list
del GSheetList[0:2] 

#Convert every item to int
IntSheet = [int(j) for j in GSheetList]

#Creating result list the same size as the other lists
ResultList = IntCsv

#Summing numbers in list
for i in range(len(IntSheet)):
    ResultList[i] = IntSheet[i] + IntCsv[i]

#Hashes comparison
if levelHashGS == '0':
    wks.update_col(levelNoCsv + 1, values=ResultList, row_offset=2)
    wks.update_value((1,levelNoCsv + 1),val=levelHashCsv)
elif levelHashGS == levelHashCsv:
    wks.update_col(levelNoCsv + 1, values=ResultList, row_offset=2)
else:
    if query_yes_no("Level was changed rewrite data?", default="no") == True:
        wks.update_col(levelNoCsv + 1, values=ResultList, row_offset=2)
        print "Data was rewritten!"
    else:
        print "All data is lost"
        # @TODO search for exists hashes and write data, or write it to new
        #wks2.update_col(levelNoCsv + 1, values=ResultList, row_offset=2)
    print levelHashGS
    print levelHashCsv