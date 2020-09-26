import pygame
pygame.init()

screen_width=852
screen_height=480

win=pygame.display.set_mode((screen_width,screen_height)) #creates a window; brackets contain tuple with resolution
pygame.display.set_caption('My Game') #title of window

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock=pygame.time.Clock()

class player:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0
        self.standing=True

    def draw(self,win):
        if self.walkCount+1>=27:
            self.walkCount=0
        if not(self.standing):    
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))

class projectile:
    def __init__(self,x,y,radius,colour,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.colour=colour
        self.facing=facing
        self.vel=8*facing #depending on positive or negative value of facing projectile goes left or right 

    def draw(self,win):
        pygame.draw.circle(win,self.colour,(self.x,self.y),self.radius)

def redrawGameWindow():
    win.blit(bg,(0,0)) #to constantly fill with background 
    man.draw(win)   
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update() #refresh the display

#main
man=player(50,350,64,64)
bullets=[]
run=True
while run:
    clock.tick(27) #27 frames/second

    #lets us close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run=False


    for bullet in bullets:
        if bullet.x<852 and bullet.x>0:
            bullet.x+=bullet.vel        #when bullets are inside the window 
        else:
            bullets.pop(bullets.index(bullet)) #when bullets are outside the window they are deleted
    #movement
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing=-1
        else:
            facing=1            
        if len(bullets)<5:
            bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing)) #divided by 2 so that bullets come from the centre of the man

    if keys[pygame.K_LEFT] and man.x>man.vel:
        man.x-=man.vel
        man.left=True
        man.right=False
        man.standing=False
    elif keys[pygame.K_RIGHT] and man.x<screen_width-man.width-man.vel:
        man.x+=man.vel
        man.right=True
        man.left=False
        man.standing=False
    else:
        man.standing=True
        man.walkCount=0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump=True
            man.right=False
            man.left=False
            man.walkCount=0
            
    else:
        if man.jumpCount>=-10:
            neg=1
            if man.jumpCount<0:
                neg=-1
            man.y-=(man.jumpCount**2)*0.5*neg
            man.jumpCount-=1
        else:
            man.isJump=False
            man.jumpCount=10
        
    redrawGameWindow()
    
pygame.quit()            
