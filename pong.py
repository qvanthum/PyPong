import pygame as py
import time
from reketid import Reket
from pall import Pall
from pygame import mixer
import os,sys

py.init()
mixer.init()

#muusika
dir = os.path.join(sys.path[0], "music.mp3")
mixer.init()
mixer.music.load(dir)
mixer.music.set_volume(0.2)

#värvid
tausta_värv = (202,135,150)
valge = (255,255,255)
skooriVärv = (179,82,104)

#ekraan
kõrgus = 400
laius = 800
ekraani_suurus = (laius, kõrgus)
ekraan = py.display.set_mode(ekraani_suurus)
py.display.set_caption("PyPong")

#muu kasulik
player1score = 0
player2score = 0
reketiKõrgus = 75
reketiLaius = 5
clock = py.time.Clock()
kordus = True
mängAlgas = False
playAgain = 1

#reketid
reketiKiirus = 8
player1 = Reket(valge, reketiLaius, reketiKõrgus)
player2 = Reket(valge, reketiLaius, reketiKõrgus)
player1.rect.x = 20
player1.rect.y = kõrgus / 2 - reketiKõrgus / 2
player2.rect.x = laius - 25
player2.rect.y = kõrgus / 2 - reketiKõrgus / 2

#pall
palliKõrgus = 10
pall = Pall(valge, palliKõrgus, palliKõrgus)
pall.rect.x = laius/2 - palliKõrgus/2
pall.rect.y = kõrgus/2 - palliKõrgus/2

#sprited
kõik_sprited = py.sprite.Group()
kõik_sprited.add(player1)
kõik_sprited.add(player2)

mixer.music.play()

def reset():
    py.draw.circle(ekraan, skooriVärv,[pall.rect.x+palliKõrgus/2,pall.rect.y+palliKõrgus/2], palliKõrgus*2)
    py.display.flip()
    kõik_sprited.remove(pall)
    pall.rect.x = laius/2 - palliKõrgus/2
    pall.rect.y = kõrgus/2 - palliKõrgus/2
    if pall.velocity[0] < 0:
        pall.velocity[0] = -pall.velocity[0]
    else:
        pall.velocity[0] = pall.velocity[0]
    pall.velocity[1] =  0
    player1.rect.y = kõrgus / 2 - reketiKõrgus / 2
    player2.rect.y = kõrgus / 2 - reketiKõrgus / 2
    kõik_sprited.add(pall)
    time.sleep(1)

while kordus:
    #Kui quit
    for event in py.event.get():
        if event.type == py.QUIT:
            kordus = False
        elif event.type == py.KEYDOWN:
            if event.key == py.K_x:
                kordus = False
        if py.key.get_pressed()[py.K_ESCAPE]:
            py.quit()
        if py.key.get_pressed()[py.K_m]:
            mixer.music.stop()
    #loogika
    kõik_sprited.update()

    #reketi kontroll
    nupud = py.key.get_pressed()
    if nupud[py.K_w]:
        player1.liiguÜles(reketiKiirus)
    if nupud[py.K_s]:
        player1.liiguAlla(reketiKiirus)
    if nupud[py.K_UP]:
        player2.liiguÜles(reketiKiirus)
    if nupud[py.K_DOWN]:
        player2.liiguAlla(reketiKiirus)
    
    
    #palli põrkumine
    if py.sprite.collide_mask(pall, player1) or py.sprite.collide_mask(pall, player2):
        pall.põrge()

    if pall.rect.x >= laius - palliKõrgus:
        player1score += 1
        pall.velocity[0] = -pall.velocity[0]
        reset()
    if pall.rect.x <= 0:
        player2score += 1
        pall.velocity[0] = -pall.velocity[0]
        reset()
    if pall.rect.y > kõrgus - palliKõrgus:
        pall.velocity[1] = -pall.velocity[1]
    if pall.rect.y < 0:
        pall.velocity[1] = -pall.velocity[1]    

    #ekraanile joonestamise kood:

    ekraan.fill(tausta_värv)
    font2 = py.font.Font(None, 50)
    font = py.font.Font(None, 74)
    tekst = font.render(str(player1score), 1, skooriVärv)
    ekraan.blit(tekst, (40, 10))
    tekst = font.render(str(player2score), 1, skooriVärv)
    ekraan.blit(tekst, (laius -72, 10))
    
    #mängulaua graafika
    py.draw.circle(ekraan, valge,[laius/2,kõrgus/2], 125)
    py.draw.circle(ekraan, tausta_värv,[laius/2,kõrgus/2], 122)
    py.draw.line(ekraan, valge, [laius/2,0], [laius/2,kõrgus], 3)

    #joonestan ekraanile kõik
    kõik_sprited.draw(ekraan) 

    #win condition
    if player1score == 4 or player2score == 4:
        if player1score > player2score:
            võitis = "Player 1 has won!"
        else:
            võitis = "Player 2 has won!"
        playAgain = 0
        player1score = 0
        player2score = 0
        mängAlgas = False
        kõik_sprited.remove(pall)

    if mängAlgas == False:
        if playAgain == 0:
            tekst = font.render('Press ENTER to play again!', True, skooriVärv)
            tekst2 = font2.render(võitis, True, valge)
            tekstiTaust = py.Surface([laius, kõrgus])
            tekstiKast = tekst.get_rect(center=(laius/2, kõrgus/2))
            tekstiKast2 = tekst.get_rect(center=(laius/2+180, kõrgus/2-50))
            tekstiTaust.fill(tausta_värv)
            tekstiTaust.blit(tekst, tekstiKast)
            tekstiTaust.blit(tekst2, tekstiKast2)
            ekraan.blit(tekstiTaust, (0, 0))
        else:
            tekst = font.render('Press ENTER to start!', True, skooriVärv)
            tekst2 = font2.render("Press ESC to quit and M to stop the music", True, skooriVärv)
            tekstiTaust = py.Surface([laius, kõrgus])
            tekstiKast = tekst.get_rect(center=(laius/2, kõrgus/2))
            tekstiKast2 = tekst.get_rect(center=(laius/2-80, kõrgus/2+50))
            tekstiTaust.fill(tausta_värv)
            tekstiTaust.blit(tekst, tekstiKast)
            tekstiTaust.blit(tekst2, tekstiKast2)
            ekraan.blit(tekstiTaust, (0, 0))

        if py.key.get_pressed()[py.K_RETURN]:
            mängAlgas = True
            playAgain = 1
            for i in range(4):
                tekst = font.render(str(3-i), True, skooriVärv)
                tekstiTaust = py.Surface([laius, kõrgus])
                tekstiKast = tekst.get_rect(center=(laius/2, kõrgus/2))
                tekstiTaust.fill(tausta_värv)
                tekstiTaust.blit(tekst, tekstiKast)
                ekraan.blit(tekstiTaust, (0, 0))
                time.sleep(1)
                py.display.flip()
            kõik_sprited.add(pall)
    py.display.flip()
    clock.tick(60)
py.quit()

