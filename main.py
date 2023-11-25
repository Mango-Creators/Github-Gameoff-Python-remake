import pygame
import space_ship
import pipe

pygame.init()

# Main window
dimensions = [900, 600]
screen = pygame.display.set_mode(tuple(dimensions))
pygame.display.set_caption("Game")

# Images of surfaces
background = pygame.image.load("Space Background.png").convert()
player = pygame.sprite.GroupSingle()
player.add(space_ship.SpaceShip(pygame.transform.rotate(
    pygame.transform.scale(pygame.image.load("Main Ship - Base - Damaged.png").convert_alpha(), (48 * 2, 48 * 2)), -90),
                                (200, dimensions[1] / 2), 600))

# Gamestates
game_states = ['menu', "play", "game_over"]
game_state = game_states[1]

# Loop Vars
is_running = True
clock = pygame.time.Clock()

# Spawning pipes
spawn_timer = pygame.time.get_ticks()
spawn_interval = 3000
pipes_track = pygame.sprite.Group()

if __name__ == "__main__":

    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        if game_state == game_states[1]:
            # Spawn Enemies
            current_time = pygame.time.get_ticks()
            if current_time - spawn_timer > spawn_interval:
                pipes_track.add(pipe.PipePair(screen))
                spawn_timer = current_time
            screen.blit(background, (0, 0))  # Displaying background

            # GameObjects displayed here
            player.draw(screen)
            player.update()
            pipes_track.update()
            for p in pipes_track.sprites():  # Garbage collection (bassically deleteing something when out of screen)
                if p.upper_pipe.x <= -52:
                    pipes_track.remove(p)
                    del p

        pygame.display.update()  # Updating all display
        clock.tick(60)  # Setting max framerate

    pygame.quit()
    exit()
