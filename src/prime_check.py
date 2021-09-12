import os
import os.path
import math
import time

invalid_number = False
invalid_restart = False
list = []

def clear(): #CLEAR CONSOLE
    os.system("cls")

def defRange(): #USER DEFINES RANGE FOR TESTING
    global minimum, maximum, str_minimum, str_maximum, invalid_number

    print("Python Prime Number Finder")
    print("")
    if invalid_number == True:
        print("ERROR: INVALID INPUT DETECTED")
        print("")
    print("Enter a minimum number to check:")
    str_minimum = str(input())

    if str_minimum.isnumeric():
        invalid_number = False
        minimum = int(str_minimum)

        print("Enter a maximum number to check:")
        str_maximum = str(input())
        if str_maximum.isnumeric() and int(str_maximum) > int(str_minimum):
            invalid_number = False
            maximum = int(str_maximum)
            clear()
            print("Testing " + str_minimum + " -> " + str_maximum)
            primeSolver()
        else:
            invalid_number = True
            clear()
            defRange()
    else:
        invalid_number = True
        clear()
        defRange()

def primeSolver(): #MAIN MATH, NESTED FOR LOOP
    for value in range(minimum, maximum + 1):
        if value > 1:
            for i in range(2, value):
                if (value % i) == 0:
                    break
            else:
                list.append(value)
    print("Prime numbers found in range from " + str_minimum + " -> " + str_maximum)
    print(list)
    output()


def output(): #OUTPUT DATA TO EXTERNAL FILE
    print("\n" + "Saving prime numbers to file...") #INFORM USER FILE IS BEING CREATED
    fileName = time.strftime("%Y%m%d" + "-" + "%H%M%S")
    outNum = "\n".join(str(n) for n in list)
    
    f = open(fileName + ".txt", "w")
    f.write("Prime numbers found in range from " + str_minimum + " -> " + str_maximum)
    f.write("\n" + outNum)

    f.close()

    print("Done" + "\n") #INFORM USER DATA IS SAVED TO FILE, OUTPUTS AFTER FILE CLOSES

    restart()

def restart(): #USER INPUT TO RESTART PROGRAM
    global invalid_restart

    print("Would you like to restart the program?")
    if invalid_restart == True:
        print("")
        print("Please enter 'yes' or 'no'")
    
    str_restart = str(input()).lower()

    if str_restart == "yes":
        invalid_restart = False
        invalid_number = False
        list.clear()
        clear()
        defRange()
    elif str_restart == "no":
        return
    else: #ERROR MESSAGE IF INPUT NOT RECOGNIZED
        invalid_restart = True
        clear()
        print("ERROR: INPUT NOT RECOGNIZED")
        print("")
        restart()

defRange()