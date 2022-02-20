#создай игру "Лабиринт"!
from pygame import *

window = display.set_mode((1000, 700))
display.set_caption('Догони меня кирпич')
background = transform.scale(image.load('dv.jpg'), (1000, 700))
window.blit(background, (0, 0))

game = True
finish = False

clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render('Вы украли гемы!', True, (255, 215, 0))
lose = font.render('Вас поймал Путин!', True, (0, 0, 0))



mixer.init()
mixer.music.load('jj.mp3')
mixer.music.play()
mixer.music.set_volume(1)

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, px, py, ps):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100, 100))
        self.speed = ps
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0: 
            self.rect.x -= self.speed
            
        if keys[K_RIGHT] and self.rect.x < 900: 
            self.rect.x += self.speed
            
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y  < 600:
        
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 700:
            
            self.direction = 'right'
        if self.rect.x >= 900:
            
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__ (self, color1, color2, color3, wallx, wally, wallwidth, wallheight):
        super().__init__()
        self.width = wallwidth
        self.height = wallheight
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wallx
        self.rect.y = wally
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


wall1 = Wall(255, 255, 255, 200, 0, 10, 550)
wall2 = Wall(0, 4, 255, 360, 150, 10, 550)
wall3 = Wall(255, 0, 0, 520, 0, 10, 550)
player = Player('kk.png', 0, 0, 5)
final = GameSprite('aa.png', 750, 10, 0)
mon = Enemy('ff.png', 750, 300, 2)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        
        player.reset()
        mon.reset()
        final.reset()
        player.update()
        mon.update()

        if sprite.collide_rect(player, mon) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3):
            finish = True
            window.blit(lose, (200,200))
            mixer.music.stop()
            kick.play()
            

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            mixer.music.stop()
            money.play()
           

        display.update()
        clock.tick(FPS) 
