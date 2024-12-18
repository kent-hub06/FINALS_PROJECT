import sys
import time
######################
def user_input():
    while True:
        ask = input("\n\nWOULD YOU LIKE TO START THE PROGRAM? (yes/no): ")
        if ask.lower() == "yes":
            print("\nLoading:")
            
            #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            
            for i in range(len(animation)):
                time.sleep(0.2)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
            print("\nDONE!")
            print("\n\t\t=========================")
            user = input("\t\t  ENTER YOUR NAME: ")
            print("\t\t=========================")
            print(f"\n\n\t---------------------------------------\n\t   HELLO WELCOME TO THE PROGRAM, {user}!\n\t---------------------------------------")
            main_menu()
            break
        elif ask.lower() == "no":
            print("\n\n\t\t=======================")
            print("\t\t     OK, GOODBYE!.")
            print("\t\t=======================\n")
            sys.exit()
        else:
            print("\nInvalid Input. Please type 'yes' or 'no'.")
######################
def main_menu():
    while True:   
        print("\n\t========================\n\t\t-Main Menu-\n\t========================")
        print("\t  1. Python Fundamentals")
        print("\t  2. Activity")
        print("\t  3. CodeChallenge")
        print("\t  4. Exit")
        print("\t========================")
        
        
        choice = input("\nEnter your choice( 1 / 2 / 3 / 4 ): ")
            

        if choice == '1':
            py_fundamentals()
        elif choice == '2':
            activity_menu()
        elif choice == '3':
            code_challenge_menu()
        elif choice == '4':
            exit_user()
            break
        else:
            print("\n\tInvalid choice. Please try again!\n")
######################
def py_fundamentals():
    while True:
        print("\n====================================================\n\t\t-Python Fundamentals-\n====================================================")
        print("\n  1. Print Statements\n  2. Variables\n  3. Operators\n  4. Conditional Statements\n  5. Loops\n  6. Lists\n  7. Functions")
        print("================================")
        print("(Type 0 to go back to Main menu)")

        choice = input("\nEnter your choice Topic(1-7):")

        if choice == '1':
            Print_statements()
        elif choice == '2':
            Variables()
        elif choice == '3':
            Operators()
        elif choice == '4':
            Conditionals()
        elif choice == '5':
            Loops()
        elif choice == '6':
            Lists()
        elif choice == '7':
            Functions()
        elif choice == '0':
            main_menu()        
        else:
            print("Invalid choice. Please try again or type (0) to back to Main Menu!")
######################
def activity_menu():
    while True:
        print("\n==================================================\n\t\t-Activity Menu-\n==================================================\n\n1. Activity 1\n2. Activity 2\n3. Activity 3\n4. Activity 4\n5. Activity 5\n6. Activity 6\n7. Activity 7\n8. Activity 8\n9. Activity 9\n10. Activity 10\n11. Activity 11\n12. Activity 12\n13. Activity 13\n14. Activity 14\n15. Activity 15\n16. Activity 16\n17. Activity 17\n18. Activity 18\n19. Activity 19\n20. Activity 20\n21. Activity 21\n22. ACtivity 22\n23. Activity 23\n24. Activity 24\n25. Activity 25")
        print("================================")
        print("(Type 0 to go back to Main menu)")
        
        choice = input("Enter your choice activity(1-25):")

        if choice == '1':
            Activity_1()
        elif choice == '2':
            Activity_2()
        elif choice == '3':
            Activity_3()
        elif choice == '4':
            Activity_4()
        elif choice == '5':
            Activity_5()
        elif choice == '6':
            Activity_6()
        elif choice == '7':
            Activity_7()
        elif choice == '8':
            Activity_8()
        elif choice == '9':
            Activity_9()
        elif choice == '10':
            Activity_10()
        elif choice == '11':
            Activity_11()
        elif choice == '12':
            Activity_12()
        elif choice == '13':
            Activity_13()
        elif choice == '14':
            Activity_14()
        elif choice == '15':
            Activity_15()
        elif choice == '16':
            Activity_16()
        elif choice == '17':
            Activity_17()
        elif choice == '18':
            Activity_18()
        elif choice == '19':
            Activity_19()
        elif choice == '20':
            Activity_20()
        elif choice == '21':
            Activity_21()
        elif choice == '22':
            Activity_22()
        elif choice == '23':
            Activity_23()
        elif choice == '24':
            Activity_24()
        elif choice == '25':
            Activity_25()
        elif choice == '0':
            main_menu()
        else:
            print("Invalid choice. Please try again or type (0) to back to Main Menu!")
######################    
def code_challenge_menu():
    while True:
        print("\n=========================================================\n\t\t-Code Challenge Menu-\n=========================================================\n1. CC_1\n2. CC_2\n3. CC_3\n4. CC_4\n5. CC_5\n6. CC_6\n7. CC_7\n8. CC_8\n9. CC_9\n10. CC_10\n11. CC_11\n12. CC_12\n13. CC_13\n14. CC_14\n15. CC_15\n16. CC_16")
        print("=============================")
        print("(type 0 to go back to Main menu)")

        choice = input("Enter your choice Code challenge(1-16):")
        
        if choice == '1':
            CC_1()
        elif choice == '2':
            CC_2()
        elif choice == '3':
            CC_3()
        elif choice == '4':
            CC_4()
        elif choice == '5':
            CC_5()
        elif choice == '6':
            CC_6()
        elif choice == '7':
            CC_7()
        elif choice == '8':
            CC_8()
        elif choice == '9':
            CC_9()
        elif choice == '10':
            CC_10()
        elif choice == '11':
            CC_11()
        elif choice == '12':
            CC_12()
        elif choice == '13':
            CC_13()
        elif choice == '14':
            CC_14()
        elif choice == '15':
            CC_15()
        elif choice == '16':
            CC_16()
        elif choice == '0':
            main_menu()
        else:
             print("Invalid choice. Please try again or type (0) to back to Main Menu!")
