#!/usr/bin/python2

# This File is an example for a very simple IRC BOT.
# Maybe this should be turned into an object oriented version,
# And this definitely needs DocStrings and stuff!

import sys
import socket

def main():
  
  # Parsing Commandline Parameters

  if len(sys.argv) != 4:
    
    print 'Usage: ./protoBot.py HOST PORT CHANNEL'
    sys.exit()

  HOST = sys.argv[1]
  PORT = int(sys.argv[2])

  if '#' not in sys.argv[3]:
    CHAN = '#'+sys.argv[3]
  else:
    CHAN = sys.argv[3]

  # Setting Bot Parameters
  
  PASS = 'none'

  BOTNICK = 'Test'
  IDENT = 'Test'
  REALNAME = 'Just a framework'
  TOPIC = 'Bot Testing. YAY!'

  # Defining the type of connection

  data = ''
  irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Defining functions for main bot functionality

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


  # Connecting to the Server and channel we got from the commandline parameters

  ircConnect(HOST, PORT, BOTNICK, IDENT, REALNAME)
  joinChan(CHAN)
  setTopic(CHAN, TOPIC)
	
  # Starting the actual main Bot-Loop :)

  while True:
    data = irc.recv(1024)
    print data
    tmp = data.split()

    # If we receive a PING, we need to answer with PONG and the value we got from the Server.
    # Otherwise, the Server would close the connection on us...

    if tmp[0] == 'PING':
      print ('PONG ' + tmp[1] + '\r\n')
      irc.send('PONG ' + tmp[1] + '\r\n')
    
    # If we're being kicked off the channel, we rejoin and send a message.

    if tmp[1] == 'KICK':
      joinChan(CHAN)
      chanMsg(CHAN, 'THAT was uncalled for...')
    
    # If we see the BotMaster join the channel, we'll greet him.
    # The nick of the Botmaster should be turned into a variable, maybe.

    if tmp[1] == 'JOIN' and tmp[0].split('!')[0] == (':TRiGGER80'):
      chanMsg(CHAN, 'TRiGGER80 is the OP of this channel.')
      irc.send('MODE ' +CHAN+ ' +o TRiGGER80' + '\r\n')
      action(CHAN, 'Salutes.')
    
    # Checking if someone is talking to us in the Channel or directly.
    # We'll reply in the same manner.

    # Replying, if we're talked to in the channel.

    if tmp[1] == 'PRIVMSG' and tmp[2] == CHAN and BOTNICK in data:
      chanMsg(CHAN, 'Receiving message in public.')

    # Replying if we're being addressed in a Private Message.

    if tmp[1] == 'PRIVMSG' and tmp[2] == BOTNICK:
      tmp=tmp[0].split('!')
      tmp=tmp[1].split('@')
      chanMsg(tmp[0], 'Receiving message on private.')
  
  # If we're gonna exit at all, we'll exit cleanly.
  # Maybe i should add a function / command for the bot, that will make it quit.

  sys.exit()
  
    
    
# This is the standard boilerplate that calls the main() function.

if __name__ == '__main__':
  main()
