import time
from weapons import dagger  # Function for choosing a weapon.
from weapons import stick  # Function for choosing a weapon.
from weapons import axe  # Function for choosing a weapon.
import sys


weapon1 = ""
weapon2 = ""
weapon3 = ""


def intro():

    play = "Y"

    while play == "Y" not in "N":  # Loop for restarting the game.
        print("You wake up in a dark room...")
        time.sleep(2)
        print("A stranger appears before you...")
        time.sleep(1)
        player = input("Stranger: What is your name?: ")
        time.sleep(1)
        print("Stranger: Hello there", player + "!")
        time.sleep(1)
        print("Stranger: The world you once knew is no more...")
        time.sleep(2)
        print("Stranger: The living dead now walks the surface of the earth...")
        time.sleep(2)
        print("Stranger: If you want to survive out there, you will need one of these...")
        print("")
        time.sleep(2)
        print("The stranger gives you an option to choose from three different weapons:\n"
              "A: A dagger.\n"
              "B: A stick.\n"
              "C: An axe.")
        chooseweapon = input("Please choose a weapon: ")

        weapon1 = dagger()
        weapon2 = stick()
        weapon3 = axe()

        while chooseweapon != "A" and chooseweapon != "B" and chooseweapon != "C":  # Input validation
            chooseweapon = input("Please choose a weapon: ")

        if chooseweapon == "A":
            print("You have been given a " + weapon1 + ".")
        elif chooseweapon == "B":
            print("You have been given a " + weapon2 + ".")
        elif chooseweapon == "C":
            print("You have been given an " + weapon3 + ".")

        time.sleep(2)
        print("Stranger: Great! Now you are set...")
        time.sleep(2)
        print("Stranger: The dead ones are about to overrun this place, we must escape! ")
        time.sleep(2)
        print("You have two choices to exit this building.")
        print("Do you want to:")
        print("A: Exit through the window.")
        print("B: Climb to the rooftop.")
        choice = input("Enter your choice: ")

        while choice != "A" and choice != "B" and choice != "C":  # Another input validation
            choice = input("You can't go there. Please try a valid exit: ")

        # Choice A
        if choice == "A" and chooseweapon == "A":
            print("You find three zombies outside the window, you manage to take down two of them but the third one\n"
                  "bit your neck.")
            time.sleep(1)
            print("You died, " + player + ".")
            play = input("Do you wish to restart? Y/N: ")
            while play != "Y" and play != "N":
                play = input("Invalid choice, please type Y or N: ")
            while play == "N":
                time.sleep(1)
                print("Okay, Goodbye " + player + "!")
                time.sleep(3)
                sys.exit()
        elif choice == "A" and chooseweapon == "B":
            print("You find three zombies outside the window, your stick is completely useless and you quickly\n"
                  " get overwhelmed.")
            print("You died, " + player + ".")
            play = input("Do you wish to restart? Y/N: ")
            while play != "Y" and play != "N":
                play = input("Invalid choice, please type Y or N: ")
            while play == "N":
                time.sleep(1)
                print("Okay, Goodbye " + player + "!")
                time.sleep(3)
                sys.exit()
        elif choice == "A" and chooseweapon == "C":
            print("You find three zombies outside the window and manage to take all of them down\n"
                  " with your axe.")
            time.sleep(2)
            print("You got out of the building, now the real journey begins.")
            print("To be continued...")
            play = input("Do you wish to restart? Y/N: ")
            while play != "Y" and play != "N":
                play = input("Invalid choice, please type Y or N: ")
            while play == "N":
                time.sleep(1)
                print("Okay, Goodbye " + player + "!")
                time.sleep(3)
                sys.exit()

        # Choice B
        elif choice == "B" and chooseweapon == "A":
            print("You climb the ladder and arrive on the rooftop.")
            print("You get spotted by a military helicopter and quickly conceal your dagger.")
            print("They let you aboard.")
            print("To be continued...")
            play = input("Do you wish to restart? Y/N: ")
            while play != "Y" and play != "N":
                play = input("Invalid choice, please type Y or N: ")
            while play == "N":
                time.sleep(1)
                print("Okay, Goodbye " + player + "!")
                time.sleep(3)
                sys.exit()
        elif choice == "B" and chooseweapon == "B":
            print("You climb the ladder and arrive on the rooftop.")
            print("You get spotted by a military helicopter.")
            print("They see you as a threat and start shooting at you.")
            print("You died, " + player + ".")
            play = input("Do you wish to restart? Y/N: ")
            while play != "Y" and play != "N":
                play = input("Invalid choice, please type Y or N: ")
            while play == "N":
                time.sleep(1)
                print("Okay, Goodbye " + player + "!")
                time.sleep(3)
                sys.exit()
        elif choice == "B" and chooseweapon == "C":
            print("You climb the ladder and arrive on the rooftop.")
            print("You get spotted by a military helicopter.")
            print("They see you as a threat and start shooting at you.")
            print("You died, " + player + ".")
            play = input("Do you wish to restart? Y/N: ")
            while play != "Y" and play != "N":
                play = input("Invalid choice, please type Y or N: ")
            while play == "N":
                time.sleep(1)
                print("Okay, Goodbye " + player + "!")
                time.sleep(3)
                sys.exit()
intro()

