# Ex-15
# Use urllib2 module to get html content from this link:
# http://www.mattmakai.com/links-learning-web-fundamentals.html
# Python has beautifulsoup library to parse html.
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Print all anchor tags, exclude relative links


import urllib2
import re

from bs4 import BeautifulSoup


try:
    response = urllib2.urlopen('http://www.mattmakai.com/links-learning-web-fundamentals.html')
    html = response.read()

except Exception as e:
    print(e)

soup = BeautifulSoup(html, 'html.parser')
exp = re.compile("^http")

for a in soup.find_all('a', href=True):
    if exp.match(a['href']):
        print(a['href'])