import os
import csv

os.chdir('C:\\Users\Paavan Gopala\\Downloads\\Ex_Files_Scripting_for_Testers\\'
         'Ex_Files_Scripting_for_Testers\\Exercise Files\\02_01\\begin')

my_list = []

with open('TestTimingData.csv', 'r') as file_read:
	contents = csv.reader(file_read)
	
	for content in contents:
		my_list.append(content)
		
print(my_list)

column_chart_data = [['Test Name', 'Diff from Avg']]
table_data = [['Test Name', 'Run Time (s)']]

for row in my_list[1:]:
	test_name = row[0]
	if not row[1] or not row[2]:
		continue
	current_run_time = float(row[1])
	average_run_time = float(row[2])
	diff_from_avg = abs(average_run_time - current_run_time)
	column_chart_data.append([test_name, diff_from_avg])
	table_data.append([test_name, current_run_time])
	
print(column_chart_data)
print(table_data)