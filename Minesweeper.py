import random
import pygame
# In preparation for creating a GUI version :)
noss = 0
nob = 0
coords = []

def setupGame(diff):
    if diff == 1:
        boardWidth = boardHeight = 10
    elif diff == 2:
        boardWidth = boardHeight = 15
    elif diff == 3:
        boardWidth = boardHeight = 20
    else:
        boardWidth = boardHeight = 10

    global coords
    coords = []
    for x in range(boardWidth):
        c = []
        coords.append(c)
        for y in range(boardHeight):
            if random.randint((int(diff) * 2) % (int(diff) + 2), 10) == 10:
                d = [True, False, 0]
            else:
                d = [False, False, 0, False]
            coords[x].append(d)
    global nob
    nob = 0
    global noss
    noss = 0
    for x in range(boardWidth):
        for y in range(boardHeight):
            if coords[x][y][0]:
                if not x - 1 < 0: coords[x - 1][y][2] += 1
                if not x + 1 >= boardWidth: coords[x + 1][y][2] += 1
                if not y - 1 < 0: coords[x][y - 1][2] += 1
                if not y + 1 >= boardHeight: coords[x][y + 1][2] += 1
                if not x - 1 < 0 and not y - 1 < 0: coords[x - 1][y - 1][2] += 1
                if not x + 1 >= boardWidth and not y - 1 < 0: coords[x + 1][y - 1][2] += 1
                if not x - 1 < 0 and not y + 1 >= boardHeight: coords[x - 1][y + 1][2] += 1
                if not x + 1 >= boardWidth and not y + 1 >= boardHeight: coords[x + 1][y + 1][2] += 1
                nob += 1
            else:
                noss += 1
    return boardWidth, boardHeight

def main():
    width = 800
    height = 600

    boardHeight = 0
    boardWidth = 0
    pygame.display.init()
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Minesweeper")
    x = y = 0

    menu = True
    buttonWidth = width/5
    buttonHeight = height/4
    buttonSelected = 1
    buttonColour = pygame.Color((100,100,100))
    buttonSelectedColour = pygame.Color((50,50,50))

    # TO DO: Make a new input system that relies on the display

    game = True
    while game:
        screen.fill((128,128,129))
        if menu:
            pygame.draw.rect(screen, buttonColour, (0.5*width/5, height/3, buttonWidth, buttonHeight))
            pygame.draw.rect(screen, buttonColour, (2*width/5, height/3, buttonWidth, buttonHeight))
            pygame.draw.rect(screen, buttonColour, (3.5*width/5, height/3, buttonWidth, buttonHeight))
            if buttonSelected == 1:
                pygame.draw.rect(screen, buttonSelectedColour, (0.5*width/5, height/3, buttonWidth, buttonHeight))
            elif buttonSelected == 2:
                pygame.draw.rect(screen, buttonSelectedColour, (2*width/5, height/3, buttonWidth, buttonHeight))
            else:
                pygame.draw.rect(screen, buttonSelectedColour, (3.5*width/5, height/3, buttonWidth, buttonHeight))
        else:
            pygame.draw.rect(screen, buttonSelectedColour, (width/2, height/2, buttonWidth, buttonHeight))


        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if menu:
                    if event.key == pygame.K_LEFT:
                        if buttonSelected > 1:
                            buttonSelected -= 1
                    if event.key == pygame.K_RIGHT:
                        if buttonSelected < 3:
                            buttonSelected += 1
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        boardWidth, boardHeight = setupGame(buttonSelected)
                        menu = not menu
                
                if not menu:
                    if event.key == pygame.K_UP:
                        y -= 1
                        if y < 0:
                            y = boardHeight - 1
                    if event.key == pygame.K_DOWN:
                        y += 1
                        if y > boardHeight - 1:
                            y = 0
                    if event.key == pygame.K_LEFT:
                        x -= 1
                        if x < 0:
                            x = boardWidth - 1
                    if event.key == pygame.K_RIGHT:
                        x += 1
                        if x > boardWidth - 1:
                            x = 0
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        check(x, y, boardWidth, boardHeight)
                    if event.key == pygame.K_SPACE:
                        coords[x][y][1] = not coords[x][y][1]
                    # Temporary fix for no screen, bad problem
                    printScreen(x, y, boardWidth, boardHeight, coords, nob, noss)
        
        pygame.display.flip()


