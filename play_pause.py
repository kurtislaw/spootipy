# sourcery skip: merge-nested-ifs
"""

pingSpeed of 50

"""

import serial
import player
import math


arduino = serial.Serial(
    port='/dev/cu.usbmodem142301',
    baudrate=9600,
    timeout=.1
)

##### BOX SPECIFICS #####
CEILING_HEIGHT = 178

count = 0
play_count = 0
prev = 178

average = 0
index = 0
VOLUME_MODE = False
SKIP = False


"""
player.sp.previous_track()
player.sp.next_track()
"""

while True:
    output = arduino.readline().decode().rstrip()  # converts byte type to str type

    if output != '':
        output = int(output)  # converts str to int

        # if hand detected, then start counting
        if not math.isclose(CEILING_HEIGHT, output, abs_tol=5):
            count += 1
            VOLUME_MODE = False
        else:  # if hand not detected, then reset counter
            count = 0

        distance_delta = output - prev

        if count > 30:  # VOLUME MODE, triggers when count over 15 ticks
            VOLUME_MODE = True
            if distance_delta != 0:
                average += distance_delta
                index += 1
                print(distance_delta)
                # player.volume_change(distance_delta)
                if index > 3: # change index for average rate
                    print(f'average: {average}')
                    player.volume_change(int(average / 20 * 50))
                    index = 0
                    average = 0

        if distance_delta > 50 and not VOLUME_MODE:  # Modifying playback state
            if play_count < 10:
                print('Modified playback state.')
                player.start_pause()
        
        


        prev = output
