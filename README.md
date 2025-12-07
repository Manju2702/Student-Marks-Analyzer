# 📊 Student Marks Analyzer (with Graphs)

A Python mini-project that allows you to:

- Add **multiple students**
- Add **multiple subjects** per student
- Safely take input (with validation)
- Calculate:
  - Total marks
  - Average marks
  - Highest & lowest scoring subjects
- Plot a **bar graph of marks** for any selected student using `matplotlib`

Perfect for **BCA mini-projects**, **Python beginners**, and **GitHub portfolio**.

---

## 🚀 Features

- ✅ Supports **multiple students**
- ✅ Each student can have **different subjects**
- ✅ Input validation using:
  - `safe_int()` → for safe integer input  
  - `safe_float()` → for safe numeric marks
- ✅ Calculates:
  - Total marks
  - Average marks
  - Highest-scoring subject
  - Lowest-scoring subject
- ✅ Uses **Python dictionary** to store data
- ✅ Plots a **bar chart** of a selected student's marks using `matplotlib`

---

## 🧠 How It Works

1. First, the program asks:  
   `How many students?`
2. For each student:
   - It asks for **student name**
   - Then asks: `How many subjects for <name>?`
   - Then for each subject:
     - Subject name
     - Marks in that subject
3. After all input:
   - It prints a **detailed marks report** for each student
4. Finally, you can choose a **student name** to **plot** their marks as a bar graph.

---

## 🧰 Technologies Used

- **Python 3**
- **matplotlib** for plotting graphs

---

## 📦 Requirements

Install `matplotlib` (only once):

```bash
pip install matplotlib

