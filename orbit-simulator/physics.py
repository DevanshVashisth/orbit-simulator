import numpy as np


G = 6.67430e-11

def gravitaional_force(m1,m2,r):
    distance = np.linalg.norm(r)
    force = G *m1*m2/distance**2
    return force * r/distance

def total_angular_momentum(planets):
    L =0

    for planet in planets:
        x = planet.position[0]
        y = planet.position[1]

        vx = planet.velocity[0]
        vy = planet.velocity[1]

        L += planet.mass *(x*vy-y*vx)
    return L