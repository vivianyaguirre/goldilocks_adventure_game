# goldilocks_adventure.py 

from characters import Goldilocks, PapaBear, MamaBear, BabyBear
from locations import forest, cottage, around_cottage, kitchen, living_room, bedroom
import interactions

def start_game():

    player = Goldilocks()

    print("Welcome to the Goldilocks Adventure Game!")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! You are now playing as {player.name}")

    papa_bear = PapaBear()
    mama_bear = MamaBear()
    baby_bear = BabyBear()

    current_location = forest
    entered_bedroom = False
    entered_kitchen = False
 
    while True:
        if current_location == forest:
            print(current_location.name)
            choice = input("Do you want to go north to the cottage? (yes/no): ").lower()

            if choice == "yes":
                current_location = cottage
                print(f"You are now at {current_location.name}.")
                break  # Exit the loop and move to the next part of the storyline
            elif choice == "no":
                print("You stay in the forest.")
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

    while True:
        if current_location == cottage:
            choice = input("Do you want to walk around the cottage or enter it? (walk/enter): ").lower()
            if choice == "walk":
                current_location = around_cottage
                print(f"You are now at {current_location.name}.")
                # New scenario when walking around the cottage
                print("You hear noises. It's getting dark, and you need to decide quickly.")
                choice = input("Do you want to run to the closest door to get inside the house or go into the deep woods? (door/woods): ").lower()
                if choice == "door":
                    current_location = kitchen
                    print(f"You quickly run to the door and get inside. You are now at {current_location.name}.")
                    entered_kitchen = True
                elif choice == "woods":
                    print("You run into the deep woods and get lost. You have to find your way back.")
                    current_location = forest
                else:
                    print("Invalid choice. Please enter 'door' or 'woods'.")
            elif choice == "enter":
                current_location = kitchen
                print(f"You are now at {current_location.name}.")
                entered_kitchen = True
            else:
                print("Invalid choice. Please enter 'walk' or 'enter'.")

        elif current_location == kitchen:
            while True:
                choice = input("Do you want to try the porridge or explore the house? (porridge/explore): ").lower()
                if choice == "porridge":
                    print("You see three bowls of porridge, each one steaming and smelling delicious.")
                    while True:
                        bowl_choice = input("Do you want to try the large, medium, or small bowl? (large/medium/small): ").lower()
                        if bowl_choice == "large":
                            print("The porridge is too hot! You move on to the next bowl.")
                        elif bowl_choice == "medium":
                            print("The porridge is too cold! You move on to the next bowl.")
                        elif bowl_choice == "small":
                            print("The porridge is just right! You eat it all up.")
                            break
                        else:
                            print("Invalid choice. Please enter 'large', 'medium', or 'small'.")
                    break
                elif choice == "explore":
                    current_location = living_room
                    entered_kitchen = True
                    break
                else:
                    print("Invalid choice. Please enter 'porridge' or 'explore'.")

        if entered_kitchen:
            print("You hear noises getting closer and see bushes rustling with a big furry creature coming towards the cottage.")
            choice = input("Do you want to enter the bedroom in fright? (yes/no): ").lower()
            if choice == "yes":
                current_location = bedroom
                print(f"You quickly run to the bedroom. You are now at {current_location.name}.")
                entered_bedroom = True
            elif choice == "no":
                print("You decide to stay in the kitchen.")
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

        if entered_bedroom:
            while True:
                choice = input("Do you want to try the beds or leave the cottage? (sleep/leave): ").lower()
                if choice == "sleep":
                    print("You try the beds.")
                    print("The bears come home and find you!")

                    # Interaction with bears
                    print(f"{papa_bear.name}: {papa_bear.description}")
                    print(f"{mama_bear.name}: {mama_bear.description}")
                    print(f"{baby_bear.name}: {baby_bear.description}")

                    while True:
                        response = input("Do you want to apologize or run away? (apologize/run): ").lower()
                        if response == "apologize":
                            print("You apologize to the bears.")
                            print("Congratulations! You've completed the adventure.")
                            return  # End the game
                        elif response == "run":
                            print("You run away.")
                            current_location = forest
                            break
                        else:
                            print("Invalid choice. Please enter 'apologize' or 'run'.")
                    break
                elif choice == "leave":
                    print("You leave the cottage.")
                    current_location = forest
                    break
                else:
                    print("Invalid choice. Please enter 'sleep' or 'leave'.")


if __name__ == "__main__":
    start_game()