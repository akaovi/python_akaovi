# 烟花
import random
import sys

import pygame

colorList = [(0, 245, 255), (0, 238, 238), (0, 255, 255), (255, 218, 185), (255, 255, 240), (245, 245, 245), (255, 250,
                                                                                                              205),
             (255, 228, 225), (121, 205, 205), (0, 238, 118), (255, 255, 0), (205, 92, 92), (255, 106, 106),
             (250, 128, 114), (250, 20, 147), (238, 44, 44), (232, 232, 232)]


class Fireworks:
    def __init__(self):
        self.x = random.randint(47, 747)
        self.y = 600
        self.vy = -10
        self.a = 0.1
        self.color = (244, 96, 108)
        self.ifBoom = False
        self.isBoom = False

    def update(self):
        if self.vy < 0:
            self.y += self.vy
            self.vy += self.a
        else:
            self.ifBoom = True


class Boom:
    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y
        self.vy = random.random()+random.randint(1, 3)
        self.vx = random.random()+random.randint(1, 3)
        self.fx = random.choice([1, -1])  # 左右方向
        self.fy = random.choice([1, -1])  # 上下方向

        # 改造成为合加速度为0删除颗粒
        self.a = 0.05  # 加速度
        self.ifPop = False

    def update(self):
        if self.fx == 1 and self.vx > 0:
            self.x += self.vx
            self.vx -= self.a
        if self.fx == -1 and self.vx > 0:
            self.x -= self.vx
            self.vx -= self.a
        if self.fy == 1 and self.vy > -5:
            self.y -= self.vy
            self.vy -= self.a
        if self.fy == -1 and self.vy > 0:
            self.y += self.vy
            self.vy -= self.a
        if self.vy <= 0 and self.vx <= 0:
            self.ifPop = True


def main():
    pygame.init()
    size = width, height = 800, 600
    color = (0, 0, 0)
    pygame.display.set_caption('烟花')

    fps = 120
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)
    fireworks = []  # 烟花
    boomedFireworks = []  # 爆炸的颗粒

    CREATEFIREWORK = pygame.USEREVENT + 1
    pygame.time.set_timer(CREATEFIREWORK, 277)

    while True:
        screen.fill(color)

        clock.tick(fps)

        if fireworks:
            for index, f in enumerate(fireworks):
                f.update()
                if f.ifBoom:
                    choiceColor = random.choice(colorList)
                    for i in range(77):
                        boomedFireworks.append(Boom(f.x, f.y, choiceColor))
                    del fireworks[index]
                pygame.draw.rect(screen, f.color, (f.x, f.y, 4, 7), 0)

        if boomedFireworks:
            for index2, b in enumerate(boomedFireworks):
                b.update()
                if b.ifPop:
                    del boomedFireworks[index2]
                pygame.draw.rect(screen, b.color, (b.x, b.y, 4, 4), 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == CREATEFIREWORK:
                fireworks.append(Fireworks())

        pygame.display.update()


if __name__ == "__main__":
    main()

