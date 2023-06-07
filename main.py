import random
import pygame
import win32api
from Boids import Boids


clock = pygame.time.Clock()
math = pygame.math


class MainProgram:
    def __init__(self):
        pygame.init()
        self.running = True
        self.width = 1800
        self.height = 1000

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Boids simulation test drive')

        # print(self.getRefreshRate(win32api.EnumDisplayDevices())) #Check clients refresh rate
        self.fps = self.getRefreshRate(win32api.EnumDisplayDevices())
        self.clock = pygame.time.Clock()

        self.form = pygame.draw.polygon(self.window, (0, 255, 255), ((10, 10), (23, 15), (10, 20)))

        self.radius = 5
        self.BoidsCount = 200
        self.bSeparation = 0.5
        self.bAcceleration = 0.3
        self.bCohesion = 0.5
        self.Boids = []

        for boids in range(self.BoidsCount):
            self.Boids.append(
                Boids(random.randint(0 + self.radius * 2, self.width - self.radius * 2), random.randint(0 +
                 self.radius * 2, self.height - self.radius * 2), self.radius))

    def getRefreshRate(self, Device):
        settings = win32api.EnumDisplaySettings(Device.DeviceName, -1)
        return getattr(settings, 'DisplayFrequency')

    def run(self):
        while self.running == True:
            # limit the framerate and get the delta time
            dt = self.clock.tick(60)

            # convert the delta to seconds (for easier calculation)
            speed = 1/float(dt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        MainProgram()

            self.window.fill((255, 255, 255))
            for boids in self.Boids:
                boids.update(self.window, self.width, self.height)
                boids.draw(self.window)
            pygame.display.update()
            self.clock.tick(self.fps)
        pygame.quit()


MainProgram().run()
