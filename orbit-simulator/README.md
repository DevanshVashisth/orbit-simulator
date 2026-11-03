# Solar System Orbit Simulator

A Python-based N-body simulation of the Solar System, built to explore Newtonian gravity, orbital mechanics, and numerical methods.

This project started as an attempt to simulate the motion of Earth around the Sun. Over time, I expanded it to include the other planets and began exploring concepts such as energy conservation, angular momentum, and Kepler's Second Law.

The project is still a learning experience, and I am documenting both the results and the challenges I encounter along the way.

## Features

- **Newtonian Gravity:** Calculates gravitational forces between bodies using Newton's law of universal gravitation.
- **N-body Simulation:** Simulates the gravitational interactions between the Sun and eight planets.
- **Velocity Verlet Integration:** Uses a numerical integration method to update planetary positions and velocities.
- **Energy Tracking:** Calculates the total kinetic and potential energy of the system over time.
- **Angular Momentum:** Tracks the system's total angular momentum to observe its conservation.
- **Kepler's Second Law:** Estimates the area swept out by Earth's orbital radius vector over time.
- **Visualisation:** Uses Matplotlib to display planetary motion, orbital trails, and numerical analysis graphs.
- **Logarithmic Scaling:** Compresses the visual distance between planets to make the entire Solar System easier to observe.

## Technologies Used

- Python
- NumPy
- Matplotlib

## Project Structure

```text
orbit-simulator/
│
├── main.py          # Main simulation and visualisation
├── planet.py        # Planet class and physical properties
├── physics.py       # Gravitational force and angular momentum
├── simulation.py    # Numerical integration and energy calculations
│
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate into the project directory:

   ```bash
   cd orbit-simulator
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the simulation:

   ```bash
   python main.py
   ```

## Some Things I Explored

### 1. Energy Conservation

I tracked the total mechanical energy of the system, which is the sum of kinetic and gravitational potential energy.

The energy graph showed fluctuations rather than remaining perfectly constant. This led me to investigate how numerical integration and timestep size affect the accuracy of a simulation.

### 2. Angular Momentum Conservation

I also tracked the total angular momentum of the system. The graph remained nearly constant throughout the simulation, providing a useful way to examine the behaviour of the gravitational system.

### 3. Kepler's Second Law

I estimated the area swept out by Earth's position vector over each timestep.

The resulting graph showed fluctuations. I began exploring how numerical approximations, timestep size, and gravitational interactions with other planets can affect this result.

## Limitations and Future Improvements

This is a simplified simulation and has several limitations:

- The initial conditions are approximate.
- The simulation uses a finite timestep.
- The logarithmic scaling is only for visualisation and does not represent actual physical distances.
- The area-swept calculation is a numerical approximation.
- The model does not account for every physical effect influencing real planetary motion.

Some improvements I would like to explore in the future include:

- Investigating how timestep size affects numerical accuracy.
- Improving the analysis of energy conservation.
- Comparing simulated orbital behaviour with Kepler's laws.
- Experimenting with different initial conditions and gravitational systems.

## About This Project

I built this project to improve my understanding of Python, computational physics, and orbital mechanics.

Rather than treating the simulation as a finished product, I see it as an ongoing experiment. Building it has helped me understand how mathematical and physical concepts can be translated into working code, and how numerical approximations behave when applied to real-world systems.

**This project is a work in progress.**
