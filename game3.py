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

    def draw(self,win):
        if self.walkCount+1>=27:
            self.walkCount=0
        if self.left:
            win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        elif self.right:
            win.blit(walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        else:
            win.blit(char,(self.x,self.y))

def redrawGameWindow():
    win.blit(bg,(0,0)) #to constantly fill with background 
    man.draw(win)   
    pygame.display.update() #refresh the display


man=player(50,350,64,64)
run=True
while run:
    clock.tick(27) #27 frames/second

    #lets us close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run=False
    
    #movement
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x>man.vel:
        man.x-=man.vel
        man.left=True
        man.right=False
    elif keys[pygame.K_RIGHT] and man.x<screen_width-man.width-man.vel:
        man.x+=man.vel
        man.right=True
        man.left=False
    else:
        man.right=False
        man.left=False
        man.walkCount=0
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
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
