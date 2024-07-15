# goldilocks_adventure.py 

from characters import Goldilocks, PapaBear, MamaBear, BabyBear
from locations import forest, cottage, around_cottage, kitchen, living_room, bedroom
from game_data import current_location
import interactions

def start_game():

    player = Goldilocks()
    
    print("Welcome to the Goldilocks Adventure Game!")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! You are now playing as {player.name}")

    papa_bear = PapaBear()
    mama_bear = MamaBear()
    baby_bear = BabyBear()

   
    while True:  
        print(current_location.get_description())
        if current_location == forest: 
            choice = input("Do you want to go north to the cottage? Enter yes or no: "). lower()
            if choice == "yes":
                current_location = cottage
            else: 
                print("You stay.")

        elif current_location == cottage:
            choice = input("Do you want to walk around the cottage or enter it? (walk/enter): ").lower()
            if choice == "walk":
                current_location == around_cottage
            elif choice == "enter":
                current_location = kitchen # type: ignore
            else: 
                print("You stay outside the cottage, wondering why would someone want to live so deep in the woods.")

        elif current_location == around_cottage:
            choice = input("Do you want to peek into the windows or enter the cottage? (peek/enter): ").lower()
            if choice == "peek":
                print(interactions.peek_windows())
            current_location = cottage

        elif current_location == kitchen:
            choice = input("Do you want to try the porridge or explore the house? (eat/explore): ").lower()
            if choice == "eat":
                print(interactions.try_porridge())
                current_location = living_room
            elif choice == "explore":
                current_location = living_room
            else:
                print("You stay in the kitchen.")

        elif current_location == living_room:
            choice = input("Do you want to try the chairs or go to the bedroom? (sit/go): ").lower()
            if choice == "sit":
                print(interactions.try_chairs())
                current_location = bedroom
            elif choice == "go":
                current_location = bedroom
            else:
                print("You stay in the living room.")

        elif current_location == bedroom:
            choice = input("Do you want to try the beds or leave the cottage? (sleep/leave): ").lower()
            if choice == "sleep":
                print(interactions.try_beds())
                print("The bears come home and find you!")

                # Interaction with bears
                print(f"{papa_bear.name}: {papa_bear.description}")
                print(f"{mama_bear.name}: {mama_bear.description}")
                print(f"{baby_bear.name}: {baby_bear.description}")

                response = input("Do you want to apologize or run away? (apologize/run): ").lower()
                if response == "apologize":
                    print(interactions.apologize_to_bears())
                    print("Congratulations! You've completed the adventure.")
                    break
                else:
                    print(interactions.run_away())
                    current_location = forest
            elif choice == "leave":
                print("You leave the cottage.")
                current_location = forest
            else:
                print("You stay in the bedroom.")

if __name__ == "__main__":
    start_game()