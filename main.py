score = 0
largest = 20
import random
my_file = open("trabitour1A.txt", "r")
content = my_file.readlines()

while score != 100:
    n = random.randint(0,largest)
    
    if (n % 2) != 0:
        n=n+1
    
    Question = input("what does " + content[n] + "mean?")
    if Question == content[n+1]:
        print("correct")
    else:
        print(content[n+1])
        mistake = input("Did you have the right answer y/n")
        if mistake == "y":
            print("you had the correct answer!")
            score += (1/largest * 100)
            print(score)

        if mistake == "n":
            print("youl get it better next time")


        

        