from turtle import width
import pygame, sys, random, os, time
from pygame.locals import *
os.chdir('c:\\FranStev')
pygame.init()
vec = pygame.math.Vector2


WIDTH = 1280
HEIGHT = 900
ACC = 0.5
FPS = 50
FRIC = -0.12
#-----------------------Music

#def gameMusic():
#    gMusic = pygame.mixer.music.load("arcade.wav")
#    pygame.mixer.music.play()

#def creditsMusic():
  #  cMusic = pygame.mixer.music.load("arcade.wav")
   # pygame.mixer.music.play()

#def mainMenuMusic():
  #  cMusic = pygame.mixer.music.load("arcade.wav")
 #   pygame.mixer.music.play()


#system 
#mainMenu = True
#game = False
#credits = False




#-----------------------

FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Franco and Steven')

game_font = pygame.font.SysFont('Verdana', 60)
text_surface = game_font.render('Success!', True, (0,0,0))
text_surface_2 = game_font.render('Defeat!', True, (0,0,0))
text_rect  = text_surface.get_rect(center = (225, 200))


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super(Player1, self).__init__()
        self.surf = pygame.Surface((40, 40))
        self.surf = pygame.image.load('T0.png')
        self.rect = self.surf.get_rect(center = (10, 420))
        
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0

    def move(self):
        self.acc = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if self.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score += 1
                        if self.score == 5:
                            displaysurface.fill((0, 255, 0))
                            displaysurface.blit(text_surface, text_rect)
                            pygame.display.update()
                            time.sleep(2)
                            pygame.quit()
                            sys.exit
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
    
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super(Player1, self).__init__()
        self.surf = pygame.Surface((40, 40))
        self.surf = pygame.image.load('F0.png')
        self.rect = self.surf.get_rect(center = (10, 420))
        
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0

    def move(self):
        self.acc = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_d]:
            self.acc.x = -ACC
        if pressed_keys[K_a]:
            self.acc.x = ACC
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if self.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    if hits[0].point == True:
                        hits[0].point = False
                        self.score += 1
                        if self.score == 5:
                            displaysurface.fill((0, 255, 0))
                            displaysurface.blit(text_surface, text_rect)
                            pygame.display.update()
                            time.sleep(2)
                            pygame.quit()
                            sys.exit()
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
    
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3



class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((32, 45, 100))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH -10), random.randint(0, HEIGHT -30)))
        self.speed = random.randint(-1, 1)
        self.moving = True
        self.point = True

    def move(self):
        if self.moving == True:
            self.rect.move_ip(self.speed,0)
            if self.speed > 0 and self.rect.left > WIDTH:
                self.rect.right = 0
                if self.speed < 0 and self.rect.right < 0:
                    self.rect.left = WIDTH

    def plat_gen():
        while len(platforms) < 7 :
            width = random.randrange(50, 100)
            p = platform()
            p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))

            platforms.add(p)
            all_sprites.add(p)

def check(platform, groupies):
    if pygame.sprite.spritecollideany(platform,groupies):
        return True
    else:
        for entity in groupies:
            if entity == platform:
                continue
        if (abs(platform.rect.top - entity.rect.bottom) < 50) and (abs(platform.rect.bottom - entity.rect.top) < 50):
            return True
        C = False

def plat_gen():
    while len(platforms) < 6 :
        width = random.randrange(50,100)
        p = platform()
        C = True

        while C:
            p = platform()
            p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))
        
            C = check(p,platforms)

        platforms.add(p)
        all_sprites.add(p)        

PT1 = platform()
PT1.moving = False
PT1.point = False
P1 = Player1()
platforms = pygame.sprite.Group()
platforms.add(PT1)

PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((146, 179, 232))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

for x in range(random.randint(5, 6)):
    pl = platform()
    platforms.add(pl)
    all_sprites.add(pl)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or pygame.K_w:
                P1.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                P1.cancel_jump() ##no longer jumping at all
    
    if P1.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            time.sleep(1)
            displaysurface.fill((255, 0, 0))
            displaysurface.blit(text_surface_2, text_rect)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit

    displaysurface.fill((0, 0, 0))
    f = pygame.font.SysFont("Verdana", 20)
    g = f.render(str(P1.score), True, (123, 255, 0))
    displaysurface.blit(g,(WIDTH/2, 10))
    #-------------------------------------Colliderect
    # if popwers.rect.colliderect(P1.rect):
    #     jumpy(jumping value) = 2
    #     powers.changePlaces()
    #     P1.score += 1

    # if P1.rect.top <= HEIGHT/3:
    #     powers.scroll()
    
    # if powers.rect.y > 900:
    #     powers.rect.y = -1

    # powers.powerUpSpawn()

    #----------------------------------------
    

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    P1.move()
    P1.update()
    plat_gen() 
    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()
    
    pygame.display.update()
    FramePerSec.tick(FPS)