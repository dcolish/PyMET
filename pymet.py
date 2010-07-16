#!/usr/local/bin/python2.5
#quick little guy to tell me the next bus times
import time
import urllib
from optparse import OptionParser
from xml.etree import ElementTree as ET



def main():
  application_id = "EC36A740E55BB5A803BB2602B"
  local_dict = []
  stop_num = []

  parser = OptionParser()

  parser.add_option("-s","--stopid", action="append", type="string", dest="stop_num", 
                    help="the stop id we're looking for, you can have more than one as long as each stop id is preceded by -s")
  parser.add_option("-r","--routeid", action="store", type="string", dest="route_num", help="the route id we're looking for")

  (options, args) = parser.parse_args()

  if not options.stop_num:
     print "The stop number is missing\n"
     parser.print_help()
     exit(-1)
  else:
      for s in options.stop_num:
        stop_num += list([s])

  if not options.route_num:
     print "The route number is missing\n"
     parser.print_help()
     exit(-1)
  else:
    route_num = options.route_num




  for i in stop_num:
    x = 0
    user_url = "http://developer.trimet.org/ws/V1/arrivals/locIDs/" + i + "/appID/" + application_id
    f = urllib.urlopen(user_url)
    elements = ET.XML(f.read())
    subelements = elements.getchildren()

    #prints the stop full name and removes from result set
    print subelements[0].get('desc')
    del subelements[0]

    #get all of the stops for the route we're taking
    for children in subelements:
      if children.get('route',route_num) == route_num:
        local_dict += list([children.attrib])


    for things in local_dict:
      if 'status' in things and x is 0:
        print "Bus " + things.get('status') + " at",
      if 'estimated' in things:
         arriving_at = time.strftime("%I:%M", time.localtime(float(things.get('estimated'))/1000))
         print arriving_at,
      elif 'scheduled' in things:
         arriving_at = time.strftime("%I:%M", time.localtime(float(things.get('scheduled'))/1000))
         print arriving_at,
      if x < len(local_dict)-1:
        print "and",
      if 'shortSign' in things and x == len(local_dict)-1:
        print "for " + things.get('fullSign') + " "
      x += 1


if __name__ == "__main__":
  main()


