import pygal
pie_chart = pygal.Pie()
pie_chart.title = 'Browser usage in February 2012 (in %)'
pie_chart.add('IE', 1)
pie_chart.add('Firefox', 2)
pie_chart.add('Chrome', 3)
pie_chart.add('Safari', 1)
pie_chart.add('Opera', 1)
pie_chart.render_to_file('bar_chart.svg')