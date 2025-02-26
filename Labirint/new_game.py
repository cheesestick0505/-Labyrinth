import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
tile_size = 32
scr_width = 1280
scr_height = 800
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 105, 180)
# Уровни игры
levels = [
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XP  XXXXXXX          XXXXXX      XXXXXXX",
        "X  XXXXXXX  XXXXXX  XXXXXXX  XX  XXXXXXX",
        "X      TXX  XXXXXX  XXXX     XX    XXXXX",
        "X      XX  XXX        XX  XX XX     XXXX",
        "XXXXXX  XX  XXX                 XXX  XXX",
        "XXXXXX  XX  XXXXXX  XXXXX     XXXXX  TXX",
        "XXXXXX  XXH   XXXX  XXXXX        XX  XXX",
        "X  XXX        XXXX  XXXXXXXXXX   XXXXXXX",
        "X  XXX  XXXXXXXXXT        XXXXX  XXXXXXX",
        "X         XXXXXXXXXXXXXXX  XXXX  XXXXXXX",
        "XT               XXXXXXXX  XXXX    XXXXX",
        "XXXXXXXXXXXX     XXXXXTTX    XXXX  XXXXX",
        "XXXXXXXXXXXXXXX  XXXXX  XXX  XXXX  XXXXX",
        "XXXTTXXXXXXXXXX         XXX  XXXX  TTXXX",
        "XXX                     XXXXXXX    XXXXX",
        "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXXX",
        "XXXXXXXXXX  XXXXXXXXXXXXXXX      XXXXXXX",

        "XXXXXXXXXX               XXXXX     XXXXX",
        "XX   XXXXX              XXXXXXXX  XXXXXX",
        "XX   XXXXXXXXXXXXX  XXXXXXXXXXXX  XXXXXX",
        "XX   XXXXXXXXXXXXX  X      XXXXX    XXXX",
        "XX         XXXX        XX     XXXX XXXXX",
        "XXXX               TXXXXXXXX  XXXX  XXXX",
        "XXXXXXXXXXXXXXXX       TXXXX        EXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    ],
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XP TXXXXXXX      H   XXXXXXX     TXXXXXX",
        "X  XXXXXXX  XXXXXX  XXXXXXX  XX  XXXXXXX",
        "X       XX  XXXXXX  XXXX     XX    XXXXX",
        "XH     XX  XXX        XX  XX XX     XXXX",
        "XXXXXX  XX  XXX                 XXX  XXX",
        "XXXXXX  XX  XXXXXX  XXXXX     XXXXX   XX",
        "XXXXXX  XX   TXXXX  XXXXXH       XX  XXX",
        "X  XXX        XXXX  XXXXXXXXXX   XXXXXXX",
        "X  XXX  XXXXXXXXXT         XXXX  XXXXXXX",
        "X   XX    XXXXXXXXXXXXXXX  XXXX  XXXXXXX",
        "X                XXXXXXXX  XXXX    XXXXX",
        "XXXXXXXXXXXX     XXXXXTTX    XXXX  XXXXX",
        "XXXXXXXXXXXXXXX  XXXXX  XXXTTXXXX XXXXXX",
        "XXX  XXXXXXXXXX         XXXTTXXXX    XXX",
        "XXX                     XXXXXXX    XXXXX",
        "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXXX",
        "XXXXXXXXXX  XXXXXXXXXXXXXXX      XXXXXXX",
        "XXXXXXXXXX               XXXXX    TXXXXX",
        "XX   XXXXX              XXXXXXXX  XXXXXX",
        "XX   XXXXXXXXXXXXX  XXXXXXXXXXXX  XXXXXX",
        "XX   TXXXXXXXXXXXX  X      XXXXX    XXXX",
        "XX        TXXXX        XX     XXXX  XXXX",
        "XXXXT              TXXXXXXXX  XXXX  XXXX",
        "XXXXXXXXXXXXXXXX       TXXXXTT      EXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    ],
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "XP       HXXXXXXXXXXXXXXH       TXXXXXXX",
        "X  XXXXXXXTTXXXXXX  XXXXXXX  XX  XXXXXXX",
        "X       XX  XXXXXX  XXXX     XX    XXXXX",
        "X      XX  XXX        XX  XX XX     XXXX",
        "XXXXXX  XX  XXX       H         XXX  XXX",
        "XXXXXX  XX  XXXXXX  XXXXX     XXXXX   XX",
        "XXXXXX  XX    XXXX  XXXXX        XXTTXXX",
        "X  XXX        XXXX  XXXXXXXXXX   XXXXXXX",
        "X  XXX  XXXXXXXXX          XXXX  XXXXXXX",
        "X         XXXXXXXXXXXXXXX  XXXX  XXXXXXX",
        "XTT              XXXXXXXX  XXXX    XXXXX",
        "XXXXXXXXXXXX     XXXXX  X   TXXXX  XXXXX",
        "XXXXXXXXXXXXXXX  XXXXX  XXX  XXXX  XXXXX",
        "XXX  XXXXXXXXXX         XXXTTXXXX    XXX",
        "XXX                     XXXXXXX    XXXXX",
        "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXXX",
        "XXXXXXXXXX  XXXXXXXXXXXXXXXTT    XXXXXXX",
        "XXXXXXXXXX               XXXXX     XXXXX",
        "XX   XXXXX              XXXXXXXX  XXXXXX",
        "XX   XXXXXXXXXXXXX  XXXXXXXXXXXX  XXXXXX",
        "XX   TXXXXXXXXXXXX  X      XXXXX    XXXX",
        "XX         XXXX        XX     XXXX  XXXX",
        "XXXX               TXXXXXXXX  XXXX  XXXX",
        "XXXXXXXXXXXXXXXX       TXXXX        EXXX",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    ],
]

