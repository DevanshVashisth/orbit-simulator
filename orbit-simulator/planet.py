import numpy as np  

class Planet:
    def __init__(self, position, velocity, mass):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = float(mass)
        self.force = np.zeros(2)
        self.acceleration =np.array([0.0,0.0])
    def update(self,dt):
        acceleration = self.force/self.mass
        self.velocity += acceleration*dt
        self.position += self.velocity *dt
