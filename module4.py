# Eugene Bellau
#Module 4 Assignment


from sys import exit
from random import randint

# Variables
myData = {} #Dictonary Variable
guesses = 0 #Integier Variable
wins = 0 #Integier Variable


with open("questions.txt", "r") as infile: #Opens an iput file as a context manager as read only
    questions = infile.readlines() # Reads all lines at once
    for question in questions:# for loop to ask a question from what it read in the input file
        if 'first' in question: # if statement to search the input file for the word first
            myData['first_name'] = input(question) # stores the input from the user in the myData variable
        elif 'last' in question: # if statement to search the input file for the word last
            myData['last_name'] = input(question)# stores the input from the user in the myData variable
        #else statement to close out of the program if there is bad data in the input file
        else:
            print("bad question in input file")
            exit()
        
            
for play in range(10): #for loop to cycle through 10 times
    number = randint(0, 100) #integir variable to pull random numbers
    solved = False # Boolean to determine if the statement was solved 
    while not solved: # While loop to run the loop as long as the solved statement is equal to False
        guess = int(input(f"Guess a number from 0 to 100 : ")) # stores the input from the user in the int variable and converts the string to an integir
        guesses += 1 # will add to the quesses variable
        if guess == number: # if statement to determine is the correct number was chossen 
            print(f"Great job {myData['first_name']}, your guess of {guess}is correct!") # will print this statement to the user and pull from the myData variable
            wins += 1 # will add to the wins variable
            solved = True # Boolean statement to change the solved variable to true
            break # this will end the loop
        if guess != number: # if statement to determine is the correct number was not chossen
            print(f"Your guess of {guess} is incorrect!") # will print this statement to the user and show them that their guess

        if guess > number: # if statement to determine if the number that was quessed is greater than the number
            print(f"Sorry, you guessed too high!!") # will print this statement to the user
        elif guess < number: # else if statement to determine if the number that was quessed is lower than the number
            print(f"Sorry, you guessed too low!!") # will print this statement to the user
        else:
            pass

    if solved: # if statement to determine if the for loop was solved
        print(f"Let's play again, you have completted {wins} out of 10 plays.") # will print this statement to the user and pull how many times they choose the correct answer from the wins variable
        continue # will continue the code

print(f"{myData['first_name']} {myData['last_name']} guessed the correct number {wins} out of 10 plays.") # will print this statement to the user and pull from the myData variable and pull how many times they choose the correct answer from the wins variable
print(f"It took {myData['first_name']} {myData['last_name']} {guesses} to do this!")# will print this statement to the user and pull from the myData variable and pull from the guesses variable
exit() # this will exit the program
