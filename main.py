import time
import pygame
import space_ship
import pipe
from events import *
import pygame.gfxdraw

pygame.init()

# Main window
dimensions = [900, 600]
screen = pygame.display.set_mode(tuple(dimensions))
pygame.display.set_caption("Game")

# Images of surfaces
background = pygame.image.load("Space Background.png").convert()
player = pygame.sprite.GroupSingle()
player.add(
    space_ship.SpaceShip(
        pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load("Main Ship - Base - Damaged.png").convert_alpha(),
                (34 * 2, 27 * 2),
            ),
            -90,
        ),
        (200, 0),
        600,
        "player",
    )
)
score = 0

main_font = pygame.font.Font("ARCADECLASSIC.ttf", 50)

# Initial setting for the score text
score_text = main_font.render(f"{score}", False, pygame.color.Color(255, 255, 255))
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10, 10)

# Creating the gameover text
game_over_text = main_font.render(
    "Game Over!Press  H  to  restart", False, pygame.color.Color(0, 0, 0)
)
game_over_text_rect = game_over_text.get_rect(
    center=(dimensions[0] // 2, dimensions[1] // 2)
)

# Gamestates
game_states = ["menu", "play", "game_over"]
game_state = game_states[1]

# Loop Vars
is_running = True
clock = pygame.time.Clock()

# Spawning pipes
spawn_timer = pygame.time.get_ticks()
spawn_interval = 3000
pipes_track = pygame.sprite.Group()


def reset():
    global game_state
    global score

    player.empty()
    player.add(
        space_ship.SpaceShip(
            pygame.transform.rotate(
                pygame.transform.scale(
                    pygame.image.load("Main Ship - Base - Damaged.png").convert_alpha(),
                    (34 * 2, 27 * 2),
                ),
                -90,
            ),
            (200, 0),
            600,
            "player",
        )
    )
    pipes_track.empty()
    game_state = game_states[1]
    score = 0


game_over = True

if __name__ == "__main__":
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_h:
                    pygame.event.post(pygame.event.Event(RESTART_EVENT))
                if event.key == pygame.K_q:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

            if event.type == GAME_OVER_EVENT:
                game_state = game_states[2]
                game_over =  True

            if event.type == RESTART_EVENT:
                reset()

            if event.type == SCORE_INCREMENT_EVENT:
                score += 1
                print(f"Score: {score}")

        if game_state == game_states[1]:
            score_text_rect.topleft = (30, 30)
            score_text = main_font.render(
                f"{score}", False, pygame.color.Color(255, 255, 255)
            )  # Updating the text as well
            # Spawn Enemies
            current_time = pygame.time.get_ticks()
            if current_time - spawn_timer > spawn_interval:
                pipes_track.add(pipe.PipePair(screen, player.sprites()[0]))
                spawn_timer = current_time
            screen.fill((0, 255, 0))
            screen.blit(background, (0, 0))  # Displaying background
            
            # Displaying the shield
            pygame.gfxdraw.box(screen, player.sprites()[0].rect, (0, 0, 255, 100)) # draw a transparent box
            
            # GameObjects displayed here
            pipes_track.update()
            player.draw(screen)
            player.update()
            for (
                p
            ) in (
                pipes_track.sprites()
            ):  # Garbage collection (bassically deleteing something when out of screen)
                if p.upper_pipe.x <= -52:
                    pipes_track.remove(p)
                    del p
                    break
            screen.blit(score_text, score_text_rect)

        if game_state == game_states[2]:
            if game_over:
                time.sleep(1)
                game_over = False

            screen.fill("#EFBC68")
            screen.blit(game_over_text, game_over_text_rect)

        pygame.display.update()  # Updating all displays
        pygame.display.flip()
        clock.tick(60)  # Setting max framerate

    pygame.quit()
    exit()
