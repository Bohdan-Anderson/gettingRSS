#http://www.python-requests.org/en/latest/user/quickstart/
import requests
#http://docs.python.org/2/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.iter
import xml.etree.ElementTree as ET

#r = requests.get('http://www.cbc.ca/podcasting/includes/spark.xml')
#r = requests.get('http://feeds.99percentinvisible.org/99percentinvisible')
#r = requests.get('http://feeds.thisamericanlife.org/talpodcast')
r = requests.get('http://feeds.wnyc.org/radiolab')
#r = requests.get('http://philosophybites.com/atom.xml')

tree = ET.fromstring(r.content)

#w = open('data','wb')
#w.write(r.content)
#w.close()

#tree = ET.parse('data').getroot()

#for children in tree:
#	print children

for channel in tree:
	for article in channel.findall('item'):
		title = article.find('title').text.encode("utf-8")
		try:
			mp3 = article.find('enclosure').get('url')
			print mp3
		except AttributeError:
			print "no mp3"

		#for child in article.iter():
		#	print child