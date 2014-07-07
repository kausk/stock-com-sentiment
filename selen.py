from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium import select
import selenium
#from sys import argv
#script, query, month, day, date = argv
#only if accessing as its own file


def url(query, month, day, date):
	url = 'http://news.search.yahoo.com/advanced'

	driver = webdriver.Firefox()
	driver.get(url)

	assert "Advanced News Search" in driver.title
	
	## Enter query
	eq = driver.find_element_by_id('f0va')
	eq.send_keys(query)
	
	### Start and End Dates ##
	el = driver.find_element_by_name('smonth')
	for option in el.find_elements_by_tag_name('option'):
		if option.text == month:
        		option.click() 
	
	el2 = driver.find_element_by_name('sday')
	for option in el2.find_elements_by_tag_name('option'):
    		if option.text == day:
        		option.click() 
	
	el3 = driver.find_element_by_name('emonth')
	for option in el3.find_elements_by_tag_name('option'):
    		if option.text == month:
        		option.click() 
	
	el4 = driver.find_element_by_name('eday')
	for option in el4.find_elements_by_tag_name('option'):
    		if option.text == day:
        		option.click()
	
	## Submit the form
	driver.find_element_by_xpath('//*[@id="yschfrm"]/form/div[2]/input').click()
	
	
	'''
	link1 = driver.find_element_by_xpath('//*[@id="web"]/ol/li[1]/div/div[1]/h3/a').get_attribute('href')
	link2 = driver.find_element_by_xpath('//*[@id="web"]/ol/li[2]/div/div[1]/h3/a').get_attribute('href')
	link3 = driver.find_element_by_xpath('//*[@id="news_cluster"]/div/div/h3/a').get_attribute('href')
	
	links.append((link1, link2, link3))
	
	t1 = driver.find_element_by_xpath('//*[@id="web"]/ol/li[1]/div/span[2]')
	t2 = driver.find_element_by_xpath('//*[@id="web"]/ol/li[1]/div/span[2]')
	t3 = driver.find_element_by_xpath('//*[@id="news_cluster"]/div/div/span[2]')
	
	times.append((t1, t2, t3))
	'''
	# First term 
	search = query.split(' ', 1)[0]
	#Search and collect terms
	links = driver.find_elements_by_partial_link_text(search)
	#Make and open file
	name = search + date + '.txt'
	file = open(name, 'a+')
	
	fnames = []
	#Save links to text file
	for link in links:
		for x in range(0,4):
			l =  link.get_attribute('href')
			if l.startswith(("http://ri.search.yahoo.com/", "http://news.yahoo.com/")):
				#for x in range(0,4):	
				file.write("%s\n" % l)

	driver.close()
	return file.name
	
