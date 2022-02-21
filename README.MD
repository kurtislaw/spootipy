# spootipy (MakeUofT 2021 project)
![](https://i.imgur.com/IU3i8WE.jpg)

View full demo [here](https://www.youtube.com/watch?v=g0BCuLezZFc)!

## Pitch
Interfaces with your spotify albums! Spootipy allows you to recapture that feeling of physically interacting with your music. It allows you to use physical objects to control music flow, much like a gramophone.



## Features
### 1. Album cartridges
![](https://github.com/kurtislaw/spootipy/blob/main/gifs/album.gif)


### 2. Volume controls (raise/lower hands)
![](https://github.com/kurtislaw/spootipy/blob/main/gifs/volume.gif)

### 3. Playback modification (swipe)
![](https://github.com/kurtislaw/spootipy/blob/main/gifs/playah.gif)

## How we built it
We made Spootipy using a/an:
* Arduino Mega
* Ultrasonic sensor HC-SR04
* Cardboard

## How it works
The ultrasonic sensor pings every 50ms. Depending on the time it takes to rebound off surfaces and reach the sensor again, we can calculate the distance between the sensor and surface.

We aim to detect change in distances. Since the ultrasensor is stationary and pointed towards the ceiling, any change in distance will mean an object has passed over it.