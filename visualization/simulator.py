import pygame

class Simulator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Smart Traffic System")
        self.clock = pygame.time.Clock()

        self.car_img = pygame.image.load("assets/car.png")
        self.car_img = pygame.transform.scale(self.car_img, (20, 40))

        self.cars = []

    def spawn_cars(self, state):
        self.cars = []
        for i, count in enumerate(state):
            for j in range(int(count)):
                if i == 0:
                    self.cars.append([390, -j*40, 0, 2])
                elif i == 1:
                    self.cars.append([410, 800 + j*40, 0, -2])
                elif i == 2:
                    self.cars.append([800 + j*40, 390, -2, 0])
                elif i == 3:
                    self.cars.append([-j*40, 410, 2, 0])

    def update_cars(self):
        for car in self.cars:
            car[0] += car[2]
            car[1] += car[3]

    def draw(self, light_state):
        self.screen.fill((255, 255, 255))

        # Roads
        pygame.draw.rect(self.screen, (50,50,50), (350,0,100,800))
        pygame.draw.rect(self.screen, (50,50,50), (0,350,800,100))

        # Traffic lights
        if light_state == 0:
            color_ns = (0,200,0)
            color_ew = (200,0,0)
        elif light_state == 2:
            color_ns = (200,0,0)
            color_ew = (0,200,0)
        else:
            color_ns = (255,200,0)
            color_ew = (255,200,0)

        pygame.draw.circle(self.screen, color_ns, (370,370), 10)
        pygame.draw.circle(self.screen, color_ew, (430,430), 10)

        for car in self.cars:
            self.screen.blit(self.car_img, (car[0], car[1]))

        pygame.display.flip()
        self.clock.tick(60)