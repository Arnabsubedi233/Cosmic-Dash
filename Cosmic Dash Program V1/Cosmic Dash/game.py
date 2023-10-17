import pygame
import buttons
import random





def game():
    pygame.init()

    font=pygame.freetype.SysFont(None, 15)
    font.origin=True

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
    spd_multi = 1

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
    
    #settings page buttons
    

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Define a Player object by extending pygame.sprite.Sprite
    # The surface drawn on the screen is now an attribute of 'player'
    class Player(pygame.sprite.Sprite):
        def __init__(self,image,left):
            super(Player, self).__init__()
            self.surf = pygame.image.load(image).convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect(bottomleft= left)
            self.move_left = False
            self.move_right = False

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


    class Sprite(pygame.sprite.Sprite):
        def __init__(self,image,top_left):
            super().__init__()
            self.surf = pygame.image.load(image).convert()
            self.surf.set_colorkey((0,0,0), RLEACCEL)
            self.rect = self.surf.get_rect(topleft = top_left)
     

    # Intializing entities
    player = Player("avatar/tile001.png",(50,500))
    floor = Sprite("images/Floor.jpg",(0,500))
    background = Sprite("images/Cosmicbackground.jpg",(0,0))
    obs = Sprite("images/meteor.png",(0,0))


    # Create groups to hold enemy sprites and all sprites
    # - all_sprites is used for rendering
    # NOT NEEDED RIGHT NOW
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(floor)
    menu_border = pygame.image.load("images/menuborder.png")
    life = 0 

    
    #audios
    asteriod_sfx = pygame.mixer.Sound("Sound Effects/asteroid.wav")
    
    

    SPEEDUPEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPEEDUPEVENT, 6500)


    while running:
        
        # Scrolling background
        screen.blit(background.surf, (bgx-800,0))
        screen.blit(background.surf, (bgx,0))
        screen.blit(background.surf, (bgx+800,0))
    
        # Running framerate
        clock.tick(60)

        # Timer
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/1000 % 60)
        minutes=int(ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(
            minutes=minutes, millis=millis, seconds=seconds)
        font.render_to(screen, (10, 20), out,pygame.Color('white'))

     


        # Checks if background has scrolled to beggining
        bgx -= (2*spd_multi)
        if bgx <= -800:
            bgx = 0

        # Draw all sprites
        ply_rect = screen.blit(player.surf, player.rect)
        screen.blit(floor.surf, floor.rect)

        #check if game is paused
        if game_paused == True:
            screen.blit(menu_border,(-16,60))
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
                    spd_multi += 0.5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_paused = True
                if event.type == pygame.QUIT:
                    running = False
            
                    # When user presses the spacebar the avatar will jump
                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_SPACE and y_change == 0:
                            y_change = 24
    
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
            player.move_right = keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]
            player.move()

            # Displays the obstacle sprite and 
            # generates a new sprite each time it goes off screen with a new speed
            obs_rect = screen.blit(obs.surf,(obs_x,423))
            asteriod_sfx.play()
            obs_x -= obs_spd
            if obs_x < -100:
                obs_x = 850
                obs_spd = (random.randint(5,10) * spd_multi)

                # Add Life Point system here (Currently ends game at collision)
            if ply_rect.colliderect(obs_rect):
                return
               
      
                
        
        # Update the display
        pygame.display.flip()
