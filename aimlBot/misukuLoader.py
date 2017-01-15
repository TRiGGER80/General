import aiml

mybot = aiml.Kernel()

mybot.setBotPredicate('name','myBot')
mybot.setBotPredicate('botmaster','Sascha')

mybot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/reductions/*.aiml')
mybot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/reductions/update/*.aiml')
mybot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/mindpixel/*.aiml')
mybot.learn('/home/pi/python/aimlBot/AIML/aiml-en-us-foundation-alice/*.aiml')
mybot.learn('/home/pi/python/aimlBot/AIML/misuku/*.aiml')
mybot.learn('/home/pi/python/aimlBot/AIML/cathaiku.aiml')

mybot.saveBrain('/home/pi/python/aimlBot/misuku.brn')
