# locations.py 

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
        self.items = []
        self.actions = [] 



    def add_item(self, item):
        self.items.appemd(item)

    def add_action(self, action):
        self.actions.append(action)

    def get_directions(self):
        return f"{self.name}: {self.description}"
    
forest = Location("Forest", "You are in a misty and dense forest. All you follow is a path leading north...or so you think is north")
cottage = Location("Cottage", "You see a small cottage peaking between the trees. It looks similar to your grandma's cottage.")
around_cottage = Location("Around the Cottage", "You are walking around the perimeter of the cottage, peeking into the windows.")
kitchen = Location("Kitchen", "You are in the kitchen and your stomach starts to rumble after smelling a familiar dish your grandma makes you.")
living_room = Location("Living Room", "You see three chairs with three bowls of steamy porridge perfectly placed in front of each chair.")
bedroom = Location("Bedroom", "You see three beds of different sizes.")
