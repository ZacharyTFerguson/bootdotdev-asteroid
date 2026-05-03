import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_event
from logger import log_state
from player import Player
from shot import Shot





VERSION = pygame.version.ver
print(f"Starting Asteroids with pygame version: 2.6.1 {VERSION}")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():

    pygame.init()
    Clock_Object = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    field = AsteroidField()


    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    while True:
        log_state()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

        dt = Clock_Object.tick(60) / 1000

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split(  )
                    pygame.sprite.Sprite.kill(shot)


        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
