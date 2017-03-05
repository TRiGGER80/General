# Just a listener, listening to a port on IRC
# and printing it out to console.

import socket
import time

HOST = 'GlaDOS'
PORT = 6667
PASS = 'none'
NICK = 'Lexxa'
IDENT = 'Lexxa'
REALNAME = 'Just a harmless fun-bot.'
CHAN = '#Bottesting'
TOPIC = 'Bot Testing. YAY!'

data = ''

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def checkPing():

        data = irc.recv(2048)
        print data
        tmp = data.split(' ')

        if tmp[0] == 'PING':
                print ('PONG ' + tmp[1] + '\r\n')
                irc.send('PONG ' + tmp[1] + '\r\n')

def ircConnect(host, port, nick, ident, realname):

	irc.connect((host, port))

	checkPing()

	#time.sleep(5)

	#checkPing()
	
	irc.send('NICK '+nick+'\r\n')

	checkPing()

	#time.sleep(5)

	#checkPing()

	irc.send('USER ' + nick + ' ' + 'MyHost' + ' ' + 'Home' ' ' + ':'+IDENT + '\r\n')

def setTopic(channel, topic):
        
	irc.send('TOPIC ' +channel+ ' :' + topic + '\r\n')


def chanMsg(channel, message):
        
	irc.send('PRIVMSG ' +channel+ ' :' + message + '\r\n')


def action(channel, action):
        
	irc.send('PRIVMSG ' +channel+ ' :\x01ACTION '+ action + ' \x01' + '\r\n')


ircConnect(HOST, PORT, NICK, IDENT, REALNAME)
irc.send('JOIN ' +CHAN+'\r\n')
setTopic(CHAN, TOPIC)
irc.send('PRIVMSG ' +CHAN+ ' :Hello, world!' + '\r\n')	

while 1:
	data = irc.recv(2048)
	print data
	tmp = data.split(' ')

	if tmp[0] == 'PING':

		print ('PONG ' + tmp[1] + '\r\n')
		irc.send('PONG ' + tmp[1] + '\r\n')

	if tmp[1] == 'PRIVMSG' and tmp[2] == NICK:

		tmp=tmp[0].split('!')
		tmp=tmp[0].lstrip(':')
		chanMsg(tmp, 'You are speaking privately to me =)')

	if tmp[1] == 'PRIVMSG' and tmp[2] == CHAN:

		chanMsg(CHAN, 'You are speaking publicly to me =)')

	if tmp[1] == 'JOIN' and tmp[0].find('TRiG80'):

		irc.send('MODE ' +CHAN+ ' +o TRiG80\r\n')
		chanMsg(CHAN, 'Master, Master! I\'m so glad to see you!')
		action(CHAN, 'jumps up and down with joy!')
				
