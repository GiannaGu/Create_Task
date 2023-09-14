
questions = ["What is 9 x 3", "What is 18 + 30?", "What is 67 x 2?", "What is the square root of 9?", "What is 10/2?", "What is 121/11?"]
answers = ["27", "48", "134", "3", "5", "11"]


def mini_quiz(questions, answers):
    points = 0
    for i in range(len(questions)):
        user = input(questions[i])
        if user == answers[i]:
            points+= 1
            print("You are correct!")
        else:
            points-= 1
            print("You are incorrect")
    return points

points = mini_quiz(questions, answers)
points_two = mini_quiz(["What is your favorite color?"], ["Green"])
print("You have", points , "Points")
print("You have", points_two , "Points")






