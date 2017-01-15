import aiml

mybot = aiml.Kernel()

mybot.setBotPredicate('name','myBot')
mybot.setBotPredicate('botmaster','Sascha')

mybot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/reductions/*.aiml')
mybot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/reductions/update/*.aiml')
mybot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/mindpixel/*.aiml')
mybot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/*.aiml')

#mybot.respond('load aiml b')

while True:
    print mybot.respond(raw_input("> "))
    

