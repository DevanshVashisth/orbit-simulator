from physics import gravitaional_force
import numpy as np

G = 6.67430e-11

def compute_forces(planets):

    for planet in planets:
        planet.force[:] = 0

    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):

            p1 = planets[i]
            p2 = planets[j]

            r = p2.position - p1.position

            force = gravitaional_force(p1.mass, p2.mass, r)

            p1.force += force
            p2.force -= force

    for p in planets:
        p.acceleration = p.force / p.mass


def total_energy(planets):

    KE = 0
    PE = 0

    for p in planets:

        v = np.linalg.norm(p.velocity)

        KE += 0.5 * p.mass * v**2

    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):

            r = np.linalg.norm(
                planets[i].position - planets[j].position
            )

            PE -= (
                G
                * planets[i].mass
                * planets[j].mass
                / r
            )

    return KE + PE


def varlet_step(planets, dt):

    old_positions = []

    for planet in planets:

        old_positions.append(planet.position.copy())

        planet.position += (
            planet.velocity * dt
            + 0.5 * planet.acceleration * dt**2
        )

    new_positions = []

    for planet in planets:
        new_positions.append(planet.position.copy())

    old_accelerations = [
        planet.acceleration.copy()
        for planet in planets
    ]

    compute_forces(planets)

    for i, planet in enumerate(planets):

        planet.velocity += (
            0.5
            * (
                old_accelerations[i]
                + planet.acceleration
            )
            * dt
        )

    old_earth = old_positions[3] - old_positions[0]
    new_earth = new_positions[3] - new_positions[0]
    dr = new_earth - old_earth

    area_swept = (
        0.5
        *
        abs(
            old_earth[0]*dr[1]
            -
            old_earth[1]*dr[0]
        )
    ) /dt

    return area_swept
def log_scale(position, scale =1e10):
    r = np.linalg.norm(position)
    if r==0:
        return position
    r_scaled = np.log1p(r/scale) * scale
    return position /r*r_scaled