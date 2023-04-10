
print("Welcome to Assignment 2  by Smeet Patel")

while True:
    print("0. Modulo Calculator")
    print("1. Integer Division Calculator")
    print("2. For Loop Counter")
    print("3. Float & Integer Calculator")
    print("4. Print ASCII values of letters in a string")
    print("5. Change Machine")
    print("6. Rock Paper Scissors")
    print("7. Mario wins a level")
# the print statements is use to select the particular function
    
    num = input("Which Program u want to run: ")
#this statement is use to select the function   
    if num == "0":
#if ,elif,else statements are used to run only which user has entered
        z = int(input("Enter the firs number: "))
        q = int(input("Enter the second number: "))
#z,q are used here to take input from user 
#and z refers to enter the first number 
#and q refers to enter the second number
        result = z % q
        print("The result of", z, "modulo", q, "is", result)
#the result statement is used for z%q 

    elif num == "1":
        z = int(input("Enter the first number: "))
        q = int(input("Enter the second number: "))

        result = z // q
        print("The result of", z, "Division ", q, "is", result)
#this code is similar to the modulo code in this code there is a dividion function 
# z/q (z) refers to first number (q) is used for entering the second number 

    elif num == "2":
        counter = float(input("Please input the intial value"))
#this statement is used for initial value to start the loop
        loopCount = int(input("How many times the loop runs?"))
#this statement is used for number count for loop to run
        Increment_i = float(input("Enter the value of increment during the loop ?"))
#this statement is used for increment in loop
        positive_negative = input("Request decrement instead of incrementing? y or n ") == 'n'
#this statement is used to ask for increment or Decrement

        if not positive_negative:
#if not is negative if statement
            Increment = Increment * -1
            for iterator in range(loopCount):
                counter += Increment
#the part runs the increment or decrement part
        print("The Final outcome is: ",counter)
                

    elif num == "3":

        num1 = float(input(" Enter  the first number: "))
        num2 = float(input(" Enter the second number: "))
#num input

        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulos")

#in this code the 5 options and asks for calculation option and the option are (1) Addition,(2) subtraction, (3) multiplication, (4) division, (5) modulos
        user_choice = input("Select your input from 1,2,3,4,5: ")
#user asked for choice

        if user_choice == '1':
            result = num1 + num2
            print("The sum of ",num1, "and", num2, "is:", result)
        elif user_choice == '2':
            result = num1 - num2
            print("The negative of ",num2, "from", num1, "is:", result)
        elif user_choice == '3':
            result = num1 * num2
            print("The sum of ",num1, "and", num2, "is:", result)
        elif user_choice == '4':
            result = num1 // num2
            print("The divided value  of ",num1, "by", num2, "is:", result)
        elif user_choice == '5':
            result = num1 % num2
            print("The modulos %  of ",num1, "divided by ", num2, "is:", result)
        else:
            print("Invalid Input")
    

    elif num == "4":
        str = input("Enter string to get ascii value ")
        strSize = len(str)
        a = 0
#Asks string size with length
        while i < strSize:
#while statement interprets the user input and runs the String value
            Asciivalue = ord(str[i])
            print("The character at", a, "is", str[a], "and its ASCII value is",Asciivalue)
            a += 1
#Gets the ascii value of the characters            
    elif num == "5":
#in this code we will input the money amount and it will divide into quaters, dimes, nickels
        amount = float(input("Enter the amount in CAD: "))
        cents = int(amount * 100)
#asks user for amount and cents

        quarters = cents // 25
        cents %= 25

        dimes = cents // 10
        cents %= 10

        nickels = cents // 5
        cents %= 5

        pennies = cents
#the below part Calculates the change
        print("Quarters:", quarters)
        print("Dimes:", dimes)
        print("Nickels:", nickels)
        print("Pennies:", pennies)
#prints the output with change value

     elif num == "6":
        import random
#in this code we have to select option rock, paper or scisors and the computer will choose the random selection 
        def rock_paper_scissors_choices(choice):
            if choice == 1:
                return "rock"
            elif choice == 2:
                return "paper"
            elif choice == 3:
                return "scissors"
            else:
                return None
        def rock_paper_scissors():
            choice = 0
#defines the code    
            while choice < 1 or choice > 3:
                choice = int(input("Select your move sir:\n 1.Rock\n 2.Paper\n 3.Scisors\n"))
#ask user for choice                
            random.seed() 
            random_number = random.randint(0, 29)
            ai_choice = (random_number + 10) // 10
            ai_attack = rock_paper_scissors_choices(ai_choice)
            user_choice = rock_paper_scissors_choices(choice)
#creates random ouput from computer side
            if user_choice == ai_attack:
                print(f"Draw happened {choice}!")
                return choice
#if same draws the game
            won = False
            if user_choice == "paper":
                if ai_attack == "scissors":
                    won = False
                else:
                    won = True
            elif user_choice == "rock":
                if ai_attack == "paper":
                    won = False
                else:
                    won = True
            elif user_choice == "scissors":
                if ai_attack == "rock":
                    won = False
                else:
                    won = True
#runs the if else  by user input and then runs the code
            if won:
                print("you won",user_input)
            else:
                print("You lost",user_choice)
            return user_choice
        rock_paper_scissors()
    elif num == "7":
#in this function we can make the stairs with the help of # tag and we have to just write the number 
       height = int(input("Enter the number of Stairs u want"))
       width = height
#asks user for value of height
       for i in range(height):
#declared height to the System
            for j in range(width):
#declares width to the system
                if j <= i:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()
#creates the output by running the code        
    else:
        print("Invalid input entered .")
    break
#breaks stop code from looping
