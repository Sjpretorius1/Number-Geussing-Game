import ai_number_picker
from random import choice

print("Welcome to the number geussing game")

name = input("Please provide your name: ")

ai_number = ai_number_picker.numberPicker().number

print(f"Welcome {name} to the number geussing game what numer am I thinking of between 1 and 20?")

geuss = input()

game_Won = False

winning_Awnsers =["Amazing how did you know my geuss was:", "Your geuss was correct my geuss was: "]

while game_Won == False:
    geuss = int(geuss)
    if geuss == ai_number:
        print(f"{choice(winning_Awnsers)} {ai_number}")
        game_Won = True
    elif geuss > ai_number:
        print(f"Your number should be lower then: {geuss}")
        geuss = input("Please geuss again: ")
    elif geuss < ai_number:
        print(f"Your number should be higher then: {geuss}")
        geuss = input("please geuss again: ")    