import cv2
import time
import datetime
import telebot
import RPi.GPIO as GPIO
import glob #finds all path names
import pygame.mixer
import asyncio
from subprocess import run
from pynput.mouse import Button, Controller
from cursor_position import mouse_pos
from gpionappi import gp_sound_btn
from screen_blank import blank_screen

async def main():
    bot = telebot.TeleBot("19*****:************QM") #<-------BUT YOUR TELEGRAM TOKEN/API KEY HERE
    run('xset s 15', shell=True) #Screen will got to sleep mode after 15s
    mouse = Controller() #Mouse position currently
    old_mouse_position = mouse.position #To set up old mouse positio information
    IMAGE_WIDTH = 1280 #Camera footage width 
    IMAGE_HEIGHT = 720 #Camera footage lentght
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#Mathematical metod to detect face
    cap = cv2.VideoCapture(0)#To capture video from cam
    cap.set(3, IMAGE_WIDTH)#Manually set the screen width
    cap.set(4, IMAGE_HEIGHT)#Manually set the screen lentght
    name = 'Photos' #File where to save images
    img_counter = 0 #Used for image numbering
    pic_save_cooldown = 0 #Used for picture cooldown to save image, one pic at the time 
    GPIO.setmode(GPIO.BCM)#gpio button numberin mode setup
    GPIO.setup(16, GPIO.IN,pull_up_down=GPIO.PUD_UP)#gpio button condition for press
    screen_blank_ones = 0 #Initialise screen blanker to work once at a time
    introduce_variable_once = 0 #Needs this to introduce variable to get the code running
    secound_pic = 0 #Needs this to introduce variable to filter out blurry images
    while True:
        inputValue = GPIO.input(16)#Button bell function goes to this pin
        if (inputValue == False):#Check button condition
            doorbell = asyncio.create_task(gp_sound_btn())#Bell function
            await doorbell
        _, img = cap.read()#Read image
        if (introduce_variable_once == 0): #This needs to be done to introduce screen_blank_timer
            screen_blank_timer = datetime.datetime.now() + datetime.timedelta(seconds=20)
            introduce_variable_once = 1
        pos = mouse_pos(old_mouse_position)#To get mose position value
        if(pos == True): #Check if mouse position is moved
            old_mouse_position = mouse.position #To save mouse old position
            screen_blank_timer = datetime.datetime.now() + datetime.timedelta(seconds=18) 
            introduce_variable_once = 1        
        if (datetime.datetime.now() >= screen_blank_timer):
            if (introduce_variable_once == 1):
                blank_screen()
                introduce_variable_once = 0   
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        #Draw the rectangle around each face
        for (x, y, w, h) in faces:
            rectangel = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            #Notify that it found face
            if True in rectangel:
                if (secound_pic == 0):
                    blurry_image_cooldown = datetime.datetime.now() + datetime.timedelta(seconds=2)
                    secound_pic = 1
                if (datetime.datetime.now() >= blurry_image_cooldown):
                    if (pic_save_cooldown == 0):
                        img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter) #Location for images
                        cv2.imwrite(img_name, img) #Write image
                        img_counter += 1 #Number pictures names
                        secound_pic = 0
                        pic_save_cooldown = 1 #To get the cooldown going
                        chat_id = 1*********5 # <-------BUT YOUR TELEGRAM CAHT ID HERE
                        bot.send_photo(chat_id, open(img_name, 'rb'))#Send image to telegram
                        t_end = datetime.datetime.now() + datetime.timedelta(seconds=30) #Cooldown to save and send
                    if (datetime.datetime.now() >= t_end):
                        pic_save_cooldown = 0 #After this,,, ready for next image to save and send       
        #Display
        cv2.imshow('img', img)
        #Stop if escape key is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"): #Press "Q" to quit program
            cap.release()
            cv2.destroyAllWindows()
            break


# Release the VideoCapture object
asyncio.run(main())
GPIO.cleanup()

