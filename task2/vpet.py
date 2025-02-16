class VirtualPet:
    def __init__(self,name,energy=10,hunger=0):
        self.name = name 
        self.energy = energy
        self.hunger = hunger
    
    def play(self):
        if self.energy < 2:
            print ("TOO tired to play")
        else:
            self.energy -= 2
            self.hunger += 2

    def feed(self):
        self.hunger = max (0, self.hunger - 3)

    def sleep(self):
        self.energy += 10

    def __str__(self):
        return f"{self.name} with {self.energy} energy points and {self.hunger} hunger level"
        
        
pass