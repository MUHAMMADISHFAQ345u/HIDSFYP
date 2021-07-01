import os
import re
#from hname import *

shorttable = {}
ctable = {}
lookfor = re.compile("GET\s/course/([a-z]+)")

for filename in os.listdir("."):
   if not filename.startswith("ac"):
      continue  # eliminate files that are not logfiles
   for line in open(filename).xreadlines():
      parts = line.split(" ")
# How much of the name / IP address do we report?
      host = hname(parts[0])
      dpsumm = host.getShort()
# Count the host usage and log any course files
      shorttable[dpsumm] = 1 + shorttable.get(dpsumm,0)
      gotten = lookfor.findall(line)
      if (not gotten): continue
      ctable[dpsumm] = ctable.get(dpsumm,"") + " " + gotten[0]

def byhits(one,two):
   global shorttable
   return shorttable[two].__cmp__(shorttable[one])

visitors = ctable.keys()
visitors.sort(byhits)

for browser in visitors:
   print (browser,ctable[browser],shorttable[browser])


   class hname:
       def __init__(self, text):
           self.dparts = text.split(".")
           if self.dparts[-1].isdigit():
               self.havename = 0
           else:
               self.havename = 1

       def getShort(self):
           if self.havename:
               if self.dparts[-1] == "uk":
                   dpp = self.dparts[-3:]
                   if dpp[0] == "demon":
                       dpp = self.dparts[-4:]
               else:
                   dpp = self.dparts[-2:]
           else:
               dpp = self.dparts[:]
           return ".".join(dpp)