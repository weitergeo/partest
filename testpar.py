import pygsheets
import pandas as pd
import numpy as np
import csv

#authorization
gc = pygsheets.authorize(service_file='ProjectTest-82e6b523785c.json')

#open the google spreadsheet
sh = gc.open('TestParse')

#select the first sheet
wks = sh[0]

#parse list from Google Sheets table
GSheetList = wks.get_values(start=(1,1), end=(100,400), returnas='matrix')
IntSheet = [[int(j) for j in i] for i in GSheetList] #and convert to int

#pasre list from LOCAL(for now) .CSV
CsvList = list(csv.reader(open('stress.csv')))
IntCsv = [[int(j) for j in i] for i in CsvList] #and convert to int

ResultList = IntCsv #the only way I found to create Result list the same size as the other lists

# summing numbers in list
for i in range(len(GSheetList)):

   for j in range(len(GSheetList[0])):
              ResultList[i][j] = IntSheet[i][j] + IntCsv[i][j]

#write data back to the Google Sheets
wks.update_values(crange='A1:OJ100', values=ResultList)
