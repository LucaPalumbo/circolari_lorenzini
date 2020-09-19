#!/usr/bin/env python
from scraper import Scraper
from circular import Circular
from database import dbmanage

def main():
    url = "http://istitutolorenzinipescia.edu.it/category/circolari/"
    S = Scraper(url)
    db = dbmanage()
    circulars = S.listCircular()
    circulars = [ Circular(c['number'],c['name'],c['date'],c['link']) for c in circulars ]

    for circular in circulars:
        print(circular.id)
        if(db.checkCircular(circular) == False):
            db.addCircular(circular)

    db.close()



if __name__ == '__main__':
    main()