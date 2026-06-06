import pygame
from circleshape import CircleShape
from shot        import Shot
from constants   import (
    PLAYER_RADIUS,
    LINE_WIDTH,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    SHOT_RADIUS,
    PLAYER_SHOT_SPEED
)

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        # Turns counterclockwise
        if keys[pygame.K_h]:
            if dt == 0.0:
                self.rotate(0.0)
            else:
                self.rotate(-1/dt)

        # Turns clockwise
        if keys[pygame.K_n]:
            self.rotate(dt)

        # Goes up
        if keys[pygame.K_c]:
            self.move(dt)

        # Goes down
        if keys[pygame.K_t]:
            if dt == 0.0:
                self.move(0.0)
            self.move(-dt)

        # Shoots
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        new_shot = Shot(self.position.x, self.position.y)
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOT_SPEED
        new_shot.velocity = rotated_with_speed_vector
