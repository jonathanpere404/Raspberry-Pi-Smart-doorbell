import RPi.GPIO as GPIO
import pygame.mixer
import datetime
from subprocess import run
import time

async def gp_sound_btn():
    pygame.mixer.init()
    pygame.mixer.music.load('s.mp3')
    pygame.mixer.music.play()

           


