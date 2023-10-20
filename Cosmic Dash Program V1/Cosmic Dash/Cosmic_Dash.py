import pygame
import buttons
import game


def home():
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

    #variables to hold buttons and images of buttons
    play_img = pygame.image.load("images/playbutton.png")
    play_button = buttons.Button(250,125,play_img,0.5)

    settings_img = pygame.image.load("images/settingsbutton.png")
    settings_img = buttons.Button(250,250,settings_img,0.5)

    exit_img = pygame.image.load("images/buttonquit.png")
    exit_button = buttons.Button(250,375,exit_img,0.5)

    #Setting page buttons
    aud_img = pygame.image.load("images/Audio Square Button.png")
    aud_button = buttons.Button(280,125,aud_img,0.5)
    music_img = pygame.image.load("images/Music Square Button.png")
    music_button = buttons.Button(280,250,music_img,0.5)
    info_img = pygame.image.load("images/Info Square Button.png")
    info_button = buttons.Button(430,125,info_img,0.5)
    back_img = pygame.image.load("images/Back Square Button.png")
    back_button = buttons.Button(430,250,back_img,0.5)
    home_img = pygame.image.load("images/Home Square Button.png")
    home_button = buttons.Button(345,380,home_img,0.5)

    background = pygame.image.load("images/menu.jpg")

    menu_border = pygame.image.load("images/menuborder.png")

    game_val = "main"
    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def win():
        pygame.init()
        victory = pygame.image.load("images/victory.png")
        vic_background = pygame.image.load("images/victory_background.jpg")

         # Import pygame.locals for easier access to key coordinates
         # Updated to conform to flake8 and black standards
        from pygame.locals import (
                RLEACCEL
            )
         # Define constants for the screen width and height
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        WHITE =  (255,255,255)
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        run = True
        pygame.font.init() # you have to call this at the start, 
                    # if you want to use this module.
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface2 = my_font.render('press space to restart', False, (WHITE))
        while run == True:
            clock.tick(60)
            screen.fill((0,0,0))
            screen.blit(vic_background,(0,0))
            screen.blit(victory,(0,0))
            screen.blit(text_surface2,(200,200))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False
                if event.type == pygame.QUIT:
                    quit()
            pygame.display.flip()


    def gameover():
        pygame.init()
        game_over = pygame.image.load("images/gameover.png")

         # Import pygame.locals for easier access to key coordinates
         # Updated to conform to flake8 and black standards
        from pygame.locals import (
                RLEACCEL
            )
         # Define constants for the screen width and height
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        WHITE =  (255,255,255)
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        run = True
        pygame.font.init() # you have to call this at the start, 
                    # if you want to use this module.
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface2 = my_font.render('press space to restart', False, (WHITE))
        while run == True:
            clock.tick(60)
            screen.fill((0,0,0))
            screen.blit(game_over,(200,200))
            screen.blit(text_surface2,(250,400))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False
                if event.type == pygame.QUIT:
                    quit()
            pygame.display.flip()

    def info():
   
        pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
        my_font = pygame.font.SysFont('Impact', 25,)
        screen.fill(white)  
        screen.blit(background,(0,0))
        screen.blit(menu_border,(-16,60))
        text_surface1 = my_font.render('Controls', False, (0, 0, 0))
        screen.blit(text_surface1,(350,150))
        text_surface2 = my_font.render('Space = Jump', False, (0, 0, 0))
        screen.blit(text_surface2,(230,200))
        text_surface3 = my_font.render('A/Left Arrow = move left', False, (0, 0, 0))
        screen.blit(text_surface3,(230,275))
        text_surface4 = my_font.render('D/Right arrow = move right', False, (0, 0, 0))
        screen.blit(text_surface4,(230,350))
        text_surface5 = my_font.render('Escape = Pause', False, (0, 0, 0))
        screen.blit(text_surface5,(230,450))
        

        

        
    pygame.mixer.pre_init(frequency=44100,size=-16,channels=10,buffer=4096)
    pygame.mixer.set_num_channels(8)
    channel1 = pygame.mixer.Channel(1)
    #flag for mainloop
    run = True
    #clock for better frames
    clock = pygame.time.Clock()
    white=(255,255,255)
    main = pygame.mixer.Sound("Sound Effects/mainmenu.mp3")
    game_over = pygame.mixer.Sound("Sound Effects/game over.mp3")
    #main loop
    game_restart = False

    music = True
    while run == True:
        #fills screen colour
        screen.fill((0, 0, 20))
        screen.blit(background,(0,0))
        #screen.blit(menu_border,(-16,60))
        clock.tick(60)

        if music:
            main.set_volume(0.4)
            main.play()
        else:
            main.stop()
        #selection for if button press = true then executes command
        if game_val == "main":
            if play_button.draw(screen):
                val2 = game.game()
                main.stop()
                print(val2)
                if val2 == None:
                    game_over.play()
                    gameover()
                elif val2 == "win":
                    win()

            if settings_img.draw(screen):
                game_val = "side"
            if exit_button.draw(screen):
                run = False
        elif game_val == "side":
            if aud_button.draw(screen):
                pass
            if music_button.draw(screen):
                music = not music
            if back_button.draw(screen):
                game_val = "main"
            if home_button.draw(screen):
                game_val = "main"
            if info_button.draw(screen):
                pass
                

        

        #driver
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False

        #displays on screen
        pygame.display.flip()
home()

