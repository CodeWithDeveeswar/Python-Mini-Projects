# Basic Alarm Clock

import datetime
import time

alarm_time = input("Get alarm (HH:MM): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("⏰ Wake up!")
        break
    time.sleep(1)

# Challenge: Play an actual .mp3 or .wav alarm sound when the alarm triggers.

# python -m pip install playsound4

"""
import datetime
import time
from playsound4 import playsound

alarm_time = input("Get alarm (HH:MM): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("⏰ Wake up!")
        playsound("alarm.mp3")
        break
    time.sleep(1)
"""