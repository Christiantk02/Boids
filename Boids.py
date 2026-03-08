import pygame
import random
import numpy as np

# Parameters
fps = 60
width, height = 1200, 1200

number_of_boids = 100

max_speed = 5
view_radius = 50

separation_weight = 1
alignment_weight = 0.5
cohesion_weight = 0.01

# Boid Class
class Boid:
    def __init__(self, x, y, view_radius, max_speed, separation_weight, alignment_weight, cohesion_weight):
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.random.rand(2) * 2 - 1
        self.acceleration = np.zeros(2)

        self.view_radius = view_radius
        self.max_speed = max_speed

        self.velocity *= self.max_speed

        self.separation_weight = separation_weight
        self.alignment_weight = alignment_weight
        self.cohesion_weight = cohesion_weight

    def update(self):

        self.velocity += self.acceleration

        speed = np.linalg.norm(self.velocity)

        if speed > self.max_speed:
            self.velocity = (self.velocity / speed) * self.max_speed

        self.position += self.velocity
        self.acceleration = np.zeros(2)

        self.position = self.position % np.array([width, height])

    def applyForce(self, boids):
        velocities = 0
        positions = 0
        count = 0
        for boid in boids:
            diff = self.position - boid.position
            if boid is not self and (diff[0]**2 + diff[1]**2) < self.view_radius**2:
                positions += boid.position
                velocities += boid.velocity
                count += 1

                diff = self.position - boid.position
                distance = np.linalg.norm(diff)

                if distance > 0:
                    self.acceleration += (diff / distance) * self.separation_weight

        if count > 0:
            average_velocity = velocities / count
            self.acceleration += (average_velocity - self.velocity) * self.alignment_weight

            average_positions = positions / count
            self.acceleration += (average_positions - self.position) * self.cohesion_weight


# Initialize pygame
pygame.init()
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


# Initialize boids
boids = []
for i in range(number_of_boids):
    x = random.randint(0, width)
    y = random.randint(0, height)
    boids.append(Boid(x, y, view_radius, max_speed, separation_weight, alignment_weight, cohesion_weight))


# Main loop
running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))

    for boid in boids:
        boid.applyForce(boids)
        boid.update()
        pygame.draw.circle(win, (255,255,255), boid.position.astype(int), 5)

    pygame.display.update()

pygame.quit()