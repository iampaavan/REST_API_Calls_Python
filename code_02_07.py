import csv, os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
os.chdir('C:\\Users\\Paavan Gopala\\Downloads')

credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project 4164-7c6b951aca42.json', scope)
client = gspread.authorize(credentials)

sheet = client.open('TestRunData').sheet1

# read in the data from the spreadsheet
spreadsheet_data = sheet.get_all_values()

# a note to help you out here
#   We don't need the Test Name or Average Run Time
#   data, so we can remove those from each row using
#   del row_data[x] where x is the index of the element
#   we want to remove
run_times = []
for row in spreadsheet_data:
# Remove the first 2 items from the row since we are not
# interested in the Test Name or Avg Run time
	del row[0]
	del row[1]
	run_times.append(row)

# read in csv data
csv_data = []
with open('C:\\Users\Paavan Gopala\\Downloads\\Ex_Files_Scripting_for_Testers\\'
          'Ex_Files_Scripting_for_Testers\\Exercise Files\\02_07\\LatestTestRunData.csv') as f:
	files = csv.reader(f)
	
	for file in files:
		csv_data.append(file)
	
print(csv_data)

# for the sake of simplicity we are going to assume a few things:
# 1. All of the tests in the csv data were run on the same date
# 2. The test are in the same order in the csv file as they are in the
#    spreadsheet data

# find the run date
# remember that we can assume that all the tests in the csv file were run on the same date
# which means we can get the run date from the 3rd column of the 2nd row in the csv data

run_date = csv_data[1][2]
spreadsheet_header_row = run_times[0]
spreadsheet_header_row.append(run_date)
del spreadsheet_header_row[0]

# now get the first row of the run_times list and modify it to remove the oldest value
# and add in the new run date
for spreadsheet_row,csv_row in zip(run_times[1:],csv_data[1:]):
    new_value = csv_row[1] #second column in the csv data is the new run time
    spreadsheet_row.append(new_value)
    del spreadsheet_row[0]

# similar to above, do this for each remaining row
# loop over the run_times and csv_data lists and for each time through the loop,
# get the new value from the csv_data and add it to the end of the run_times row
# and then remove the oldest value from that row
# note that you can use zip to iterate over multiple lists at the same time
for spreadsheet_row, csv_row in zip(run_times[1:], csv_data[1:]):
	new_value = csv_row[1]  # second column in the csv data is the new run time
	spreadsheet_row.append(new_value)
	del spreadsheet_row[0]
	
# write the new spreadsheet data back into the spreadsheet
# don't forget that lists are indexed starting from 0 and the
# spreadsheet index starts at 1.  Also remember that we want to
# start writing the data in the 3rd column in the spreadsheet
# since the first two columns have the test name and the average run time.
# As a reminder, if you want both the value and the index
# of a list you can use the enumerate function
for row_index, row in enumerate(run_times):
    for col_index, cell in enumerate(row):
        sheet.update_cell(row_index+1, col_index+3, cell)


# read in the average data from the spreadsheet
# Hint: use sheet.col_values
avg_data = sheet.col_values(2)

# intializing the chart_data list with the headers
chart_data = [["Test Name", "Diff From Avg"]]
for avg, current in zip(avg_data[1:], csv_data[1:]):
    diff = float(avg)-float(current[1])
    chart_data.append([current[0], diff])

# add test names and the difference from the average for each
# of the test to the chart_data list
# hint: use zip again to loop over both the avg_data and the
# csv_data lists at the same time


from string import Template

# first substitution is the header, the rest is the data
htmlString = Template("""<html><head><script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart(){
      var data = google.visualization.arrayToDataTable([
      $labels,
      $data
      ],
      false);

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
<div id = 'chart_div' style='width:800; height:600'><div>
</body>

</html>""")

# format the data correctly
chart_data_str = ''
for row in chart_data[1:]:
    chart_data_str += '%s,\n'%row
    
# Substitute the data into the template
completedHtml = htmlString.substitute(labels=chart_data[0], data=chart_data_str)

with open('Chart.html', 'w') as f:
    f.write(completedHtml)

# Write the html to a file
