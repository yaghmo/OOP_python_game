import pygame, numpy, time, os, sys, signal
from threading import Timer

WIDTH = 700
HEIGHT = 406
BACKGROUND = pygame.image.load("Assets/Ingame_bg.png")
TICK = 10
pygame.init()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def get_position(self):
        return (self.rect.x, self.rect.y)

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Player(Sprite):
    def __init__(self, num, startx, starty, step, health, movement_speed, attacking_speed, attacking_range, defending_range, blocking_time):
        super().__init__("Assets/p"+str(num)+"_front.png", startx, starty)
        self.stand_image = self.image
        self.jump_image = pygame.image.load("Assets/p"+str(num)+"_front.png")
        self.jump_image = pygame.image.load("Assets/p"+str(num)+"_front.png")
        self.jump_imageD = pygame.image.load("Assets/p"+str(num)+"_front.png")
        self.jump_imageG = pygame.image.load("Assets/p"+str(num)+"_front.png")
        self.attack_image = pygame.image.load("Assets/p"+str(num)+"_front.png")
        self.bloc_image = pygame.image.load("Assets/p"+str(num)+"_front.png")
        self.num = num
        self.walk_cycle = [pygame.image.load(
            f"Assets/p"+str(num)+"_front.png") for i in range(1, 12)]
        self.animation_index = 0
        self.facing_left = False

        self.step = step
        self.movement_speed = movement_speed
        self.jumpspeed = movement_speed

        self.on_def = False

        self.attacking_speed = attacking_speed
        self.attacking_range = attacking_range*60
        self.defending_range = defending_range
        self.blocking_time = TICK/blocking_time

        self.points = 0
        self.health = health
        self.vsp = 0
        self.gravity = 100
        self.min_jumpspeed = 4
        self.prev_key = pygame.key.get_pressed()

    def walk_animation(self):
        self.image = self.walk_cycle[self.animation_index]
        if self.facing_left:
            self.image = pygame.transform.flip(self.image, True, False)
        if self.animation_index < len(self.walk_cycle)-1:
            self.animation_index += 1
        else:
            self.animation_index = 0

    def update(self, sol, player2, clock, count):
        hsp = 0
        onground = self.check_collision(0, 1, sol)
        # on recupere la touche pressé
        key = pygame.key.get_pressed()
        # Mouvement a gauche
        if key[pygame.K_LEFT] and self.num == 2:
            self.walk_animation()
            hsp = -self.step
        # Mouvement a droit
        elif key[pygame.K_RIGHT] and self.num == 2:
            self.walk_animation()
            hsp = self.step
        # Mouvement attack
        elif key[pygame.K_o] and self.num == 2:
            self.image = self.attack_image

            if (Sprite.get_position(self)[0]-self.attacking_range <= Sprite.get_position(player2)[0] and not player2.on_def):
                self.points += 1
                player2.health -= 10

        elif key[pygame.K_q] and self.num == 1:
            self.walk_animation()
            hsp = -self.step
        # Mouvement a droit
        elif key[pygame.K_d] and self.num == 1:
            self.walk_animation()
            hsp = self.step
        # Mouvement attack
        elif key[pygame.K_z] and self.num == 1:
            self.image = self.attack_image

            if (Sprite.get_position(player2)[0]-self.attacking_range <= Sprite.get_position(self)[0] and not player2.on_def):
                self.points += 1
                player2.health -= 10
        elif not self.on_def:
            self.image = self.stand_image
        # fonction pour desactiver la defense

        def descative():
            self.on_def = False
            self.image = self.stand_image
        # Mouvement block joueur 1
        if key[pygame.K_s] and self.num == 1:
            self.image = self.bloc_image
            # activer la defense
            self.on_def = True
            # timer pour la desactiver
            t = Timer(self.blocking_time, descative)
            t.start()
        # Mouvement block joueur 2
        if key[pygame.K_p] and self.num == 2:
            self.image = self.bloc_image
            # activer la defense
            self.on_def = True
            t = Timer(self.blocking_time, descative)
            t.start()

        if key[pygame.K_i] and onground and self.num == 2:
            clock.tick(TICK/self.movement_speed)
            self.image = self.jump_imageG
            hsp = -self.step
            self.vsp = -self.step*10
        if key[pygame.K_m] and onground and self.num == 2:
            clock.tick(TICK/self.movement_speed)
            self.image = self.jump_imageD
            hsp = self.step
            self.vsp = -self.step*10
        if key[pygame.K_a] and onground and self.num == 1:
            clock.tick(TICK/self.movement_speed)
            self.image = self.jump_imageG
            hsp = -self.step
            self.vsp = -self.step*10
        if key[pygame.K_e] and onground and self.num == 1:
            clock.tick(TICK/self.movement_speed)
            self.image = self.jump_imageD
            hsp = self.step
            self.vsp = -self.step*10
        self.prev_key = key
        # vitesse de chute / effet gravité
        if self.vsp < 10 and not onground:
            self.vsp += self.gravity
        # si la chute ne le remet pas a terre visuellement on le met a 0
        if onground and self.vsp > 0:
            self.vsp = 0
        self.move(hsp, self.vsp, sol, player2, key)

    def move(self, x, y, sol, player2, key):
        dx = x  # distance a parcourir sur x
        dy = y  # distance a parcourir sur y
        # on peux modifier la positon vertical a condition de pas avoir de collision si non on tombe plus
        while self.check_collision(0, dy, sol):
            dy -= numpy.sign(dy)
        # on peux modifier la positon a condition de pas avoir de collision si non on avance plus
        while (self.check_collision(dx, dy, sol)):
            dx -= numpy.sign(dx)
        while (self.check_collision2(dx, dy, player2)):
            dx -= numpy.sign(dx)
        self.rect.move_ip([dx, dy])

    # verification qu'on traverse pas le sol
    def check_collision(self, x, y, grounds):
        self.rect.move_ip([x, y])
        # on detecte la colision avec un autre element qui est le bloc de scene
        collide = pygame.sprite.spritecollideany(self, grounds)
        self.rect.move_ip([-x, -y])
        return collide
    # verification qu'on traverse pas le deuxieme joueur

    def check_collision2(self, x, y, player2):
        self.rect.move_ip([x, y])
        # on detecte la colision avec un autre element qui est player 2
        collide = pygame.sprite.collide_rect(self, player2)
        self.rect.move_ip([-x, -y])
        return collide


