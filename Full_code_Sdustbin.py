import telepot
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 18 
ECHO = 17

print ('Distance Measurement In Progress')

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.setwarnings(False)
GPIO.output(TRIG, False)
print ('Waiting For Sensor To Settle')
time.sleep(2)

globalMessageNew = 0
globalMessage = 0



def sendMessage(globalMessage):
	
	global telegramText
	global chat_id
	global showMessage
	
	if globalMessage == 1:
		bot.sendMessage(chat_id, 'Rubbish: Full!!!')
	
	elif globalMessage == 2:
		bot.sendMessage(chat_id, 'Rubbish: Warning!!')
		
	elif globalMessage == 3:
	    bot.sendMessage(chat_id, 'Rubbish: Low')
	
		

def mainprogram():
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
		
	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
	
	pulse_duration = pulse_end - pulse_start
	
	global distance
	distance = pulse_duration * 17150
	distance = round(distance)
	    
	global chat_id
	global globalMessage
	global globalMessageNew
	print('Distance:', distance)
		
		
		
	if distance <= 5: 
		globalMessage = 1
		if globalMessageNew != globalMessage:
		  sendMessage(globalMessage)
		  globalMessageNew = globalMessage
			
		else:
			globalMessageNew = globalMessage
		  
	elif distance <= 10 and distance > 5:
		globalMessage = 2
		if globalMessageNew != globalMessage:
		  sendMessage(globalMessage)
		  globalMessageNew = globalMessage
		
		else:
			globalMessageNew = globalMessage
	  
	elif distance <= 21 and distance > 10:
		globalMessage = 3
		if globalMessageNew != globalMessage:
		  sendMessage(globalMessage)
		  globalMessageNew = globalMessage
		  
		else:
			globalMessageNew = globalMessage
		 
	
	time.sleep(10)



def handle(msg):
  global telegramText
  global chat_id
  global showMessage
  global distance
  
  chat_id = msg['chat']['id']
  telegramText = msg['text']
  
  print('Message received from ' + str(chat_id))
  if telegramText == '/start':
    bot.sendMessage(chat_id, 'Welcome to Smart Dustbin')
    bot.sendMessage(chat_id, 'Location:  Lorong Industri Impian 1, Taman Industri Impian, 14000 Bukit Mertajam, Pulau Pinang')
 
    while True:
        mainprogram()
      
      
bot = telepot.Bot('779066943:AAGMLfHzwiyWro1nmMCfe_kTrkd8zOZc2i8')
MessageLoop(bot, handle).run_as_thread()
	
while 1:
    time.sleep(10)
