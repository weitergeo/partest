import pygsheets
import csv
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
CsvList = list(csv.reader(open('../../../build/win/BotReports/test/statistics.csv')))

#Parse level number and hash from .CSV
levelHashCsv = CsvList[0][0]
levelNoCsv = int(CsvList[1][0])

#Delete number and hash from list
del CsvList[0:2] 

#Convert every item to int
IntCsv = [int(j[0]) for j in CsvList]

#Authorization
gc = pygsheets.authorize(service_file="ProjectTest-82e6b523785c.json")

#Open the google spreadsheet
sh = gc.open('Level Tester')

#Select the first sheet
wks = sh.worksheet_by_title('LevelData')
#Parse list from Google Sheets table
GSheetList = wks.get_col(levelNoCsv + 1, returnas='matrix')

#Define level hash
levelHashGS = GSheetList[0]
#Delete number and hash from list
del GSheetList[0:2] 

#Convert every item to int
IntSheet = [int(j) for j in GSheetList]

#Creating result list the same size as the other lists

#Summing numbers in list
    
#Hashes comparison
if levelHashGS == '0':
    wks.update_col(levelNoCsv + 1, values=IntCsv, row_offset=2)
    wks.update_cell((1,levelNoCsv + 1),val=levelHashCsv)
    print "Data successfully loaded to Google Sheets!"
elif levelHashGS == levelHashCsv:
    for i in range(len(IntCsv)):
        IntCsv[i] = IntSheet[i] + IntCsv[i]
    wks.update_col(levelNoCsv + 1, values=IntCsv, row_offset=2)
    print "Data successfully loaded to Google Sheets!"
else:
    if query_yes_no("Level was changed rewrite data?", default="no") == True:
        wks.update_col(levelNoCsv + 1, values=IntCsv, row_offset=2)
        wks.update_cell((1,levelNoCsv + 1),val=levelHashCsv)
        print "Data was rewritten!"
    else:
        print "All data is lost"
        # @TODO search for exists hashes and write data to existing hashes, or write it to new columns
        #wks2.update_col(levelNoCsv + 1, values=IntCsv, row_offset=2
    print levelHashGS
    print levelHashCsv