class Bloc(Sprite):
    def __init__(self, startx, starty):
        super().__init__("Assets/Bloc.png", startx, starty)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main():
    pygame.mixer.music.load('Backgroundmusic/InGame.wav')
    pygame.mixer.music.play(-1)
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Player(1, 100, 200, 5, 1000, 1, 4, 2, 4, 4)
    player2 = Player(2, 580, 200, 5, 1000, 1, 4, 2, 4, 4)

    # delimiter la zone de combat avec le sol et les murs non visible a l'ecran
    sol = pygame.sprite.Group()
    for bx in range(0, 735, 70):
        sol.add(Bloc(bx, 406))
    for by in range(0, 500, 70):
        sol.add(Bloc(-35, by))
        sol.add(Bloc(735, by))
    font = pygame.font.SysFont("Myriad Pro", 30)

    loop = 1
    count = 0
    while True:
        screen.blit(BACKGROUND, (0, 0))
        pygame.event.pump()
        # compteur de la frame
        if count != TICK:
            count += 1
        else:
            count = 0
        player.update(sol, player2, clock, count)
        player2.update(sol, player, clock, count)

        screen.blit(BACKGROUND, (0, 0))
        player.draw(screen)
        player2.draw(screen)
        sol.draw(screen)

        draw_text(str(player.points)+"   -----    "+str(player2.points),
                  font, "white", screen, (WIDTH//2)-60, 100)
        # draw_text("clock"+str(TICK), font, (0, 0, 0), screen, 500, 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                if os.path.exists("main.py"):
                    os.system("python main.py")
                else:
                    os.system('cls')
                    print("Un fichier manquant a ete detecte, nous ne pouvons pas vous rediriger vers le menu principal; veuillez restaurer toute la version originale du jeu SVP pour eviter des erreurs internes")
                    time.sleep(10)
                os.kill(os.getppid(), signal.SIGTERM)
                os.system("exit")

        pygame.display.update()

        if (player.health < 0 or player2.health < 0):
            draw_text("Game over", pygame.font.SysFont(
                "Myriad Pro", 55), (0, 0, 0), screen, 100, 100)
            time.sleep(10)
            break

        clock.tick(TICK)

main()
