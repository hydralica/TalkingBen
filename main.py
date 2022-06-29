from playsound import playsound
import random

sounds = ["sounds\\ben.wav", "sounds\\hahoho.wav", "sounds\\jadajada.wav", "sounds\\no01.wav", "sounds\\yes01.wav"]

while True:
    benStart = input("what would you like to ask ben?: ")
    soundChoice = random.choice(sounds)
    playsound(soundChoice)