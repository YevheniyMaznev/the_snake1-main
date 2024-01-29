from random import randint

import pygame

# Инициализация PyGame:
pygame.init()

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()
# Тут опишите все классы игры.


class GameObject:
    """Описание родительского класса игрового объекта."""

    def __init__(self):
        """Описание атрибутов класса - изначальных позиции и цвета."""
        self.position = [(SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2)]
        self.body_color = None

    def draw(self):
        """Прорисовка объекта - пропущена."""
        pass


class Apple(GameObject):
    """Дочерний класс Яблоко."""

    def __init__(self):
        """Конструктор класса - внесение атрибутов - цвет, позиция."""
        super().__init__()
        self.body_color = APPLE_COLOR
        self.position = self.randomize_position()

    def randomize_position(self):
        """Случайная позиция яблока на экране."""
        return (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE, randint(0, GRID_HEIGHT - 1)
            * GRID_SIZE
        )

    def draw(self, surface):
        """Отрисовка яблока - прекод."""
        rect = pygame.Rect(
            (self.position[0], self.position[1]),
            (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Дочерний класс Змея."""

    def __init__(self):
        """Атрибуты класса - длина, положение, направление, цвет, посл. эл."""
        super().__init__()
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        self.last = None

    def update_direction(self):
        """Обновление направления движения - прекод."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Логика движения змеи, проверка на столкновение с собой, когда змея
        больше 2 квадратов.
        """
        head_position = self.get_head_position()
        x, y = self.direction
        new_position = (((head_position[0] + (x * GRID_SIZE)) % SCREEN_WIDTH),
                        ((head_position[1] + (y * GRID_SIZE)) % SCREEN_HEIGHT))

        if len(self.positions) > 2 and new_position in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_position)

        if len(self.positions) > self.length:
            self.last = self.positions.pop()

    def draw(self, surface):
        """Отрисовка - прекод."""
        for position in self.positions[:-1]:
            rect = (
                pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
            )
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, BORDER_COLOR, rect, 1)
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(surface, self.body_color, head_rect)
        pygame.draw.rect(surface, BORDER_COLOR, head_rect, 1)

        if self.last:
            last_rect = pygame.Rect(
                (self.last[0], self.last[1]),
                (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Позиция головы."""
        return self.positions[0]

    def reset(self):
        """Сброс игры."""
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2)]
        self.direction = (1, 0)


def handle_keys(game_object):
    """Работа кнопок - прекод."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Логика игры - скорость игры, управление, обновление движения по команде
    кнопок, движение, увеличение, если яблоко "съедено", прорисовка змеи на
    новой позиции, прорисовка яблока, обновление экрана.
    """
    apple = Apple()
    snake = Snake()

    while True:
        clock.tick(10)
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple = Apple()
        apple.draw(screen)
        snake.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
