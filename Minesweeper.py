import random
from pynput import keyboard
from pynput.keyboard import Key

diff = input("Enter difficulty level (1, 2, 3): ")
while not diff.isdigit() or not 3 >= int(diff) > 0:
    diff = input("That is not an option\nEnter difficulty level (1, 2, 3): ")

if diff == "1":
    a = b = 10
elif diff == "2":
    a = b = 15
elif diff == "3":
    a = b = 20
else:
    a = b = 10

coords = []
for x in range(a):
    c = []
    coords.append(c)
    for y in range(b):
        if random.randint((int(diff) * 2) % (int(diff) + 2), 10) == 10:
            d = [True, False, 0]
        else:
            d = [False, False, 0, False]
        coords[x].append(d)

nob = 0
noss = 0
for x in range(a):
    for y in range(b):
        if coords[x][y][0]:
            if not x - 1 < 0: coords[x - 1][y][2] += 1
            if not x + 1 >= a: coords[x + 1][y][2] += 1
            if not y - 1 < 0: coords[x][y - 1][2] += 1
            if not y + 1 >= b: coords[x][y + 1][2] += 1
            if not x - 1 < 0 and not y - 1 < 0: coords[x - 1][y - 1][2] += 1
            if not x + 1 >= a and not y - 1 < 0: coords[x + 1][y - 1][2] += 1
            if not x - 1 < 0 and not y + 1 >= b: coords[x - 1][y + 1][2] += 1
            if not x + 1 >= a and not y + 1 >= b: coords[x + 1][y + 1][2] += 1
            nob += 1
        else:
            noss += 1


def check(x, y):
    global noss
    if not coords[x][y][3]:
        noss -= 1
        if coords[x][y][2] == 0:
            coords[x][y][3] = True
            if not x - 1 < 0:
                if coords[x - 1][y][2] == 0: check(x - 1, y)
                coords[x - 1][y][3] = True
            if not x + 1 > a - 1:
                if coords[x + 1][y][2] == 0: check(x + 1, y)
                coords[x + 1][y][3] = True
            if not y - 1 < 0:
                if coords[x][y - 1][2] == 0: check(x, y - 1)
                coords[x][y - 1][3] = True
            if not y + 1 > b - 1:
                if coords[x][y + 1][2] == 0: check(x, y + 1)
                coords[x][y + 1][3] = True
            if not x - 1 < 0 and not y - 1 < 0:
                if coords[x - 1][y - 1][2] == 0: check(x - 1, y - 1)
                coords[x - 1][y - 1][3] = True
            if not x + 1 > a - 1 and not y - 1 < 0:
                if coords[x + 1][y - 1][2] == 0: check(x + 1, y - 1)
                coords[x + 1][y - 1][3] = True
            if not x - 1 < 0 and not y + 1 > b - 1:
                if coords[x - 1][y + 1][2] == 0: check(x - 1, y + 1)
                coords[x - 1][y + 1][3] = True
            if not x + 1 > a - 1 and not y + 1 > b - 1:
                if coords[x + 1][y + 1][2] == 0: check(x + 1, y + 1)
                coords[x + 1][y + 1][3] = True
        else:
            coords[x][y][3] = True


x = y = 0


def on_press(key):
    global x, y
    if key == Key.up:
        x -= 1
        if x < 0: x = a - 1
    elif key == Key.down:
        x += 1
        if x > a - 1: x = 0
    elif key == Key.left:
        y -= 1
        if y < 0: y = b - 1
    elif key == Key.right:
        y += 1
        if y > b - 1: y = 0
    elif key == Key.space:
        if not coords[x][y][0]:
            if not coords[x][y][3]: coords[x][y][1] = not coords[x][y][1]
        else: coords[x][y][1] = not coords[x][y][1]
    elif key == Key.shift or key == Key.shift_r:
        if not coords[x][y][0]: check(x, y)
        else: return False
    else:
        pass

    print("\n" * 40 + "┌─" + "──┬─" * (a - 1) + "──┐")
    for e in range(b):
        line = "│"
        for f in range(a):
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
        if e != b - 1: print("├─" + "──┼─" * (a - 1) + "──┤")
    print("└─" + "──┴─" * (a - 1) + "──┘")
    print("Number of safe spaces: " + str(noss))
    print("Number of bombs: " + str(nob))


def on_release(key):
    if key == Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    input(
        "Controls: ↑↓←→ to move\nSpace to set/remove flag\nShift to check for bomb (Press enter to continue)")
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)
listener.start()
