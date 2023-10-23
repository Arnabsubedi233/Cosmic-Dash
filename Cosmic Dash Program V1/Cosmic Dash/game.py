import pygame
from pygame.time import delay
import buttons
import random
import time




    
def game():
    pygame.mixer.pre_init(frequency=44100,size=-16,channels=10,buffer=4096)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(8)
    
    voice = pygame.mixer.Channel(5)

    pygame.init()

    font=pygame.freetype.SysFont(None, 15)
    font.origin=True
    
    font2=pygame.freetype.SysFont(None, 30)
    font2.origin=True

    # Import pygame.locals for easier access to key coordinates
    # Updated to conform to flake8 and black standards
    from pygame.locals import (
        RLEACCEL
    )

    # Define constants for the screen width and height
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    WHITE =  (255,255,255)

    # Other variables to be defined
    y_change = 0
    x_change = 0
    gravity = 1
    bgx = 0
    obs_x = 700
    obs_spd = 5
    scrap_spd = 5
    spd_multi = 1
    fps = 60
    fps_count = 0
    points = 0
    scrap_x = random.randint(0,600)
    scrap_y = random.randint(200,400)

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Variable to keep the main loop running
    running = True
    #States
    game_paused = False


   



    #game paused variable
    
    game_val = "main"
    
    #load button images and button instances
    resume_img = pygame.image.load("images/buttonresume.png")
    exit_img = pygame.image.load("images/buttonquit.png")
    menu_img = pygame.image.load("images/Menu Button.png")
    resume_button = buttons.Button(250,125,resume_img,0.5)
    exit_button = buttons.Button(250,375,exit_img,0.5)
    menu_button = buttons.Button(250,250,menu_img,0.5)

    
    #animations variables
    run_right = [pygame.image.load("avatar/tile008.png"),pygame.image.load("avatar/tile009.png"),pygame.image.load("avatar/tile010.png"),pygame.image.load("avatar/tile011.png")]
    run_left = [pygame.image.load("avatar/tile012.png"),pygame.image.load("avatar/tile013.png"),pygame.image.load("avatar/tile014.png"),pygame.image.load("avatar/tile014.png")]
  
    

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Define a Player object by extending pygame.sprite.Sprite
    # The surface drawn on the screen is now an attribute of 'player'
    class Player(pygame.sprite.Sprite):
        def __init__(self,image,left):
            super(Player, self).__init__()
            self.surf = pygame.image.load(image).convert_alpha()
            self.rect = self.surf.get_rect(bottomleft= left)
            self.move_left = False
            self.move_right = False
            self.current_sprite_l = 0
            self.current_sprite_r = 0

        def move(self):
            x_change = 0
            if not game_paused:
                if self.move_left:
                    x_change = -4
                elif self.move_right:
                    x_change = 4
                    
           

                if 0 <= player.rect.left and player.rect.right <= 800:
                    player.rect.x += x_change
                elif 0 >= player.rect.left:
                    player.rect.x = 0
                elif player.rect.right >= 800:
                    player.rect.right = 800

        def left(self):
            self.current_sprite_l+=0.2

            if self.current_sprite_l >= len(run_left):
                self.current_sprite_l = 0

            self.surf = run_left[int(self.current_sprite_l)]

        def right(self,val):
            self.current_sprite_r+=val

            if self.current_sprite_r >= len(run_right):
                self.current_sprite_r = 0

            self.surf = run_right[int(self.current_sprite_r)]

    def gameover():
        screen.fill((0,0,0))
        pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render('GAME OVER', False, (0, 0, 0))
        screen.blit(text_surface, (0,0))
        
        
        

    class Sprite(pygame.sprite.Sprite):
        def __init__(self,image,top_left,offset = 0,characterWidth = 0):
            super().__init__()
            self.surf = pygame.image.load(image).convert_alpha()
            self.rect = self.surf.get_rect(topleft = top_left)
            self.otherrect = pygame.Rect(self.surf.get_rect().left, self.surf.get_rect().top, characterWidth, self.surf.get_rect().height- offset)
     
    def inverted(img):
       inv = pygame.Surface(img.get_rect().size, pygame.SRCALPHA)
       inv.fill((255,255,255,255))
       inv.blit(img, (0,0), None, pygame.BLEND_RGB_SUB)
       return inv

    # Intializing entities
    player = Player("avatar/tile001.png",(50,500))
    floor = Sprite("images/Floor.jpg",(0,500))
    background = Sprite("images/Cosmicbackground.jpg",(0,0))
    obs = Sprite("images/meteor.png",(0,0),12,60)
    heart1 = Sprite('images/heart.png',(10,25))
    heart2 = Sprite('images/heart.png',(30,25))
    
    ship = ["spacecraft/Arm1.png","spacecraft/Arm2.png","spacecraft/Arm3.png","spacecraft/Arm4.png"]
    scrap = Sprite(ship[random.randint(0,3)],(10,25))


    # Create groups to hold enemy sprites and all sprites
    # - all_sprites is used for rendering
    # NOT NEEDED RIGHT NOW

    menu_border = pygame.image.load("images/menuborder.png")
    
    #audios

    asteriod_sfx = pygame.mixer.Sound("Sound Effects/asteroid.wav")
    scrap_sfx = pygame.mixer.Sound("Sound Effects/coin2.wav")
    
    

    SPEEDUPEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPEEDUPEVENT, 6500)
    COLLIDEEVENT = pygame.USEREVENT + 2
    Collide_event = pygame.event.Event(COLLIDEEVENT)
    WINEVENT = pygame.USEREVENT + 3
    Win_event = pygame.event.Event(WINEVENT)

    downsize = False
    while running:
        
        
        # Scrolling background
        screen.blit(background.surf, (bgx-800,0))
        screen.blit(background.surf, (bgx,0))
        screen.blit(background.surf, (bgx+800,0))

        screen.blit(floor.surf, (bgx-800,500))
        screen.blit(floor.surf,(bgx,500))
        screen.blit(floor.surf, (bgx+800,500))
    
        # Running framerate
        clock.tick(60)
        
        # Timer
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        # seconds=int(ticks/1000 % 60)
        # minutes=int(ticks/60000 % 24)
        # out='{minutes:02d}:{seconds:02d}:{millis}'.format(
        #     minutes=minutes, millis=millis, seconds=seconds)
        # font.render_to(screen, (10, 20), out,pygame.Color('white'))

        
        total_seconds = fps_count // fps
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        out='{minutes:02d}:{seconds:02d}:{millis:02d}'.format(
             minutes=minutes,millis=millis, seconds=seconds)
        font.render_to(screen, (10, 20), out,pygame.Color('white'))
        fps_count += 1
        
        out = '{score}/15'.format(score=points)
        font2.render_to(screen, (720,30),out,pygame.Color('white'))
            
        # Life Points
        screen.blit(heart1.surf,heart1.rect)
        screen.blit(heart2.surf,heart2.rect)

        # Checks if background has scrolled to beggining
        bgx -= (2*spd_multi)
        if bgx <= -800:
            bgx = 0

        # Draw all sprites
        if downsize == False:
            ply_rect = screen.blit(player.surf, player.rect)
        elif downsize == True:
            ply_rect = screen.blit(player.surf, player.rect)

        if ply_rect:
            player.right(0.1)
        

        # Ends game when health falls to 0
        if heart2.rect.x > 10000 and heart1.rect.x > 10000:
            running = False
            
        #check if game is paused
        if game_paused == True:
            if resume_button.draw(screen):
                game_paused = False
            if exit_button.draw(screen):
                running = False
            if menu_button.draw(screen):
                return
            for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       game_paused = False
        else:
        
            # Exits the game window when the user presses X
            for event in pygame.event.get():

                if event.type == SPEEDUPEVENT:
                    spd_multi += 0.3
                    
                if event.type == COLLIDEEVENT:
                    # pygame.mixer.Channel(5).play(pygame.mixer.Sound('Sound Effects/asteroid3.ogg'), maxtime=600)
                    if voice.get_busy():
                        print("AAAAAAAAAAAAAAAAAAAAAA")
                    
                    if heart2.rect.x < 10000:
                        heart2.rect.x = 90000
                    else:
                        heart1.rect.x = 90000
                        
                    player.rect.x = 50
                    obs_x = 850
                    time.sleep(0.5)
                    spd_multi = 1
                    downsize = True
                    
                    
                
                # Add win screen here
                if event.type == WINEVENT:
                    return "win"
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_paused = True
                        total_seconds = 0
                        fps_count = 0
                        
                if event.type == pygame.QUIT:
                    running = False
            
                    # When user presses the spacebar the avatar will jump
                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_SPACE and y_change == 0:
                            y_change = 19
    
            # This checks the avatars current position 
            # And changes its position when needed
            if y_change > 0 or player.rect.bottom < 500:
                player.rect.bottom -= y_change
                y_change -= gravity
            if player.rect.bottom > 500:
                player.rect.bottom = 500
            if player.rect.bottom == 500 and y_change < 0:
                y_change = 0
            
            keys = pygame.key.get_pressed()
            player.move_left  = keys[pygame.K_LEFT]  and not keys[pygame.K_RIGHT]
            if player.move_left:
                player.left()

            player.move_right = keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]
            if player.move_right:
                player.right(0.2)
            player.move()
            
            
            # Displays the obstacle sprite and 
            # generates a new sprite each time it goes off screen with a new speed
            obs_rect = screen.blit(obs.surf,(obs_x,423))
            obs_rect = obs_rect.inflate(-20,0)
            
            obs_x -= obs_spd
            if obs_x < -100:
                obs_x = 850
                obs_spd = (random.randint(3,8) * spd_multi)

                # Add Life Point system here (Currently ends game at collision)
            if ply_rect.colliderect(obs_rect):
                # pygame.mixer.Channel(0).play(pygame.mixer.Sound('Sound Effects/asteroid.wav'), maxtime=600)
                pygame.event.post(Collide_event)
                
            if downsize == True:
                    player.surf = pygame.transform.scale(player.surf,(player.rect.height//1.4,player.rect.width//1.4))
            else: 
                 pass

                
            scrap2 = pygame.transform.scale(scrap.surf, (int(scrap.rect.height), int(scrap.rect.width)))
            
            scrap_rect = screen.blit(scrap2,(scrap_x,scrap_y))
            scrap_rect = scrap_rect.inflate(-20,0)
            scrap_x -= scrap_spd
              
            if scrap_x < -100:
                scrap_x = 850
                scrap_y = random.randint(200,400)
                scrap_spd = (random.randint(3,8) * spd_multi)

            if ply_rect.colliderect(scrap_rect):
                scrap = Sprite(ship[random.randint(0,3)],(10,25))
                scrap_x = 850
                scrap_y = random.randint(200,400)
                points += 1
         
        if points >= 15:
            pygame.event.post(Win_event)
            return "win"
            

        
      
                
                
               
      
                
        
        # Update the display
        pygame.display.flip()
