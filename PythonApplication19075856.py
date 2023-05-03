import pygame
import random


pygame.init()

screenX = 640
screenY = 480

Taust = (3, 44, 55)
tekst = (0, 0, 0)
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
Pall=[r,g,b]


screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Умри солнышко")

# Шрифт для отображения счета
font = pygame.font.SysFont(None, 36)

# Начальное значение счета
score = 0

# Создание шарика
ball_radius = random.randint(5,80)
ball_pos = [random.randint(ball_radius, screenX - ball_radius),
            random.randint(ball_radius, screenY - ball_radius)]
ball_color = Pall
ball_speed = [random.randint(2, 6), random.randint(2, 6)]


#цикл игры
game_over = False
clock = pygame.time.Clock()
while not game_over:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка попадания мышкой в шарик
            mouse_pos = pygame.mouse.get_pos()
            if ((mouse_pos[0] - ball_pos[0]) ** 2 +
                    (mouse_pos[1] - ball_pos[1]) ** 2 <= ball_radius ** 2):
                # Увеличение счета при попадании в шарик
                score += 1
               
                # Создание нового шарика
                ball_pos = [random.randint(ball_radius, screenX - ball_radius),
                            random.randint(ball_radius, screenY - ball_radius)]
                ball_speed = [random.randint(2, 6), random.randint(2, 6)]
                ball_radius = random.randint(5,80)
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                Pall=[r,g,b]
                ball_color = Pall
    # Обновление положения шарика
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]
    if ball_pos[0] < ball_radius or ball_pos[0] > screenX - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] < ball_radius or ball_pos[1] > screenY - ball_radius:
        ball_speed[1] = -ball_speed[1]

    screen.fill(Taust)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    score_text = font.render("Счет: {}".format(score), True, tekst)
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
