# ================================
# Question 1 – May/June 2025
# ================================

# ---------- 1(a) ----------
Stack = []
TopOfStack = -1

for _ in range(20):
    Stack.append("-1")


# ---------- 1(b) ----------
def Push(Data):
    global TopOfStack, Stack
    if TopOfStack == 19:
        return -1
    TopOfStack += 1
    Stack[TopOfStack] = Data
    return 1


# ---------- 1(c) ----------
def Pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        return "-1"
    value = Stack[TopOfStack]
    TopOfStack -= 1
    return value


# ---------- 1(d) ----------
def ReadData(FileName):
    try:
        f = open(FileName, "r")
        for line in f:
            if Push(line.strip()) == -1:
                print("Stack full")
        f.close()
    except:
        print("Cannot open file")


# ---------- 1(e) ----------
def Calculate():
    # First value is always a number
    total = int(Pop())

    while True:
        operator = Pop()
        if operator == "-1":
            break

        number = int(Pop())

        if operator == "+":
            total += number
        elif operator == "-":
            total -= number
        elif operator == "*":
            total *= number
        elif operator == "/":
            total /= number
        elif operator == "^":
            total **= number

    return total


# ---------- 1(f)(i) ----------
filename = input("Enter the filename: ")
ReadData(filename)
result = Calculate()
print(result)

# ---------- 1(f)(ii) ----------
# Screenshot replaced by comment:
# StackData.txt   -> 131
# SecondStack.txt -> 320
