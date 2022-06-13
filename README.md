# Raspberry-Pi-Smart-doorbell
# Smart doorbell made from raspberry pi

Backround to get it working. 

I had problems with the new version of Raspberry Pi OS "Bullseye" at the time. The problems was with OpenCV installation, speakers and touchscreen. I could not get them to work. Maby Bullsey works better now, but i choose older "Buster" operating system for this project.

## Before you get it to working
This Smart Doorbell system works with Telegrambot. First you need to get BOT and (Token/API key) to use it.

## You need to install them as well
Install OpenCV
```
sudo apt-get install python-opencv
```
install all dependencies for OpenCV
```
sudo apt-get install libatlas-base-dev libjasperdev libqtgui4 python3-pyqt5 libqt4-test libilmbase-dev libopenexr-dev
libgstreamer1.0-dev libavcodec58 libavformat58 libswscale5
```
inastall telegrambot API
```
sudo pip3 install pyTelegramBotAPI
```
upgrade API
```
sudo pip3 install --upgrade pyTelegramBotAPI
```
Pynput is needed for the cursor position check. At least it worked on my touch screen

#RC070S  #7Inch #1024*600 #IPS #60fps #speaker #HDMI&USB #165*120mm #235g
```
sudo pip3 install pynput
```
