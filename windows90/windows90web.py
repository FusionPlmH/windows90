#!/usr/bin/env python
#!/usr/bin/env python3
from flask import Flask, render_template, request
import requests
from time import sleep

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])


def move():
        result = ""
        if request.method == 'POST':
		if request.form['submit'] == 'Open windows':
            		result="Open windows"
			import RPi.GPIO as GPIO
                        import time
                        GPIO.setmode(GPIO.BOARD)
                        control_pins = [7,11,13,15]
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
                                    GPIO.output(control_pins[pin], halfstep_seq1[halfstep][pin])
                                time.sleep(0.001)
                        GPIO.cleanup()
		if request.form['submit'] == 'Close windows':
			result="Close windows"
			import RPi.GPIO as GPIO
                        import time
                        GPIO.setmode(GPIO.BOARD)
                        control_pins = [7,11,13,15]
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
                                                GPIO.output(control_pins[pin], halfstep_seq2[halfstep][pin])
                                        time.sleep(0.001)
                        GPIO.cleanup()
                if request.form['submit'] == 'Open 15 degree':
            		result="Open 15 degree"
            		import RPi.GPIO as GPIO
                        import time
                        GPIO.setmode(GPIO.BOARD)
                        control_pins = [7,11,13,15]
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
                                                GPIO.output(control_pins[pin], halfstep_seq1[halfstep][pin])
                                            time.sleep(0.001)
                        GPIO.cleanup()
                if request.form['submit'] == 'Close 15 degree':
                        result="Close 15 degree"
			import RPi.GPIO as GPIO
                        import time
                        GPIO.setmode(GPIO.BOARD)
                        control_pins = [7,11,13,15]
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
                                                GPIO.output(control_pins[pin], halfstep_seq2[halfstep][pin])
                                            time.sleep(0.001)
                        GPIO.cleanup()

                if request.form['submit'] == 'Int_open':
                        result="Int_opene"
            		import RPi.GPIO as GPIO
                        import time
                        GPIO.setmode(GPIO.BOARD)
                        control_pins = [7,11,13,15]
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
                                                GPIO.output(control_pins[pin], halfstep_seq1[halfstep][pin])
                                            time.sleep(0.001)
                        GPIO.cleanup()

                if request.form['submit'] == 'Int_close':
                        result="Int_close"
            		import RPi.GPIO as GPIO
                        import time
                        GPIO.setmode(GPIO.BOARD)
                        control_pins = [7,11,13,15]
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
                                                    GPIO.output(control_pins[pin], halfstep_seq2[halfstep][pin])
                                            time.sleep(0.001)
                        GPIO.cleanup()
                        
                if request.form['submit'] == 'weather':
                        result="weather"
                        city = 'Hong Kong'
                        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=f20c6a20e81c4b93cc382bab54ef936b&units=metric'.format(city)
                        res = requests.get(url)
                        data = res.json()
                        wind_speed = data['wind']['speed']
                        latitude = data['coord']['lat']
                        longitude = data['coord']['lon']
                        description = data['weather'][0]['description']
                        return render_template('windows.html',rain=rain_info,res_str=result,data_d=description,data_w=wind_speed,data_la=latitude,data_lo=longitude)                                  
        return render_template('windows.html')



if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', debug=True, threaded=False)
	except:
		pass


        

        
