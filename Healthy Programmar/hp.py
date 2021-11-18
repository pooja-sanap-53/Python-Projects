'''
Exercise#7 Healthy Programmer
Assume that a programmer works at the office from 9am-5 pm. We have to take care of his health and remind him three things,

To drink a total of 3.5-liter water after some time interval between 9-5 pm.
To do eye exercise after every 30 minutes.
To perform physical activity after every 45 minutes.

Instructions:
The task is to create a program that plays mp3 audio until the programmer enters the input which implies that he has done the task.

For Water, the user should enter “Drank”
For Eye Exercise, the user should enter “EyDone”
For Physical Exercise, the user should enter “ExDone”
After the user enters the input, a file should be created for every task separately, which contains the details about the time when the user performed a certain task.

Challenge:
You will have to manage the clashes between the reminders such that no two reminders play at the same time.
'''

from pygame import mixer
from datetime import datetime
from time import time


def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")

if __name__ == "__main__":
    # musicloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    eyesecs = 1810
    exsecs = 2720

    while True :
        if time() - init_water > watersecs:
            print("Water drinking time. Enter 'Drank' to stop the alarm. ")
            musicloop("water.mp3", 'Drank')
            init_water = time()
            log_now("Drank water at")

        if time() - init_eyes > eyesecs:
            print("Eyes workout time. Enter 'Done' to stop the alarm. ")
            musicloop("eyes.mp3", 'Done')
            init_eyes = time()
            log_now("Did eyes workout at")

        if time() - init_exercise > exsecs:
            print("Physical Activity time. Enter 'Done' to stop the alarm. ")
            musicloop("physical.mp3", 'Done')
            init_exercise = time()
            log_now("Did physical activity at")