import pygame, sys, os, signal, time
from button import Button

# this bunch of following code has been taken from a gitbub
# heres the link https://github.com/baraltech/Menu-System-PyGame

pygame.init()

# make a screen with caption
SCREEN = pygame.display.set_mode((405, 720))
pygame.display.set_caption("Menu")

# load back grounds
back_ground = pygame.image.load("Assets/Back_ground.png")
guide_bg = pygame.image.load("Assets/Guide_bg.png")
play_bg = pygame.image.load("Assets/Play_bg.png")
Ingame_bg = pygame.image.load("Assets/Back_ground.png")

# load the font


def get_font(size):
    return pygame.font.Font("Assets/Hirokawa.ttf", size)


# play button
def play():
    while True:
        # mouse coords
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        # background
        SCREEN.blit(play_bg, (0, 0))
        # screen text
        PLAY_TEXT = get_font(22).render(
            "Veillez choisir une version", False, "black")
        PLAY_TEXTr = get_font(22).render(
            "Veillez choisir une version", True, "red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(203, 65))
        SCREEN.blit(PLAY_TEXTr, PLAY_RECT)
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # screen buttons
        PLAY_BACK = Button(image=None, pos=(100, 640), text_input="Precedent", font=get_font(
            20), base_color="red", hovering_color="yellow")

        PLAY_GRAPHIC = Button(image=pygame.image.load("Assets/Graphique.png"), pos=(200, 270),
                              text_input="GRAPHIC", font=get_font(32), base_color="#d7fcd4", hovering_color="red")

        PLAY_TERMINAL = Button(image=pygame.image.load("Assets/Terminal.png"), pos=(200, 460),
                               text_input="TERMINAL", font=get_font(32), base_color="#d7fcd4", hovering_color="red")

        for button in [PLAY_BACK, PLAY_GRAPHIC, PLAY_TERMINAL]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        # close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.kill(os.getppid(), signal.SIGTERM)
                os.system("exit")
                sys.exit()

            # onclick play graphic version
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_GRAPHIC.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\Select.wav"))
                    time.sleep(0.5)
                    pygame.quit()
                    if os.path.exists("graphic.py"):
                        os.system("python graphic.py")
                        sys.exit()
                    else:
                        os.system('cls')
                        print(
                            'Le jeu a detecte un fichier manquant, veuillez restaurer toute la version originale du jeu SVP pour eviter des erreurs internes')
                        time.sleep(5)
                        os.kill(os.getppid(), signal.SIGTERM)
                        os.system("exit")
                        sys.exit()


            # onclick play terminal version
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_TERMINAL.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\Select.wav"))
                    time.sleep(0.5)
                    pygame.quit()
                    if os.path.exists("terminal.py"):
                        os.system("python terminal.py")
                        sys.exit()
                    else:
                        os.system('cls')
                        print(
                            'Le jeu a detecte un fichier manquant, veuillez restaurer toute la version originale du jeu SVP pour eviter des erreurs internes')
                        time.sleep(5)
                        os.kill(os.getppid(), signal.SIGTERM)
                        os.system("exit")
                        sys.exit()

            # onclick back button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\Select.wav"))
                    main_menu()

        pygame.display.update()


def keybing():

    while True:
        GUIDE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(guide_bg, (0, 0))

        GUIDE_TEXTr = get_font(30).render("Touches", False, "red")
        GUIDE_TEXT = get_font(30).render("Touches", True, "black")
        GUIDE_RECT = GUIDE_TEXT.get_rect(center=(203, 65))

        GUIDE_TEXT1b = get_font(14).render(
            "Joueur 1      -      Joueur 2", True, "red")
        GUIDE_TEXT1 = get_font(14).render(
            "Joueur 1      -      Joueur 2", False, "black")
        GUIDE_RECT1 = GUIDE_TEXT1.get_rect(center=(203, 200))

        GUIDE_TEXT2b = get_font(14).render(
            "d : avancer a droite - FG : avancer a gauche", True, "black")
        GUIDE_TEXT2 = get_font(14).render(
            "d : avancer a droite - FG : avancer a gauche", False, "red")
        GUIDE_RECT2 = GUIDE_TEXT2.get_rect(center=(203, 230))

        GUIDE_TEXT3b = get_font(14).render(
            "q : avancer a gauche - FD : avancer a gauche", True, "black")
        GUIDE_TEXT3 = get_font(14).render(
            "q : avancer a gauche - FD : avancer a gauche", False, "red")
        GUIDE_RECT3 = GUIDE_TEXT3.get_rect(center=(203, 260))

        GUIDE_TEXT4b = get_font(14).render(
            "e : sauter a droite - m : sauter a droite", True, "black")
        GUIDE_TEXT4 = get_font(14).render(
            "e : sauter a droite - m : sauter a droite", False, "red")
        GUIDE_RECT4 = GUIDE_TEXT4.get_rect(center=(203, 290))

        GUIDE_TEXT5b = get_font(14).render(
            "a : sauter a gauche - l : sauter a gauche", True, "black")
        GUIDE_TEXT5 = get_font(14).render(
            "a : sauter a gauche - l : sauter a gauche", False, "red")
        GUIDE_RECT5 = GUIDE_TEXT5.get_rect(center=(203, 320))

        GUIDE_TEXT6b = get_font(14).render(
            "z : attaquer - o : attaquer", True, "black")
        GUIDE_TEXT6 = get_font(14).render(
            "z : attaquer - o : attaquer", False, "red")
        GUIDE_RECT6 = GUIDE_TEXT6.get_rect(center=(203, 350))

        GUIDE_TEXT7b = get_font(14).render(
            "s : bloquer - p : attaquer", True, "black")
        GUIDE_TEXT7 = get_font(14).render(
            "s : bloquer - p : attaquer", False, "red")
        GUIDE_RECT7 = GUIDE_TEXT7.get_rect(center=(203, 380))

        SCREEN.blit(GUIDE_TEXTr, GUIDE_RECT)
        SCREEN.blit(GUIDE_TEXT, GUIDE_RECT)
        SCREEN.blit(GUIDE_TEXT1b, GUIDE_RECT1)
        SCREEN.blit(GUIDE_TEXT1, GUIDE_RECT1)
        SCREEN.blit(GUIDE_TEXT2b, GUIDE_RECT2)
        SCREEN.blit(GUIDE_TEXT2, GUIDE_RECT2)
        SCREEN.blit(GUIDE_TEXT3b, GUIDE_RECT3)
        SCREEN.blit(GUIDE_TEXT3, GUIDE_RECT3)
        SCREEN.blit(GUIDE_TEXT4b, GUIDE_RECT4)
        SCREEN.blit(GUIDE_TEXT4, GUIDE_RECT4)
        SCREEN.blit(GUIDE_TEXT5b, GUIDE_RECT5)
        SCREEN.blit(GUIDE_TEXT5, GUIDE_RECT5)
        SCREEN.blit(GUIDE_TEXT6b, GUIDE_RECT6)
        SCREEN.blit(GUIDE_TEXT6, GUIDE_RECT6)
        SCREEN.blit(GUIDE_TEXT7b, GUIDE_RECT7)
        SCREEN.blit(GUIDE_TEXT7, GUIDE_RECT7)

        GUIDE_BACK = Button(image=None, pos=(100, 640),
                            text_input="Precedent", font=get_font(20), base_color="Black", hovering_color="red")
        GUIDE_BACK.changeColor(GUIDE_MOUSE_POS)
        GUIDE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.kill(os.getppid(), signal.SIGTERM)
                os.system("exit")
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_BACK.checkForInput(GUIDE_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\Select.wav"))
                    guide()

        pygame.display.update()


def guide():

    while True:
        GUIDE_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(guide_bg, (0, 0))
        GUIDE_TEXTr = get_font(30).render("Guide", False, "red")
        GUIDE_TEXT = get_font(30).render("Guide", True, "black")
        GUIDE_RECT = GUIDE_TEXT.get_rect(center=(203, 65))

        GUIDE_TEXT1b = get_font(14).render(
            "Dans ce jeu vous pouvez sauter,", True, "black")
        GUIDE_TEXT1 = get_font(14).render(
            "Dans ce jeu vous pouvez sauter,", False, "red")
        GUIDE_RECT1 = GUIDE_TEXT1.get_rect(center=(203, 200))

        GUIDE_TEXT2b = get_font(14).render(
            "attquer, bloquer et vous deplacer...", True, "black")
        GUIDE_TEXT2 = get_font(14).render(
            "attquer, bloquer et vous deplacer...", False, "red")
        GUIDE_RECT2 = GUIDE_TEXT2.get_rect(center=(203, 230))

        GUIDE_TEXT3b = get_font(14).render(
            "attention ce pendant il est un peu ", True, "black")
        GUIDE_TEXT3 = get_font(14).render(
            "attention ce pendant il est un peu ", False, "red")
        GUIDE_RECT3 = GUIDE_TEXT3.get_rect(center=(203, 260))

        GUIDE_TEXT4b = get_font(14).render(
            "intuif que vous pouvez ne pas traverser", True, "black")
        GUIDE_TEXT4 = get_font(14).render(
            "intuif que vous pouvez ne pas traverser", False, "red")
        GUIDE_RECT4 = GUIDE_TEXT4.get_rect(center=(203, 290))

        GUIDE_TEXT5b = get_font(14).render(
            "un obstacle ou votre adversaire ;) ", True, "black")
        GUIDE_TEXT5 = get_font(14).render(
            "un obstacle ou votre adversaire ;) ", False, "red")
        GUIDE_RECT5 = GUIDE_TEXT5.get_rect(center=(203, 320))

        GUIDE_TEXT6b = get_font(14).render(
            "Pour ganger un point vous devez atteindre", True, "black")
        GUIDE_TEXT6 = get_font(14).render(
            "Pour ganger un point vous devez atteindre", False, "red")
        GUIDE_RECT6 = GUIDE_TEXT6.get_rect(center=(203, 350))

        GUIDE_TEXT7b = get_font(14).render(
            "votre adveraise avec une attaque non ", True, "black")
        GUIDE_TEXT7 = get_font(14).render(
            "votre adveraise avec une attaque non ", False, "red")
        GUIDE_RECT7 = GUIDE_TEXT7.get_rect(center=(203, 380))

        GUIDE_TEXT8b = get_font(14).render(
            "bloquee ni paree. Vous ne pouvez pas", True, "black")
        GUIDE_TEXT8 = get_font(14).render(
            "bloquee ni paree. Vous ne pouvez pas", False, "red")
        GUIDE_RECT8 = GUIDE_TEXT8.get_rect(center=(203, 410))

        GUIDE_TEXT9b = get_font(14).render(
            "traverser les objets, ", True, "black")
        GUIDE_TEXT9 = get_font(14).render(
            "traverser les objets, ", False, "red")
        GUIDE_RECT9 = GUIDE_TEXT9.get_rect(center=(203, 440))

        GUIDE_TEXT10b = get_font(14).render(
            "votre adversaire est concidere comme objet", True, "black")
        GUIDE_TEXT10 = get_font(14).render(
            "votre adversaire est concidere comme objet", False, "red")
        GUIDE_RECT10 = GUIDE_TEXT10.get_rect(center=(203, 470))

        GUIDE_TEXT11b = get_font(14).render(
            'neamoins les bugs ("Features") existent', True, "black")
        GUIDE_TEXT11 = get_font(14).render(
            'neamoins les bugs ("Features") existent', False, "red")
        GUIDE_RECT11 = GUIDE_TEXT11.get_rect(center=(203, 500))

        SCREEN.blit(GUIDE_TEXTr, GUIDE_RECT)
        SCREEN.blit(GUIDE_TEXT, GUIDE_RECT)
        SCREEN.blit(GUIDE_TEXT1b, GUIDE_RECT1)
        SCREEN.blit(GUIDE_TEXT1, GUIDE_RECT1)
        SCREEN.blit(GUIDE_TEXT2b, GUIDE_RECT2)
        SCREEN.blit(GUIDE_TEXT2, GUIDE_RECT2)
        SCREEN.blit(GUIDE_TEXT3b, GUIDE_RECT3)
        SCREEN.blit(GUIDE_TEXT3, GUIDE_RECT3)
        SCREEN.blit(GUIDE_TEXT4b, GUIDE_RECT4)
        SCREEN.blit(GUIDE_TEXT4, GUIDE_RECT4)
        SCREEN.blit(GUIDE_TEXT5b, GUIDE_RECT5)
        SCREEN.blit(GUIDE_TEXT5, GUIDE_RECT5)
        SCREEN.blit(GUIDE_TEXT6b, GUIDE_RECT6)
        SCREEN.blit(GUIDE_TEXT6, GUIDE_RECT6)
        SCREEN.blit(GUIDE_TEXT7b, GUIDE_RECT7)
        SCREEN.blit(GUIDE_TEXT7, GUIDE_RECT7)
        SCREEN.blit(GUIDE_TEXT8b, GUIDE_RECT8)
        SCREEN.blit(GUIDE_TEXT8, GUIDE_RECT8)
        SCREEN.blit(GUIDE_TEXT9b, GUIDE_RECT9)
        SCREEN.blit(GUIDE_TEXT9, GUIDE_RECT9)
        SCREEN.blit(GUIDE_TEXT10b, GUIDE_RECT10)
        SCREEN.blit(GUIDE_TEXT10, GUIDE_RECT10)
        SCREEN.blit(GUIDE_TEXT11b, GUIDE_RECT11)
        SCREEN.blit(GUIDE_TEXT11, GUIDE_RECT11)

        GUIDE_BACK = Button(image=None, pos=(100, 640),
                            text_input="Precedent", font=get_font(20), base_color="Black", hovering_color="red")
        GUIDE_NEXT = Button(image=None, pos=(300, 640),
                            text_input="Suivant", font=get_font(20), base_color="Black", hovering_color="red")
        GUIDE_BACK.changeColor(GUIDE_MOUSE_POS)
        GUIDE_BACK.update(SCREEN)
        GUIDE_NEXT.changeColor(GUIDE_MOUSE_POS)
        GUIDE_NEXT.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.kill(os.getppid(), signal.SIGTERM)
                os.system("exit")
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_NEXT.checkForInput(GUIDE_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\Select.wav"))
                    keybing()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_BACK.checkForInput(GUIDE_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\Select.wav"))
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.mixer.music.load('Backgroundmusic/MainMenu.wav')
    pygame.mixer.music.play(-1)
    while True:
        SCREEN.blit(back_ground, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(64).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(204, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Assets/Play_button.png"), pos=(200, 300),
                             text_input="Jouer", font=get_font(32), base_color="#d7fcd4", hovering_color="red")
        GUIDE_BUTTON = Button(image=pygame.image.load("Assets/Guide_button.png"), pos=(200, 450),
                              text_input="Guide", font=get_font(32), base_color="#d7fcd4", hovering_color="red")
        QUIT_BUTTON = Button(image=pygame.image.load("Assets/Quit_Button.png"), pos=(200, 600),
                             text_input="Quitter", font=get_font(32), base_color="#d7fcd4", hovering_color="red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.kill(os.getppid(), signal.SIGTERM)
                os.system("exit")
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\Select.wav"))
                    play()
                if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\Select.wav"))
                    guide()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sounds\Select.wav"))
                    time.sleep(0.5)
                    pygame.quit()
                    os.kill(os.getppid(), signal.SIGTERM)
                    os.system("exit")
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
