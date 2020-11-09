import time
import pygame as pg
pg.init()

# screen size
size = height, width = 600, 600

# colours
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
red = (255, 0, 0)
blue = (0, 0, 255)

# display size
screen = pg.display.set_mode(size)

# display name
pg.display.set_caption("Tic-Tac-Toe")

# Images
x_image = pg.transform.scale(pg.image.load(
    "made_with_pygame/tic_tac_toe/x.png"), (150, 150))
o_image = pg.transform.scale(pg.image.load(
    "made_with_pygame/tic_tac_toe/o.png"), (150, 150))


def initialize_window():
    # display colour
    screen.fill(white)

    # draw lines
    # draw vertical lines
    pg.draw.line(screen, black, (int(width/3), 0), (int(width/3), height), 5)
    pg.draw.line(screen, black, (int((width/3) * 2), 0),
                 (int((width/3) * 2), height), 5)

    # draw horizontal lines
    pg.draw.line(screen, black, (0, int(height/3)), (width, int(height/3)), 5)
    pg.draw.line(screen, black, (0, int((height/3) * 2)),
                 (width, int((height/3) * 2)), 5)

    pg.display.flip()


def win_check(board):
    """Checks to see if any player has won the game.

    Args:
        board (list): The game board.

    Returns:
        True if any of the win check conditions are satisfied.

    """

    # rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != None:
            pos = int((row+1)*100)
            pg.draw.line(screen, blue, (0, pos), (width, pos), 3)

            pg.display.update()

            pg.time.wait(2000)

            return True

    # columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != None:
            pos = int((col+1)*100)
            pg.draw.line(screen, blue, (pos, 0), (pos, height), 3)

            pg.display.update()

            pg.time.wait(2000)

            return True

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != None:
        pg.draw.line(screen, blue, (0, 0), (width, height), 3)

        pg.display.update()

        pg.time.wait(2000)

        return True

    elif board[0][2] == board[1][1] == board[2][0] != None:
        pg.draw.line(screen, blue, (width, 0), (0, height), 3)

        pg.display.update()

        pg.time.wait(2000)

        return True


def winner_display(turn):
    screen.fill(white)
    winner = pg.font.Font(None, 50).render(
        f'Player {turn} is the winner!', 1, red)

    w = int(width/2)
    h = int(height/2)

    text_rect = winner.get_rect(center=(w, h))
    screen.blit(winner, text_rect)

    pg.display.update()


def place_mark(row_num, col_num, turn):
    if row_num == 0:
        posy = 25
    elif row_num == 1:
        posy = 225
    else:
        posy = 425

    if col_num == 0:
        posx = 25
    elif col_num == 1:
        posx = 225
    else:
        posx = 425

    if turn == 'X':
        screen.blit(x_image, (posx, posy))
        winner = win_check(GAME_DISPLAY)
        if not winner:
            turn = 'O'
        else:
            winner_display(turn)

    elif turn == 'O':
        screen.blit(o_image, (posx, posy))
        winner = win_check(GAME_DISPLAY)
        if not winner:
            turn = 'X'
        else:
            winner_display(turn)

    pg.display.update()


def mouse_click(board, turn):
    # getting mouse co-ordinates
    x, y = pg.mouse.get_pos()

    # which column
    if x < 200:
        col = 0
    elif x in range(200, 401):
        col = 1
    elif x > 400:
        col = 2
    else:
        col = None

    # which row
    if y < 200:
        row = 0
    elif y in range(200, 401):
        row = 1
    elif y > 400:
        row = 2
    else:
        row = None

    if row and col and board[row][col] == None:
        if turn == 'X':
            board[row][col] = 'X'

        elif turn == 'O':
            board[row][col] = 'O'

        place_mark(row, col, turn)


if __name__ == "__main__":
    GAME_ON = False

    while True:
        # the game board
        GAME_DISPLAY = [[None]*3, [None]*3, [None]*3]

        # display colour
        screen.fill(white)

        welcome_message = pg.font.Font(None, 70).render(
            'Welcome to tic-tac-toe!', 1, black)
        start = pg.font.Font(None, 50).render(
            'Press spacebar to START!', 1, black)

        w = int(width/2)
        h1 = int(height/2 - 100)
        h2 = int(height/2)

        text_rect_one = welcome_message.get_rect(center=(w, h1))
        text_rect_two = start.get_rect(center=(w, h2))

        screen.blit(welcome_message, text_rect_one)
        screen.blit(start, text_rect_two)

        pg.display.update()
        pg.time.wait(500)

        start = pg.font.Font(None, 50).render(
            'Press spacebar to START!', 1, white)
        screen.blit(start, text_rect_two, special_flags=pg.BLEND_MAX)

        pg.display.flip()
        pg.time.wait(500)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.KEYDOWN:
                if pg.K_SPACE:
                    # initialize window
                    initialize_window()
                    turn = 'X'
                    GAME_ON = True

        while GAME_ON:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if turn == 'X':
                        mouse_click(GAME_DISPLAY, turn)

                    elif turn == 'O':
                        mouse_click(GAME_DISPLAY, turn)
