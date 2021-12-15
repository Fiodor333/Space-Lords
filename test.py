from os import replace
import pygame

import time

import random


w = 800
h = 500
color = [255, 255, 255]


pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Meteor Rain')
s_sh = pygame.mixer.Sound('snd\\Jump.mp3')
clock = pygame.time.Clock()
bg = pygame.image.load('img\\sky2.jpg')
bg2 = pygame.image.load('img\\sky2.jpg')
pl = pygame.image.load('img\\player.png')
pl2 = pygame.image.load('img\\player2.png')


FPS = 60
x = 380
y = 460
luchcount = 5
c = 0
bgy = 0
bg2y = -500
cc = [0, 0, 255]
r = random.randint(30, h-200)
x2 = random.randint(r, w-r)
y2 = -r
x3 = 10
vibor = True
strafecounter = 5
y3 = 10
speed = 5
speed2 = 10
score = 0
my_font = pygame.font.SysFont(None, 30)
text1 = my_font.render(f'Your score is {score}', True, (255, 0, 0))
strafetext = my_font.render(f'strafes: {strafecounter}', True, (255, 0, 0))
luchtext = my_font.render(f'laser rays: {luchcount}', True, (255, 0, 0))
my_font2 = pygame.font.SysFont(None, 70)
my_font_m = pygame.font.SysFont(None, 50)
ff = open("123.txt", encoding="utf-8")
f1 = ff.read()
ff.close()
luch = False
text01 = my_font.render(f'Record: {f1}', True, (255, 0, 0))
skin = my_font2.render(f"select skin", True, (255, 0, 0))
select_music = my_font2.render(f"select music", True, (255, 0, 0))
megaD = my_font_m.render("Megadeath - Holy Wars...The Punishment Due", True, (255, 255, 255))
IronM = my_font_m.render("Iron Maiden - Aces High", True, (255, 255, 255))
cont = my_font2.render(">", True, (255, 0, 0))
selsk = 0
selsong = 0






screen = pygame.display.set_mode([w, h])
screen.fill(color)

game_run = True
up, down, right, left, upsh, downsh, rightsh, leftsh = False, False, False, False, False, False, False, False

while vibor:
        screen.blit(bg, (0, 0))
        screen.blit(skin, (x3+270, y3))
       #pygame.draw.rect(screen, [0,0,0],[337,70,50,38])
       # pygame.draw.rect(screen, [0,0,0],[437,70,50,38])
        screen.blit(pl, (337, 70))
        screen.blit(pl2, (437, 70))
        screen.blit(select_music, (x3+270, y3+200))
        screen.blit(megaD, (x3+10, y3+280))
        screen.blit(IronM, (x3+230, y3+330))
        screen.blit(cont, (x3+400, y3+400))
        pygame.display.flip()


        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                vibor = False
                game_run = False


            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 337 < i.pos[0] < 387 and 70 < i.pos[1] < 108:
                        selsk = 1
                    if 437 < i.pos[0] < 487 and 70 < i.pos[1] < 108:
                        selsk = 2
                    if 290 < i.pos[1] < 340:
                        selsong = 1
                    if 340 < i.pos[1] < 390:
                        selsong = 2
                    if 410 < i.pos[1] < 480 and selsong != 0 and selsk != 0:
                        vibor = False
        
if selsk == 1:
    pl = pygame.image.load('img\\player.png')
else:
    pl = pygame.image.load('img\\player2.png')

if selsong == 1:
    pygame.mixer.music.load('snd\\Megadeath - Holy Wars...The Punishment Due.mp3')
else:
    pygame.mixer.music.load('snd\\Iron Maiden - Aces High.mp3')

pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

