import pygame
import numpy as np
from config import width, height, cell_size, black, white, update_delay
import random

import random

# Список цветов
colors = [
    (220, 20, 60),    # Crimson
    (255, 69, 0),     # Orange Red
    (255, 215, 0),    # Gold
    (0, 255, 0),      # Lime
    (0, 255, 127),    # Spring Green
    (0, 255, 255),    # Cyan
    (0, 191, 255),    # Deep Sky Blue
    (30, 144, 255),   # Dodger Blue
    (123, 104, 238),  # Medium Slate Blue
    (255, 0, 255),    # Magenta (Fuchsia)
    (255, 105, 180),  # Hot Pink
    (255, 99, 71),    # Tomato
    (255, 255, 0),    # Yellow
    (144, 238, 144),  # Light Green
    (64, 224, 208),   # Turquoise
    (127, 255, 212),  # Aqua Marine
    (65, 105, 225),   # Royal Blue
    (128, 0, 128),    # Purple
    (238, 130, 238),  # Violet
    (218, 112, 214),  # Orchid
    (127, 255, 0),    # Chartreuse
    (255, 165, 0),    # Orange
    (250, 128, 114),  # Salmon
    (199, 21, 133),   # Medium Violet Red
    (255, 127, 80),   # Coral
    (255, 140, 0),    # Dark Orange
    (34, 139, 34),    # Forest Green
    (70, 130, 180),   # Steel Blue
    (60, 179, 113),   # Medium Sea Green
    (240, 128, 128)   # Light Coral
]

class GameOfLife:
    def __init__(self, fill_percentage):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Game of Life')
        self.cols = width // cell_size
        self.rows = height // cell_size
        self.grid = np.zeros((self.rows, self.cols))
        self.paused = True
        self.running = True

        # Заполнение случайными живыми клетками в зависимости от процента
        self.fill_random_cells(fill_percentage)

    def fill_random_cells(self, fill_percentage):
        total_cells = self.cols * self.rows
        num_cells_to_fill = int((fill_percentage / 100) * total_cells)
        filled_cells = 0

        while filled_cells < num_cells_to_fill:
            x = random.randint(0, self.cols - 1)
            y = random.randint(0, self.rows - 1)
            if self.grid[y][x] == 0:  # Если клетка мёртвая, делаем её живой
                self.grid[y][x] = 1
                filled_cells += 1

    def draw_grid(self):
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                if self.grid[y][x] == 1:
                    # Выбор случайного цвета
                    # color = random.choice(colors)
                    color = white
                    pygame.draw.rect(self.screen, color, rect)
                else:
                    pygame.draw.rect(self.screen, black, rect, 1)

    def update_grid(self):
        new_grid = np.copy(self.grid)
        for y in range(self.rows):
            for x in range(self.cols):
                neighbors = np.sum(self.grid[y-1:y+2, x-1:x+2]) - self.grid[y, x]
                
                if self.grid[y, x] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[y, x] = 0
                else:
                    if neighbors == 3:
                        new_grid[y, x] = 1
        self.grid = new_grid

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                if event.key == pygame.K_q:
                    self.running = False
            if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
                x, y = pygame.mouse.get_pos()
                self.grid[y // cell_size][x // cell_size] = 1
            if pygame.mouse.get_pressed()[2]:  # Правая кнопка мыши
                x, y = pygame.mouse.get_pos()
                self.grid[y // cell_size][x // cell_size] = 0

    def run(self):
        while self.running:
            self.screen.fill(black)
            self.handle_events()

            if not self.paused:
                self.update_grid()

            self.draw_grid()
            pygame.display.flip()
            pygame.time.delay(update_delay)

        pygame.quit()

# Запуск игры
if __name__ == "__main__":
    # Запрашиваем процент заполнения поля
    fill_percentage = float(input("Enter the percentage of the grid to fill with random live cells: "))
    game = GameOfLife(fill_percentage)
    game.run()