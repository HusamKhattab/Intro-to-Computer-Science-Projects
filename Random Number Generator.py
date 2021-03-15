import random

def main():

    randomNumber= random.randint (0,10)

    count =0

    while True:

        guess = int(input("Guess?\n"))

        

        if(guess == randomNumber):

            count = count+1

            print ("Congratulations found guessed correct number and number of guesses are ",count)

            break

        elif (guess >10 or guess <0):

            print ("Input should be in between 0 and 10")
            
        
        elif guess > randomNumber:

            count= count+1

            print ("Too high, try again.")
            
        
        elif guess < randomNumber:

            count= count+1

            print ("Too low, try again.")

if __name__=='__main__':

    main()
