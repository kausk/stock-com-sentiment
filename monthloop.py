#from sys import argv
#script, query = argv
from selen import url

def scrape(query):
	'''
	### February
	feb = 1
	while feb < 29:
		month = 'Feb'
		mnum = '02'
		day = str(feb)
		if len(day) == 1:
			date = '0' + day	
		else:
			date = str(feb)

		concat = '2014' + '-' + mnum + '-' + date  
		execs = url(query,  month,  day, concat) #call url function
		return execs
		feb += 1
	'''
	
	mar = 1
	while mar < 32:
        	month = 'Mar'
        	mnum = '03'
		day = str(mar)
        	if len(day) == 1:
                        date = '0' + day
                else:
			 date = str(mar)
                concat = '2014' + '-' + mnum + '-' + date 
		
		execs = url(query, month, day, concat)
		mar += 1
	

