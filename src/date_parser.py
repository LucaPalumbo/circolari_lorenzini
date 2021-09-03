#!/usr/bin/env python

def dateParser(oldDate):
    listDate= oldDate.split()
    months = ['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre']
    index = months.index(listDate[1].lower())+1
    date = '20'+listDate[2]+'-'+str(index)+'-'+listDate[0]
    return date


