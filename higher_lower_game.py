import os
import random
from resources import game_art
from database import database

print(game_art.game_logo)
data = database.data
score = 0


def display_info(choice):
    name = choice["name"]
    description = choice["description"]
    country = choice["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(user_guess, followers_count_first, followers_count_second):
    if followers_count_first < followers_count_second:
        if user_guess == 1:
            return False
        else:
            return True
    else:
        if user_guess == 1:
            return True
        else:
            return False


second_choice = random.choice(data)
while True:
    first_choice = second_choice
    second_choice = random.choice(data)
    while first_choice == second_choice:
        second_choice = random.choice(data)
    print(f"Compare 1: {display_info(first_choice)}")
    print(game_art.vs)
    print(f"Compare 2: {display_info(second_choice)}")

    guess = int(input("Who has more followers? Type 1 or 2: "))
    followers_first = first_choice["followers"]
    followers_second = second_choice["followers"]
    result = check_answer(guess, followers_first, followers_second)
    data.remove(data[data.index(first_choice)])
    os.system("cls")
    print(game_art.game_logo)
    if result:
        score += 1
        if len(data) > 1:
            print(f"Right! Your score is: {score}")
    else:
        print(f"Wrong! Your completed the game and your score is: {score}")
        break
    if len(data) <= 1:
        print(f"Congrats! You answered all the questions right! Your score is: {score}")
        break
