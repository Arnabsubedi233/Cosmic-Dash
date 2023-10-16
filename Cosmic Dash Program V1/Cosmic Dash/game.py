import pygame
import buttons

def game():
    pygame.init()

    # Import pygame.locals for easier access to key coordinates
    # Updated to conform to flake8 and black standards
    from pygame.locals import (
        RLEACCEL
    )

    # Define constants for the screen width and height
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    WHITE =  (255,255,255)

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Variable to keep the main loop running
    running = True
    #game paused variable
    game_paused = False

    #load button images
    resume_img = pygame.image.load("images/button_resume.png")
    exit_img = pygame.image.load("images/button_quit.png")

    #button instance
    resume_button = buttons.Button(250,125,resume_img,0.5)
    exit_button = buttons.Button(250,250,exit_img,0.5)

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()

    # Define a Player object by extending pygame.sprite.Sprite
    # The surface drawn on the screen is now an attribute of 'player'
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.surf = pygame.image.load("images/avatar.png").convert()
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect(bottomleft=(50,500))

    class Sprite(pygame.sprite.Sprite):
        def __init__(self,image,top_left):
            super().__init__()
            self.surf = pygame.image.load(image).convert()
            self.surf.set_colorkey((0,0,0), RLEACCEL)
            self.rect = self.surf.get_rect(topleft = top_left)
        


    player = Player() 
    floor = Sprite("images/Template_Floor.jpg",(0,500))
    background = Sprite("images/Cosmicbackground.jpg",(0,0))
    y_change = 0
    gravity = 1
    # Create groups to hold enemy sprites and all sprites
    # - all_sprites is used for rendering
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(floor)


    while running:
    
        # Fill the screen with blue
        screen.fill((0, 0, 20))
        screen.blit(background.surf, background.rect)
    
        # Running framerate
        clock.tick(60)

    

        # Creates a rectangle for the floor the last var is 
        # [indent from left, indent from top, width, height]
        floor = pygame.draw.rect(screen,WHITE,[0,500,SCREEN_WIDTH,300])
    
        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        #check if game is paused
        if game_paused == True:
            if resume_button.draw(screen):
                game_paused = False
            if exit_button.draw(screen):
                running = False
            for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       game_paused = False
        else:
            pass


        
        # Exits the game window when the user presses X
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_paused = True
            if event.type == pygame.QUIT:
                running = False
            
            # When user presses the spacebar the avatar will jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and y_change == 0:
                    y_change = 18
    
        # This checks the avatars current position 
        # And changes its position when needed
        if y_change > 0 or player.rect.bottom < 500:
            player.rect.bottom -= y_change
            y_change -= gravity
        if player.rect.bottom > 500:
            player.rect.bottom = 500
        if player.rect.bottom == 500 and y_change < 0:
            y_change = 0
            
        # Update the display
        pygame.display.flip()







   



