# Presentation Script: Student Feedback Analyzer

## 1. Introduction (what to say first)

"Good morning everyone. My project is the **Student Feedback Analyzer**. It reads student feedback from a CSV file and tells us three things: how students rated the course, which words appear most in their comments, and whether the feedback is mostly positive, neutral or negative. I built it in **Python 3** using **Pandas** and **Matplotlib**."

## 2. The Problem

"Imagine a teacher gets feedback from 100 students. Reading every comment by hand takes time. This program does the counting automatically."

The input file `feedback.csv` has 3 columns:
- **StudentID** (for example S1)
- **Rating** (1 to 5)
- **Comment** (a short sentence)

## 3. How the Program Works

The program is divided into 4 small functions. Each one does only one job.

**Function 1: `load_valid_rows()`**
- It checks that the file exists. If not, it prints an error instead of crashing.
- It reads the file with Pandas.
- It checks each rating. A valid rating is a whole number from 1 to 5.
- If a rating is invalid (like `6` or `abc`), it prints a **warning with the row number** and skips that row.
- It returns two lists, one of valid ratings and one of valid comments.

**Function 2: `show_summary()`**
- **Average rating** = sum of all ratings ÷ number of ratings. Here it is 23 ÷ 6 = **3.83**.
- **Rating counts** are made with `ratings.count(5)`, `count(4)` and so on.
- **Top 3 words**:
  1. Make each comment lowercase and split it into words.
  2. Remove punctuation and **stop words** (and, but, the, is, a, of, too).
  3. Count each word using a **dictionary** (word → count).
  4. Sort by highest count first, and alphabetically if counts are tied.

**Function 3: `show_sentiment()`**
- Rating **4-5** → Positive
- Rating **3** → Neutral
- Rating **1-2** → Negative
- It calculates each percentage and shows a **bar chart** using Matplotlib.

**Function 4: `main()`**
- It shows a menu: **1 = Summary, 2 = Sentiment**.
- It takes the user's choice and calls the correct function.

## 4. Live Demo (what to show)

| Menu choice | Output |
|---|---|
| 1 | Valid feedback: 6, Average: 3.83, Top 3: great (3), notes (3), clear (2) |
| 2 | Positive 66.67%, Neutral 16.67%, Negative 16.67% + bar chart |

**Invalid input demo:** add `S7,6,Nice` and `S8,abc,Nice` to the file. The program prints:
> Warning: Row 7 skipped - rating must be a whole number from 1 to 5.
> Warning: Row 8 skipped - rating must be a whole number from 1 to 5.

It then continues with the 6 valid rows only.

## 5. Concepts Used (this matches the syllabus line on the sheet)

- **Strings**: `lower()`, `split()`, `strip()`
- **Pandas**: `read_csv()` and looping through rows
- **Frequency analysis**: counting words with a dictionary
- **Visualization**: a bar chart with Matplotlib
- **Error handling**: a missing file and invalid ratings
