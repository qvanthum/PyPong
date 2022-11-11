import pygame as py
from reketid import Reket
from pall import Pall

py.init()

#värvid

tausta_värv = (202,135,150)
valge = (255,255,255)

#ekraan

ekraani_suurus = (700,500)
ekraan = py.display.set_mode(ekraani_suurus)
py.display.set_caption("Poooong")

#muu kasulik

clock = py.time.Clock()
kordus = True

#reketid

reketPlayer = Reket(valge, 5, 75)
reketArvuti = Reket(valge, 5, 75)
reketPlayer.rect.x = 20
reketPlayer.rect.y = 200
reketArvuti.rect.x = 670
reketArvuti.rect.y = 200

#pall

pall = Pall(valge, 10, 10)
pall.rect.x = 345
pall.rect.y = 245

#spritedega mässamine

kõik_sprited = py.sprite.Group()
kõik_sprited.add(reketPlayer)
kõik_sprited.add(reketArvuti)
kõik_sprited.add(pall)

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
        reketPlayer.liiguÜles(5)
    if nupud[py.K_s]:
        reketPlayer.liiguAlla(5)
    
    #palli põrkumine
    if pall.rect.x >= 690:
        pall.velocity[0] = -pall.velocity[0]
    if pall.rect.x <= 0:
        pall.velocity[0] = -pall.velocity[0]
    if pall.rect.y > 490:
        pall.velocity[1] = -pall.velocity[1]
    if pall.rect.y < 0:
        pall.velocity[1] = -pall.velocity[1]
    
    if py.sprite.collide_mask(pall, reketPlayer) or py.sprite.collide_mask(pall, reketArvuti):
        pall.põrge()

    #ekraanile joonestamise kood:

    ekraan.fill(tausta_värv)
    
    #mängulaua graafika
    py.draw.circle(ekraan, valge,[349,250], 125)
    py.draw.circle(ekraan, tausta_värv,[349,250], 122)
    py.draw.line(ekraan, valge, [349,0], [349,500], 3)

    #joonestan ekraanile kõik
    kõik_sprited.draw(ekraan)

    py.display.flip()
    clock.tick(60)

py.quit()