######################
def Print_statements():
    print("\n-----------------\nPrint Statements\n-----------------")
    print("-A print() function is used to show messages or outputs on the screen.")
    print("\n---Example---\n\nInput:\n\nprint('Hello, World!')\n\nOutput:\n\nHello, World!")
    ask = input("\n\n\nWould you like to go back?(yes/no):")
    if ask.lower()== "yes":
        py_fundamentals()
    elif ask.lower()== "no":
        Print_statements()
    else:
        print("Goodbye!")
        py_fundamentals()
######################
def Variables():
    print("\n-----------------\n  Variables\n-----------------")
    print("-Name, Age, and Height are variables.")
    print("\nVariables store different types of data like text (string), numbers (integer, float).")
    print("\nThe print function displays the values of these variables")
    print("\n\n---Example---\n\nInput:\n\nname = 'Kent'\nage = 18\nheight = 5.5\n\nprint('Name:', name)\nprint('Age:', age)\nprint('Height:', height)")
    print("\n\nOutput:\n\nName: Kent\nAge: 18\nHeight: 5.5")    
    ask = input("\n\n\nWould you like to go back?(yes/no):")
    if ask.lower()== "yes":
        py_fundamentals()
    elif ask.lower()== "no":
        Variables()
    else:
        print("Goodbye!")
        py_fundamentals()
######################
def Operators():
  while True:
      print("\n-----------------\n\t\b\b\b\bOperators\n-----------------")
      print("-Operators are special symbols or keywords in Python that are used to perform operations on values or variables. These operations can be mathematical, logical, or related to comparisons..")
      print("\n-Types of Python Operators-\n\n1. Arithmetic Operators\n- Used to perform mathematical calculations.\n\n+	Addition	10 + 20 = 30\n-	Subtraction	20 – 10 = 10\n*	Multiplication	10 * 20 = 200\n/	Division	20 / 10 = 2\n%	Modulus 	22 % 10 = 2\n**	Exponent	4**2 = 16\n//	Floor Division	9//2 = 4\n\n2. Comparison (Relational) Operators\n- Used to compare two values. They return True or False.\n==	Equal\t\t\t\t4 == 5 is not true.\n!=	Not Equal\t\t\t4 != 5 is true.\n>	Greater Than\t\t\t4 > 5 is not true\n<	Less Than\t\t\t4 < 5 is true\n>=	Greater than or Equal to\t4 >= 5 is not true.\n<=	Less than or Equal to\t\t4 <= 5 is true.\n\n3. Assignment Operators\n- Used to assign values to variables in Python.\n\n=	Assignment Operator\t\ta = 10\n+=	Addition Assignment\t	a += 5 (Same as a = a + 5)\n-=	Subtraction Assignment\t	a -= 5 (Same as a = a - 5)\n*=	Multiplication Assignment	a *= 5 (Same as a = a * 5)\n/=	Division Assignment\t	a /= 5 (Same as a = a / 5)\n%=	Remainder Assignment\t	a %= 5 (Same as a = a % 5)\n**=	Exponent Assignment\t	a **= 2 (Same as a = a ** 2)\n//=	Floor Division Assignment	a //= 3 (Same as a = a // 3)\n\n4. Logical Operators\n- Used to combine conditional statements\n\nand:  Returns True if both statements are true	x < 5 and  x < 10	\nor:   Returns True if one of the statements is true	x < 5 or x < 4	\nnot:  Reverse the result, returns False if the result is true	not(x < 5 and x < 10)")
      print("\nExample:\nIn Code Challenge 4\n\nInput:\n\nnumber1 = eval(input('Enter a number ----> '))\nnumber2 = eval(input('Enter a number ----> '))\n\nanswer = number1 + number2\nanswer2 = number1 - number2\nanswer3 = number1 * number2\nanswer4 = number1 / number2\nanswer5 = number1 ** number2\nanswer6 = number1 // number2\nanswer7 = number1 % number2\n\nprint('The sum of ' ,number1 , ' and ',number2 ,' is ' , answer)\nprint('The difference of ' ,number1 , ' and ',number2 ,' is ' , answer2)\nprint('The product of ' ,number1 , ' and ',number2 ,' is ' , answer3)\nprint('The quotient of ' ,number1 , ' and 'number2 ,' is ' , answer4)\nprint('The exponent of ' ,number1 , ' and ',number2 ,' is ', answer5)\nprint('The floor division of  ',number1 , ' and ',number2 ,' is ' , answer6)\nprint('The reminder of ' ,number1 , ' and ',number2 ,' is ' , answer7)")
      ask = input("\nWould you like to run this code(yes/no):")
      if ask.lower()== "yes":
          print("here is the Output:")
          CC_4()
          break
      elif ask.lower()== "0":
          main_menu()
      elif ask.lower()== "no":
          print("Goodbye!")
          py_fundamentals()
      else:
          print("\nInvalid input. Please enter 'yes' or 'no'!")
          continue
######################
def Conditionals():
    while True:
        print("\n----------------------\nConditional Statement\n----------------------")
        print("\nTypes of Conditional Statements in Python:")
        print("\nIf Statement:\n\nThe if statement checks if a condition is true.\nIf the condition is True, the block of code under it is executed")
        print("\nIf-else Statement:\n\nThe if-else statement adds an else block to handle cases where the condition is False")
        print("\nIf-elif-else Statement:\n\nThe if-elif-else statement Allows you to check multiple conditions using elif (short for 'else if')\nThe else block handles the case where none of the conditions are True")
        print("\nExample:\n\nIn Activity 9")
        print("\nThe program uses an if-elif-else structure to determine and print the user's life stage based on the entered age.")
        ask = input("\nWould you like to run this code(yes/no):")
        if ask.lower()== "yes":
            print("here is the Output:")
            Activity_9()
            break
        elif ask.lower()== "0":
            main_menu()
        elif ask.lower()== "no":
            print("Goodbye!")
            py_fundamentals()
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'!")
            continue
