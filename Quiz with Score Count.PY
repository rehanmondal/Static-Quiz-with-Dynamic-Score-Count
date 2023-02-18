print("\n~~~~~~~~~~~~~~~~~ QUIZ GAME ~~~~~~~~~~~~~~~~~~~~~~~~")
print('''\nInstruction : Answer 5 questions and Correct minimum 3 to Win The GAME ''')
print("\n-----------------  ALL THE BEST   --------------\n")

def set_1():
    score=0

    # 1 no
    print("Q1. What is the name of the capital of India ?")
    print("a. Chennai")
    print("b. Delhi")
    print("c. Uttar Pradesh")
    print("d. New Delhi\n")

    ans_1=input("Choose Option - ")

    if ans_1=='d':
        print("Congrats .. Right Answer !!! \n")
        score=score+1
        
    else:
        print("Oh! Its Wrong ")
        print("Correct answer is - New Delhi\n")

    # 2 no
    print("Q2. What is the name of the capital of West Bengal ?")
    print("a. Nadia")
    print("b. South 24 PGS")
    print("c. Calcutta")
    print("d. Kolkata\n")

    ans_2=input("Choose Option - ")

    if ans_2=='d':
        print("Congrats .. Right Answer !!! \n")
        score=score+1
    else:
        print("Oh! Its Wrong ")
        print("Correct answer is - Kolkata\n")

    # 3 no
    print("Q3. How many states are in India ?")
    print("a. 18")
    print("b. 29")
    print("c. 28")
    print("d. 27\n")

    ans_3=input("Choose Option - ")

    if ans_3=='c':
        print("Congrats .. Right Answer !!! \n")
        score=score+1
    else:
        print("Oh! Its Wrong ")
        print("Correct answer is - 28\n")
    # 4 no
    print("Q4. Bay of Bengal situated in - ?")
    print("a. East of India")
    print("b. West of India")
    print("c. North of India")
    print("d. None of the above\n ")

    ans_4=input("Choose Option - ")

    if ans_4=='a':
        print("Congrats .. Right Answer !!! \n")
        score=score+1
    else:
        print("Oh! Its Wrong ")
        print("Correct answer is - East of India\n")
    # 5 no 
    print("Q5. How many continents are there in the world ?")
    print("a. 7")
    print("b. 5")
    print("c. 6")
    print("d. None of the above \n")

    ans_5=input("Choose Option - ")

    if ans_5=='a':
        print("Congrats .. Right Answer !!! \n")
        score=score+1
    else:
        print("Oh! Its Wrong ")
        print("Correct answer is - 7\n")
    #print(score)
    print("You have attempt",score,"questions correctly. ")
    print("Marks : ",score/5*100,"%")
    if score>2:
        print("You Win !\n")
    elif score<3:
        print("Sorrow ! You Lose,Try Better Next Time.\n")
        

set=set_1()

