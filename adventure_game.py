# -- Developer: Sami
# -- Program Name : Adventure Game


# -- Global imports


import time  # for sleep
import random  # for random

# -- Global objects


# - places


places = ["forest", "desert", "ocean"]

# - objects


# - weapons


weapons = ["sword", "knife", "hands", "rock"]

# - enemies


forest_enemies = ["dinosaur", "Forebears", "werewolves"]
desert_enemies = ["mummy lord", "giant scorpion"]
ocean_enemies = ["aquatic elf", "triton", "giant octopus"]

# - game_result


game_result = ["win", "lose"]


# - Methods


# simulates a loading screen


def simulate_loading():
    print_pause("loading")
    print_pause(".", 1)
    print_pause(".", 1)
    print_pause(".\n", 1)


# simulates a clear screen


def clear_screen():
    print("\n" * 100)


# print message


def print_pause(message, seconds=2):
    print(message)
    time.sleep(seconds)


# introduction


def introduction():
    print_pause("Welcome to the DD game adventure", 3)
    print_pause("Prepare yourself to live the best adventure", 3)
    print_pause("We will provide game options, choose wisely !", 3)


# get player name


def get_player_name():
    player_name = ""
    while player_name == "":
        player_name = str(input("Please enter your name \n\t> "))
        if player_name == "":
            print("please put your name")
    return player_name


# print places


def print_places():
    print_pause("The places : \n\t")
    i = 1  # index to show to users for places
    for place in places:
        print_pause("[" + str(i) + "] - " + place + "\n\t", 1)
        i += 1
    print("\n")


# get place chosen


def get_chosen_place():
    print_pause("\tfor forest, you can type 1, f or forest\n")
    print_pause("\tfor desert, you can type 2, d or desert\n")
    print_pause("\tfor ocean, you can type 3, o or ocean\n")
    print_pause("\tcase insensitive\n")

    # choice of place

    place_choice = ""

    while place_choice not in places:
        place_choice = str(
            input("Please choose which place you want to go to : \n\t> ")
        )
        place_choice = place_choice.lower()
        if place_choice == "forest" \
                or place_choice == "f" \
                or place_choice == "1":
            place_choice = "forest"
        elif place_choice == "DESERT" \
                or place_choice == "d" \
                or place_choice == "2":
            place_choice = "desert"
        elif place_choice == "OCEAN" \
                or place_choice == "o" \
                or place_choice == "3":
            place_choice = "ocean"
        else:
            place_choice = ""
            print("Not a valid choice\n")

    return place_choice


# get chosen weapon


def get_chosen_weapon():
    current_weapon = random.choice(weapons)
    print_pause("you have this weapon " + current_weapon)

    change_request = str(
        input("would you like to change weapon?\n"
              "[yes or y for yes / anything else for no]\n")
    )
    change_request = change_request.lower()

    if change_request == "yes" \
            or change_request == "y":
        are_same_weapons = True
        while are_same_weapons:
            new_weapon = random.choice(weapons)
            are_same_weapons = new_weapon == current_weapon
            if not are_same_weapons:
                current_weapon = new_weapon
        print_pause("Now, you have this weapon " + current_weapon)

    return current_weapon


# enemy spawn


def enemy_spawn(place_choice):
    print_pause("now you see in front of you a ")

    if place_choice == places[0]:  # forest
        print_pause(random.choice(forest_enemies))
    if place_choice == places[1]:  # desert
        print_pause(random.choice(desert_enemies))
    if place_choice == places[2]:  # ocean
        print_pause(random.choice(ocean_enemies))


# weapon_interaction


def weapon_interaction():
    print_pause("You use weapon to kill monster\n")
    fight_result = random.choice(game_result)
    if fight_result == game_result[0]:  # win
        print_pause("You killed the monster")
    else:
        print_pause("You died")
    print_pause("you " + fight_result)


# no interaction


def no_interaction():
    print_pause("You do nothing\n")
    print_pause("The monster comes and kill you")
    print_pause("you " + game_result[1])


# get handle_choice from enemy interaction


def enemy_interaction():
    options = ["1", "2"]
    explicit_options = ["fight", "nothing"]
    qualified_explicit_options = ["1-fight", "2-nothing"]

    print_pause("What do you want to do ?")
    print_pause("1-fight")
    print_pause("2-nothing")

    choice = ""

    test1 = choice not in options
    test2 = choice not in explicit_options
    test3 = choice not in qualified_explicit_options

    test = test1 and test2 and test3

    while test:
        choice = str(input("Choose what to do\n\t> "))

        test1 = choice not in options
        test2 = choice not in explicit_options
        test3 = choice not in qualified_explicit_options

        test = test1 and test2 and test3

        if test:
            print("Wrong input")

    if choice == options[0] \
            or choice == explicit_options[0] \
            or choice == qualified_explicit_options[0]:
        weapon_interaction()
    else:
        no_interaction()

    # game end


def game_end():
    print_pause("GAME OVER")

    replay_choice = str(
        input("would you like to replay?\n"
              "[yes or y for yes / anything else for no]\n")
    )

    if replay_choice == "yes" \
            or replay_choice == "y":
        print("restarting the game in 3 seconds\n")
        simulate_loading()  # loading for 3 seconds
        play_game()  # replay game

    print("see you later alligator...\n")  # reached only if exit


# play game


def play_game():
    # clear the screen

    clear_screen()

    # display introduction

    introduction()

    # get player name

    player_name = get_player_name()
    print_pause("hey " + player_name + "\n")

    # display places

    print_places()

    # let user choose place

    place_choice = get_chosen_place()
    print_pause("You are in " + place_choice + "\n")

    # let user choose weapon

    current_weapon = get_chosen_weapon()
    print_pause("You have " + current_weapon + "\n")

    # summarize situation

    print_pause("you are in " +
                place_choice +
                " and you have " +
                current_weapon)

    # enemy spawn

    enemy_spawn(place_choice)

    # enemy interaction

    enemy_interaction()

    # game end

    game_end()


# - Main Program


play_game()
