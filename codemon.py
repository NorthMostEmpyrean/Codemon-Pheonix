import pygame
from maps import Maps
from player import Player

clock_speed = 10 

#main function for Codemon
def main():
    # Load in map bullshit
    default_map = Maps(name = "default_test", map_path="default_test.map.txt")

    #Spawn in player
    player = Player(default_map.get_center())

    #Black background colour
    background_color = (0,0,0)
    screen_size = (default_map.TILE_WIDTH * 8, default_map.TILE_HEIGHT * 8)

    # Pygame boilerplate setup
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    running = True

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
            player.set_y(player.get_y() - 1)
        if keys[pygame.K_s]:
            player.set_y(player.get_y() + 1)
        if keys[pygame.K_a]:
            player.set_x(player.get_x() - 1)
        if keys[pygame.K_d]:
            player.set_x(player.get_x() + 1)

        #End Game Logic Section
        ##########################
        # Start Render Section
        ##
        # Blank the Screen
        screen.fill(background_color) 

        sprite_box = (player.get_player_pos()[0] * default_map.get_tile_width(), 
                      player.get_player_pos()[1] * default_map.get_tile_height(), 
                      default_map.get_tile_height(), 
                      default_map.get_tile_width())
        pygame.draw.rect(
            screen, 
            "white", 
            sprite_box
        )

        # Draw to screen.
        pygame.display.flip()
 
        # End Render Section 
        ##########################

        clock.tick(clock_speed) 
    # End Main Game Loop
    ##############################    

if __name__ == "__main__":
    main()
