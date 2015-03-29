# Code adaprted from 'Learn To Code' By TuxRadar.com
# Python 2.7 Standard
# Report any issues on our GitHub Page!

import time
lasttime = 1
lastin = 0
lastout = 0

def getspeed():
  x=open('/proc/net/dev','r')
  for line in x.readlines():
    line = line.strip()
    if (line[:4] == 'eth0'):
      line = line[5:].split()
      bin = int(line[0])
      bout = int(line[8])
  return(bin, bout)
  
while True:
  z = getspeed()
  timedelta = time.time()-lasttime
  lasttime = time.time()
  sin = (float(z[0]-lastin))/(1024*timedelta)
  sout = (float(z[1]-lastout))/(1024*timedelta)
  print sin, sout
  lastin = z[0]
  lastout = z[1]
  time.sleep(5)
