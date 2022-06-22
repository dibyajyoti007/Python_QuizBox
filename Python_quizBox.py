
user = input('Do you want to play some quiz? (type "y" to continue) : ')
if user.lower() != 'y':
    quit()

print("great. Lets play")
score = 0

ans1 = input("What is the full form of ROM?\n")
if ans1.lower() == "read only memory":
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

ans2 = input("What is the full form of UI?\n")
if ans2.lower() == "user interface":
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

ans3 = input("How many types of inheritance in python?\n")
if ans3.lower() == "five" or ans3 == '5':
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

ans4 = input("Collection of heterogeneous data separated by comma and collected within [] are called ?\n")
if ans4.lower() == "list":
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

ans5 = input("LIST is mutable then TUPLE is ?\n")
if ans5.lower() == "immutable":
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

ans6 = input(" '=' is _____ operator.\n")
if ans6.lower() == "assignment":
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

ans7 = input("What is the output for: \n  s='string' \n  s.index(r)\n")
if ans7.lower() == "2":
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

ans8 = input("Python comment line is stated with?\n")
if ans8.lower() == "#":
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

ans9 = input("With what method we add item to last index of a list?\n")
if ans9.lower() == "append":
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

ans10 = input("what LIST method can convert a list into string?\n")
if ans10.lower() == "join":
    print('Correct answer.')
    score += 10
else:
    print("Wrong answer!!")
    score -= 5

print("Your Score is: ", score, "/100")









