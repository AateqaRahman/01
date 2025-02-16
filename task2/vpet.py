class VirtualPet:
    def __init__(self,name,energy=10,hunger=0):
        self.name_of_pet = name 
        self.energy_levels = energy
        self.hunger_levels = hunger
    
    def play(self):
        if self.energy_levels < 2:
            print ("Too tired to play")
        else:
            self.energy_levels -= 2
            self.hunger_levels += 2

    def feed(self):
        self.hunger_levels = max (0, self.hunger_levels - 3)
        
    def sleep(self):
        self.energy_levels += 10

    def __str__(self):
        return f"{self.name_of_pet} with {self.energy_levels} energy level and {self.hunger_levels} hunger level"
        
        
pass
