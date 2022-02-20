from time import sleep
from black import out
import serial
import math
import player


# try:
arduino = serial.Serial(
    port='/dev/cu.usbmodem142301',
    baudrate=9600,
    timeout=.1
)
# except:
#     print('Check port.')

##### BOX SPECIFICS #####
CEILING_HEIGHT = 178


# while True:
#     output = arduino.readline().decode('utf-8')
#     if output != '' and output != '\r\n' and output != '\n':
#         if not math.isclose(BOX_LENGTH, int(output), abs_tol=5): # if not bouncing off ceiling
#             print(output)
#     else:
#         print('touching ceiling')

count = 0
detected = False
prev = 178
while True:
    output = arduino.readline().decode().rstrip() # converts byte type to str type

    if output != '':
        output = int(output) # converts str to int

        # print(output)
        # print(prev)
        # if math.isclose(CEILING_HEIGHT, output, abs_tol= 5): # detects ceiling
        #     print(f'No object detected, ceiling @ {output}cm')
        #     count = 0
        #     # detected = False
        # else: #object detected
            
        #     print('object detected')
        #     print(count)
        #     count += 1
        #     if count > 5:
        #         print('Hand detected')
        #         # detected = True
        
        if (prev - output) > 50:
            player.start_pause()
        
        prev = output