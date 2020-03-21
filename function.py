#function:
import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep
level=0
key=False
key2=True
# even
def checkevent(ship,bullets,screen,button,button2,left):
    
    
    for event in pygame.event.get():
        # quit
        if event.type==pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.rightmove=True
            elif event.key==pygame.K_LEFT:
                ship.leftmove=True
            elif event.key==pygame.K_SPACE:
                if len(bullets)<3:
                    newbullet=Bullet(screen,ship)
                    bullets.add(newbullet)
            elif event.key==pygame.K_UP:
                ship.upmove=True
            elif event.key==pygame.K_DOWN:
                ship.downmove=True


                    
                
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                ship.rightmove=False
            elif event.key==pygame.K_LEFT:
                ship.leftmove=False
            elif event.key==pygame.K_UP:
                ship.upmove=False
            elif event.key==pygame.K_DOWN:
                ship.downmove=False
                
                
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mousex,mousey=pygame.mouse.get_pos()
            if button.rect.collidepoint(mousex,mousey):
                global key
                key=True
            if button2.rect.collidepoint(mousex,mousey):
                global key2
                key2=True
                left.life=3
                
                
def display(button):
    if key==False:
        button.draw()


def display2(button2):
    if  not key2:
        button2.draw()
        
def scorecheck(score,ms):
    if ms.score<score.primary:
        ms.score=score.primary
        ms.newimage()










        
        

def keycontrol(aliens,bullets,screen,button2,score,ms,level1,left):
    if left.life==0:
        
        global key2
        key2=False
        scorecheck(score,ms)
        
        score.primary=0
        score.newimage()
        
        display2(button2)
        global level
        level=0
        level1.msg=str(level)
        level1.newimage()
        
    
                    

# bullets          
def screenupdate(bullets):
    for bullet1 in bullets.sprites():
        bullet1.show()

def delbullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.y<0:
            bullets.remove(bullet)

# aliens

    



    
def showaliens(screen,aliens,ship,bullets):
    alien=Alien(screen,ship,bullets)

    screen_rect=screen.get_rect()
    numx=int((screen_rect.width-(2*alien.rect.width))/(2*alien.rect.width))
    numy=int((screen_rect.height-(3*alien.rect.height))/(2*alien.rect.height))
    for y in range(numy):
        for x in range(numx):
            alien=Alien(screen,ship,bullets)
            if level:
                alien.vx=6*level
            alien.rect.x=alien.rect.width+2*alien.rect.width*x
            alien.rect.y=alien.rect.height+2*alien.rect.height*y
            aliens.add(alien)
    
def movealien(aliens):
    for alien in aliens.sprites():
        alien.turn()

# debug
def reagain(screen,aliens,ship,bullets,level1):
    if len(aliens)==0:
        global level
        level+=1
        level1.msg=str(level)
        level1.newimage()
        bullets.empty()
        
        showaliens(screen,aliens,ship,bullets)
        
   
# collide:

def kill(aliens,bullets,score):
    t=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if t:
        score.primary+=10
        score.newimage()        
       
        
        

    
def die(ship,aliens,bullets,screen,score,left):
    if pygame.sprite.spritecollideany(ship,aliens):
        restartgame(aliens,bullets,ship,screen)
        left.life-=1
        left.show()
        score.primary-=50
        score.newimage()
        
        
def die2(aliens,screen,bullets,ship,score):
    screenrect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screenrect.bottom:
            score.primary-=10
            score.newimage()
            restartgame(aliens,bullets,ship,screen)


            
def restartgame(aliens,bullets,ship,screen):
        aliens.empty()
        bullets.empty()
        ship.restart()
        
        showaliens(screen,aliens,ship,bullets)
        sleep(1)
        
        
        
