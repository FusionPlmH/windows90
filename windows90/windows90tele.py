import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import requests
import RPi.GPIO as GPIO

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/Openwindows':
        bot.sendMessage(chat_id, str('Now opening windows'))
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        control_pins = [7,11,13,15]
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for pin in control_pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, 0)
        halfstep_seq1 = [
                    [1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]
                                        ]
        for i in range(128):
            for halfstep in range(8):
                for pin in range(4):
                    while GPIO.input(10) == GPIO.HIGH:
                         print("Button was pushed!")
                         GPIO.output(pin, 0)
                         GPIO.cleanup()
                         break 
                    GPIO.output(control_pins[pin], halfstep_seq1[halfstep][pin])
                time.sleep(0.001)
        GPIO.cleanup()
    elif command == '/Openwindows15':
        bot.sendMessage(chat_id, str('Now opening windows'))
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        control_pins = [7,11,13,15]
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for pin in control_pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, 0)
        halfstep_seq1 = [
                    [1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]
                                        ]
        for i in range(21):
            for halfstep in range(8):
                for pin in range(4):
                    while GPIO.input(10) == GPIO.HIGH:
                         print("Button was pushed!")
                         GPIO.output(pin, 0)
                         GPIO.cleanup()
                         break 
                    GPIO.output(control_pins[pin], halfstep_seq1[halfstep][pin])
                time.sleep(0.001)
        GPIO.cleanup()
    elif command == '/intOpenwindows':
        bot.sendMessage(chat_id, str('Now opening windows'))
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        control_pins = [7,11,13,15]
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for pin in control_pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, 0)
        halfstep_seq1 = [
                    [1,0,0,0],
                    [1,1,0,0],
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1]
                                        ]
        for i in range(512):
            for halfstep in range(8):
                for pin in range(4):
                    while GPIO.input(10) == GPIO.HIGH:
                         print("Button was pushed!")
                         GPIO.output(pin, 0)
                         GPIO.cleanup()
                         break 
                    GPIO.output(control_pins[pin], halfstep_seq1[halfstep][pin])
                time.sleep(0.001)
        GPIO.cleanup()              
    elif command == '/Closewindows':
        bot.sendMessage(chat_id, str('Now closing windows'))
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        control_pins = [7,11,13,15]
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for pin in control_pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, 0)
        halfstep_seq2 = [
                                  [1,0,0,1],
                                  [0,0,0,1],
                                  [0,0,1,1],
                                  [0,0,1,0],
                                  [0,1,1,0],
                                  [0,1,0,0],
                                  [1,1,0,0],
                                  [1,0,0,1]
                                        ]
        for i in range(128):
            for halfstep in range(8):
                for pin in range(4):
                    while GPIO.input(10) == GPIO.HIGH:
                         print("Button was pushed!")
                         GPIO.output(pin, 0)
                         GPIO.cleanup()
                         break 
                    GPIO.output(control_pins[pin], halfstep_seq2[halfstep][pin])
                time.sleep(0.001)
        GPIO.cleanup()
    elif command == '/Closewindows15':
        bot.sendMessage(chat_id, str('Now closing windows'))
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        control_pins = [7,11,13,15]
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for pin in control_pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, 0)
        halfstep_seq2 = [
                                  [1,0,0,1],
                                  [0,0,0,1],
                                  [0,0,1,1],
                                  [0,0,1,0],
                                  [0,1,1,0],
                                  [0,1,0,0],
                                  [1,1,0,0],
                                  [1,0,0,1]
                                        ]
        for i in range(21):
            for halfstep in range(8):
                for pin in range(4):
                    while GPIO.input(10) == GPIO.HIGH:
                         print("Button was pushed!")
                         GPIO.output(pin, 0)
                         GPIO.cleanup()
                         break                    
                    GPIO.output(control_pins[pin], halfstep_seq2[halfstep][pin])
                time.sleep(0.001)
        GPIO.cleanup()
    elif command == '/intClosewindows':
        bot.sendMessage(chat_id, str('Now closing windows'))
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        control_pins = [7,11,13,15]
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        for pin in control_pins:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, 0)
        halfstep_seq2 = [
                                  [1,0,0,1],
                                  [0,0,0,1],
                                  [0,0,1,1],
                                  [0,0,1,0],
                                  [0,1,1,0],
                                  [0,1,0,0],
                                  [1,1,0,0],
                                  [1,0,0,1]
                                       ]
        for i in range(512):
            for halfstep in range(8):
                for pin in range(4):
                    while GPIO.input(10) == GPIO.HIGH:
                         print("Button was pushed!")
                         GPIO.output(pin, 0)
                         GPIO.cleanup()
                         break                    
                    GPIO.output(control_pins[pin], halfstep_seq2[halfstep][pin])

                time.sleep(0.001)  
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
        bot.sendMessage(chat_id, str('/Openwindows15'))
        bot.sendMessage(chat_id, str('/intOpenwindows'))
        bot.sendMessage(chat_id, str('/Closewindows'))
        bot.sendMessage(chat_id, str('/Closewindows15'))
        bot.sendMessage(chat_id, str('/intClosewindows'))
        bot.sendMessage(chat_id, str('/weather'))

            
bot = telepot.Bot('*** copy bot token  ***')
MessageLoop(bot, handle).run_as_thread()

print 'I am listening ...'
        
while 1:
    time.sleep(1)



    

