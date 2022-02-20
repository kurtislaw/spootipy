from charset_normalizer import detect
import serial
import math
import player

arduino = serial.Serial(
    port='/dev/cu.usbmodem142301',
    baudrate=9600,
    timeout=.1
)


CEILING_HEIGHT = 178

first = False
detected = False
count = 0
while True:
    output = arduino.readline().decode().rstrip()
    if output != '':
        output = int(output)
        
        
        if math.isclose(CEILING_HEIGHT, output, abs_tol= 5): # detects ceiling
            print(f'No Hand. Ceiling @ {output}cm.')
            count = 0
        else:
            detected = True