import pygsheets
import pandas as pd

a = 'weitergeo'
#authorization
gc = pygsheets.authorize(service_file='/Users/Huawei/Documents/Yehor/ProjectTest-82e6b523785c.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['twitter users'] = ['vicesam', 'oksklim', a]

#open the google spreadsheet
sh = gc.open('TestParse')

#select the first sheet
wks = sh[0]

#update the first sheet with df, starting at cell B2.
wks.set_dataframe(df,(1,1))
