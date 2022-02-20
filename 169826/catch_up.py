from pygame import *

window = display.set_mode((673, 900))
display.set_caption('Догони меня кирпич')
background = transform.scale(image.load('background.png'), (673, 900))
window.blit(background, (0, 0))

speed = 5
x1 = 290
y1 = 0
sprite1 = transform.scale(image.load('sprite1.png'), (80,80))

x2 = 290
y2 = 800
sprite2 = transform.scale(image.load('sprite2.png'), (80,80))

game = True

clock = time.Clock()
FPS = 60

while game:
    window.blit(background, (0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    keys = key.get_pressed()

    if keys[K_LEFT] and x1 > 20:
        x1 -= speed
    if keys[K_RIGHT] and x1 < 573:
        x1 += speed
    if keys[K_UP] and y1 > 20:
        y1 -= speed
    if keys[K_DOWN] and y1 < 800:
        y1 += speed
    
    if keys[K_a] and x2 > 20:
        x2 -= speed
    if keys[K_d] and x2 < 573:
        x2 += speed
    if keys[K_w] and y2 > 20:
        y2 -= speed
    if keys[K_s] and y2 < 800:
        y2 += speed

    display.update()
    clock.tick(FPS)

