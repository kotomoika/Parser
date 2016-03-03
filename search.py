__author__ = 'root'

import lxml.html
import lxml.etree
from urllib import urlopen

#functions-------------------------------------
#cut all before and uncluding 'url(' and the last ')'
def cut_str(x):
    l = x.split('url')
    if len(l) > 1:
        return l[1].split(')')[0][1:]
    else:
        return ''

def cut_url(list):
    return map(cut_str, list)
#----------------------------------------------

myhtml = lxml.html.parse('http://www.stejka.com')
next_html = myhtml.xpath('//a[@href]/@href') #link next page
data = lxml.etree.Element('data')

for el in range(20, 40): #first text fragments are almost always the same, so we take them from the middle
    page = lxml.etree.SubElement(data, 'page')
    text = myhtml.xpath('//a/text()')
    images = myhtml.xpath('//img[@src]/@src|//div[@class="foto"]/@style')
    images = cut_url(images)

    fragment_t = lxml.etree.SubElement(page, 'fragment', type='text')
    fragment_t.text = text[el]
    fragment_i = lxml.etree.SubElement(page, 'fragment', type='image')
    fragment_i.text = images[el-20] #because we have few images
    #get new page
    url = 'http://www.stejka.com' + next_html[el] #we match them togather because links on site are not full
    myhtml = lxml.html.parse(url) #change on an old page

    #task 2
    #print next url
    a = urlopen(url)
    print a.geturl()

FILE = open('data.xml', 'w')
FILE.writelines(lxml.etree.tostring(data, encoding="utf-8", pretty_print=True))
