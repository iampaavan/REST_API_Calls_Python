import os
import csv
from string import Template

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
	diff_from_avg = average_run_time - current_run_time
	column_chart_data.append([test_name, diff_from_avg])
	table_data.append([test_name, current_run_time])

print(column_chart_data)
print(table_data)

html_string = Template("""<html>
<head>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {
     var data = google.visualization.arrayToDataTable([
      $labels,
      $data
      ],
      false); // 'false' means that the first row contains labels, not data.
    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
<div id="chart_div" style="width:800; height:600"></div>
</body>
</html>""")

char_data_str = ''

for row in column_chart_data[1:]:
	char_data_str += '%s \n'%row

print(char_data_str)
	
completed_html = html_string.substitute(labels=column_chart_data[0], data=char_data_str)

with open('column_chart.html', 'w') as f:
	f.write(completed_html)
