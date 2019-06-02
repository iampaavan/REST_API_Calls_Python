import csv, os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#read in the data from the spreadsheet
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
os.chdir('C:\\Users\\Paavan Gopala\\Downloads')
creds = ServiceAccountCredentials.from_json_keyfile_name('My Project 4164-7c6b951aca42.json', scope)
client = gspread.authorize(creds)

sheet = client.open('TestRunData').sheet1

spreadsheet_data = sheet.get_all_values()
run_times = []
for row in spreadsheet_data:
    #we remove the first 2 items from the row since we are not
    #interested in the Test Name or Avg Run time
    del row[0]
    del row[1]

    run_times.append(row)

print(run_times)