__author__ = 'root'

import lxml.html
import lxml.etree

goods = lxml.etree.Element('goods')

pages = [
    'http://mebli-lviv.com.ua/duvan_artek_4802',
    'http://mebli-lviv.com.ua/duvan_respekt_lux',
    'http://mebli-lviv.com.ua/duvan_dutjachuy_sonechko',
    'http://mebli-lviv.com.ua/duvan_dutjachuy_panda',
    'http://mebli-lviv.com.ua/krisla_disney'
]
titles = [
    '//div[@id="page_content"]/div[@class="path"]/a[@href="duvan_artek_4802"]/@title',
    '//div[@id="page_content"]/div[@class="path"]/a[@href="duvan_respekt_lux"]/@title',
    '//div[@id="page_content"]/div[@class="path"]/a[@href="duvan_dutjachuy_sonechko"]/@title',
    '//div[@id="page_content"]/div[@class="path"]/a[@href="duvan_dutjachuy_panda"]/@title',
    '//div[@id="page_content"]/div[@class="path"]/a[@href="krisla_disney"]/@title'
]

for i in range(0, 5):
    myhtml = lxml.html.parse(pages[i])

    title = myhtml.xpath(titles[i])
    title = title[0]

    image = myhtml.xpath('//div[@id="page_content"]/div[2]/table/tr/td/a/img/@src')
    image = image[0]

    text = myhtml.xpath('//div[@id="page_content"]/div[2]/table/tr/td[2]/text()')

    good = lxml.etree.SubElement(goods, 'good')
    title_el = lxml.etree.SubElement(good, 'title', type='text')
    title_el.text = title
    image_el = lxml.etree.SubElement(good, 'image', type='image')
    image_el.text = image

    text_el = lxml.etree.SubElement(good, 'text', type='text')
    for t in text:
        text_string = ''.join(t) #for correct string
        p = lxml.etree.SubElement(text_el, 'p')
        p.text = text_string

FILE = open('goods.xml', 'w')
FILE.writelines(lxml.etree.tostring(goods, encoding='utf-8', pretty_print=True))


