import random
import sys
from pathlib import Path

import pygame


WIDTH, HEIGHT = 720, 720
BOARD_SIZE = 560
GRID_SIZE = 20
CELL_SIZE = BOARD_SIZE // GRID_SIZE
BOARD_X = (WIDTH - BOARD_SIZE) // 2
BOARD_Y = 90
FPS = 60

BG_COLOR = (9, 12, 20)
BOARD_COLOR = (18, 24, 39)
GRID_COLOR = (32, 46, 62)
SNAKE_COLOR = (67, 217, 132)
SNAKE_HEAD_COLOR = (35, 122, 78)
FOOD_COLOR = (255, 92, 92)
TEXT_COLOR = (228, 236, 255)
SUBTEXT_COLOR = (148, 163, 184)
ACCENT_COLOR = (96, 165, 250)
DANGER_COLOR = (248, 113, 113)

HIGHSCORE_PATH = Path(__file__).with_name("snake_highscore.txt")


def load_high_score():
    try:
        if HIGHSCORE_PATH.exists():
            value = HIGHSCORE_PATH.read_text(encoding="utf-8").strip()
            return int(value) if value else 0
    except (ValueError, OSError):
        pass
    return 0


def save_high_score(score):
    try:
        HIGHSCORE_PATH.write_text(str(score), encoding="utf-8")
    except OSError:
        pass


def draw_text(surface, text, size, x, y, color=TEXT_COLOR, bold=False):
    font = pygame.font.SysFont("Segoe UI", size, bold=bold)
    label = font.render(text, True, color)
    rect = label.get_rect(center=(x, y))
    surface.blit(label, rect)


def draw_panel(surface, title, value, x, y, width, height, accent=ACCENT_COLOR):
    panel_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, (18, 24, 39), panel_rect, border_radius=16)
    pygame.draw.rect(surface, accent, panel_rect.inflate(-3, -3), 2, border_radius=14)
    draw_text(surface, title, 17, x + width * 0.5, y + 22, SUBTEXT_COLOR)
    draw_text(surface, str(value), 32, x + width * 0.5, y + 52, TEXT_COLOR, bold=True)


def random_food(snake):
    free_cells = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if (col, row) not in snake:
                free_cells.append((col, row))
    if not free_cells:
        return None
    return random.choice(free_cells)


