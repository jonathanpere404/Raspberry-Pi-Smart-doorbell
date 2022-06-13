# Raspberry-Pi-Smart-doorbell
# Smart doorbell made from raspberry pi

Backround to get it working. 

I had problems with the new version of Raspberry Pi OS "Bullseye" at the time. The problems was with OpenCV installation, speakers and touchscreen. I could not get them to work. Maby Bullsey works better now, but i choose older "Buster" operating system for this project.

## Before you get it to working
This Smart Doorbell system works with Telegrambot. First you need to get the BOT and (Token/API key) to use it.

## You need to install them as well
1. Install OpenCV
```
sudo apt-get install python-opencv
```
2. Install all dependencies for OpenCV
```
sudo apt-get install libatlas-base-dev libjasperdev libqtgui4 python3-pyqt5 libqt4-test libilmbase-dev libopenexr-dev
libgstreamer1.0-dev libavcodec58 libavformat58 libswscale5
```
3. Inastall telegrambot API
```
sudo pip3 install pyTelegramBotAPI
```
4. Upgrade API
```
sudo pip3 install --upgrade pyTelegramBotAPI
```
5. Pynput is needed for the cursor position check. At least it worked on my touch screen

#RC070S  #7Inch #1024*600 #IPS #60fps #speaker #HDMI&USB #165*120mm #235g
```
sudo pip3 install pynput
```
6. Clone code
```
git clone https://github.com/jonathanpere404/Raspberry-Pi-Smart-doorbell.git
```

When you have all done you need also to figure out what is your telegram chat ID.

7. Replace Telegram (Token/API key = line 16) and (chat ID = line 70) in face-detection.py
```
bot = telebot.TeleBot("19*****:************QM") #<-------BUT YOUR TELEGRAM TOKEN/API KEY HERE
chat_id = 1*********5 # <-------BUT YOUR TELEGRAM CAHT ID HERE
```

After that you should be all set. Just run the program.
```
python3 face-detection.py
```
