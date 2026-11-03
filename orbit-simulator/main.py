import numpy as np
import matplotlib.pyplot as plt

from planet import Planet
from simulation import compute_forces, log_scale, total_energy, varlet_step
from physics import total_angular_momentum


# =========================
# PLANETS
# =========================

sun = Planet([0, 0], [0, 0], 1.989e30)

earth = Planet(
    [1.5e11, 0],
    [0, 30000],
    5.97e24
)

mars = Planet(
    [2.2e11, 0],
    [0, 24000],
    6.39e23
)

venus = Planet(
    [1.1e11, 0],
    [0, 35000],
    4.87e24
)

mercury = Planet(
    [5.8e10, 0],
    [0, 47000],
    3.3e23
)

jupiter = Planet(
    [7.8e11, 0],
    [0, 13000],
    1.9e27
)

saturn = Planet(
    [1.4e12, 0],
    [0, 9600],
    5.68e26
)

uranus = Planet(
    [2.9e12, 0],
    [0, 6800],
    8.68e25
)

neptune = Planet(
    [4.5e12, 0],
    [0, 5400],
    1.02e26
)

planets = [
    sun,
    mercury,
    venus,
    earth,
    mars,
    jupiter,
    saturn,
    uranus,
    neptune
]


# =========================
# VISUAL SETTINGS
# =========================

planet_colors = [
    "#FFD700",
    "#B0B0B0",
    "#E6C97A",
    "#2E86C1",
    "#C1440E",
    "#D2B48C",
    "#F4D03F",
    "#85C1E9",
    "#2874A6"
]

planet_sizes = [
    22,
    6,
    8,
    9,
    7,
    14,
    12,
    11,
    11
]

planet_names = [
    "Sun",
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
]


# =========================
# FIGURE
# =========================

plt.style.use("dark_background")

fig, ax = plt.subplots(figsize=(12, 12))

fig.patch.set_facecolor('black')
ax.set_facecolor("black")

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xlim(-1.2e11, 1.2e11)
ax.set_ylim(-1.2e11, 1.2e11)

ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])

# fill the whole figure — do NOT call set_title inside the loop
ax.set_position([0.0, 0.0, 1.0, 1.0])


# =========================
# STARFIELD
# =========================

np.random.seed(42)

star_x = np.random.uniform(-2.3e11, 2.3e11, 300)
star_y = np.random.uniform(-2.3e11, 2.3e11, 300)
star_sizes = np.random.uniform(0.5, 3.0, 300)

ax.scatter(
    star_x,
    star_y,
    s=star_sizes,
    color="white",
    alpha=0.7,
    zorder=0
)


# =========================
# GLOWING SUN
# =========================

for glow_size, alpha in zip(
    [1200, 800, 500],
    [0.03, 0.05, 0.08]
):
    ax.scatter(
        [0],
        [0],
        s=glow_size,
        color="#FFD700",
        alpha=alpha,
        zorder=1
    )


# =========================
# TITLE (once, as text inside axes)
# =========================

ax.text(
    0.5, 0.02,          # bottom center
    "Computational Solar System Simulation",
    transform=ax.transAxes,
    color="white",
    fontsize=13,
    ha="center",
    va="bottom",
    family="monospace",
    zorder=5
)


# =========================
# PLANET OBJECTS
# =========================

planet_dots = []
planet_trails = []

planet_paths_x = [[] for _ in planets]
planet_paths_y = [[] for _ in planets]

for color, size in zip(planet_colors, planet_sizes):

    trail, = ax.plot(
        [], [],
        color=color,
        linewidth=1.0,
        alpha=0.6,
        zorder=2
    )

    dot, = ax.plot(
        [], [],
        "o",
        color=color,
        markersize=size,
        zorder=3
    )

    planet_trails.append(trail)
    planet_dots.append(dot)


# =========================
# HUD TEXT
# =========================

info_text = ax.text(
    0.02, 0.97,
    "",
    transform=ax.transAxes,
    color="white",
    fontsize=11,
    verticalalignment="top",
    family="monospace",
    zorder=5
)


# =========================
# SIMULATION SETUP
# =========================

dt = 60 * 60 * 24

compute_forces(planets)

energies = []
angularies = []
areas = []

time = 0


# =========================
# MAIN LOOP
# =========================

plt.ion()

for step in range(5000):

    area_swept = abs(varlet_step(planets, dt))
    areas.append(area_swept)

    E = total_energy(planets)
    L = total_angular_momentum(planets)

    energies.append(E)
    angularies.append(L)

    time += dt

    for i, planet in enumerate(planets):

        pos_scaled = log_scale(planet.position)
        x = pos_scaled[0]
        y = pos_scaled[1]

        planet_paths_x[i].append(x)
        planet_paths_y[i].append(y)

        max_trail = 700
        if len(planet_paths_x[i]) > max_trail:
            planet_paths_x[i] = planet_paths_x[i][-max_trail:]
            planet_paths_y[i] = planet_paths_y[i][-max_trail:]

        planet_dots[i].set_data([x], [y])
        planet_trails[i].set_data(planet_paths_x[i], planet_paths_y[i])

    info_text.set_text(
        f"TIME : {time/(60*60*24):.1f} days\n\n"
        f"TOTAL ENERGY :\n{E:.3e}\n\n"
        f"ANGULAR MOMENTUM :\n{L:.3e}\n\n"
        f"TIMESTEP :\n{dt/3600:.1f} hours"
    )

    plt.pause(0.0001)

plt.ioff()


# =========================
# ANALYSIS PLOTS
# =========================

initial_energy = energies[0]
energy_error = [(E - initial_energy) / abs(initial_energy) for E in energies]

plt.figure(figsize=(10, 5))
plt.plot(energy_error, linewidth=1.5, color="#00FFFF")
plt.title("Energy vs Time")
plt.xlabel("Time Step")
plt.ylabel("Relative Energy Error")
plt.grid(alpha=0.3)

plt.figure(figsize=(10, 5))
plt.plot(angularies, linewidth=1.5, color="#FFD700")
plt.title("Angular Momentum vs Time")
plt.xlabel("Time Step")
plt.ylabel("Angular Momentum")
plt.grid(alpha=0.3)

plt.figure(figsize=(10, 5))
plt.plot(areas, linewidth=1.5, color="#00FF7F")
plt.title("Kepler Second Law")
plt.xlabel("Time Step")
plt.ylabel("Area Swept per Unit Time")
plt.grid(alpha=0.3)

plt.show()