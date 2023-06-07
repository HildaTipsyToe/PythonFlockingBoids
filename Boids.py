import math
import random
import pygame

vector3 = pygame.math.Vector3
vector = pygame.math.Vector2


class Boids:
    # self.form = pygame.draw.polygon(self.window, (0, 255, 255))
    def __init__(self, x=100, y=100, radius=3, vel=vector(5, 5), color=(0, 0, 0)):
        self.position = vector(x, y)
        self.color = color
        self.vel = self.getspeed(vel)
        self.radius = radius
        self.numpoints = 300

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.radius)

    def update(self, window, width, height):
        self.vel += self.obstacleAvoidance()
        self.position += self.vel

        if self.position.x > width:
            self.position.x = 0

        if self.position.x < 0:
            self.position.x = width

        if self.position.y > height:
            self.position.y = 0

        if self.position.y < 0:
            self.position.y = height

        pygame.draw.line(window, (0, 0, 0),  self.position, self.position + self.vel, 2)


    def AvoidanceMethod(self, boids, other_boids):



    def obstacleAvoidance(self):
        goldenRatio = (1 + math.sqrt(5)) / 2
        angleIncrement = math.pi * 2 * goldenRatio

        for i in range(self.numpoints):
            t = i / self.numpoints
            inclination = math.acos(1-2*t)
            azimuth = angleIncrement * i

            xspeed = math.sin(inclination) * math.cos(azimuth)
            yspeed = math.sin(inclination) * math.sin(azimuth)
            print(vector(xspeed, yspeed)
)
            return vector(xspeed, yspeed)


#            dst = i / (self.numpoints - 1)
#            angle = 2 * math.pi *

    def getspeed(self, vel = vector()):
        angle = 360 * random.random()
        xspeed = vel.x * math.sin(angle)
        yspeed = vel.y * math.cos(angle)
        return vector(xspeed, yspeed)


    def separation(self):
        pass

    def alignment(self):
        pass

    def cohesion(self):
        pass
