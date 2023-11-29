import pygame, os, sys, random
import button

#initialise pygame
pygame.init()
pygame.mixer.init()

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)

#colors
WHITE = 255, 255, 255
RED = 255, 0, 0
bg_color = 47, 54, 74

#screen stuff
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bob the Scary')
clock = pygame.time.Clock()
FPS = 60
icon_img = pygame.image.load('assets/icon.png').convert_alpha()
pygame.display.set_icon(icon_img)

#game variables
game_paused = True
guy_x = 100
guy_y = 100
end = False

#load images
bob_img = pygame.image.load('assets/bob.png').convert_alpha()
quit_img = pygame.image.load('assets/quit_button.png').convert_alpha()
play_img = pygame.image.load('assets/play_button.png').convert_alpha()
guy_img = pygame.image.load('assets/guy.png').convert_alpha()

#make button instances
play_button = button.Button(200, 300, play_img, 1)
quit_button = button.Button(200, 400, quit_img, 1)

#fonts
title_font = pygame.font.SysFont("Arial", 100)
font = pygame.font.SysFont("Bahnschrift", 40)

#text drawing
def draw_text(text, font, text_col, x, y):
    text = font.render(text, True, text_col)
    screen.blit(text, (x, y))

#player class
class Player():

    clock.tick(FPS)

    def __init__(self, x, y):
        self.image = pygame.transform.scale(bob_img, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= 1
        if key[pygame.K_d]:
            self.rect.x += 1
        if key[pygame.K_w]:
            self.rect.y -= 1
        if key[pygame.K_s]:
            self.rect.y += 1
        
		
    def draw(self):
        screen.blit(self.image, self.rect)

#guy class
class Guy():

    clock.tick(FPS)
    
    def __init__(self, x, y):
        self.image = guy_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

		
bob = Player(SCREEN_WIDTH // 2, 400)
guy = Guy(200, 400)
guy_later = Guy(guy_x, guy_y)

counter, text = 5, '5'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)

#game loop
run = True
while run:
    #draw background
    screen.fill((bg_color))

    #game paused
    if game_paused == True:
        draw_text(("Bob the Scary"), title_font, (255, 255, 255), 141, 30)
        if quit_button.draw(screen):
            run = False
        if play_button.draw(screen):
            game_paused = False

        #music
        pygame.mixer.music.load('assets/menu.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

    #unpaused game loop
    else:
        pass

        #hide mouse
        pygame.mouse

        #render bob
        bob.draw()
        bob.move()

        #player can't go out of map
        if bob.rect.y < 0:
            bob.rect.y = 0
        if bob.rect.x < 0:
            bob.rect.x = 0
        if bob.rect.y > 475:
            bob.rect.y = 475
        if bob.rect.x > 675:
            bob.rect.x = 675

        
        #render guy
        guy.draw()

        if bob.rect.colliderect(guy.rect):
            counter += 1
            guy.rect.x = (random.randint(10, 750))
            guy.rect.y = (random.randint(10, 540))

        bg_color = 255, 255, 255

        bob_rect = bob_img.get_rect
        guy_rect = bob_img.get_rect
        
        #unpaused event handler
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3)
                if counter > 0:
                    run = True
                else: 
                    text ='boom!'
                    end = True
        screen.blit(font.render(text, True, (0, 9, 9)), (32, 48))

        if event.type == pygame.QUIT:
            run = False


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #end game
    if end == True:
        end_screen = pygame.Rect(0, 0, 800, 600)
        pygame.mixer.music.stop()
        pygame.draw.rect(screen, bg_color, end_screen)
        game_over = font.render("Game Over!", True, (0, 0, 0))
        screen.blit(game_over, game_over.get_rect(center = screen.get_rect().center))

	#update display window
    pygame.display.update()

pygame.quit()