import aiml

mybot = aiml.Kernel()

mybot.setBotPredicate('name','Testy')

mybot.learn('/home/pi/python/aimlBot/AIML/standard-aiml/std2-startup.xml')
mybot.respond('load aiml b')

while True:
    print mybot.respond(raw_input("> "))
    

