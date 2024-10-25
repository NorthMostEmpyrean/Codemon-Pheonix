import pygame
from maps import Maps
from player import Player

#Black background colour
background_color = (0,0,0)
screen_size = (1024, 768)

#main function for Codemon
def main():
    # Pygame boilerplate setup
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    running = True

    screen_center_x = screen_size[0] // 2
    screen_center_y = screen_size[1] // 2

    player = Player(screen_center_x, screen_center_y)
    default_map = Maps("default", (10, 10))

    # Start Main Game Loop
    while running:
        ##########################
        # Start Game Logic Section
        ##

        ###
        # Poll for events
        for event in pygame.event.get():
            # Game told to quit
            if event.type == pygame.QUIT:
                running = False

        ##
        # Poll for keyboard events - Player Movement section
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.set_y(player.get_y() - 32)
        if keys[pygame.K_s]:
            player.set_y(player.get_y() + 32)
        if keys[pygame.K_a]:
            player.set_x(player.get_x() - 32)
        if keys[pygame.K_d]:
            player.set_x(player.get_x() + 32)

        #End Game Logic Section
        ##########################
        # Start Render Section
        ##
        screen.fill(background_color) # Blank the Screen
        sprite_box = (player.get_player_pos()[0],player.get_player_pos()[1], 32, 32)
        pygame.draw.rect(
            screen, 
            "white", 
            sprite_box
        )

        # Draw to screen.
        pygame.display.flip()
 
        # End Render Section 
        ##########################

        clock.tick(60)
    # End Main Game Loop
    ##############################    

    

if __name__ == "__main__":
    main()
