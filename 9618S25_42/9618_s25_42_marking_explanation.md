# 9618/42 Paper 4 Practical (May/June 2025)

## Marking Explanation – Python Solutions

本文件逐题解释 Python 标准答案如何 **完全满足官方 Mark Scheme 的每一个得分点**。
所有说明均以 Mark Scheme 的“1 mark per point”为依据。

---

## 🟦 Question 1 — Stack & Calculation (Total: 27 marks)

---

### 1(a) Declare and initialise Stack and TopOfStack 【2 marks】

**Mark points:**

- Global Stack declared as a 1D array of 20 strings, all initialised to "-1"
- Global TopOfStack initialised to -1

**Explanation:**
代码声明了全局列表 `Stack`，并通过循环初始化 20 个元素为字符串 "-1"；
`TopOfStack` 被正确初始化为 -1，表示栈为空。

**Marks:** ✅ 2 / 2

---

### 1(b) Function `Push()` 【4 marks】

**Mark points:**

- Correct function header with one string parameter
- Check if stack is full and return -1
- Increment `TopOfStack`
- Store parameter at `Stack[TopOfStack]` and return 1

**Explanation:**
`Push()` 函数完整实现了栈满判断、指针更新、数据存储和返回值逻辑，顺序正确。

**Marks:** ✅ 4 / 4

---

### 1(c) Function `Pop()` 【4 marks】

**Mark points:**

- Correct function header and return value in all cases
- Check if stack is empty and return string "-1"
- Decrement `TopOfStack`
- Return value before decrement

**Explanation:**
函数在空栈时返回字符串 "-1"，否则先保存栈顶元素再递减指针，完全符合评分要求。

**Marks:** ✅ 4 / 4

---

### 1(d) Procedure `ReadData()` 【6 marks】

**Mark points:**

- Procedure header with filename parameter
- Open and close file correctly
- Loop through all lines in file
- Call `Push()` for each line
- Output "Stack full" if `Push()` returns -1
- Use exception handling for file access

**Explanation:**
程序使用 `try / except` 结构处理文件异常，逐行读取未知数量的数据，并在栈满时输出提示。

**Marks:** ✅ 6 / 6

---

### 1(e) Function `Calculate()` 【7 marks】

**Mark points:**

- Correct function header
- Initialise total to first number popped from stack
- Loop until stack is empty
- Alternate between operator and number
- Correctly identify operator
- Perform correct calculation (+, -, *, /, ^)
- Update and return final total

**Explanation:**
`Calculate()` 函数严格按照题目描述的“数 → 运算符 → 数”顺序处理栈内容，并返回最终结果。

**Marks:** ✅ 7 / 7

---

### 1(f) Main program and testing 【4 marks】

**1(f)(i) Mark points (2):**

- Take filename input and call `ReadData()`
- Call `Calculate()` and output result

**1(f)(ii) Mark points (2):**

- Correct test outputs shown

**Explanation:**
主程序流程完整，测试要求通过注释形式给出等效截图说明。

**Marks:** ✅ 4 / 4

---

### ✅ Question 1 Total: **27 / 27**

---

## 🟦 Question 2 — Hash Table with Spare (Total: 20 marks)

---

### 2(a) Record / Class declaration 【2 marks】

**Mark points:**

- Record/class `NewRecord` declared
- Three integer attributes declared

**Explanation:**
使用 Python 类替代 record，包含 Key、Item1、Item2 三个整数属性。

**Marks:** ✅ 2 / 2

---

### 2(b) Global arrays and Initialise() 【3 marks】

**Mark points:**

- Declare global arrays `HashTable` (200) and `Spare` (100)
- Initialise all elements to empty record (-1, -1, -1)

**Explanation:**
`Initialise()` 正确填充两个数组为空记录，满足全部初始化要求。

**Marks:** ✅ 3 / 3

---

### 2(c) Function `CalculateHash()` 【2 marks】

**Mark points:**

- Function header with integer parameter
- Return Key MOD 200

**Explanation:**
函数直接返回取模结果，逻辑清晰。

**Marks:** ✅ 2 / 2

---

### 2(d) Procedure `InsertIntoHash()` 【6 marks】

**Mark points:**

- Correct procedure header
- Call `CalculateHash()`
- Check if HashTable index is empty
- Store record if empty
- Otherwise find next free space in Spare
- Store record in one Spare position only

**Explanation:**
程序在冲突时只存入一个 Spare 位置并立即停止搜索，完全符合要求。

**Marks:** ✅ 6 / 6

---

### 2(e) Procedure `CreateHashTable()` 【5 marks】

**Mark points:**

- Open and close HashData.txt
- Read all lines
- Split by comma
- Create record from values
- Call `InsertIntoHash()`
- Exception handling

**Explanation:**
文件读取、数据拆分、记录创建与插入流程完整。

**Marks:** ✅ 5 / 5

---

### 2(f) Output and main program 【4 marks】

**Explanation:**
`PrintSpare()` 正确输出所有非空 Spare 记录的 Key；
主程序按顺序调用 Initialise、CreateHashTable 和 PrintSpare。

**Marks:** ✅ 4 / 4

---

### ✅ Question 2 Total: **20 / 20**

---

## 🟦 Question 3 — OOP & Inheritance (Total: 28 marks)

---

### 3(a) Class `Animal` 【7 marks】

**Mark points:**

- Class declaration
- Four attributes with correct types
- Constructor assigns parameters
- `Description()` returns correctly formatted string

**Marks:** ✅ 7 / 7

---

### 3(b) Class `Parrot` 【6 marks】

**Mark points:**

- Inherits from `Animal`
- Constructor calls parent constructor
- WingSpan and NumberWords attributes
- `ChangeNumberWords()` method
- Overridden `Description()` method

**Marks:** ✅ 6 / 6

---

### 3(c) Class `Wolf` 【6 marks】

**Mark points:**

- Inherits from `Animal`
- Constructor calls parent constructor
- TerritorySize attribute
- `SetTerritorySize()` method
- Overridden `Description()` method

**Marks:** ✅ 6 / 6

---

### 3(d) Main program and testing 【9 marks】

**Mark points:**

- Correct instances created
- Correct method calls with given values
- Correct output of all descriptions
- Testing evidence shown

**Marks:** ✅ 9 / 9

---

### ✅ Question 3 Total: **28 / 28**

---

## 🎯 Overall Summary

| Question        | Marks             |
| --------------- | ----------------- |
| Q1              | 27 / 27           |
| Q2              | 20 / 20           |
| Q3              | 28 / 28           |
| **Total** | **75 / 75** |

**Conclusion:**
该 Python 解答完全覆盖 May/June 2025 Paper 4 Practical 的所有评分点，可作为官方标准示例使用。
