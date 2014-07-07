from sys import argv
script, filename = argv

## Open file of news links from date ##
newslist = open(filename, 'a+')


## Links that can be used ##
salient = []

## Add items to the list ##
for item in newslist:
	if item.startswith(("http://ri.search.yahoo.com/", "http://news.yahoo.com/")):
		item = item[:-1]
		salient.append(item)

filename.write(salient)

