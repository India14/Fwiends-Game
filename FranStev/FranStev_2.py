import pygame
from pygame.locals import *
import sys
import random
import time
import os
os.chdir("c:\FranStev")
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional
 
jumpy = 1
HEIGHT = 1000
WIDTH = 700
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Forest Fwiends")
gameIcon = pygame.image.load('mushy.png')
pygame.display.set_icon(gameIcon)
bg = pygame.image.load("Scene2.png")
WIDTH = 700    
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_font = pygame.font.SysFont('Verdana', 20)
text_surface = game_font.render('You Won!', True, (0, 0, 0))
text_surface_2 = game_font.render('You Lost!', True, (0, 0, 0))
text_surface_3 = game_font.render('Created by Ty, India and Andie \n Forest Friends 2022', True, (0, 0, 0))
text_rect = text_surface.get_rect(center =(100, 200))

start_button = pygame.image.load('star.png')
s_button_rect = start_button.get_rect(center = (WIDTH/2, 150))
quit_button = pygame.image.load('quit.png')
q_button_rect = quit_button.get_rect(center = (WIDTH/2, 300))
creds_button = pygame.image.load('creds.png')
c_button_rect = creds_button.get_rect(center = (WIDTH/2, 450))
b_button = pygame.image.load ('back.png')
b_button_rect = b_button.get_rect(center = (WIDTH/2, 700))
#-----------------------Music
def gameMusic():
    gMusic = pygame.mixer.music.load("game music.mp3")
    pygame.mixer.music.play()

def creditsMusic():
    cMusic = pygame.mixer.music.load("credit music.mp3")
    pygame.mixer.music.play()

def deathMusic():
    cMusic = pygame.mixer.music.load("death music.mp3")
    pygame.mixer.music.play()

def winMusic():
    cMusic = pygame.mixer.music.load("win music.mp3")
    pygame.mixer.music.play()
    
    
#system = True
#mainMenu = True
#game = False
#credits = False




#-----------------------

def menu_screen():
    while True:
        creditsMusic()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if s_button_rect.collidepoint(event.pos):
                    plat_game()
                if q_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit
                #if c_button_rect.collidepoint(event.pos):
                    #displaysurface.fill((3, 244, 252))
                    #displaysurface.blit(text_surface_3, text_rect)
                    #displaysurface.blit(b_button, b_button_rect)
                    #pygame.display.update()
                    #if event.type == MOUSEBUTTONDOWN:
                        #if b_button_rect.collidepoint(event.pos):
                            #menu_screen()  

        displaysurface.fill((134,56,200))
        displaysurface.blit(start_button, s_button_rect)
        displaysurface.blit(quit_button, q_button_rect)
        #displaysurface.blit(creds_button, c_button_rect)
        pygame.display.update()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.image.load("F1.png")
        self.walkRight = pygame.image.load('F1.png')
        self.walkLeft = pygame.image.load('F0.png')
        self.rect = self.surf.get_rect()
        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0 
        self.index = 1
 
    def move(self):
        self.acc = vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
            self.surf = self.walkLeft
            self.index += 1
            if self.index > 8:
                self.index = 0 
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
            self.surf = self.walkRight
            self.index += 1
            if self.index > 8:
                self.index = 0 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
             
        self.rect.midbottom = self.pos
 
    def jump(self): 
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -20 * jumpy
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def update(self):
        hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:   
                        hits[0].point = False   
                        self.score += 1
                        if self.score == 20:
                            winMusic()
                            displaysurface.fill((0, 255, 0))
                            displaysurface.blit(text_surface, text_rect)
                            pygame.display.update()
                            time.sleep(2)
                            pygame.quit()
                            sys.exit
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((151,182,159))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),  random.randint(0, HEIGHT-30)))
        self.speed = random.randint(-1, 2)
        
        self.point = True  
        self.moving = True
        
    
    def move(self):
        if self.moving == True:  
            self.rect.move_ip(self.speed,0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
            if self.speed < 0 and self.rect.right < 0:
                self.rect.left = WIDTH
 
 
def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform,groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 40) and (abs(platform.rect.bottom - entity.rect.top) < 40):
                return True
        C = False
 
def plat_gen():
    while len(platforms) < 7:
        width = random.randrange(50,100)
        p  = platform()      
        C = True
         
        while C:
             p = platform()
             p.rect.center = (random.randrange(0, WIDTH - width),
                              random.randrange(-50, 0))
             C = check(p, platforms)
        platforms.add(p)
        all_sprites.add(p)
 
class powerUp():
    def __init__(self):
        self.image = pygame.image.load("PowerUp.png")
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 370)
        self.rect.y = 300 

    def powerUpSpawn(self):
        displaysurface.blit(self.image, self.rect)
        #pygame.draw.rect(displaysurface, self.rect, 4)

    def changePLaces(self):
        self.rect.x = random.randint(0,370)
        self.rect.y = -20 #changeto random after testing

    def scroll(self):
        self.rect.y += abs(P1.vel.y)
        
powers = powerUp()
PT1 = platform()
P1 = Player()
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((213,233,218))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

PT1.moving = False
PT1.point = False  
 
for x in range(random.randint(4,5)):
    C = True
    pl = platform()
    while C:
        pl = platform()
        C = check(pl, platforms)
    platforms.add(pl)
    all_sprites.add(pl)


def plat_game():
    while True:
        P1.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    P1.jump()
                    #jumpy = 1
            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_SPACE:
                    P1.cancel_jump()


        if P1.rect.top > HEIGHT:
            for entity in all_sprites:
                deathMusic()
                entity.kill()
                time.sleep(1)
                displaysurface.fill((255,0,0))
                displaysurface.blit(text_surface_2, text_rect)
                pygame.display.update()
                time.sleep(3)
                pygame.quit()
                sys.exit()
    
        if P1.rect.top <= HEIGHT / 3:
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
    
        plat_gen()
        screen.blit(bg,(0,0))
        f = pygame.font.SysFont("Verdana", 20)     
        g  = f.render(str(P1.score), True, (123,255,0))   
        displaysurface.blit(g, (WIDTH/2, 10))   
        

        if powers.rect.colliderect(P1.rect):
            jumpy = 2
            powers.changePLaces()
            P1.score += 2
            
        if P1.rect.top <= HEIGHT/3:
            powers.scroll()

        if powers.rect.y > 900:  #THIS IS THE SPAWN RATE
            powers.rect.y = -1

        powers.powerUpSpawn()
        
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)
            entity.move()
    
        pygame.display.update()
        FramePerSec.tick(FPS)

menu_screen()