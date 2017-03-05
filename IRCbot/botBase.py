#!/usr/bin/python


import sys

def main():
  
  if len(sys.argv) != 4:
    
    print 'Usage: ./sysargv.py HOST PORT CHANNEL'
    sys.exit()

  HOST = sys.argv[1]
  PORT = sys.argv[2]

  if '#' not in sys.argv[3]:
    CHAN = '#' + sys.argv[3]
  else:
    CHAN = sys.argv[3]

  PASS = 'none'

  NICK = 'Test'
  IDENT = 'Test'
  REALNAME = 'Just a framework'
  TOPIC = 'Bot Testing. YAY!'

  print HOST + '\r\n'
  print PORT + '\r\n'
  print CHAN + '\r\n'

  sys.exit()
  
    
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
