# Diary App

import datetime

choice = input("1.write 2.Read: ")

if choice == "1":
    entry = input("Today's entry: ")
    with open("diary.txt", "a") as f:
        f.write(f"{datetime.date.today()}: {entry} \n")    
else: 
    with open("diary.txt", "r") as f:
        print(f.read()) 