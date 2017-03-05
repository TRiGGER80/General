#!/usr/bin/python


import sys
import socket
import aiml

myBot = aiml.Kernel()
myBot.setBotPredicate('name','myBot')
myBot.setBotPredicate('botmaster','Sascha')


myBot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/reductions/*.aiml')
myBot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/reductions/update/*.aiml')
myBot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/mindpixel/*.aiml')
myBot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/*.aiml')



def main():

  
  
  if len(sys.argv) != 4:
    
    print 'Usage: ./protoBot.py HOST PORT CHANNEL'
    sys.exit()

  HOST = sys.argv[1]
  PORT = int(sys.argv[2])

  if '#' not in sys.argv[3]:
    CHAN = '#'+sys.argv[3]
  else:
    CHAN = sys.argv[3]

  PASS = 'none'

  BOTNICK = 'myBot'
  IDENT = 'Test'
  REALNAME = 'Just a framework'
  TOPIC = 'Bot Testing. YAY!'

  data = ''

  irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def action(channel, action):
    irc.send('PRIVMSG ' +channel+ ' :\x01ACTION '+ action + ' \x01' + '\r\n')	

  def chanMsg(channel, message):
    irc.send('PRIVMSG ' +channel+ ' :' + message + '\r\n')

  def joinChan(channel):
    irc.send('JOIN ' +channel+ '\r\n')

  def setTopic(channel, topic):
    irc.send('TOPIC ' +channel+ ' :' +topic+ '\r\n')
        
  def setMode(channel, nickname, mode):
    irc.send('MODE ' +channel+ ' :' +topic+ '\r\n')

  def ircConnect(host, port, nick, ident, realname):
    irc.connect((host, port))
    irc.send('NICK '+nick+'\r\n')
    irc.send('USER '+ident+' '+host+' bla :'+realname+'\r\n')

  ircConnect(HOST, PORT, BOTNICK, IDENT, REALNAME)
  joinChan(CHAN)
  setTopic(CHAN, TOPIC)
	
  while 1:
    data = irc.recv(1024)
    print data
    tmp = data.split()

    if tmp[0] == 'PING':
      print ('PONG ' + tmp[1] + '\r\n')
      irc.send('PONG ' + tmp[1] + '\r\n')

    if tmp[1] == 'KICK':
      joinChan(CHAN)
      chanMsg(CHAN, 'THAT was uncalled for...')
      
    if tmp[1] == 'JOIN' and tmp[0].split('!')[0] == (':TRiGGER80'):
      chanMsg(CHAN, 'TRiGGER80 is the OP of this channel.')
      irc.send('MODE ' +CHAN+ ' +o TRiGGER80' + '\r\n')
      action(CHAN, 'Salutes.')

    if tmp[1] == 'PRIVMSG' and tmp[2] == CHAN and BOTNICK in data:
      chanMsg(CHAN, 'Receiving message in public.')

    if tmp[1] == 'PRIVMSG' and tmp[2] == BOTNICK:
      msg = data.split(':')[2]
      tmp=tmp[0].split('!')
      tmp=tmp[0].split(':')
      answ = str(myBot.respond(msg))
      print answ
      chanMsg(tmp[1], answ)

  sys.exit()
  
    
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
