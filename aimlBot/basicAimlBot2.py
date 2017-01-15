import aiml

mybot = aiml.Kernel()

mybot.setBotPredicate('name','Testy')

mybot.learn('/home/pi/python/aimlBot/AIML/Reductions/*.aiml')
mybot.learn('/home/pi/python/aimlBot/AIML/standard-aiml/standard/*.aiml')


mybot.learn('/home/pi/python/aimlBot/AIML/annotated_alice/*.aiml')

#mybot.respond('load aiml b')

while True:
    print mybot.respond(raw_input("> "))
    