# Игровое окно
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Labyrinth")

# Игрок
player_pos = [1, 1]  # Начальная позиция игрока


# Загрузка изображения стен
stena_image = pygame.image.load("data/kirpich3.jpg")
stena_image = pygame.transform.scale(stena_image, (tile_size, tile_size))  # Масштабирует под размер клетки

# Загрузка изображения выхода
door_image = pygame.image.load("data/door.jpg")
door_image = pygame.transform.scale(door_image, (tile_size, tile_size))  # Масштабирует под размер клетки

# Загрузка изображения ловушки
lov_image = pygame.image.load("data/lovuskha.jpg")
lov_image = pygame.transform.scale(lov_image, (tile_size, tile_size))  # Масштабирует под размер клетки

# Загрузка изображения трофея
trophy_image = pygame.image.load("data/Cubok.jpg")
trophy_image = pygame.transform.scale(trophy_image, (tile_size, tile_size))  # Масштабирует под размер клетки

# Загрузка шрифтов
font = pygame.font.SysFont(None, 36)

# Текущий уровень
current_level = 0


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Загружаем изображения для разных направлений
        self.image_up = pygame.image.load("data/player_up_1.jpg")
        self.image_down = pygame.image.load("data/player_down_1.jpg")
        self.image_left = pygame.image.load("data/player_left_1.jpg")
        self.image_right = pygame.image.load("data/player_right_1.jpg")

        # Уменьшаем размер изображений на X пикселей
        reduction_pixels = 3  # Количество пикселей, на которое уменьшаем
        new_width = tile_size - reduction_pixels
        new_height = tile_size - reduction_pixels

        # Масштабируем изображения
        self.image_up = pygame.transform.scale(self.image_up, (new_width, new_height))
        self.image_down = pygame.transform.scale(self.image_down, (new_width, new_height))
        self.image_left = pygame.transform.scale(self.image_left, (new_width, new_height))
        self.image_right = pygame.transform.scale(self.image_right, (new_width, new_height))

        # Текущее изображение и направление
        self.image = self.image_down  # Начинаем смотреть вниз
        self.rect = self.image.get_rect()
        self.rect.x = x * tile_size
        self.rect.y = y * tile_size
        self.direction = "down"  # Начальное направление
        self.speed = 1  # Скорость движения

    def update(self, direction):
        # Обновляем изображение в зависимости от направления
        if direction == "up":
            self.image = self.image_up
            self.direction = "up"
        elif direction == "down":
            self.image = self.image_down
            self.direction = "down"
        elif direction == "left":
            self.image = self.image_left
            self.direction = "left"
        elif direction == "right":
            self.image = self.image_right
            self.direction = "right"

    def move(self, level):
        keys = pygame.key.get_pressed()  # Получаем состояние всех клавиш
        dx = 0
        dy = 0

        # Проверяем нажатие клавиш и устанавливаем направление
        # 0.06 скорость перемещения
        if keys[pygame.K_LEFT]:
            dx = -0.06  # Двигаемся на одну клетку влево
            self.update("left")
        if keys[pygame.K_RIGHT]:
            dx = 0.06  # Двигаемся на одну клетку вправо
            self.update("right")
        if keys[pygame.K_UP]:
            dy = -0.06  # Двигаемся на одну клетку вверх
            self.update("up")
        if keys[pygame.K_DOWN]:
            dy = 0.06  # Двигаемся на одну клетку вниз
            self.update("down")

        # Проверка коллизий перед перемещением
        if dx != 0 or dy != 0:  # Проверяем, была ли нажата клавиша
            # Проверяем столкновение с объектами на уровне
            if not self.check_collision(level, dx, dy):
                # Перемещаем игрока в соответствующем направлении
                self.rect.x += dx * tile_size
                self.rect.y += dy * tile_size

    def check_collision(self, level, dx, dy):
        temp_rect = self.rect.copy()
        temp_rect.x += dx * tile_size
        temp_rect.y += dy * tile_size

        for y, row in enumerate(level):
            for x, tile in enumerate(row):
                if tile == "X":  # Проверяем столкновение
                    wall_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                    if temp_rect.colliderect(wall_rect):
                        return True  # Есть столкновение
        return False  # Нет столкновений


