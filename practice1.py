#These are the two lists that can be pulled from to randomize the question and get the correct answer
questions = ["What is 9 x 3", "What is 18 + 30?", "What is 67 x 2?", "What is the square root of 9?", "What is 10/2?", "What is 121/11?"]
answers = ["27", "48", "134", "3", "5", "11"]

# This is the funtion that chooses a question and its coorlating anwser. Its reusable (as seen with a different question and different answer) it can be inputed with
# any question or anwser and add points to the counter and return whether the answer is right or wrong
def mini_quiz(questions, answers):
# variable that counts how many correct anwsers and incorrect answers and gives you a score
    points = 0
# This is the loop that loops through the given list and chooses a random question from the list, it continues to run until all the questions have been asked.
    for i in range(len(questions)):
        user = input(questions[i])
# These if statements question if the question and the coorelating answer matches the answer of the user, and adds a point if correct and takes away a point if incorrect.
        if user == answers[i]:
            points+= 1
            print("You are correct!")
        else:
            points-= 1
            print("You are incorrect")
    return points

# These functions return the number of points gained at the end of the math quiz.
points = mini_quiz(questions, answers)
points_two = mini_quiz(["What is your favorite color?"], ["Green"])
print("You have", points , "Points")
print("You have", points_two , "Points")






