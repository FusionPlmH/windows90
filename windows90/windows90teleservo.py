import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import requests
from time import sleep



def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)
	
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/Openwindows':
        bot.sendMessage(chat_id, str('Now opening windows'))
		import RPi.GPIO as GPIO
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(03, GPIO.OUT)
		pwm=GPIO.PWM(03, 50)
		pwm.start(90)
		GPIO.setwarnings(False)
		pwm.stop()
		GPIO.cleanup() 
         
    elif command == '/Closewindows':
        bot.sendMessage(chat_id, str('Now closing windows'))
		import RPi.GPIO as GPIO
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(03, GPIO.OUT)
		pwm=GPIO.PWM(03, 50)
		pwm.start(0)
		GPIO.setwarnings(False)
		pwm.stop()
		GPIO.cleanup() 
	elif '/Customize' in command:
		command = command + angle
		import RPi.GPIO as GPIO
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(03, GPIO.OUT)
		pwm=GPIO.PWM(03, 50)
		pwm.start(angle)
		GPIO.setwarnings(False)
		pwm.stop()
		GPIO.cleanup() 
		

        
    elif command == '/weather':
        bot.sendMessage(chat_id, str('Now feching weather'))
        city = 'Hong Kong'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=f20c6a20e81c4b93cc382bab54ef936b&units=metric'.format(city)
        res = requests.get(url)
        data = res.json()
        wind_speed = data['wind']['speed']
        temp = data['main']['temp']
        city = data['name']
        description = data['weather'][0]['description']
        message1 = 'City: '
        message2 = 'Wind speed (m/s) : '
        message3 = 'Weather : '
        message4 = 'Temperature (degree celsius) : '
        message5 = 'Rain sensor: '
        import RPi.GPIO as GPIO
        water_sensor = 19
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(water_sensor, GPIO.IN)
		GPIO.setwarnings(False)
        if GPIO.input(water_sensor):
            rain_info = "No Rain Detected"
        else:
            rain_info = "Rain Detected"
        bot.sendMessage(chat_id, message1)
        bot.sendMessage(chat_id, city)
        bot.sendMessage(chat_id, message2)
        bot.sendMessage(chat_id, wind_speed)
        bot.sendMessage(chat_id, message3)
        bot.sendMessage(chat_id, description)
        bot.sendMessage(chat_id, message4)
        bot.sendMessage(chat_id, temp)
        bot.sendMessage(chat_id, message5)
        bot.sendMessage(chat_id, rain_info)

    elif command == '/start':
        bot.sendMessage(chat_id, str('Im working, Here is a list of commend')) 
        bot.sendMessage(chat_id, str('/Openwindows'))
        bot.sendMessage(chat_id, str('/Closewindows'))
		bot.sendMessage(chat_id, str('/Customize'+ angle))
        bot.sendMessage(chat_id, str('/weather'))

            
bot = telepot.Bot('508362029:AAHLoRYFjWWfDNGQHbjbRcOiMF1-fnoFUWQ')
MessageLoop(bot, handle).run_as_thread()

print 'I am listening ...'
        
while 1:
    time.sleep(1)



    