# Функция рисования карты
def draw_map():
    # Цвет дорожек
    screen.fill(WHITE)

    for y, row in enumerate(levels[current_level]):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
            if tile == "X":  # Стены
                screen.blit(stena_image, rect)
            elif tile == "E":  # Выход
                screen.blit(door_image, rect)
            elif tile == "T":  # Ловушка
                screen.blit(lov_image, rect)
            elif tile == "H":  # Приз
                screen.blit(trophy_image, rect)


def check_trap(player, level):
    player_rect = player.rect

    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile == "T":  # Проверяем столкновение с ловушкой
                trap_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                if player_rect.colliderect(trap_rect):
                    return True  # Игрок попал в ловушку
    return False  # Игрок не в ловушке


def show_menu():
    # Загрузка фонового изображения для меню
    menu_background = pygame.image.load("data/Fonn.jpg")

    while True:
        # Отображение фонового изображения
        screen.blit(menu_background, (0, 0))  # Рисуем фон в позиции (0, 0)

        title_text = font.render("ЛАБИРИНТ", True, RED)
        start_text = font.render("Нажмите 'ENTER' для начала игры", True, WHITE)
        help_text = font.render("Нажмите 'H' для помощи", True, WHITE)
        exit_text = font.render("Нажмите 'ESC' для выхода", True, WHITE)

        screen.blit(title_text, (scr_width // 2 - title_text.get_width() // 2, scr_height // 2 - 50))
        screen.blit(start_text, (scr_width // 2 - start_text.get_width() // 2, scr_height // 2))
        screen.blit(help_text, (scr_width // 2 - help_text.get_width() // 2, scr_height // 2 + 50))
        screen.blit(exit_text, (scr_width // 2 - exit_text.get_width() // 2, scr_height // 2 + 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Нажатие ENTER
                    return  # Начать игру
                if event.key == pygame.K_h:  # Нажатие H
                    show_help()  # Показать справку
                if event.key == pygame.K_ESCAPE:  # Нажатие ESC, выход
                    pygame.quit()
                    sys.exit()


def show_help():
    # Загрузка фонового изображения для меню помоши
    help_background = pygame.image.load("data/Fonn.jpg")

    while True:
        screen.blit(help_background, (0, 0))

        # screen.fill(BLACK)
        help_text1 = font.render("Управление:", True, WHITE)
        help_text2 = font.render("Стрелки - Движение", True, WHITE)
        help_text3 = font.render("Нажмите 'ESC' для выхода в меню", True, WHITE)

        screen.blit(help_text1, (scr_width // 2 - help_text1.get_width() // 2, scr_height // 2 - 100))
        screen.blit(help_text2, (scr_width // 2 - help_text2.get_width() // 2, scr_height // 2 - 50))
        screen.blit(help_text3, (scr_width // 2 - help_text3.get_width() // 2, scr_height // 2 - 5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Нажатие ENTER
                    return  # Вернуться в меню
                if event.key == pygame.K_ESCAPE:  # Нажатие ESC
                    return  # Вернуться в меню


def show_level_selection():
    while True:
        screen.fill(BLACK)
        title_text = font.render()
        level1_text = font.render()
        level2_text = font.render()
        level3_text = font.render()
        back_text = font.render()

        screen.blit(title_text, (scr_width // 2 - title_text.get_width() // 2, scr_height // 2 - 150))
        screen.blit(level1_text, (scr_width // 2 - level1_text.get_width() // 2, scr_height // 2 - 100))
        screen.blit(level2_text, (scr_width // 2 - level2_text.get_width() // 2, scr_height // 2 - 50))
        screen.blit(level3_text, (scr_width // 2 - level3_text.get_width() // 2, scr_height // 2))
        screen.blit(back_text, (scr_width // 2 - back_text.get_width() // 2, scr_height // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 0
                elif event.key == pygame.K_2:
                    return 1
                elif event.key == pygame.K_3:
                    return 2
                elif event.key == pygame.K_ESCAPE:
                    return None


# Функция для отображения экрана завершения игры
def show_game_over(collected_items, total_items):
    help_background = pygame.image.load("data/fonn2.jpg")  # Замените на путь к вашему изображению

    while True:
        screen.blit(help_background, (0, 0))
        # screen.fill(BLACK)
        game_over_text = font.render("Игра окончена!", True, WHITE)
        score_text = font.render(f"Собрано призов: {collected_items}/{total_items}", True, WHITE)
        exit_text = font.render("Нажмите 'ESC' для выхода", True, WHITE)

        screen.blit(game_over_text, (scr_width // 2 - game_over_text.get_width() // 2, scr_height // 2 - 50))
        screen.blit(score_text, (scr_width // 2 - score_text.get_width() // 2, scr_height // 2))
        screen.blit(exit_text, (scr_width // 2 - exit_text.get_width() // 2, scr_height // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Нажатие ESC
                    pygame.quit()
                    sys.exit()


# Сообщение о окончание игры
def show_game_completed():
    help_background = pygame.image.load("data/Proo.jpg")


    while True:
        screen.blit(help_background, (0, 0))
        # screen.fill(BLACK)
        completed_text = font.render("Игра пройдена!", True, BLACK)
        congratulations_text = font.render("Поздравляю!", True, BLACK)
        exit_text = font.render("Нажмите 'ESC' для выхода", True, BLACK)

        screen.blit(completed_text, (scr_width // 2 - completed_text.get_width() // 2, scr_height // 2 - 50))
        screen.blit(congratulations_text,
                    (scr_width // 2 - congratulations_text.get_width() // 2, scr_height // 2))
        screen.blit(exit_text, (scr_width // 2 - exit_text.get_width() // 2, scr_height // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Нажатие ESC
                    pygame.quit()
                    sys.exit()


def draw_status(collected_items, total_items, current_level):
    # Черный цвет
    BLACK = (0, 0, 0)

    # Отображение количества собранных трофеев и общего количества трофеев
    status_text = font.render(f"Трофеи: {collected_items}/{total_items}", True, BLACK)
    level_text = font.render(f"Уровень: {current_level + 1}", True, BLACK)  # +1 для удобства восприятия

    # Позиция текста в правом верхнем углу
    screen.blit(status_text, (scr_width - status_text.get_width() - 50, 10))
    screen.blit(level_text, (scr_width - level_text.get_width() - 50, 40))


# Основной игровой цикл
def main():
    global current_level, player_pos

    while True:
        show_menu()  # Показать главное меню перед началом игры
        current_level = 0  # Сброс уровня
        collected_items = 0  # Сброс собранных призов

        clock = pygame.time.Clock()

        # Создаем игрока
        player = Player(1, 1)
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

        total_items = sum(row.count("H") for row in levels[current_level])  # Считаем общее количество призов

        running = True
        while running:
            screen.fill(BLACK)

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Перемещаем игрока
            player.move(levels[current_level])

            # Проверяем, не попал ли игрок в ловушку
            if check_trap(player, levels[current_level]):
                show_game_over(collected_items, total_items)
                running = False

            # Проверка предметов
            current_tile = levels[current_level][player.rect.y // tile_size][player.rect.x // tile_size]
            if current_tile == "H":
                collected_items += 1
                print(f"Трофеи: {collected_items}/{total_items}")
                # Удаляем трофей с карты
                levels[current_level][player.rect.y // tile_size] = (
                        levels[current_level][player.rect.y // tile_size][:player.rect.x // tile_size]
                        + " "
                        + levels[current_level][player.rect.y // tile_size][player.rect.x // tile_size + 1:]
                )

            # Проверка победы
            if current_tile == "E":
                print(f"Выход с уровня {current_level + 1}")
                if collected_items == total_items:
                    print("Все трофеи собраны")
                else:
                    print(f"Вы прошли уровень {current_level + 1}, но не собрали все трофеи.")

                # Переход на следующий уровень
                current_level += 1
                if current_level >= len(levels):
                    # Если все уровни пройдены, показываем сообщение об окончании игры
                    show_game_completed()
                    running = False  # Завершить игровой цикл
                else:
                    player = Player(1, 1)  # Создаем нового игрока на следующем уровне
                    all_sprites = pygame.sprite.Group()
                    all_sprites.add(player)
                    collected_items = 0  # Сброс собранных трофеев
                    total_items = sum(row.count("H") for row in levels[current_level])  # Обновление количества трофеев

            # Рисование карты и игрока
            draw_map()
            all_sprites.draw(screen)  # Рисование игрока

            # Статус игры
            draw_status(collected_items, total_items, current_level)

            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