def reset_game():
    snake = [(GRID_SIZE // 2, GRID_SIZE // 2), (GRID_SIZE // 2 - 1, GRID_SIZE // 2), (GRID_SIZE // 2 - 2, GRID_SIZE // 2)]
    direction = (1, 0)
    next_direction = (1, 0)
    food = random_food(snake)
    return snake, direction, next_direction, food, 0


def main():
    pygame.init()
    pygame.display.set_caption("Snake Elite")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    high_score = load_high_score()
    score = 0
    state = "playing"
    paused = False
    move_delay = 120
    last_move = pygame.time.get_ticks()

    snake, direction, next_direction, food, score = reset_game()

    while True:
        now = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_p):
                    if state == "playing":
                        paused = True
                        state = "paused"
                    elif state == "paused":
                        paused = False
                        state = "playing"
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    if state == "game_over":
                        snake, direction, next_direction, food, score = reset_game()
                        state = "playing"
                        paused = False
                        high_score = load_high_score()
                        last_move = pygame.time.get_ticks()
                elif event.key in (pygame.K_UP, pygame.K_w):
                    candidate = (0, -1)
                    if direction != (0, 1) and next_direction != (0, 1):
                        next_direction = candidate
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    candidate = (0, 1)
                    if direction != (0, -1) and next_direction != (0, -1):
                        next_direction = candidate
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    candidate = (-1, 0)
                    if direction != (1, 0) and next_direction != (1, 0):
                        next_direction = candidate
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    candidate = (1, 0)
                    if direction != (-1, 0) and next_direction != (-1, 0):
                        next_direction = candidate

        if state == "playing" and not paused and now - last_move >= move_delay:
            direction = next_direction
            head_x, head_y = snake[0]
            delta_x, delta_y = direction
            new_head = (head_x + delta_x, head_y + delta_y)

            if (
                new_head[0] < 0
                or new_head[0] >= GRID_SIZE
                or new_head[1] < 0
                or new_head[1] >= GRID_SIZE
                or new_head in snake[:-1]
            ):
                state = "game_over"
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)
            else:
                snake.insert(0, new_head)
                if food is not None and new_head == food:
                    score += 1
                    food = random_food(snake)
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)
                    move_delay = max(50, 120 - (score * 4))
                else:
                    snake.pop()
                last_move = now

        screen.fill(BG_COLOR)

        title_rect = pygame.Rect(0, 0, WIDTH, 80)
        pygame.draw.rect(screen, (15, 21, 32), title_rect)
        draw_text(screen, "SNAKE ELITE", 33, WIDTH // 2, 42, TEXT_COLOR, bold=True)

        left_panel_x = 56
        mid_panel_x = 230
        right_panel_x = 404
        panel_width = 140
        panel_height = 92

        draw_panel(screen, "Score", score, left_panel_x, 16, panel_width, panel_height, ACCENT_COLOR)
        draw_panel(screen, "Best", high_score, mid_panel_x, 16, panel_width, panel_height, (108, 92, 231))
        draw_panel(screen, "Speed", int(1000 / move_delay), right_panel_x, 16, panel_width, panel_height, (59, 130, 246))

        board_rect = pygame.Rect(BOARD_X, BOARD_Y, BOARD_SIZE, BOARD_SIZE)
        pygame.draw.rect(screen, BOARD_COLOR, board_rect, border_radius=18)
        pygame.draw.rect(screen, (24, 31, 50), board_rect, 3, border_radius=18)

        for x in range(0, BOARD_SIZE + 1, CELL_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (BOARD_X + x, BOARD_Y), (BOARD_X + x, BOARD_Y + BOARD_SIZE))
        for y in range(0, BOARD_SIZE + 1, CELL_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (BOARD_X, BOARD_Y + y), (BOARD_X + BOARD_SIZE, BOARD_Y + y))

        if food is not None:
            food_x = BOARD_X + food[0] * CELL_SIZE + CELL_SIZE // 2
            food_y = BOARD_Y + food[1] * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(screen, FOOD_COLOR, (food_x, food_y), CELL_SIZE // 2 - 2)
            pygame.draw.circle(screen, (255, 176, 176), (food_x - 4, food_y - 5), 5)

        for index, segment in enumerate(snake):
            rect = pygame.Rect(
                BOARD_X + segment[0] * CELL_SIZE + 2,
                BOARD_Y + segment[1] * CELL_SIZE + 2,
                CELL_SIZE - 4,
                CELL_SIZE - 4,
            )
            color = SNAKE_HEAD_COLOR if index == 0 else SNAKE_COLOR
            pygame.draw.rect(screen, color, rect, border_radius=7)
            if index == 0:
                eye_offset = 5
                eye_y = rect.centery - 3
                eye_x_left = rect.x + 6
                eye_x_right = rect.right - 10
                pygame.draw.circle(screen, (18, 24, 39), (eye_x_left, eye_y), 2)
                pygame.draw.circle(screen, (18, 24, 39), (eye_x_right, eye_y), 2)

        if state == "paused":
            overlay = pygame.Surface((BOARD_SIZE, BOARD_SIZE), pygame.SRCALPHA)
            overlay.fill((14, 20, 30, 180))
            screen.blit(overlay, (BOARD_X, BOARD_Y))
            draw_text(screen, "PAUSED", 40, WIDTH // 2, HEIGHT // 2 - 20, TEXT_COLOR, bold=True)
            draw_text(screen, "Press P to resume", 18, WIDTH // 2, HEIGHT // 2 + 22, SUBTEXT_COLOR)

        if state == "game_over":
            overlay = pygame.Surface((BOARD_SIZE, BOARD_SIZE), pygame.SRCALPHA)
            overlay.fill((10, 12, 20, 180))
            screen.blit(overlay, (BOARD_X, BOARD_Y))
            draw_text(screen, "GAME OVER", 42, WIDTH // 2, HEIGHT // 2 - 18, DANGER_COLOR, bold=True)
            draw_text(screen, f"Final score: {score}", 22, WIDTH // 2, HEIGHT // 2 + 22, TEXT_COLOR)
            draw_text(screen, "Press Enter to restart", 18, WIDTH // 2, HEIGHT // 2 + 58, SUBTEXT_COLOR)

        draw_text(screen, "Controls: Arrows / WASD · P to pause", 18, WIDTH // 2, HEIGHT - 30, SUBTEXT_COLOR)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()

