from tkinter.font import BOLD
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
    exit_button2 = buttons.Button(250,500,exit_img,0.5)
    home_img = pygame.image.load("images/Home Square Button.png")
    home_button = buttons.Button(345,380,home_img,0.5)
    audio_off = pygame.image.load("images/Audio Square Button Off.png")
    audio_off_b = buttons.Button(280,125,audio_off,0.5)
    music_off = pygame.image.load("images/Music Square Button Off.png")
    music_off_b = buttons.Button(280,250,music_off,0.5)

    background = pygame.image.load("images/menu.jpg")
    instructions = pygame.image.load("images/instructions.jpg")

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
        arrows = pygame.image.load("images/arrows.png")
        space = pygame.image.load("images/space.png")
        asteroid = pygame.image.load("images/meteor.png")
        heart = pygame.image.load("images/heart.png")
        part = pygame.image.load("spacecraft/wing3Red.png")

   
        pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
        my_font = pygame.font.Font('GidoleFont/Gidole-Regular.ttf', 20,)
        font_title = pygame.font.Font('GidoleFont/Gidole-Regular.ttf', 45)
        screen.fill(white)  
        screen.blit(instructions,(0,0))
        text_surface1 = font_title.render('INSTRUCTIONS', False, (WHITE))
        screen.blit(text_surface1,(250,50))
        screen.blit(arrows,(50,150))
        text_surface2 = my_font.render('You can move left and right with your left and right arrow key', False, (WHITE))
        screen.blit(text_surface2,(150,150))
        screen.blit(space,(50,225))
        text_surface3 = my_font.render('You can Jump with the Spacebar to avoid incoming asteroids', False, (WHITE))
        screen.blit(text_surface3,(150,225))
        screen.blit(asteroid,(50,300))
        text_surface4 = my_font.render('You have to avoid incoming asteroids ', False, (WHITE))
        screen.blit(text_surface4,(150,300))
        screen.blit(heart,(50,375))
        text_surface5 = my_font.render('You have 2 lives so be wise with your next move', False, (WHITE))
        screen.blit(text_surface5,(150,375))
        screen.blit(part,(50,450))
        text_surface6 = my_font.render('You have to collect 15 crashed space craft parts to get out', False, (WHITE))
        screen.blit(text_surface6,(150,450))
        

        

        
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
    off = False
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
            screen.fill(white)  
            screen.blit(background,(0,0))
            if aud_button.draw(screen):
                pygame.mixer.quit
                off = not off
            if music_button.draw(screen):
                music = not music

            if music == False:
                music_off_b.draw(screen)
            else: 
                pass
            if off == True:
                audio_off_b.draw(screen)
            else:
                pass

                
            if back_button.draw(screen):
                game_val = "main"
            if home_button.draw(screen):
                game_val = "main"
            if info_button.draw(screen):
                game_val = "info"
        elif game_val == "info":
            info()
            if exit_button2.draw(screen):
                game_val = "side"
                
                
                

        

        #driver
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False

        #displays on screen
        pygame.display.flip()
home()

