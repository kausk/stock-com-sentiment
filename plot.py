import math
import plotly
import Quandl
py = plotly.plotly("kausk", "p24ixqvuzo")
import glob
def plot(query, name):
	
	mydata = Quandl.get(name, authtoken="P4XxRkeVJCEmXmzJuESv", trim_start="2014-03-01", trim_end="2014-03-31", returns="numpy")
	
	stockdates = [str(i[0]) for i in mydata]

        openp = [str(i[1]) for i in mydata]

        high = [str(i[2]) for i in mydata]

        low = [str(i[3]) for i in mydata]

        close = [str(i[4]) for i in mydata]

        changes = []

        for i in close:
                for j in openp:
                        cf = ((float(i) - float(j)) / (float(j)))
                        changes.append(cf)
	graph_data = []
	
	text = []
	search = query.split(' ', 1)[0] + '.txt'
        datafiles = glob.glob(search)
        matching = [s for s in datafiles if entry in s]
                #print(matching)

        for item in matching:

                        ### Just opening the file, still same error##
                        #linkfile = open(item, 'r')
                        ### First 5 lines of file opening ##
		with open(item) as f:
                	e = list(f)
                	g = list(set(e))
                	file = list(islice(g,0,1,1))
                        #x = 1 #first 4 articles
                	for link in file:
				text.append(link)
	y = zip(changes, text)
	graph_data.append(
	{
		'name' : query + 'Stock price % movement',
		'x' : [i[0] for i in mydata],
		'y' : [i[0] for i in y],
		'text' : [i[1] for i in y],
     		'type': 'scatter',
        		'mode': 'markers',
		
        		'marker': { # specify the style of the individual scatter points
#            		'size': [math.sqrt(row[1])/1.e3 for row in data if row[2] == continent],
            		'sizemode': 'area',
            		'sizeref': 0.05,
            		'opacity': 0.55
        		}
    		})
		
	
	layout = {
 		'xaxis': {'title': 'Date'},
 		'yaxis': {'title': 'Change in percentage'},
 		'title': {'stock'}
	}

	py.plot(graph_data, layout=layout,filename='My first plotly graph', fileopt='overwrite', world_readable=True, width=1000, height=650)


plot("Apple", "GOOG/NASDAQ_AAPL")
