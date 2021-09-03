#!/usr/bin/env python
from bs4 import BeautifulSoup as bs
import requests
from circular import Circular
import logging
import re
from database import dbmanage
class Scraper:
    #constructor, make a get request and parse response
    def __init__(self, url):
        self.url = url
        print("Connecting to {}".format(url))
        try:
            self.rawHTML = requests.get(self.url).text
            self.soupHTML = bs(self.rawHTML, 'html.parser')
        except:
            print("Something went wrong")

    #print html function for debugging purpose
    def printHTML(self,mode):
        if(mode == 'raw'):
            print(self.rawHTML)
        if(mode == 'soup'):
            print(self.soupHTML)
    
    # get all circular in html
    def listCircular(self):
        circularsDiv = self.soupHTML.findAll('div', {'class':'post-box-archive'})
        circularsList = []
        for div in circularsDiv:
            name = div.h4.text
            number = int(re.search('\d+', name).group(0))
            date = div.span.text
            link = div.a['href']

            circularsList.append( {'number': number, 'name': name, 'date': date, 'link': link} )
        return circularsList 

    #setter url (maybe useless)
    def setWebsite(self, site):
        website = site

"""
url = "http://istitutolorenzinipescia.edu.it/category/circolari/"
S = Scraper(url)
S.listCircular()"""

def do_scraping():
    url = "http://istitutolorenzinipescia.edu.it/category/circolari/"
    S = Scraper(url)
    db = dbmanage()
    circulars = S.listCircular()
    circulars = [ Circular(c['number'],c['name'],c['date'],c['link']) for c in circulars ]
    newCircular = []
    for circular in circulars:
        if(db.checkCircular(circular) == False):
            newCircular.append(circular)
            db.addCircular(circular)
    db.close()
    return newCircular