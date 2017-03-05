# Just a listener, listening to a port on IRC
# and printing it out to console.

import socket

HOST = 'raspberrypi'
PORT = 6667
PASS = 'none'
NICK = 'Test'
IDENT = 'Test'
REALNAME = 'Just a framework'
CHAN = '#BOT'
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
        irc.send('TOPIC ' +channel+ ' :' +topic+ '\r\n')

def ircConnect(host, port, nick, ident, realname):
        irc.connect((host, port))
        irc.send('NICK '+nick+'\r\n')
        irc.send('USER '+ident+' '+host+' bla :'+realname+'\r\n')

ircConnect(HOST, PORT, NICK, IDENT, REALNAME)
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
                
        
	if tmp[1] == 'PRIVMSG' and tmp[2] == NICK:
		tmp=tmp[0].split('!')
		tmp=tmp[1].split('@')
		chanMsg(tmp[0], 'Receiving message on private.')
				
	if tmp[1] == 'PRIVMSG' and tmp[2] == CHAN and NICK in data:
		chanMsg(CHAN, 'Receiving message in public.')
		
	if tmp[1] == 'JOIN' and tmp[0].split('!')[0] == (':TRiGGER80'):
                chanMsg(CHAN, 'TRiGGER80 is the OP of this channel.')
                irc.send('MODE ' +CHAN+ ' +o TRiGGER80' + '\r\n')
                action(CHAN, 'Salutes.')

        
				