######################
def Loops():
  while True:
      print("\n-----------------\n\t\b\bLoops\n-----------------")
      print("\n-A loop is a way to repeat a block of code multiple times, either for a specific number of iterations or until a condition is met. Loops are useful for automating repetitive tasks.")
      print("\nType of Python Loops\n\n  For Loop:\nUsed to go through items in a sequence, such as a list or a range of numbers.\n\n  While Loop:\nUsed to repeat a block of code as long as a condition is True")
      print("\nExample:\nIn Code Challenge 15")
      print("\nThe While loop is used for repeatedly asking the user whether they want to add another triangle or terminate the program, It keeps running until the user types 'no'.\n\nThe For loops are used to build and print the triangle pattern.")
      ask = input("\nWould you like to run this code(yes/no):")
      if ask.lower()== "yes":
          CC_15()
          break
      elif ask.lower()== "0":
          main_menu()
      elif ask.lower()== "no":
          print("Goodbye!")
          py_fundamentals()
      else:
          print("\nInvalid input. Please enter 'yes' or 'no'!")
          continue
######################
def Lists():
  while True:
      print("\n-----------------\n\t\bLists\n-----------------")
      print("\n-Lists are used to store multiple items in a single variable.")
      print("\nExample:\nIn activity 25")
      print("\nThis program use lists for storing and manipulating fruit names. It demonstrates list operations such as indexing, appending, inserting,\nand removing items, and it interacts with the user to dynamically modify the list.")
      ask = input("\nWould you like to run this code(yes/no):")
      if ask.lower()== "yes":
          print("here is the Output:")
          Activity_25()
          break
      elif ask.lower()== "0":
          main_menu()
      elif ask.lower()== "no":
          print("Goodbye!")
          py_fundamentals()
      else:
          print("\nInvalid input. Please enter 'yes' or 'no'!")
          continue
######################
def Functions():
  while True:
      print("\n-----------------\n\t\b\b\b\bFunctions\n-----------------")
      print("\n-A function in Python is a reusable block of code that performs a specific task.\nIt helps make your code modular, organized, and easier to maintain.\nFunctions are especially useful when you need to perform the same task multiple times in a program.")
      print("\nExample:\nIn activity 21\n\nInput:\n#BASIC REQUIREMENT OF CREATING YOUR OWN PYTHON FUNCTION\n\ndef pang_hello():\n\tprint('Hello IT1C')\n\npang_hello()\n#FUNCTION WITH A PARAMETER\ndef pang_hello_v2(name):\n\tprint(f'Hello {name}')\ndef activity3():\n\tnum1 = eval(input('Please Enter the First Number: '))\n\tnum2 = eval(input('Please Enter the Second Number: '))\n\tresult = num1 + num2\n\tprint(result)\ntuloy = True\nwhile tuloy == True:\n\task = input('Please provide a name: ')\n\tif ask.lower() != 'stop':\n\tpang_hello_v2(ask)\nelif ask.lower() == '3':\n\tactivity3()\n\tcontinue\nelse:\n\tbreak")
      print("\n-This code demonstrates basic function usage, parameters, and interaction through a loop. ")
      ask = input("\nWould you like to go back?(yes/no):")
      if ask.lower()== "yes":
        py_fundamentals()
        break
      elif ask.lower()== "0":
          main_menu()
      elif ask.lower()== "no":
          print("Goodbye!")
          Functions()
      else:
          print("\nInvalid input. Please enter 'yes' or 'no'!")
          continue
###################### 
def Activity_1():
    print("\n----------\nActivity 1\n----------")
    print("Hello World")
    name = input("Please Enter your Name: ")
    print("Hi, " +name,"!")
def Activity_2():
    print("\n----------\nActivity 2\n----------")
    num1 = eval(input("Please Enter the First Number: "))
    num2 = eval(input("Please Enter the Second Number: "))
    answer = num1 + num2
    print(num1, "+" , num2 , "=" , answer)
def Activity_3():
    print("\n----------\nActivity 3\n----------")
    num1 = eval(input("Please Enter the First Number: "))
    num2 = eval(input("Please Enter the Second Number: "))

    result = num1 + num2
    print(result)
def Activity_4():
    print("\n----------\nActivity 4\n----------")
    number1 = eval(input("Enter a number ----> "))
    number2 = eval(input("Enter a number ----> "))

    answer = number1 + number2
    answer2 = number1 - number2
    answer3 = number1 * number2
    answer4 = number1 / number2
    answer5 = number1 ** number2
    answer6 = number1 // number2
    answer7 = number1 % number2

    print("The sum of " ,number1 , " and ",number2 ," is " , answer)
    print("The difference of " ,number1 , " and ",number2 ," is " , answer2)
    print("The product of " ,number1 , " and ",number2 ," is " , answer3)
    print("The quotient of " ,number1 , " and ",number2 ," is " , answer4)
    print("The exponent of " ,number1 , " and ",number2 ," is " , answer5)
    print("The floor division of " ,number1 , " and ",number2 ," is " , answer6)
    print("The reminder of " ,number1 , " and ",number2 ," is " , answer7)
def Activity_5():
    print("\n----------\nActivity 5\n----------")
    print("FAHRENTHEIT to CELCIUS CONVERTER")
    temp = eval(input("Enter temperature in Fahreinheit: "))

    celcius = (temp - 32) * 5 / 9

    print(f"The Convertion of {temp} degree Fahrenheit is {round(celcius, 2)} degree Celcius")
######################
def Activity_6():
    print("\n-----------\nActivity 6\n----------")
    #Assigment operators
    x = 10
    print(x)

    a = x + 10
    print(a)

    c = 100
    c += 100
    print(c)

    d =  100
    d -= 100
    print(d)

    e = 100
    e *= 100
    print(e)

    f = 100
    f /= 100
    print(f)

    g = 100
    g //= 100
    print(f)

    h = 100
    h **= 1
    print(h)

    i = 100
    i %= 100
    print(i)
