# Countdown Timer
# Create a terminal countdown timer using time.sleep(), loops and time formatting.
# Concepts: TIME • LOOPS • F-STRINGS

import time
import winsound

seconds = int(input("Countdown from: "))

while seconds > 0:
    mins, secs = divmod(seconds, 60)
    timer = f"{mins:02d}:{secs:02d}"
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up! 🚀")

# Challenge: Play alarm when countdown reaches 0
winsound.Beep(1000, 1500)