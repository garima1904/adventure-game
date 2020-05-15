import time
import random

def print_msg(msg):
    print(msg)
    time.sleep(2)

def start(item, option):
    print_msg("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.\n")
    print_msg("Rumor has it that a "+str(option)+" is somewhere around "
                "here, and has been terrifying the nearby village.\n")
    print_msg("In front of you is a house.\n")
    print_msg("To your right is a dark Cave.\n")
    print_msg("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")

def game_cave(item, option):
    if "sword" in item:
        print_msg("\nYou peer cautiously into the game_cave.")
        print_msg("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty Cave"
                    " now.")
        print_msg("\nYou walk back to the field.\n")
    else:
        print_msg("\nYou peer cautiously into the Cave.")
        print_msg("\nIt turns out to be only a very small Cave.")
        print_msg("\nYour eye catches a glint of metal behind a "
                    "rock.")
        print_msg("\nYou have found the magical Sword of Ogoroth!")
        print_msg("\nYou discard your silly old dagger and take "
                    "the sword with you.")
        print_msg("\nYou walk back out to the field.\n")
        item.append("sword")
    field(item, option)

def game_door(item, option):
    print_msg("\nYou approach the game_door of the house.")
    print_msg("\nYou are about to knock when the game_door "
                f"opens and out steps a {option}.")
    print_msg(f"\nEep! This is the {option}'s house!")
    print_msg(f"\nThe {option} attacks you!\n")
    if "sword" not in item:
        print_msg("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    while True:
        response = input("Would you like to (1) fight or (2) run away?")
        if response == "1":
            if "sword" in item:
                print_msg(f"\nAs the {option} moves to attack, "
                            "you unsheath your new sword.")
                print_msg("\nThe Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_msg(f"\nBut the {option} takes one look at "
                            "your shiny new toy and runs away!")
                print_msg(f"\nYou have rid the town of the {option}"
                            ". You are victorious!\n")
            else:
                print_msg("\nYou do your best...")
                print_msg(f"but your dagger is no match for the {option}.")
                print_msg("\nYou have been defeated!\n")
            play_again()
            break
        if response == "2":
            print_msg("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            field(item, option)
            break

def field(item, option):
    print_msg("Enter 1 to knock on the Door of the house.")
    print_msg("Enter 2 to peer into the Cave.")
    print_msg("What would you like to do?")
    while True:
        response = input("(Please enter 1 or 2.)\n")
        if response == "1":
            game_door(item, option)
            break
        elif response == "2":
            game_cave(item, option)
            break

def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_msg("\n\n\nExcellent! Restarting the game ...\n\n\n")
        play()
    elif again == "n":
        print_msg("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()

def play():
    item = []
    option = random.choice(["dracula", "pirate", "dragon", "troll",
                            "thief"])
    start(item, option)
    field(item, option)

play()
