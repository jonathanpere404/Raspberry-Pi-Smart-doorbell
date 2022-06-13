import time
import datetime
import asyncio
from subprocess import run

def blank_screen():
    run('vcgencmd display_power 1', shell=True)#hdmi on/of switch