while game_run:
    clock.tick(FPS)

    while vibor:
        screen.blit(bg, (0, 0))
        screen.blit(skin, (x3+270, y3))
        pygame.draw.rect(screen, [255,255,255],[337,70,50,38])
        pygame.draw.rect(screen, [255,255,255],[437,70,50,38])
        screen.blit(pl, (337, 70))
        screen.blit(pl2, (437, 70))
        screen.blit(select_music, (x3+270, y3+200))
        screen.blit(megaD, (x3+10, y3+280))
        screen.blit(IronM, (x3+230, y3+330))
        screen.blit(cont, (x3+400, y3+400))
        pygame.display.flip()


        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                vibor = False
                game_run = False


            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if 337 < i.pos[0] < 387 and 70 < i.pos[1] < 108:
                        selsk = 1
                    if 437 < i.pos[0] < 487 and 70 < i.pos[1] < 108:
                        selsk = 2
                    if 290 < i.pos[1] < 340:
                        selsong = 1
                    if 340 < i.pos[1] < 390:
                        selsong = 2
                    if 410 < i.pos[1] < 480 and selsong != 0 and selsk != 0:
                        vibor = False


    # colision
    if x2-r < x+25 < x2+r and y2-r < y+19 < y2+r:
        ff = open("123.txt", "r+", encoding="utf-8")
        f1 = ff.read()
        if int(f1) < score:
            f1 = score
            text12 = my_font2.render(f"Game over", True, (255, 0, 0))
            text123 = my_font2.render(f"New record: {score}", True, (0, 255, 0))
            screen.blit(bg, (0, 0))
            screen.blit(text12, (x3, y3+50))
            screen.blit(text123, (x3, y3+100))
            pygame.display.flip()
        else:
            text2 = my_font2.render(f"Game over, your score is {score}", True, (255, 0, 0))
            screen.blit(bg, (0, 0))
            screen.blit(text2, (x3, y3))
            pygame.display.flip()

        
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                game_run = False

                ff.seek(0)
                ff.write(str(f1))
                ff.close()
        

    else:

        

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                game_run = False

            # control    
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w or i.key == pygame.K_UP:
                    up = True
                if i.key == pygame.K_a or i.key == pygame.K_LEFT:
                    left = True
                if i.key == pygame.K_d or i.key == pygame.K_RIGHT:
                    right = True 
                if i.key == pygame.K_s or i.key == pygame.K_DOWN:
                    down = True


            if i.type == pygame.KEYUP:
                if i.key == pygame.K_w or i.key == pygame.K_UP:
                    up = False
                if i.key == pygame.K_a or i.key == pygame.K_LEFT:
                    left = False
                if i.key == pygame.K_d or i.key == pygame.K_RIGHT:
                    right = False 
                if i.key == pygame.K_s or i.key == pygame.K_DOWN:
                    down = False


            # лазерный луч
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and luchcount > 0:
                    luchcount -= 1
                    c = 5
                    luchx = i.pos[0]
                    luchy = i.pos[1]
                    if x2-r < luchx < x2+r and y2-r < luchy < y2+r:
                        s_sh.play()
                        r = random.randint(30, h-200)
                        y2 = -r
                        speed += 0.5
                        score += 1
                        speed2 += 0.5
                        x2 = random.randint(0, 800)
                        cc = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                        strafecounter += 1



            # strafe
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_q and x > 0 and strafecounter > 0:
                    x -= 200
                    strafecounter -= 1
                if i.key == pygame.K_e and x < 750 and strafecounter > 0:
                    x += 200
                    strafecounter -= 1


        if up and y > 0:
            y -= speed2
        if down and y < 460:
            y += speed2
        if right and x < 750:
            x += speed2
        if left and x > 0:
            x -= speed2



        if y2 >= h + r:
            s_sh.play()
            luchcount += 1
            r = random.randint(30, h-200)
            y2 = -r
            speed += 0.5
            score += 1
            speed2 += 0.5
            x2 = random.randint(0, 800)
            cc = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]




        y2 += speed
        bgy += 4
        bg2y += 4
        luchtext = my_font.render(f'laser rays: {luchcount}', True, (255, 0, 0))
        strafetext = my_font.render(f'strafes: {strafecounter}', True, (255, 0, 0))
        text1 = my_font.render('Your score is:', True, (255, 0, 0))
        ff = open("123.txt", "r+", encoding="utf-8")
        f1 = ff.read()
        if int(f1) < score:
            scorechar = my_font.render(f'{score}', True, (0, 255, 0))
            record = my_font.render('new record', True, (0, 255, 0))
            screen.blit(record, (x3, y3+20))
        else:
            scorechar = my_font.render(f'{score}', True, (255, 0, 0))
        ff.close()


        if bgy == 500:
            bgy = -500
        if bg2y == 500:
            bg2y = -500


        if c > 0:
            pygame.draw.line(screen,[0,255,255] , [x+25, y], [luchx, luchy], 6)
            c -= 1


        pygame.display.flip()
        screen.blit(bg, (0, bgy))
        screen.blit(bg2, (0, bg2y))
        screen.blit(pl, (x, y))
        pygame.draw.circle(screen,cc, [x2,y2], r)
        screen.blit(text1, (x3, y3))
        screen.blit(scorechar, (x3+138, y3))
        screen.blit(text01, (x3+250, y3))
        screen.blit(strafetext, (x3+450, y3))
        screen.blit(luchtext, (x3+650, y3))


   


pygame.quit()