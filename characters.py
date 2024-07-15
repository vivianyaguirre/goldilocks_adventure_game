# characters.py

# This module defines classes to represent characters in a text-based adventure game.

# Classes:
# - Character: A base class representing a generic character with a name and description.
# - Goldilocks: Subclass of Character, representing the protagonist Goldilocks.
# - Bear: Subclass of Character, representing various bears in the game.

# Usage:
# Characters in the game are represented with attributes such as name and description,
# allowing for different interactions and scenarios based on their roles in the game's story.

class Character:

    def __init__(self, name, description):

        self.name = name 
        self.description = description

class Goldilocks(Character):
    
    def __init__(self): 
        super().__init__("Goldilocks", "A curious little girl.")

class Bear(Character): 

    def __init__(self, name, description):
        super().__init__(name, description)

class PapaBear(Bear): 
    def __init__(self):
        super().__init__("Papa Bear", "Be careful, he is very protective of his house.")

class MamaBear(Bear): 
    def __init__(self):
        super().__init__("Mama Bear", "Be careful, she is protective of her child.")
    
class BabyBear(Bear): 
    def __init__(self):
        super().__init__("Baby Bear", "He won't bite...Of so we think.")

