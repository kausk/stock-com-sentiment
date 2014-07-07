################################## USING MECHANIZE ##############################
'''
## Import Mechanize crawler ##
import re
import mechanize

# Init browser and link
br = mechanize.Browser()
url = "http://news.search.yahoo.com/advanced"

## open page
br.open(url)

# select form 
br.select_form(name="as")
print br.form

## Exact values ##
br["vp"] = ["apple"]
response2 = br.submit()
'''
########################################################################################
'''
# import lxml lib
from lxml.html import parse
## url 
url = "http://news.search.yahoo.com/advanced"

## get links ##
doc = parse(url).getroot()
print(doc.forms)
form = doc.forms[0]
print(form.inputs.keys())
'''
########################################################################################
'''
import requests
import lxml.html as lh
from lxml.html import parse

def geturl(query, month, day):
	url = "http://news.search.yahoo.com/advanced"
	form_data = {
		'vp' : query,
		'smonth' : month,
		'sday' : day,
		'emonth' : month,
		"eday" : day,
		'submit' : 'submit'
	}
	
	response = requests.post(url, data=form_data)
	tree = lh.document_fromstring(response.content)
	return tree.text_content()

print(geturl("apple", '2', '15'))
'''
'''
import lxml.html
from lxml.html import parse
from pprint import pprint
from lxml.html import submit_form


url = "http://news.search.yahoo.com/advanced"
page = parse(url).getroot()
f = page.forms[0]
pprint(f.form_values())
for key in sorted(f.fields.keys()):
	print key

name = 'apple'
month = '2'
day = '13'
f.fields['vp'] = 'apple'
f.fields['smonth'] = month
f.fields['sday'] = day
f.fields['emonth'] = month
f.fields['eday'] = day

submit = submit_form(f)
print(submit.text_content())
'''
import mechanize
import re
b = mechanize.Browser()
b.open("http://news.search.yahoo.com/advanced")
query = 'apple'
month = '2'
day = '13'
b.select_form(name='as')
b['vp'] = query
b['smonth'] = month
b['sday'] = day
b['emonth'] = month
b['eday'] = day
b.submit()

