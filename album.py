"""

MAKE SURE TO CHANGE pingSpeed TO 1000


"""

import serial
import player
import math

arduino = serial.Serial(
    port='/dev/cu.usbmodem142301',
    baudrate=9600,
    timeout=.1
)

##### USER SPECIFICS #####
CEILING_HEIGHT = 178

# FIRST TRACKS
"""
height 1 - oncle jazz
height 4 - flower boy
height 8 - dark side
"""
##########################

counter = 0
while True:
    output = arduino.readline().decode().rstrip()

    if output != '':
        output = int(output)
        print(output)

        if math.isclose(output, 1, abs_tol=1):
            counter += 1
            if counter == 1:
                player.play_track(player.get_tracks_uri('oncle jazz'))
        elif math.isclose(output, 4, abs_tol=1):
            counter += 1
            if counter == 1:
                player.play_track(player.get_tracks_uri('flower boy'))
        elif math.isclose(output, 8, abs_tol=1):
            counter += 1
            if counter == 1:
                player.play_track(player.get_tracks_uri('dark side'))
        else:
            counter = 0
        print(f'counter {counter}')