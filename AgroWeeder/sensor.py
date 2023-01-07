import RPi.GPIO as GPIO
import time

#def distance(measure = 'cm'):
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
    

    #TRIG = 23 
    #ECHO = 24

    #print ("Distance Measurement In Progress")

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
GPIO.output(23, False)
     
while GPIO.input(24) == 0:
    nosig = time.time()
while GPIO.input(24) == 1:
    sig =time.time()
tl = sig - nosig
if measure == 'cm':
    distance = tl / 0.000058
elif measure == 'in':
    distance = tl / 0.000148
else:
    print('improper choice')
    distance = None
#GPIO.cleanup()
#return distance
print(distance,'cm')
    
