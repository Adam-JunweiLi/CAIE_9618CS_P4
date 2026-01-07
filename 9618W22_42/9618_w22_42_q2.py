# =========================================
# 9618 W22 Paper 42 - Question 2 (a–g)
# Character Game
# =========================================

# ---------- Q2(a)(b)(c) ----------
class Character:
    def __init__(self, Name, XCoordinate, YCoordinate):
        self.__Name = Name
        self.__XCoordinate = XCoordinate
        self.__YCoordinate = YCoordinate

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange


# ---------- Q2(d) ----------
Characters = []

try:
    file = open("Characters.txt", "r")
    for _ in range(10):
        name = file.readline().strip()
        x = int(file.readline().strip())
        y = int(file.readline().strip())
        Characters.append(Character(name, x, y))
    file.close()
except:
    print("File not found")


# ---------- Q2(e) ----------
Position = -1
while Position == -1:
    user_input = input("Enter the Character to move: ").lower()
    for i in range(10):
        if Characters[i].GetName().lower() == user_input:
            Position = i


# ---------- Q2(f) ----------
valid = False
while not valid:
    move = input("Enter A for left, W for up, S for down or D for right: ").upper()

    if move == "A":
        Characters[Position].ChangePosition(-1, 0)
        valid = True
    elif move == "D":
        Characters[Position].ChangePosition(1, 0)
        valid = True
    elif move == "W":
        Characters[Position].ChangePosition(0, 1)
        valid = True
    elif move == "S":
        Characters[Position].ChangePosition(0, -1)
        valid = True


# ---------- Q2(g)(i) ----------
print(
    Characters[Position].GetName(),
    "has changed coordinates to X =",
    Characters[Position].GetX(),
    "and Y =",
    Characters[Position].GetY()
)

# ---------- Q2(g)(ii) ----------
# Screenshot replaced by comment:
#
# Input:
# THOMAS
# qui
# X
# A
#
# Output:
# Qui has changed coordinates to X = 82 and Y = 0
