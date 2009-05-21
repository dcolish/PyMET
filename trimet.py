#!/usr/local/bin/python2.5

import urllib
import string
from xml.etree import ElementTree as ET

f = urllib.urlopen("http://developer.trimet.org/ws/V1/arrivals/locIDs/1927/appID/6314951981D5C02DFC189B44D")


s = f.read()
 
#print s

elements = ET.XML(s)

subelements = elements.getchildren()



for children in subelements:
  if children.get('route','45') == '45':
    print children.keys()
    print children.items()



