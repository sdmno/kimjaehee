import pygame

class tower :
    def __init__(self):
        self.x = 0
        self.y = 0
        self.is_support = False
        self.width = 0
        self.height = 0
        self.damage = 1
        self.plus_damage = 0
        self.range = 100
        self.speed = 1
        self.level = 0
        self.attack = 0
        self.timer = 0
        self.selected = False
        self.attack_on = False
        self.upgrade_price = [50, 100, 150]
        self.sell_price = [25, 50, 75]
        self.Timage = []
        self.Timage.append(pygame.image.load("tower/normal_tower1.png"))
        self.Timage.append(pygame.image.load("tower/normal_tower2.png"))
        self.sell = pygame.image.load("tower/sell.png")
        self.upgrade = pygame.image.load("tower/upgrade.png")


    def blit_tower(self, screen):
        self.draw_menu(screen)
        self.draw_surface(screen)
        screen.blit(self.Timage[self.attack], \
                    (self.x - self.Timage[self.attack].get_width()/2, self.y - self.Timage[self.attack].get_height()/2))


    def select_tower(self, X, Y):         #마우스 X좌표 Y좌표
        if X <= self.x + self.width/2 and X >= self.x - self.width/2 :
            if Y <= self.y + self.height/2 and Y >= self.y - self.height/2 :
                return True
        return False

    def draw_menu(self, screen):
        if self.selected:
            screen.blit(self.sell, (400, 650))
            screen.blit(self.upgrade, (620, 650))

    def draw_surface(self, screen):
        if self.selected:
            surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            screen.blit(surface, (self.x - self.range, self.y - self.range))

    def build_tower(self, x, y):
        self.x = x
        self.y = y
        self.width = self.Timage[self.attack].get_width()
        self.height = self.Timage[self.attack].get_height()

    def sell_tower(self):
        return self.sell_price[self.level]

    def upgrade_tower(self):
        self.level += 1
        self.range += 25
        self.damage += 1
        return self.upgrade_price[self.level]

    def tower_attack(self):
        self.attack += 1
        self.attack %= 2







