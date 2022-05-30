import random
import pygame
# In preparation for creating a GUI version :)
noss = 0
coords = []


def main():
    pygame.display.init()
    screen = pygame.display.set_mode((800,600))
    x = y = 0

    # TO DO: Make a new input system that relies on the display
    diff = input("Enter difficulty level (1, 2, 3): ")
    while not diff.isdigit() or not 3 >= int(diff) > 0:
        diff = input("That is not an option\nEnter difficulty level (1, 2, 3): ")
    if diff == "1":
        width = height = 10
    elif diff == "2":
        width = height = 15
    elif diff == "3":
        width = height = 20
    else:
        width = height = 10

    global coords
    coords = []
    for x in range(width):
        c = []
        coords.append(c)
        for y in range(height):
            if random.randint((int(diff) * 2) % (int(diff) + 2), 10) == 10:
                d = [True, False, 0]
            else:
                d = [False, False, 0, False]
            coords[x].append(d)

    nob = 0
    global noss
    noss = 0
    for x in range(width):
        for y in range(height):
            if coords[x][y][0]:
                if not x - 1 < 0: coords[x - 1][y][2] += 1
                if not x + 1 >= width: coords[x + 1][y][2] += 1
                if not y - 1 < 0: coords[x][y - 1][2] += 1
                if not y + 1 >= height: coords[x][y + 1][2] += 1
                if not x - 1 < 0 and not y - 1 < 0: coords[x - 1][y - 1][2] += 1
                if not x + 1 >= width and not y - 1 < 0: coords[x + 1][y - 1][2] += 1
                if not x - 1 < 0 and not y + 1 >= height: coords[x - 1][y + 1][2] += 1
                if not x + 1 >= width and not y + 1 >= height: coords[x + 1][y + 1][2] += 1
                nob += 1
            else:
                noss += 1

    game = True
    while game:


        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 1
                    if y < 0:
                        y = height - 1
                if event.key == pygame.K_DOWN:
                    y += 1
                    if y > height - 1:
                        y = 0
                if event.key == pygame.K_LEFT:
                    x -= 1
                    if x < 0:
                        x = width - 1
                if event.key == pygame.K_RIGHT:
                    x += 1
                    if x > width - 1:
                        x = 0
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    check(x, y, width, height)
                if event.key == pygame.K_SPACE:
                    coords[x][y][1] = not coords[x][y][1]
                
                # Temporary fix for no screen, bad problem
                printScreen(x, y, width, height, coords, nob, noss)
        
        pygame.display.flip()


def check(x, y, width, height):
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