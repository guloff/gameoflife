import pygame
import numpy as np
from config import width, height, cell_size, black, white, update_delay

class GameOfLife:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Game of Life')
        self.cols = width // cell_size
        self.rows = height // cell_size
        self.grid = np.zeros((self.rows, self.cols))
        self.paused = True
        self.running = True

    def draw_grid(self):
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                if self.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, white, rect)
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
    game = GameOfLife()
    game.run()