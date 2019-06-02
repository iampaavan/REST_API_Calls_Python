import gspread, os
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
os.chdir('C:\\Users\\Paavan Gopala\\Downloads')
credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project 4164-7c6b951aca42.json', scope)

client = gspread.authorize(credentials)

sheet = client.open('Test').sheet1

row_column = sheet.update_cell(1, 1, 'test')
print(row_column)

read = sheet.row_values(1)
print(read)

all_values = sheet.get_all_values()
print(all_values)

my_data = [[1, 2, 3], [4, 5, 6]]
contents = 0

for row_index, row in enumerate(my_data):
	for col_index, value in enumerate(row):
		contents = sheet.update_cell(row_index+1, col_index+1, value)
		print(contents)
