import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рисование в реальном времени")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Переменные для хранения координат мыши
drawing = False
last_pos = None

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_x, mouse_y = event.pos
                pygame.draw.line(screen, BLACK, last_pos, (mouse_x, mouse_y), 5)
                last_pos = (mouse_x, mouse_y)

    pygame.display.flip()