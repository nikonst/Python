import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.nikonst.gr/testPython/index.html")
print "Status Code:", page.status_code

soup = BeautifulSoup(page.content, 'html.parser')

html = list(soup.children)[2] #html

title = html.find_all('title')
for t in title:
    print "Page's Title:", t.get_text()

headingOne = html.find_all('h1')
print "Number of H1 headings:",len(headingOne)
for head in headingOne:
    print "\t",head.get_text()

paragrpahs = html.find_all('p')
print "Number of Paragraphs",len(paragrpahs)

for p in paragrpahs:
        print "\t",p.get_text()

ahrefs = html.find_all('a')
print "Number of Links",len(ahrefs)
print "Anchor Texts:"
for links in ahrefs:
    print "\t",links.get_text()
print "The Links:"
for links in ahrefs:
    print "\t",links['href']

imgs= html.find_all('img')
print "Number of Images",len(imgs)

print "html Length", len(html)

print "--------------"
print "The HTML Document"
print html
print "--------------"

print "The HTML Nodes"
for item in html:
    print item

print "**********"

#print page.content
#print(soup.prettify())
#print [type(item) for item in list(soup.children)]
#print list(soup.children)