def check(x, y, width, height):
    global nob
    global noss
    global coords
    try:
        if not coords[x][y][3]:
            noss -= 1
            if coords[x][y][2] == 0:
                coords[x][y][3] = True
                if not x - 1 < 0:
                    if coords[x - 1][y][2] == 0: check(x - 1, y, width, height)
                    coords[x - 1][y][3] = True
                if not x + 1 > width - 1:
                    if coords[x + 1][y][2] == 0: check(x + 1, y, width, height)
                    coords[x + 1][y][3] = True
                if not y - 1 < 0:
                    if coords[x][y - 1][2] == 0: check(x, y - 1, width, height)
                    coords[x][y - 1][3] = True
                if not y + 1 > height - 1:
                    if coords[x][y + 1][2] == 0: check(x, y + 1, width, height)
                    coords[x][y + 1][3] = True
                if not x - 1 < 0 and not y - 1 < 0:
                    if coords[x - 1][y - 1][2] == 0: check(x - 1, y - 1, width, height)
                    coords[x - 1][y - 1][3] = True
                if not x + 1 > width - 1 and not y - 1 < 0:
                    if coords[x + 1][y - 1][2] == 0: check(x + 1, y - 1, width, height)
                    coords[x + 1][y - 1][3] = True
                if not x - 1 < 0 and not y + 1 > height - 1:
                    if coords[x - 1][y + 1][2] == 0: check(x - 1, y + 1, width, height)
                    coords[x - 1][y + 1][3] = True
                if not x + 1 > width - 1 and not y + 1 > height - 1:
                    if coords[x + 1][y + 1][2] == 0: check(x + 1, y + 1, width, height)
                    coords[x + 1][y + 1][3] = True
            else:
                coords[x][y][3] = True
    except:
        print("f")



# def on_press(key):
#     global x, y
#     if key == Key.up:
#         x -= 1
#         if x < 0: x = a - 1
#     elif key == Key.down:
#         x += 1
#         if x > a - 1: x = 0
#     elif key == Key.left:
#         y -= 1
#         if y < 0: y = b - 1
#     elif key == Key.right:
#         y += 1
#         if y > b - 1: y = 0
#     elif key == Key.space:
#         if not coords[x][y][0]:
#             if not coords[x][y][3]: coords[x][y][1] = not coords[x][y][1]
#         else: coords[x][y][1] = not coords[x][y][1]
#     elif key == Key.shift or key == Key.shift_r:
#         if not coords[x][y][0]: check(x, y)
#         else: return False
#     else:
#         pass
def printScreen(x, y, width, height, coords, nob, noss):

    print("\n" * 40 + "┌─" + "──┬─" * (width - 1) + "──┐")
    for f in range(height):
        line = "│"
        for e in range(width):
            if e == x and f == y:
                line += "<"
            else:
                line += " "
            if coords[e][f][1]:
                line += "⚑"
            elif not coords[e][f][0]:
                if coords[e][f][3]:
                    if coords[e][f][2] == 0:
                        line += " "
                    else:
                        line += str(coords[e][f][2])
                else:
                    line += "█"
            else:
                line += "█"
            if e == x and f == y:
                line += ">│"
            else:
                line += " │"
        print(line)
        if f != height - 1: print("├─" + "──┼─" * (width - 1) + "──┤")
    print("└─" + "──┴─" * (width - 1) + "──┘")
    print("Number of safe spaces: " + str(noss))
    print("Number of bombs: " + str(nob))

while True:
    main()