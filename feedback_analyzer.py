# Student Feedback Analyzer (PS 84)
# Reads feedback.csv (StudentID, Rating, Comment) and shows:
#   1. Summary: average rating, rating counts, top 3 words
#   2. Sentiment: positive / neutral / negative percentages + bar chart

import os
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "feedback.csv"
STOP_WORDS = ["and", "but", "the", "is", "a", "of", "too"]


def load_valid_rows():
    """Read the CSV, skip invalid ratings (with a warning) and return valid rows."""
    # Handle a missing file
    if not os.path.exists(FILE_NAME):
        print("Error: " + FILE_NAME + " not found.")
        return None

    # Read everything as text so values like 'abc' or '3.5' don't cause problems
    data = pd.read_csv(FILE_NAME, dtype=str)

    valid_ratings = []
    valid_comments = []

    # row_number counts data rows only (header is not counted)
    row_number = 0
    for index, row in data.iterrows():
        row_number = row_number + 1
        rating_text = str(row["Rating"]).strip()

        # A valid rating is a whole number from 1 to 5
        if rating_text.isdigit() and 1 <= int(rating_text) <= 5:
            valid_ratings.append(int(rating_text))
            comment = row["Comment"]
            if pd.isna(comment):
                comment = ""
            valid_comments.append(comment)
        else:
            print("Warning: Row " + str(row_number) +
                  " skipped - rating must be a whole number from 1 to 5.")

    return valid_ratings, valid_comments


def show_summary(ratings, comments):
    """Average rating, count of each rating and top 3 words."""
    print("Valid feedback: " + str(len(ratings)))

    # Average rating
    average = sum(ratings) / len(ratings)
    print("Average rating: " + format(average, ".2f"))

    # Count of each rating (5 down to 1)
    counts_text = []
    for star in [5, 4, 3, 2, 1]:
        counts_text.append(str(star) + " -> " + str(ratings.count(star)))
    print("Ratings: " + ", ".join(counts_text))

    # Count every word in all comments (ignoring stop words)
    word_count = {}
    for comment in comments:
        for word in comment.lower().split():
            word = word.strip(".,!?;:")
            if word == "" or word in STOP_WORDS:
                continue
            if word in word_count:
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1

    # Sort: highest count first, ties in alphabetical order
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

    top_words = []
    for word, count in sorted_words[:3]:
        top_words.append(word + " (" + str(count) + ")")
    print("Top 3 words: " + ", ".join(top_words))


def show_sentiment(ratings):
    """Positive (4-5), Neutral (3), Negative (1-2) percentages + bar chart."""
    positive = 0
    neutral = 0
    negative = 0

    for rating in ratings:
        if rating >= 4:
            positive = positive + 1
        elif rating == 3:
            neutral = neutral + 1
        else:
            negative = negative + 1

    total = len(ratings)
    print("Positive: " + str(positive) + " (" + format(positive / total * 100, ".2f") + "%)")
    print("Neutral: " + str(neutral) + " (" + format(neutral / total * 100, ".2f") + "%)")
    print("Negative: " + str(negative) + " (" + format(negative / total * 100, ".2f") + "%)")

    # Bar chart
    plt.bar(["Positive", "Neutral", "Negative"], [positive, neutral, negative],
            color=["green", "gold", "red"])
    plt.title("Student Feedback Sentiment")
    plt.ylabel("Number of students")
    plt.show()
    print("(bar chart is displayed)")


def main():
    result = load_valid_rows()
    if result is None:
        return

    ratings, comments = result
    if len(ratings) == 0:
        print("No valid feedback found.")
        return

    print("1. Summary and top 3 words")
    print("2. Sentiment")
    choice = input("Choose an option (1 or 2): ").strip()
    print()

    if choice == "1":
        show_summary(ratings, comments)
    elif choice == "2":
        show_sentiment(ratings)
    else:
        print("Invalid choice. Please enter 1 or 2.")


main()
