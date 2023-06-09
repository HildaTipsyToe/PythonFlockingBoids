import math
import random
import pygame

vector3 = pygame.math.Vector3
vector = pygame.math.Vector2


class Boids:
    # self.form = pygame.draw.polygon(self.window, (0, 255, 255))
    def __init__(self, x=100, y=100, radius=3, vel=vector(1, 1), identity=0, color=(0, 0, 0)):
        self.identity = identity
        self.position = vector(x, y)
        self.color = color
        self.acc = vector()
        self.vel = self.getRandomDirection(vel)
        self.radius = radius
        self.numpoints = 300

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.radius)

    def update(self, window, width, height, Main_Boids, other_boids):
        self.vel += self.acc
        self.position += self.vel

        self.acc = vector()
        print(self.vel)

        if self.position.x > width:
            self.position.x = 0

        if self.position.x < 0:
            self.position.x = width

        if self.position.y > height:
            self.position.y = 0

        if self.position.y < 0:
            self.position.y = height
        self.avoidanceMethod(other_boids, window)
        pygame.draw.line(window, (0, 0, 0), self.position, self.position + self.vel, 2)

    def accelerate(self, acc):
        self.acc += acc

    def avoidanceMethod(self, other_boids, window):
        self.FieldOfView(window)
        for otherboid in other_boids:
            if otherboid.identity != self.identity:
                distancebetween = vector.distance_to(self.position, otherboid.position)
                #print(distancebetween," boids id: ", self.identity, " other boids id: ", otherboid.identity)
                if distancebetween < 25:
                    self.collisionMethod(otherboid, distancebetween)
                    if self.identity > otherboid.identity:
                        pass
                        #pygame.draw.line(window, (0,0,0), self.position, otherboid.position, 2)


    def collisionMethod(self, other_boids, distanceBetween=100):
        if self.radius + other_boids.radius + 1 >= distanceBetween:
            self.vel *= -1
            if self.color == (0,0,0):
                pass
                #self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            #return print("De rammer     id: ", self.identity, " og other id: ", other_boids.identity, "----------------------------")
            return print(self.vel, "------", self.identity)

    def randomMovement(self, window):
        pass

    def FieldOfView(self, window):
        pygame.draw.arc(window, (0, 0, 0), (self.position.x, self.position.y, 20, 20), math.pi/2, math.pi*2)

    def getRandomDirection(self, vel=vector()):
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
