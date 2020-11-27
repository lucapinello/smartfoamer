#in /etc/rc.local add python -u /home/pi/foam2.py  > /home/pi/log_foam 2>&1 &
import RPi.GPIO as GPIO
import time


IS_FOAMING=False

FOAM_TIME=70
WARM_TIME=60*2+15

LED_PIN=4
BUTTON_PIN=18
RELAY_PIN=14

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(RELAY_PIN,GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def simulate_press():
    #relay
    GPIO.output(RELAY_PIN,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RELAY_PIN,GPIO.LOW)
    time.sleep(0.5)
    
def buttonPress():
   
    global IS_FOAMING

    print ("Button pressed!")

    if IS_FOAMING:
	print('Already foaming!')
	return
    else:
	IS_FOAMING=True

    #led on
    GPIO.output(LED_PIN,GPIO.HIGH)
    
    simulate_press()
    simulate_press()
    time.sleep(FOAM_TIME)
    simulate_press()
    simulate_press()
    simulate_press()
    simulate_press()
    simulate_press()
    time.sleep(WARM_TIME)
    simulate_press()
    time.sleep(0.5)   
    #led off
    GPIO.output(LED_PIN,GPIO.LOW)
    print('Done foaming!')
    IS_FOAMING=False
    
#GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=buttonPress, bouncetime=500)

print ('Luigi Ready to foam!')
while True: 
   time.sleep(0.1)
   
   if GPIO.input(BUTTON_PIN) == GPIO.LOW:
       print("START!")
       buttonPress()

GPIO.cleanup() # Clean up
    
    
