# Boids Flocking Simulation

## Description

This project implements a **real-time flocking simulation** using **Pygame** and **NumPy**.  
The simulation models the collective movement of agents (called **boids**) based on simple behavioral rules.

Each boid follows three local interaction rules inspired by natural flocking behavior seen in birds and fish:

- **Separation** – avoid crowding nearby boids.
- **Alignment** – match velocity with neighboring boids.
- **Cohesion** – move toward the average position of nearby boids.

These simple rules produce complex, emergent group behavior where the boids move together in a coordinated swarm.

The simulation uses **periodic boundary conditions**, meaning boids that exit one side of the screen reappear on the opposite side.

---

## Installation

To run the code, install the required Python packages:

```
pip install pygame numpy
```

---

## Usage

1. Run the Python script.
2. A window will open displaying the boids simulation.
3. Boids will automatically move and interact based on the flocking rules.
4. The simulation continues until the window is closed.

You can experiment with different behaviors by modifying parameters such as:

- `number_of_boids`
- `max_speed`
- `view_radius`
- `separation_weight`
- `alignment_weight`
- `cohesion_weight`

Changing these values can significantly affect the swarm dynamics.

---

## Simulation Parameters

The following parameters control the behavior of the system:

- **number_of_boids** – number of agents in the simulation.
- **max_speed** – maximum velocity of each boid.
- **view_radius** – distance within which other boids influence behavior.
- **separation_weight** – strength of collision avoidance.
- **alignment_weight** – strength of velocity matching.
- **cohesion_weight** – strength of movement toward neighbors.

---

## References

- Craig Reynolds, *Flocks, Herds, and Schools: A Distributed Behavioral Model* (1987)
- ChatGPT-generated structure and Markdown formatting for README.