def Activity_7():
    print("\n----------\nActivity 7\n----------")
    #Conditional Statement
    gold = 0 
    miner = input("Hi, please Enter your Name: ")
    HasMine = input("Did you mine something today?(yes/no): ")

    if HasMine.lower() == "yes":
        gold += 1_000_000_000
        print(f"Hi {miner}, today you have a total of {gold} gold")
    elif HasMine.lower() == "no":
        print(f"Hi {miner}, Please mine a Gold!:)")
    elif HasMine.lower() != "yes" and "no":
        print("Please write the right Input")
    else:
        print(f"Hi {miner}, today you have a total of {gold} gold")
def Activity_8():
    print("\n----------\nActivity 8\n----------")
    Password = input("Please Enter your Password: ")

    if Password.lower() == "secret":
        print("Access Granted")
        print("Welcome to the System")
        print("Enjoy using the System")
    else:
        print("Access Denied!")
        print("Thank your for using the System!")
def Activity_9():
    print("\n----------\nActivity 9\n----------")
    Age = eval(input("Enter your Age: "))

    if Age >= 0 and Age <= 7:
        print("You are a Toddler")
    elif Age > 7 and Age <= 13:
        print("You are a Pre-Teen")
    elif Age > 13 and Age <= 18:
        print("You are a Teenager")
    elif Age > 18 and Age <= 31:
        print("You are an Early Adult ")
    elif Age > 31 and Age <= 45:
        print("You are a Mid Adult ")
    elif Age > 45 and Age <=59: 
        print("You are a Past Adult")
    elif Age > 59 and Age <=120:
        print("You are a Senior")
    else: 
        print("Please Input a Valid Number")
def Activity_10():
    print("\n-----------\nActivity 10\n-----------")
    print("DLL Free BSIT Scholarship Form\n")
    isDLL = input("Are you a current student of DLL ( yes / no ) : ")
    isIT = input("Are you interested in taking the course of Bachelor Science in Information Technology ( yes / no ): ")

    if isIT.lower() == "yes":
        print("Welcome Future IT Student!")
    
        if isDLL.lower() == "yes":
            print("Welcome to the DLL BSIT Scholarship!")
        
            isGG = input("Are you from Brgy. 10 ( yes / no ): ")

            if isGG.lower() == "yes":
                print("Please Fill up the Second Form ")
            
                isLevel = input("What is your curent year level right now in DLL: \nF - Freshmen \nS - Sophomore \nJ - Junior \nR - Senior \nPlease input your answer: ")
            
                if isLevel.lower() == "f":
                    print("Hi, Freshmen!")
                elif isLevel.lower() == "f":
                    print("Hi, Sophomore!")
                elif isLevel.lower() == "j":
                    print("Hi, Junior!")
                elif isLevel.lower() == "r":
                    print("Hi, Senior!")
                else:
                    print("Invalid Choice")

                isNeeded = input("Do you need this Scholarship ( yes / no): ")

                if isNeeded.lower() == "yes":
                    print("Scholarship Granted!")
                else:
                    print("Thank you for stopping by!")
            else:
                print("Sorry, this Scholarship are only given from the Residents of Barangay 10.")
        else:
            print("Thank you for stopping by!")
    else:
        print("Sorry, this Form is only for those who want to take the Course of BSIT in DLL\nThank you for stopping by! ")

    print("Thank you for stopping by!")
######################  
def Activity_11():
    print("\n-----------\nActivity 11\n-----------")
    #Print Hello World 10 times
    for x in range(1, 11):
        print(x, "Hello World")
        print("Happy Foundation Day")
        name = input("Hi, what is your name: ")
        print(f"Hi {name}!") 
def Activity_12():
    print("\n-----------\nActivity 12\n-----------")
    for cycle in range(10, 0, -1):
        print(cycle)
def Activity_13():
    print("\n-----------\nActivity 13\n-----------")
    num1 = eval(input("Enter any number: "))
    factorial = 1
    for i in range(num1, 0 , -1):
        factorial *= i

    print(f" the factorial of {sum} is {factorial} ")
def Activity_14():
    print("\n-----------\nActivity 14\n-----------")
    for x in range(0, 11):
        print(x, end = "")

        for y in range(x, 11):
            print("*", end = " ")
        print()
def Activity_15():
    print("\n-----------\nActivity 15\n-----------")
    for x in range(0, 21):
        print(x, end= " ")
        for y in range(0, x):
            print("*", end= " ")
        print()
######################
def Activity_16():
    print("\n-----------\nActivity 16\n-----------")
    for a in range(1, 6):
        for b in range(6, a,  -1):
            print(" ", end = " ")
        for c in range(1, a + 1):
            print("*", end = " ")
        for c in range(1, a + 1):
            print("*", end = " ")
        print()
def Activity_17():
    print("\n-----------\nActivity 17\n-----------")
    col = eval(input("Enter number of column: "))

    for x in range(1, 11):
        for y in range(1,col +1):
            print(f"{x} x {y} = {x*y}", end =  "\t")
        print()
def Activity_18():
    print("\n-----------\nActivity 18\n-----------")
    no = eval(input("Enter number of Triangle: "))
    for x in range(1, 5):
        for r in range(1,no + 1):
            for y in range(1,x + 1):
                print("*", end= " ")
    
            for z in range(5, x, -1):
                print(" ",end= " ")
        print()
def Activity_19():
    print("\n-----------\nActivity 19\n-----------")
    tuloy = True

    while tuloy == True:
        name = input("Please enter a name: ")

        if name.lower() == "stop":
            print("Program Terminated")
            break 
        else:
            continue    
