"""
Visualizing Dictionary Data with Bar Charts and Scatter Plots
"""

import matplotlib.pyplot as plt

# ======================================================================
# MODEL 1 -- Bar Charts from Keys and Values
#
# The dictionary below stores the number of votes received by each food
# in a class survey. The keys are categories (names), and the values are
# numbers.
# ======================================================================

def model_one():
    votes = {"Pizza": 12, "Tacos": 9, "Sushi": 7, "Burgers": 4}
    names = list(votes.keys())
    counts = list(votes.values())
    plt.bar(names, counts)
    plt.xlabel("Food")
    plt.ylabel("Number of votes")
    plt.title("Favorite Foods")
    plt.show()

# Q1. Call the model_one() function. What does each bar represent? What determines the
#     height of each bar?
#
#
#


# Q2. Which line of code gets the data for the x-axis? Which line of code
#     gets the data for the y-axis?
#
#
#


# Q3. In what order do the bars appear? How does that compare to the order
#     of the items in the dictionary?
#
#
#


# Q4. Make each of the following changes to the function above, ONE AT A
#     TIME, and run it. Describe what happens to the chart, and undo each
#     change before trying the next one.
#
#   CHANGE 1: Add  "Salad": 6  to the votes dictionary.
#   What happened to the chart?
#
#
#   CHANGE 2: Change  plt.bar(names, counts)  to  plt.barh(names, counts)
#   What happened to the chart?
#
#
#   CHANGE 3: Change  plt.bar(names, counts)  to
#             plt.bar(names, counts, color="green")
#   What happened to the chart?
#
#
#   CHANGE 4: Change the value of "Sushi" to 15.
#   What happened to the chart?
#
#

# the code below builds a chart from the same data in a different way. 
def model_one_sorted():
    votes = {"Pizza": 12, "Tacos": 9, "Sushi": 7, "Burgers": 4}

    names = sorted(votes)
    counts = []
    for n in names:
        counts.append(votes[n])

    plt.bar(names, counts)
    plt.xlabel("Food")
    plt.ylabel("Number of votes")
    plt.title("Favorite Foods (sorted by name)")
    plt.show()

# Q5. Call the model_one_sorted() function.
#   a) How did the order of the bars change?
# 
#
#   b) What does sorted(votes) return? 
# 
#
#   c) In the loop, what is the purpose of  votes[n] ?
# 
#
#   d) Why must counts be built inside a loop after sorting, rather than
#      using  list(votes.values()) ?
#
#

# Q6. Why is a bar chart a good choice for this dictionary? 
# 
#


# ======================================================================
# MODEL 2 -- Scatter Plots from Nested Dictionaries
#
# Each bar in a bar chart compares one value per category. A scatter plot
# shows the relationship between two numbers for each item. The
# dictionary below stores information about each student: hours studied 
# and exam score.
# ======================================================================

students = {
    "Ana": {"year": 1, "hours": 6, "score": 88},
    "Ben": {"year": 2, "hours": 3, "score": 72},
    "Cai": {"year": 3, "hours": 8, "score": 95},
    "Dee": {"year": 2, "hours": 2, "score": 64},
    "Eli": {"year": 1, "hours": 5, "score": 84},
    "Fay": {"year": 3, "hours": 4, "score": 79},
    "Gus": {"year": 1, "hours": 1, "score": 55},
    "Hal": {"year": 2, "hours": 7, "score": 91},
}

def build_hours_scores_lists():
    hours = []
    scores = []
    for name in students:
        hours.append(students[name]["hours"])
        scores.append(students[name]["score"])

    print(hours)
    print(scores)

    return hours, scores

def model_two():
    hours, scores = build_hours_scores_lists()
    plt.scatter(hours, scores)
    plt.xlabel("Hours studied")
    plt.ylabel("Exam score")
    plt.title("Study Time and Exam Scores")
    plt.show()

# Q7. Run the model_two() function. How many points are plotted? 
#     What does each point represent?
#
#
#


# Q8. In the expression  students[name]["hours"], what does students[name]
#     give you? Why does "hours" need to be in quotes?
#
#
#


# Q9. Compare the lists printed for hours and scores. Which student does
#     the first value in each list belong to? How do you know the two
#     lists stay "matched up"?
#
#
#


# Q10. Describe the relationship you see in the plot. In general, what
#      happens to the scores as hours increase?
#
#
#


# Q11. Predict what would happen if you removed the line
#         scores.append(students[name]["score"])
#      from the loop in build_hours_scores_lists(). Then, 
#      comment out the line and record the result. 
#
# Prediction:
#
# Result:
#
#


# Q12. The code below adds a label to each point. Call the function
#      and then answer the questions.

def model_two_labeled():
    hours, scores = build_hours_scores_lists()
    plt.scatter(hours, scores)
    for name in students:
        plt.annotate(name, (students[name]["hours"], students[name]["score"]))
    plt.xlabel("Hours studied")
    plt.ylabel("Exam score")
    plt.title("Study Time and Exam Scores (labeled)")
    plt.show()

#   a) What do the added labels show?
#
#
#
#   b) Which student studied the fewest hours? What was that student's
#      score?
#
#
#
#   c) Which student has the highest score? How many hours did that
#      student study?
#
#
#


# YOUR TURN: Make a scatter plot with each student's "year" on the
#            x-axis instead of "hours". You will need to build a new 
#            list named years (using a loop like the one above), and 
#            then call plt.scatter with years and scores. Include axis 
#            labels and a title.



# Q13. Is the relationship between year and score as clear as the
#      relationship between hours and score? Explain.
# 
#
#
#


# Q14. A bar chart could also show these scores, with one bar per student.
#      What question does the bar chart answer better? What question does
#      the scatter plot answer better?
# 
#
#
#


# Q15. For each of the following datasets, decide whether a bar chart or a
#      scatter plot is more appropriate, and explain your choice.
#   a) A dictionary mapping each month to the number of rainy days.
#
#
#
#   b) A dictionary mapping each car model to a dictionary containing its
#      weight and fuel economy.
#
#
#
#   c) A dictionary mapping each word in a book to the number of times it
#      appears.
#
#
#
#


# Q16. Write a short plan, in words (not code), for how you would get 
#      each of the following into lists so they can be plotted:
# (a) the keys and values of a simple dictionary
# 
#
# (b) two fields from a nested dictionary
#
#