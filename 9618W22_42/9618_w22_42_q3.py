# =========================================
# 9618 W22 Paper 42 - Question 3 (a–e)
# Linear Queue + Recursion
# =========================================

# ---------- Q3(a) ----------
Queue = [-1 for _ in range(100)]
HeadPointer = -1
TailPointer = 0


# ---------- Q3(b) ----------
def Enqueue(Data):
    global Queue, HeadPointer, TailPointer

    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = Data
        TailPointer += 1
        return True
    else:
        return False


# ---------- Q3(c) ----------
Success = False
for i in range(1, 21):
    Success = Enqueue(i)

if Success:
    print("Successful")
else:
    print("Unsuccessful")


# ---------- Q3(d) ----------
def RecursiveOutput(Start):
    if Start == 0:
        return Queue[Start]
    else:
        return Queue[Start] + RecursiveOutput(Start - 1)


# ---------- Q3(e)(i) ----------
result = RecursiveOutput(TailPointer - 1)
print(result)


# ---------- Q3(e)(ii) ----------
# Screenshot replaced by comment:
#
# Output:
# Successful
# 210
