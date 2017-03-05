#!/usr/bin/ python
import aiml

mybot = aiml.Kernel()

mybot.setBotPredicate('name','myBot')
mybot.setBotPredicate('botmaster','Sascha')

mybot.loadBrain('/home/pi/python/aimlBot/misuku.brn')

#mybot.respond('load aiml b')

while True:
    print mybot.respond(raw_input("> "))
    

