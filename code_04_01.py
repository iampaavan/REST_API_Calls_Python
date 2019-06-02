import json
from string import Template

json_data = open('JiraJsonData.json', 'r').read()
data = json.loads(json_data)

status_count = {}

for project in data['projects']:
	for issue in project['issues']:
		status = issue['status']
		status_count[status] = status_count.get(status, 0) + 1
		
print(status_count)

template = Template("""
<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Status', 'Number of Issues'],
          $my_data
        ]);

        var options = {
          title: 'Issues by Status'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart" style="width: 900px; height: 500px;"></div>
  </body>
</html>""")

formatted_data = ''

for stat in status_count:
	formatted_data += "['%s',%s],\n"%(stat, status_count[stat])

print(formatted_data)
html_string = template.substitute(my_data=formatted_data)
print(html_string)

with open('piechcart.html', 'w') as f:
	f.write(html_string)
	
