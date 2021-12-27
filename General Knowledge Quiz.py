import time

score=int()
print("Welcome to the General Knowledge Quiz!")
print('\n')
time.sleep(2)
print("Question 1")
time.sleep(2)
Question1 = input ("How many states are in the country of India? ")
if Question1 == ("28") or Question1 == ("twenty-eight"):
    print("Correct answer!")
    score = score + 1 
else:
    print("Incorrect answer. The correct answer is Pakistan")
time.sleep(2)
print("Question 2")
time.sleep(2)
Question2 = input("In which English city is Buckingham Palace located? ")
if Question2 == ("London") or Question2 == ("london"):
    print("Correct answer!")
    score = score + 1
else:
    print("Incorrect answer. The correct answer is London")
time.sleep(2)
print("Question 3")
time.sleep(2)
Question3 = input("How many hours are there in a week? ")
if Question3 == ("168"):
    print("Correct answer!")
    score = score + 1
else:
    print("Incorrect answer. The correct answer is 168 hours")
time.sleep(2)
print("Question 4")
time.sleep(2)
Question4 = input("In which sport can you win the Davis Cup? ")
if Question4 == ("Tennis") or Question4 == ("tennis"):
    print("Correct answer!")
    score = score + 1
else:
    print("Incorrect answer. The correct answer is Tennis")
time.sleep(2)
print("Question 5")
time.sleep(2)
Question5 = input("What is the capital of Cyprus? ")
if Question5 == ("Nicosia") or Question5 == ("nicosia"):
    print("Correct answer!")
    score = score + 1
else:
    print("Incorrect answer. The correct answer is Nicosia.")
time.sleep(2)
print("Question 6")
time.sleep(2)
Question6 = input("How many golden stars feature on the flag of the European Union? ")
if Question6 == ("twelve") or Question6 == ("Twelve") or Question6 == ("12"):
    print("Correct answer!")
    score = score + 1
else:
    print("Incorrect answer. The correct answer is 12")
time.sleep(2)
print("Question 7")
time.sleep(2)
Question7 = input("Which YouTube channel has the most subscribers? ")
if Question7 == ("T-Series") or Question7== ("t-series") or Question7 == ("t-Series") or Question7 == ("T-series"):
    print("Correct answer! The YouTube channel 'T-Series' has over 210M subscribers!")
    score = score + 1
else:
    print("Incorrect answer. The correct answer is T-Series")
time.sleep(2)
print("Question 8")
time.sleep(2)
Question8=input("In which year did Theresa May become Prime Minister of the UK? ")
if Question8 == ("2016"):
    print("Correct answer!")
    score = score + 1
else:
    print("Incorrect answer. The correct answer is 2016")
time.sleep(2)
print("Question 9")
time.sleep(2)
Question9 = input("What is 5/11 of 231? ")
if Question9 == ("105") or Question9  == ("one hundred and five") or Question9 == ("a hundred and 5"):
    print("Correct answer!")
    score = score + 1
else:
    print("Incorrect asnwer. The correct answer is 48")
time.sleep(2)
print("Question 10")
time.sleep(2)
Question10 = input("Which type of angle is greater than 90 degrees but less than 180 degrees? ")
if Question10 == ("obtuse") or ("Obtuse"):
    print("Correct answer!")
    score = score + 1
else:
    print("Incorrect asnwer. The correct answer is obtuse.")
time.sleep(2)
print("Congratulations! You have made it to the end of the quiz!")
time.sleep(1)
print("You got",(score),"/ 10")
num1 = (score)
num2 = 10
print('{0:.2f}%!'.format((num1 / num2 * 100)))
