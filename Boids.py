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
        self.boidsList = []
        self.FOWList = []
        self.FOW = 50

    def draw(self, window):
        pygame.draw.circle(window, self.color, self.position, self.radius)

    def update(self, window, width, height, other_boids, Max_speed):
        if self.identity == 0:
            self.radius = 10
            self.color = (0, 0, 255)  # Blå
        if self.identity == len(self.boidsList):
            self.color = (0, 255, 0)  # Grøn
        if self.identity == 15:
            self.color = (255, 0, 0)  # Rød

        if not self.boidsList:  # not kan bruges istedet for "self.boidsList == []"
            for boids in other_boids:
                if boids.identity != self.identity:
                    self.boidsList.append(boids)

        self.acc += self.steeredTowards(window)

        self.vel += self.acc

        if self.vel.length() > Max_speed:
            self.vel.scale_to_length(Max_speed)

        self.position += self.vel
        self.acc = vector()

        if self.position.x > width:
            self.position.x = 0

        if self.position.x < 0:
            self.position.x = width

        if self.position.y > height:
            self.position.y = 0

        if self.position.y < 0:
            self.position.y = height

        pygame.draw.line(window, (0, 0, 0), self.position, self.position + self.vel * 2, 2)
        pygame.draw.circle(window, (0, 0, 0), self.position, 50, width=1)

    '''if self.position.x + self.radius >= width or self.position.x - self.radius <= 0:
            self.position.x = -self.position.x

        if self.position.y + self.radius >= height or self.position.y - self.radius <= 0:
           self.position.y = -self.position.y'''


    def steeredTowards(self, window):
        self.FOWList = []
        CohesionMove = vector()

        for boids in self.boidsList:
            self.inSideFOW(boids, window)

        if self.FOWList == []:
            return vector()
        for boids in self.FOWList:
            dst = vector(boids.position.x - self.position.x, boids.position.y - self.position.y)
            if dst == 0:
                return vector()
            CohesionMove += vector.normalize(dst)

        CohesionMove /= len(self.FOWList)

        return CohesionMove


    def distance(self, window):
        self.FOWList = []
        acc = vector()

        for boids in self.boidsList:
            self.inSideFOW(boids, window)
        print(len(self.FOWList), "   -----   ", self.identity)
        if self.FOWList:
            for boids in self.FOWList:
                dst = vector(boids.position.x - self.position.x, boids.position.y - self.position.y)
                acc += vector.normalize(dst)
                print(len(self.FOWList))
        else:
            return vector.normalize(vector(self.vel))

        if not self.FOWList:
            acc /= len(self.FOWList)
            return acc

    def inSideFOW(self, boid, window):
        distance_between = vector.distance_to(self.position, boid.position)
        if distance_between < self.FOW and self.identity != boid.identity:
            pygame.draw.line(window, (0, 0, 0), self.position, boid.position, 1)
            self.FOWList.append(boid)

    def getDistanceInVectorNormalize(self, window):
        for boids in self.boidsList:
            if self.avoidanceMethod(boids, window):
                dst = vector(boids.position.x - self.position.x, boids.position.y - self.position.y)
                return vector.normalize(dst)
            else:
                return vector.normalize(vector(self.vel))

    def avoidanceMethod(self, boid, window):
        distance_between = vector.distance_to(self.position, boid.position)
        if distance_between < 50 and self.identity > boid.identity:
            pygame.draw.line(window, (0, 0, 0), self.position, boid.position, 1)
            print(self.identity, " hvem kigger den efter?: ", boid.identity)

    def collisionMethod(self, other_boids, distanceBetween=100):
        if self.radius + other_boids.radius + 1 >= distanceBetween:
            self.vel *= -1

    def getRandomDirection(self, vel=vector()):
        angle = 360 * random.random()
        xspeed = vel.x * math.sin(angle)
        yspeed = vel.y * math.cos(angle)
        return vector(xspeed, yspeed)

    def separation(self):
        for boid in self.FOWList:
            if vector.distance_to(self.position, boid.position) < self.FOW/2:


    def alignment(self):
        pass

    def cohesion(self):
        pass
