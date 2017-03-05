# Just a listener, listening to a port on IRC
# and printing it out to console.

import socket

HOST = 'devPi'
PORT = 6667
PASS = 'none'
NICK = 'Test'
IDENT = 'Test'
REALNAME = 'Just a framework'
CHAN = '#BOTTEST'
TOPIC = 'Bot Testing. YAY!'

data = ''

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

irc.connect((HOST, PORT))
irc.send('NICK '+NICK+'\r\n')
irc.send('USER '+IDENT+' '+HOST+' bla :'+REALNAME+'\r\n')

irc.send('JOIN ' +CHAN+'\r\n')
irc.send('TOPIC ' +CHAN+ ' :' + TOPIC + '\r\n')
irc.send('PRIVMSG ' +CHAN+ ' :Hello, world!' + '\r\n')

#irc.send("PRIVMSG nickserv :iNOOPE\r\n")

def action(channel, action):
	irc.send('PRIVMSG ' +channel+ ' :\x01ACTION '+ action + ' \x01' + '\r\n')	

def chanMsg(channel, message):
	irc.send('PRIVMSG ' +channel+ ' :' + message + '\r\n')

def joinChan(channel):
        irc.send('JOIN ' +CHAN+ '\r\n')
	
while 1:
	data = irc.recv(1024)
	print data
        tmp = data.split()
        
	if tmp[0] == 'PING':
		print ('PONG ' + tmp[1] + '\r\n')
		irc.send('PONG ' + tmp[1] + '\r\n')
		
	if tmp[1] == 'KICK':
                joinChan(CHAN)
        
	if tmp[1] == 'PRIVMSG' and tmp[2] == NICK:
		tmp=tmp[0].split('!')
		tmp=tmp[1].split('@')
		chanMsg(tmp[0], 'Receiving message on private.')
	if tmp[1] == 'PRIVMSG' and tmp[2] == CHAN:
		chanMsg(CHAN, 'Receiving message in public.')
	if tmp[1] == 'JOIN' and tmp[0].find('TRiGGER80'):
                chanMsg(CHAN, 'TRiGGER80 is the OP of this channel.')
                irc.send('MODE ' +CHAN+ ' +o TRiGGER80' + '\r\n')
                action(CHAN, 'Salutes.')

        
				
