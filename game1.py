import pygame
pygame.init()

screen_width=500
screen_height=500

win=pygame.display.set_mode((screen_width,screen_height)) #creates a window; brackets contain tuple with resolution
pygame.display.set_caption('My Game') #title of window

x=50
y=450
width=40
height=60
vel=5
jumpCount=10
isJump=False
run=True

while run:
    pygame.time.delay(100)

    #lets us close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            run=False
    
    #movement
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x<screen_width-width-vel:
        x+=vel
    if not(isJump):
        if keys[pygame.K_UP] and y>vel:
            y-=vel
        if keys[pygame.K_DOWN] and y<screen_height-height-vel:
            y+=vel
        if keys[pygame.K_SPACE]:
            isJump=True
    else:
        if jumpCount>=-10:
            neg=1
            if jumpCount<0:
                neg=-1
            y-=(jumpCount**2)*0.5*neg
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10
        
    #draw a character
    win.fill((0,0,0)) #to constantly remove old rectangle 
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update() #refresh the display


    
pygame.quit()            
