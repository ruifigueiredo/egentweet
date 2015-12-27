import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer

# lista termos
TERMS = ['#egenventures','#enear','#edge','#edgeinnovation','#driven','#designsete','#outfit','#east','#evision','#egen']

# numero do pin do GPIO  onde esta ligado o LED
LED = 22

# autenticacao do Twitter
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

# callbacks do  Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')
                        print
                        GPIO.output(LED, GPIO.HIGH)
                        time.sleep(10)
                        GPIO.output(LED, GPIO.LOW)

# Setup GPIO output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

# criar streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()
from subprocess import call
call(["fswebcam","-d","/dev/video0","-l","10","idots-%Y-%m-%d-%H-%M-%S.jpeg"])

