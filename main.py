# main game:
import pygame
from ship import Ship
import function
from pygame.sprite import Group
from button import Button
from score import Score
from max import Max
# bug level change;
from level import Level
from lifes import Lifes

# bug: level chaqnge (mark ,key=1, key++)

def game():
    pygame.init()
    screen=pygame.display.set_mode((900,600))
    screencolor=(230,230,230)
    pygame.display.set_caption('ALIAN!!!')
    ship=Ship(screen)
    bullets=Group()
    aliens=Group()
    function.showaliens(screen,aliens,ship,bullets)
    msg='PLAY'
    msg2='AGAIN'
    msg3='0'
    button=Button(screen,msg)
    button2=Button(screen,msg2)
    score=Score(screen)
    ms=Max(screen)
    level1=Level(screen,msg3)
    left=Lifes(screen,ship)
    while True:
        screen.fill(screencolor)
        ship.show()
        function.checkevent(ship,bullets,screen,button,button2,left)
        aliens.draw(screen)
        function.display(button)
        function.keycontrol(aliens,bullets,screen,button2,score,ms,level1,left)
        score.show()
        ms.show()
        level1.show()
        left.show()

        
        if function.key and function.key2:
            ship.move()
            function.kill(aliens,bullets,score)
            bullets.update()
            function.screenupdate(bullets)
            function.delbullet(bullets)
            function.movealien(aliens)
        #aliens.draw(screen)
            function.die(ship,aliens,bullets,screen,score,left)
            function.die2(aliens,screen,bullets,ship,score)
            function.reagain(screen,aliens,ship,bullets,level1)
            #left.show()
            
            
        
        

        pygame.display.flip()
    



game()
