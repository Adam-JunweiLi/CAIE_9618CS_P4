# =========================================
# 9618 W22 Paper 42 - Question 1 (a–g)
# Priority Jobs
# =========================================

# ---------- Q1(a) ----------
Jobs = []              # 2D array: [jobNumber, priority]
NumberOfJobs = 0       # number of jobs stored


# ---------- Q1(b) ----------
def Initialise():
    global Jobs, NumberOfJobs
    Jobs = []
    for _ in range(100):
        Jobs.append([-1, -1])
    NumberOfJobs = 0


# ---------- Q1(c) ----------
def AddJob(JobNumber, Priority):
    global Jobs, NumberOfJobs
    if NumberOfJobs == 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs] = [JobNumber, Priority]
        NumberOfJobs += 1
        print("Added")


# ---------- Q1(e) ----------
def InsertionSort():
    global Jobs, NumberOfJobs
    for i in range(1, NumberOfJobs):
        current_job = Jobs[i][0]
        current_priority = Jobs[i][1]

        while i > 0 and Jobs[i - 1][1] > current_priority:
            Jobs[i][0] = Jobs[i - 1][0]
            Jobs[i][1] = Jobs[i - 1][1]
            i -= 1

        Jobs[i][0] = current_job
        Jobs[i][1] = current_priority


# ---------- Q1(f) ----------
def PrintArray():
    for i in range(NumberOfJobs):
        print(Jobs[i][0], "priority", Jobs[i][1])


# ---------- Q1(d) + Q1(g) ----------
def main():
    Initialise()

    AddJob(12, 10)
    AddJob(526, 9)
    AddJob(33, 8)
    AddJob(12, 9)
    AddJob(78, 1)

    InsertionSort()
    PrintArray()


main()

# ---------- Q1(g)(ii) ----------
# Screenshot replaced by comment:
#
# Expected output:
# Added
# Added
# Added
# Added
# Added
# 78 priority 1
# 33 priority 8
# 526 priority 9
# 12 priority 9
# 12 priority 10
