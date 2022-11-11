import pygame as py
import time
from reketid import Reket
from pall import Pall

py.init()

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

#reketid
reketiKiirus = 8
player1 = Reket(valge, reketiLaius, reketiKõrgus)
player2 = Reket(valge, reketiLaius, reketiKõrgus)
player1.rect.x = 20
player1.rect.y = kõrgus / 2 - reketiKõrgus / 2
player2.rect.x = laius - 30
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

def reset():
    py.draw.circle(ekraan, skooriVärv,[pall.rect.x+palliKõrgus/2,pall.rect.y+palliKõrgus/2], palliKõrgus*1.5)
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

    if pall.rect.x >= laius-10:
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

    if mängAlgas == False:
        tekst = font.render('Vajuta ENTER, et alustada!', True, skooriVärv)
        tekstiTaust = py.Surface([laius, kõrgus])
        tekstiKast = tekst.get_rect(center=(laius/2, kõrgus/2))
        tekstiTaust.fill(tausta_värv)
        tekstiTaust.blit(tekst, tekstiKast)
        ekraan.blit(tekstiTaust, (0, 0))
        
        if py.key.get_pressed()[py.K_RETURN]:
            mängAlgas = True
            kõik_sprited.add(pall)

    py.display.flip()
    clock.tick(60)

py.quit()

