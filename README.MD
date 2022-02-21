# spootipy (MakeUofT 2021 project)
![](https://i.imgur.com/IU3i8WE.jpg)

sp__ti for spotify, oo for the sensors, py for python

## Pitch
Interfaces with your spotify albums! Spootipy allows you to recapture that feeling of physically interacting with your music. It allows you to use physical objects to control music flow, much like a gramophone.



## Features
### 1. Album cartridges
![](https://media3.giphy.com/media/R00QlySaMx08cSee46/giphy.gif?cid=790b76118b09a92511981d2e6e7413803d01d92f689a3ff1&rid=giphy.gif&ct=g)


### 2. Volume controls (raise/lower hands)
![](https://media1.giphy.com/media/7bWzCawFTKaQAwQk7o/giphy.gif?cid=790b761159f8e47e81a4fef3ab8e8dedc5659724868e0cb9&rid=giphy.gif&ct=g)

### 3. Playback modification (swipe)
![](https://media4.giphy.com/media/9tMSUrcdF1tjXbFRlL/giphy.gif?cid=790b76113da77b85cfadb87794262b079d3e34d962aa9359&rid=giphy.gif&ct=g)

## How we built it
We made Spootipy using a/an:
* Arduino Mega
* Ultrasonic sensor HC-SR04
* Cardboard

## How it works
The ultrasonic sensor pings every 50ms. Depending on the time it takes to rebound off surfaces and reach the sensor again, we can calculate the distance between the sensor and surface.

We aim to detect change in distances. Since the ultrasensor is stationary and pointed towards the ceiling, any change in distance will mean an object has passed over it.