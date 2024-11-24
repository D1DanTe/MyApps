import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Improved Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Игрок
player = pygame.Rect(375, 275, 50, 50)
player_speed = 5

# Точка
target = pygame.Rect(random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30), 30, 30)
target_speed = 2

# Бонусная точка
bonus = pygame.Rect(random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30), 20, 20)
bonus_timer = 0

# Счёт и уровень
score = 0
level = 1

# Основной цикл игры
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Движение цели
    target.y += target_speed
    if target.y > HEIGHT:
        target.y = 0
        target.x = random.randint(0, WIDTH-30)

    # Проверка столкновения
    if player.colliderect(target):
        score += 1
        target.x = random.randint(0, WIDTH-30)
        target.y = 0

    # Появление бонуса
    if bonus_timer == 0 and random.random() < 0.01:
        bonus.x = random.randint(0, WIDTH-20)
        bonus.y = random.randint(0, HEIGHT-20)
        bonus_timer = 200  # Бонус будет доступен 200 кадров
    if bonus_timer > 0:
        bonus_timer -= 1
    if player.colliderect(bonus):
        score += 5
        bonus_timer = 0

    # Уровень сложности
    if score % 10 == 0 and score > 0:
        level += 1
        target_speed += 1
        score += 1  # Чтобы уровень не пересчитывался на каждом кадре

    # Рендеринг
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, target)
    if bonus_timer > 0:
        pygame.draw.rect(screen, BLUE, bonus)

    # Отображение счёта и уровня
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score} | Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()