def Activity_20():
    print("\n-----------\nActivity 20\n-----------")
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another Triangle(Yes/No): ")

        if ask.lower() == "no":
            print('PROGRAM TERMINATED')
            break
            isContinue = False
        else:
            os.system('cls')
            no += 1
            for x in range (1, 5):
                for r in range(1,no + 1):
                    for y in range(1,x, +1):
                        print("*", end = " ")
                
                    for z in range(5, x, -1):
                        print(" ", end = " ")
                print()
            continue
######################
def Activity_21():
    print("\n-----------\nActivity 21\n-----------")
    #BASIC REQUIREMENT OF CREATING YOUR OWN PYTHON FUNCTION

    def pang_hello():
        print("Hello IT1C")

    pang_hello()

    #FUNCTION WITH A PARAMETER
    def pang_hello_v2(name):
        print(f"Hello {name}")

    def activity3():
        num1 = eval(input("Please Enter the First Number: "))
        num2 = eval(input("Please Enter the Second Number: "))

        result = num1 + num2
        print(result)

    tuloy = True
    while tuloy == True:
        ask = input("Please provide a name: ")

        if ask.lower() != "stop":
            pang_hello_v2(ask)
        elif ask.lower() == "3":
            activity3()
            continue
        else:
            break           
def Activity_22():
    print("\n-----------\nActivity 22\n-----------")
    #Creating own python functions

    import os
    def panghello():
        print("\nHello IT1C")

    def Activity2():
        num1= eval(input("\nPlease input a number: "))
        num2= eval(input("Please input another number: "))
        print("\n", num1, "Floor divided to ", num1 , " = " , num1 // num2)

    def Activity4():
        num1= eval(input("Enter a number-->"))

        num2= eval(input("Enter another number -->"))

        add= num1+num2
        minus= num1-num2
        times= num1*num2
        divide=num1/num2

        print("The sum of" , num1, "and ", num2, "is " ,add )
        print("The difference of" , num1, "and ", num2, "is " ,minus )
        print("The product of" , num1, "and ", num2, "is " ,times )
        print("The quotient of" , num1, "and ", num2, "is " ,divide)
    
    def Activity5():
        temp=int(input("Enter temperature in Farenheit:"))

        cel =(temp-32)*5/9
        round=(round(cel,2))

        print(f"The conversion of {temp} degrees fahrenheit is {round} degrees celcuis")
    
    def Activity6():
        x=5
        print(x)

        x=x+10

        print(x)

        x=x+20

        print(x)


        x=x+30

        print(x)

    def Activity7():
    #conditional statements
        gold=0

        min= input("Hola! Please enter your name-->")

        #answerable by yes or no

        ismine=input("Did you mine gold today??")

        #introduction to decision structure and relational operators
        if ismine.lower()=="yes":
            gold+=1
            print(f"Hi{min}, today you have a total of {gold} gold")
        else:
            print(f"Hi{min}, today you have a total of {gold} gold")

    def Activity8():
        password = input ("enter your password -->: ") 


        if password.lower() == "arete":
            print("Access Granted")
            print("Enjoy using the system")
        elif password.lower() == "lol":
            print ("Access Granted")
        elif password.lower() =="ror":
            print("Access Denied")
            print("Charot")
        else:
            print ("Access Denied") 
        print("Sytem Exit")

    def Activity9():
        age= eval(input(" Enter your age here---> "))

        if age >= 1 and age <= 7 :
            print ("Your a toddler")
        elif age >= 8 and age <= 13 :
            print("Your a Pre-teen")
        elif age >= 14 and age <= 18 :
            print ("Your a Teenager")
        elif age >= 19 and age <= 31 :
            print("Your in Early Adulthood")
        elif age >= 32 and age <=45  :
            print ("Your in Mid Adulthood")
        elif age >= 46 and age <= 59 :
            print ("Your in Post Adultood")
        elif age >= 60 :
            print ("Your a Senior")
        else:
            print("Invalid age")

    def Activity10():
        DLL= input("Are you a current student of DLL [yes / no] :")

        if DLL.lower()== "yes":
            print("welcome to Dalubhasaan ng Lungsod ng Lucena")
            isBSIT= input("Are you currently enrolled in Bachelor of Science in Information Technology? [yes / no]")
        
            if isBSIT.lower() =="yes":
                print("What a Beautiful Day. Glad to have you in BSIT")
                print("Please fill up the second form")
            
                isLevel= input("What current year level are you right now in DLL? \n F-FRESHMEN \n S-SOPHOMORE \n J-JUNIOR \n SS-SENIOR \n Please input your answer here-->")
                if isLevel.lower()=="f":
                    print("WELCOME FRESHMEN")
                elif isLevel.lower()=="s":
                    print("WELCOME SOPHOMORE")
                elif isLevel.lower()=="j":
                    print("WELCOME JUNIOR")
                elif isLevel.lower()=="ss":
                    print("WELCOME SENIOR")                
                
            else:
                print("Sorry you are not welcome here")
                    
        else:
            print("Thanks for stopping by ^_^")
            

    def Activity11():
    #print Marvelous 10 times

        for x in range (1,20):
            print("Marvelous")
            print("Hi!")
    

    def Activity12():
        for x in range(10,1,-1):
            print(x)

    def Activity13():

        Factorial = 1
        factor= eval(input(f"Enter a number:"))
        for x in range (factor, 0,-1):
         factor *= x
        
        print (factor)


    for x in range (1,6):
        for z in range (1,x+1):
            print (" ",end=" ")
        
        for y in range (6,x,-1):
            print ("*",end= " ")
        
        for a in range (5,x,-1):
            print ("*",end= " ")
        print ()
        
    def Activity14():
        #for  x in range 

        for x in range (1, 15):
            #print (x, end= "+")
            print(x, end= "")
            for y in range (1,15):
                print("*", end= "")
            print("\n")
        
        for x in range (0,10):
            print("@", end= "")
            for y in range (0,10):
                print(x, end= "")
            print("")

    def Activity15():
        for x in range (0,11):
            print(x,"\t", end= " ")
        for y in range (0,x):
            print("*", end= " ")
        print()
        
        
        for x in range (10,0,-1):
            for y in range (0, x):
                print(" * ", end= " ")
            print()

    def Activity16():
        for x in range (1,6):
            for y in range(1,x+1):
                print(" ", end=" ")
            for z in range (6,x,-1):
                print("*", end=" ")
            for a in range (6,x,-1):
                print ("*", end=" ")
            print()
        
    def Activity17():
        #create a multiplication table

        column= eval(input("Enter number of columns-->"))
        for x in range (1,11):
            for y in range (1, column+1):
                print(f"{x} x {y} = {x*y}", end ="\t")
            print()

    def Activity18():
        #repeated triangle

        nt= eval(input("Enter number of triangle--> "))
        for x in range (1,5):
            for r in range (1,nt+1):
                for y in range (1,x+1):
                    print ("*", end=" ")
                for z in range (5,x,-1):
                    print (" ", end=" ")
            print()

    def Activity19():
        import os
        tuloy= True
        os.system('cls')

        while tuloy ==True:
            name = input("Please enter a name-->")
        
            if name.lower() =="stop":
                print("Program Terminated")
                break
    
            else:
                continue


    def Activity20():
            isContinue = True
            nt = 0
            import os
            while isContinue == True:
                ask =input (" Would you like to add another triangle (y/n) -->")
        
                if ask.lower() == "no":
                    print("Program Terminated")
                    break
                    isContinue =False
                elif ask.lower()=="yes":
                    os.system('cls')
                nt +=1
                for x in range(1,5):
                    for y in range (1, nt +1):
                        for z in range (1,x+1):
                            print("*", end=" ")
                        for a in range (5,x,-1):
                            print(" ", end=" ")
                        print(end=" ")
                    print()
                    continue
        
                else:
                    print("TRY AGAIN")
                    continue

    def Activity21():
    #keep on asking for a name until user types stop, once stop provide the number of names

        go =True
        count=0
        while go== True:
            name=input("Please enter a name:")
    
            if name.lower() =="stop":
                print("Loop has now stooped")
                print(f"You have entered {count} number of names")
                break
                go == False
            else:
                count+=1
                continue       
    isContinue =True

    while isContinue:
    
        print("\n\t SELECT FROM THE FOLLOWING CODE \n\t 1= PANG HELLO \n\t 2= DIVISION PROGRAM \n\t 3= ACT 2"
            "\n\t 4= ACT 4 \n\t 5= ACT 5 \n\t 6= ACT 6 \n\t 7= ACT 7 \n\t 8= ACT 8"
            "\n\t 9= ACT 9 \n\t 10= ACT 10 \n\t 11= ACT 12 \n\t 13= ACT 13 \n\t 14= ACT 14 \n\t 15= ACT 15"
            "\n\t 16= ACT 16 \n\t 17= ACT 17 \n\t 18= ACT 18 \n\t 19= ACT 19 \n\t 20= ACT 20"
            "\n\t 21= ACT 21 \n\t 22= EXIT")
    
        ask =input("\nWhich program would you like to run, select from the options above?")
        os.system("cls")

        if ask =="1":
            panghello()
            continue
        elif ask =="2":
            pass
        elif ask =="3":
            Activity2()
            continue
        elif ask =="4":
            Activity4()
            continue
        elif ask =="5":
            Activity5()
            continue
        elif ask =="6":
            Activity6()
            continue
        elif ask =="7":
            Activity7()
            continue
        elif ask =="8":
            Activity8()
            continue
        elif ask =="9":
            Activity9()
            continue
        elif ask =="10":
            Activity10()
            continue
        elif ask =="11":
            Activity11()
            continue
        elif ask =="12":
            Activity12()
            continue
        elif ask =="13":
            Activity13()
            continue
        elif ask =="14":
            Activity14()
            continue
        elif ask =="15":
            Activity15()
            continue
        elif ask =="16":
            Activity16()
            continue
        elif ask =="17":
            Activity17()
            continue
        elif ask =="18":
            Activity18()
            continue
        elif ask =="19":
            Activity19()
            continue
        elif ask =="20":
            Activity20()
            continue
        elif ask =="21":
            Activity21()
            continue
        elif ask =="22":
            print("\nProgram Terminated")
            break
        else:
            print("Invalid Choice")
            continue    
def Activity_23():
    print("\n-----------\nActivity 23\n-----------")
     
    def factorial(number):
        """ This Function again is for calculating Factorial Numbers, just provide a value, and it would automatincally compute the factorial"""
        fact = 1
        for x in range(number, 0, -1):
            fact *= 1
        return fact
    print(f"The factorial of 13 is {factorial(13)}")
def Activity_24():
    print("\n-----------\nActivity 24\n-----------")
    #MODULES

    from activity23 import factorial
    print(f"The factorial of 7 is {factorial(7)}")
def Activity_25():
    print("\n-----------\nActivity 25\n-----------")
    #LIST

    #fruit1 = "apples"
    #fruit2 = "banana"
    #fruit3 = "oranges"
    #furuit4 = "star apple"
    #fruit5 = "guyabano"

    #PYTHON LIST

    fruits = ["apples", "banana", "orange", "star apple", "guyabano"]

    print(fruits)

    #INDEXING / INDEX - Address / Location of an item inside a list
    #            0          1        2          3           4   
    #fruits = ["apples", "banana", "orange", "star apple", "guyabano"]

    print(f"\nMy favorite childhood fruit is {fruits[1]}\n")
    print(f"\nThe last item on the list is {fruits[-1]}\n")

    #Adding another Item on the list

    fruits.append("longgan")
    print(fruits)
    fruits.append("chico")
    print(fruits)

    #Inserting Item on specific index

    fruits.insert(3, "papaya")
    print(fruits)

    #Removing an Item on a list

    fruits.remove("longgan")
    print(fruits)

    while True:
        fruit = input("Do you wish to add more fruits(Yes/No):")

        if fruit.lower() == "no":
            print(fruits)
            break
        else:
            print("Fruit added to list!")
            continue
######################
def CC_1():
    print("\n-----------------\nCode challenge 1\n----------------- ")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b       * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b    * * * * *  \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b * * * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t  * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b   * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b       *")
def CC_2():
    print("\n-----------------\nCode challenge 2\n----------------- ")
    name = input("what is your name:")

    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t      * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b  * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b   * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b ------------- \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b  *  |Hi! "+name+"|   * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b ------------- \n\t\t\t\t\t\t\t\t\t\t\t\t\t  * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b\b\b\b     * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b       *")
def CC_3():
    print("\n-----------------\nCode challenge 3\n----------------- ")
    
    fullname = input("PLEASE INPUT YOUR FULLNAME : ")
    age = input("PLEASE INPUT YOUR AGE : ")
    birthmonth = input("PLEASE INPUT YOUR BIRTHMONTH : ")
    birthday = input("PLEASE INPUT THE DAY YOU WERE BORN : ")
    birthyear = input("PLEASE INPUT YOUR BIRTHYEAR : ")
    birthplace = input("PLEASE INPUT YOUR BIRTHPLACE : ")
    address = input("PLEASE INPUT YOUR COMPLETE ADDRESS : ")
    citizenship = input("PLEASE INPUT YOUR CITIZENSHIP: ")
    status = input("PLEASE INPUT YOUR CIVIL STATUS : ")
    father = input("PLEASE INPUT YOUR FATHER NAME : ")
    mother = input("PLEASE INPUT YOUR MOTHER NAME : ")
    email = input("PLEASE INPUT YOUR EMAIL ADDRESS: ")
    phonenumber = input("PLEASE INPUT YOUR MOBILE NUMBER : ")
def CC_4():
    print("\n-----------------\nCode challenge 4\n----------------- ")
    number1 = int(input("Enter 1st number: "))
    number2= int(input("Enter 2nd number: "))
    answer = number1 + number2
    answer = number1 - number2
    answer = number1 * number2
    answer = number1 / number2
    answer = number1 % number2
    answer = number1 ** number2
    answer = number1 // number2


    print("The sum of" , number1 , "and" , number2 ,"is" ,number1 + number2 )
    print("The difference of" , number1 , "and" , number2 ,"is" ,number1 - number2 )
    print("The product of" , number1 , "and" , number2 ,"is" ,number1 * number2 )
    print("The quotient of" , number1 , "and" , number2 ,"is" ,number1 / number2 )
    print("The exponent of" , number1 , "and" , number2 ,"is" ,number1 % number2 )
    print("The remainder of" , number1 , "and" , number2 ,"is" ,number1 ** number2 )
    print("The floor division of" , number1 , "and" , number2 ,"is" ,number1 // number2 )
######################
def CC_5():
    print("\n-----------------\nCode challenge 5\n----------------- ")
    bank_name = input("Please Input your Bank Account Name: ")
    pera = eval(input("Please Enter Amount to Deposit:       "))

    dp1 = pera // 1000
    n1 = pera % 1000
    dp2 = n1 // 500
    n2 = n1 % 500
    dp3 = n2 // 200
    n3 = n2 % 200
    dp4 = n3 // 100
    n4 = n3 % 100
    dp5 = n4 // 50
    n5 = n4 % 50
    dp6 = n5 // 20
    n6 = n5 % 20
    dp7 = n6 // 10
    n7 = n6 % 10
    dp8 = n7 // 5
    n8 = n7 % 5
    dp9 = n8 // 1


    print(dp1 , "- 1000") 
    print(dp2, "- 500")
    print(dp3 , "- 200")
    print(dp4 , "- 100")
    print(dp5 , "- 50") 
    print(dp6 , "- 20")
    print(dp7, "- 10")
    print(dp8 , "- 5") 
    print(dp9 , "- 1")
def CC_6():
    print("\n-----------------\nCode challenge 6\n----------------- ")
    Prelim = eval(input("Enter your Prelim grades :"))
    Midterm = eval(input("Enter your Midterm grades:")) 
    Final = eval(input("Enter your final grades :"))
    Quiz = eval(input("Enter your Quiz grades :"))
    Semi_final = eval(input("Enter your Semi-final grades :"))
    Project = eval(input("Enter your Project grades :"))

    Final_grade = (Prelim * .15) + (Midterm * .15) + (Final * .15) + (Semi_final * .15) + (Quiz * .25) + (Project * .15)

    if Final_grade > 100:
        print("You are overqualified passer")
    elif Final_grade >= 74:
         print("Congratulations!You passed the course!")
    else:
        print("Sorry,you failed!bawi next life")
def CC_7():
    print("\n-----------------\nCode challenge 7\n----------------- ")
    customer = input("What is the customer's name?")
    isCustomerAge = eval(input("What is the customer's age?: "))
    hadGrocery = input("Have you done your groceries? (yes/no)> ")
    item = input("What item did you get? ")
    itemPrice = eval(input("How much is the Item? "))
    money = eval(input("How much would you like to pay?> "))
    taxed = itemPrice + (itemPrice * 0.123)
    total = taxed
    change = money - total

    if isCustomerAge >= 60:
        print("They can have a senior discount of 5.2% from the total price.")
    else:
        print("They are not eligible for the senior discount.")
    print(f"Hi {customer}, you purchased a {item}, with a price of {itemPrice} plus 12.3% tax '{taxed}' \ntotal of {total} \nAmount Given {money}\nChange : {change}")   
def CC_8():
    print("\n-----------------\nCode challenge 8\n----------------- ")
    odd = 0
    even = 0
    sum = 0
    for x in range (1,11): 
        num = int(input(f"Enter number {x} : "))
        sum +- num
        if num % 2 == 0:
            even += num
        else:
            odd += num
        
    print(f"The sum of all numbers given is {sum}")
    print(f"The sum of all numbers given is {odd}")
    print(f"The sum of all numbers given is {even}")
######################
def CC_9():
    print("\n-----------------\nCode challenge 9\n----------------- ")
    z = eval(input("Enter a number: "))
    for x in range(z, 0,-1):
	    for y in range(z,x,-1):
		    print(" ", end=" ")
	    print("* " * x)
def CC_10():
    print("\n-----------------\nCode challenge 10\n----------------- ")
    for x in range(6, 0, -1):
        for y in range(1, x + 1):
            print(" ", end=" ")
        for z in range(6, x, -1):
            print("*", end=" ")
        for a in range(6, x, -1):
            print("*", end=" ")
        print()

    for x in range(1, 5):
        for y in range(1, x + 2):
            print(" ", end=" ")
        for z in range(5, x, -1):
            print("*", end=" ")
        for a in range(5, x, -1):
            print("*", end=" ")
        print()
def CC_11():
    print("\n-----------------\nCode challenge 11\n----------------- ")
    for x in range(1,5):
        for y in range(x,9):
            print(" ",end=" ")
        for a in range(1, x):
            print("*",end=" ")
        for b in range(0,x):
            print("*",end=" ")
    
        print()
    
    for x in range(4, 1, -1):
        for y in range(x,10):
            print(" ",end=" ")
        for a in range(1,x):
            print("*",end=" ")
        for b in range(2,x):
            print("*",end=" ")
        print()
def CC_12():
    print("\n-----------------\nCode challenge 12\n----------------- ")
    for x in range(7, 0, -1):
        for y in range(1, x + 1):
            print(" ", end=" ")
        for z in range(6, x, -1):
            print("*", end=" ")
        for a in range(5, x, -1):
            print("*", end=" ")
        print()
    for x in range(0, 4):
        for y in range(4, 0, -1):
            print(" ", end= " ")
        for z in range(1,1):
            print("*", end= " ")
        for a in range(3, 0, -1):
            print("*", end= " ")
        print()
######################
def CC_13():
    print("\n-----------------\nCode challenge 13\n----------------- ")
    for x in range(1,7):
        for y in range(6, x, -1):
            print(" ", end= " ")
        for z in range(x, 1, -1):
            print(z, end= " ")
        for a in range(1, x + 1):
            print(a, end= " ")
        print()
    for x in range(5, 0, -1):
        for y in range(5 - x + 1):
            print(" ", end=" ")
        for z in range(x, 0, -1):
            print(z, end=" ")
        for a in range(2, x + 1):
            print(a, end=" ")
        print()
def CC_14():
    print("\n-----------------\nCode challenge 14\n----------------- ")
    tuloy = True
    a = 0
    while tuloy == True:
        number = eval(input("Enter a number--->  "))
        if number == 0:
            print("Program Terminated")
            print(f"The total of the number you enter is {a}")
            break

        else:
            a += number
            continue
def CC_15():
    print("\n-----------------\nCode challenge 15\n----------------- ")
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        elif ask.lower() == "yes":
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        else:
            print("INVALID ANSWER it's only (yes/no)")
            continue
def CC_16():
    print("\n-----------------\nCode challenge 16\n----------------- ")
    def denomination(amount):
        print("\nDenomination Breakdown:")
        A = amount // 1000
        AA = amount % 1000

        B = AA // 500
        BB = AA % 500

        C = BB // 200
        CC = BB % 200

        D = CC // 100
        DD = CC % 100

        E = DD // 50
        EE = DD % 50

        F = EE // 20
        FF = EE % 20

        G = FF // 10
        GG = FF % 10

        H = GG // 5
        HH = GG % 5

        I = HH // 1

        print("1000---", A)
        print("500----", B)
        print("200----", C)
        print("100----", D)
        print("50-----", E)
        print("20-----", F)
        print("10-----", G)
        print("5------", H)
        print("1------", I)


    accounts = {}

    def create_account():
        username = input("Enter a username: ")
        if username in accounts:
            print("Account already exists!")
        else:
            accounts[username] = 0
            print(f"Account created successfully for {username}.")


    def deposit():
        username = input("Enter your username: ")
        if username in accounts:
            try:
                amount = int(input("Enter amount to deposit : "))
                if amount > 0:
                    accounts[username] += amount
                    print(f"Deposited {amount} successfully. New balance: {accounts[username]}")
                    denomination(amount)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def withdrawal():
        username = input("Enter your username: ")
        if username in accounts:
            try:
                amount = int(input("Enter amount to withdraw (whole numbers only): "))
                if 0 < amount <= accounts[username]:
                    accounts[username] -= amount
                    print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                    denomination(amount)
                else:
                    print("Insufficient funds or invalid amount!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def check_balance():
        username = input("Enter your username: ")
        if username in accounts:
            print(f"Your balance: {accounts[username]}")
        else:
            print("Account not found!")


    def options():
        while True:
            print("\nBanking System")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                create_account()
            elif choice == '2':
                deposit()
            elif choice == '3':
                withdrawal()
            elif choice == '4':
                check_balance()
            elif choice == '5' or "Exit":
                print("Thank you for using the Banking System!")
                break
            else:
                print("Invalid option. Please try again.")

    options()
######################
def exit_user():
    while True:
        ask = input("\n\nDO YOU WANT TO EXIT THE PROGRAM? (yes/no): ")
        if ask.lower() == "yes":
            print("\nLoading:")
            
            #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
            animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
            
            for i in range(len(animation)):
                time.sleep(0.2)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
            print("\nDONE!")
            print("\n==========================================\nTHANK YOU FOR USING THE PROGRAM. GOODBYE!.\n==========================================\n")
            sys.exit()
        elif ask.lower() == "no":
            print("\nContinuing the Program...")
            main_menu()
        else:
            print("\nInvalid Input. Please type 'yes' or 'no'.")

user_input()
main_menu()