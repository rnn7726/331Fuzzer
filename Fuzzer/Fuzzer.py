import requests
from lxml import html
from urlparse import urlparse


def text():
    link = raw_input('Insert Link Here: ')
    r = requests.get(link)
    print (r.text)


def getLinks():
    # http://127.0.0.1:8080/bodgeit/
    link = raw_input('Insert Link Here: ')
    r = requests.get(link)
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    for x in ahreflist:
        print (link + x)


def getLinksAuth():
    # http://127.0.0.1:8080/bodgeit/
    link = raw_input('Insert Link Here: ')
    r = requests.get(link, auth=('admin', 'password'))
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    for x in ahreflist:
        print (link + x)


def parseURL():
    link = raw_input('Insert Link Here: ')
    r = requests.get(link)
    reqhtml =  html.fromstring(r.text)
    ahreflist = reqhtml.xpath("//a/@href")
    for x in ahreflist:
        result = urlparse(x)
        print result


#getLinks()
getLinksAuth()
#parseURL('http://127.0.0.1:8080/bodgeit/product.jsp')
parseURL()
#parseURL('http://127.0.0.1:8080/bodgeit/product.jsp?typeid=2')









