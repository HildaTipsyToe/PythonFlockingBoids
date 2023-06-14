import random
import pygame
import win32api
from Boids import Boids

vector = pygame.math.Vector2
clock = pygame.time.Clock()
math = pygame.math


class MainProgram:
    def __init__(self):
        pygame.init()
        self.running = True
        self.width = 1280
        self.height = 720

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Boids simulation test drive')

        # print(self.getRefreshRate(win32api.EnumDisplayDevices())) #Check clients refresh rate
        self.fps = self.getRefreshRate(win32api.EnumDisplayDevices())
        self.clock = pygame.time.Clock()

        self.form = pygame.draw.polygon(self.window, (0, 255, 255), ((10, 10), (23, 15), (10, 20)))

        self.BoidsCount = 200
        self.identity = 0
        self.radius = 6
        self.bSeparation = 0.5
        self.bAcceleration = 0.3
        self.bCohesion = 0.5
        self.Boids = []

        self.maxSpeed = 2

        for boids in range(self.BoidsCount):
            self.Boids.append(
                Boids(random.randint(0 + self.radius * 2, self.width - self.radius * 2), random.randint(0 +
                 self.radius * 2, self.height - self.radius * 2),  self.radius, pygame.math.Vector2(5, 5), self.identity))
            self.identity += 1

    def getRefreshRate(self, Device):
        settings = win32api.EnumDisplaySettings(Device.DeviceName, -1)
        return getattr(settings, 'DisplayFrequency')

    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        MainProgram()

            self.window.fill((255, 255, 255))
            for boids in self.Boids:
                boids.update(self.window, self.width, self.height, self.Boids, self.maxSpeed)
                boids.draw(self.window)
            pygame.display.update()
            self.clock.tick(self.fps)
        pygame.quit()


MainProgram().run()
