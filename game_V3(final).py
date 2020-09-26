import pygame
pygame.init()

#-----------------------------------------------------------------------------------------------------

sc_width=852
sc_height=480

win=pygame.display.set_mode((sc_width,sc_height)) #creates a window; brackets contain tuple with resolution
pygame.display.set_caption('My Game') #title of window

#-----------------------------------------------------------------------------------------------------

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')  #background image
#char = pygame.image.load('standing.png')

#-----------------------------------------------------------------------------------------------------

clock=pygame.time.Clock()

score=0

#-----------------------------------------------------------------------------------------------------

class MainCharacter:
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
        self.hitbox=(self.x+17,self.y+11,29,52)  
        
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
        self.hitbox=(self.x+17,self.y+11,29,52)#evertime when when se draw a character move thehitbox with it        
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def hit(self):
        self.isJump=False
        self.jumpCount=10
        self.x=50
        self.y=350
        self.walkCount=0
        font1= pygame.font.SysFont('comicsans',100)
        text=font1.render('-5',1,(255,0,0))
        win.blit(text,((text.get_width()/2),(text.get_height()/2)))
        pygame.display.update()
        i=0
        while(i<300):
            pygame.time.delay(10)
            i+=1

            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    i=301
                    pygame.quit()
            

#-----------------------------------------------------------------------------------------------------        

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

#-----------------------------------------------------------------------------------------------------

class VillanCharacter:
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.walkCount=0
        self.vel=3
        self.path=[self.x,self.end]
        self.hitbox=(self.x+17,self.y+2,31,57)
        self.health =10
        self.visible= True
        
    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount+1>=33:
                self.walkCount=0

            if self.vel>0:  #if velocity is positive it means it is moving right
                win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            else:
                win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10)) # -20 to keep some distance between VillanCharacterand its healthbar 
            pygame.draw.rect(win,(0,255,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health)),10))   
            self.hitbox=(self.x+17,self.y+2,31,57)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)        

    def move(self):
        if self.vel>0:
            if self.x + self.vel<self.path[1]:
                self.x+=self.vel
            else:
                self.vel=self.vel * (-1)
                self.walkCount=0
        else:
            if self.x - self.vel>self.path[0]:
                self.x+=self.vel
            else:
                self.vel=self.vel * (-1)
                self.walkCount=0

    def hit(self):
        if self.health>0:
            self.health-=1
        else:
            self.visible =False
        print('hit')

#-----------------------------------------------------------------------------------------------------        

def redrawGameWindow():
    win.blit(bg,(0,0)) #to constantly fill with background 
    text = font.render('SCORE: '+ str(score),1,(0,0,0)) 
    win.blit(text,(700,20)) # x and y coordinates for text
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update() #refresh the display

#main
font= pygame.font.SysFont('comicsans',30,True,True) #Font,size,bold,italics
man=MainCharacter(50,350,64,64)
goblin= VillanCharacter(100,350,64,64,450)
attackdist=0
bullets=[]
run=True
while run:
    clock.tick(27) #27 frames/second

    if (goblin.visible==True):
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and  man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]: 
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] +goblin.hitbox[2]: 
                man.hit()
                score-=5  #score is decremented when the goblin hits the man

    if attackdist > 0:
        attackdist +=1
    if attackdist >3:
        attackdist =0
    #lets us close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run=False

    
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]: #1.checks we are above bottom of rectangle 2.checks we are below top of rectangle
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] +goblin.hitbox[2]: #1.checks we are on right side of left side of rectangle 2.checks we are on left side of right side of rectangle
                if goblin.visible==True:
                    goblin.hit()
                    score+=1  #score is incremented when ithits the goblin
                    bullets.pop(bullets.index(bullet)) #when bullets collide with hitbox they are deleted
             
        if bullet.x<852 and bullet.x>0: 
            bullet.x+=bullet.vel        #when bullets are inside the window 
        else:
            bullets.pop(bullets.index(bullet)) #when bullets are outside the window they are deleted
    #movement
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and attackdist==0:
        if man.left:
            facing=-1
        else:
            facing=1            
        if len(bullets)<3: # < number of bullets
            bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing)) #divided by 2 so that bullets come from the centre of the man
        attackdist=1

    if keys[pygame.K_LEFT] and man.x>man.vel:
        man.x-=man.vel
        man.left=True
        man.right=False
        man.standing=False
    elif keys[pygame.K_RIGHT] and man.x<sc_width-man.width-man.vel:
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

#-----------------------------------------------------------------------------------------------------
    
pygame.quit()            
