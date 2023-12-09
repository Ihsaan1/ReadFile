

def writeText(line):
    with open("text.txt", "w") as file:
        for x in range(10):
            file.write(line)
        
##def checkText():
##    with open("mysteryText.txt", "r") as file:
##        for line in file:
##            writeText(line)


##checkText()
                

def printText():
    with open("test.txt", "r") as file:
        for line in file:
            writeText(line)
               
            

#printText()

def printFileWords(file):
    try:
        with open(file, "r") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("File not found")




#def printNumber(number):
    total = addNumbers("2", "4")
    print("the total is", total)

def addNumbers(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    
    total = number1 + number2
    return total

def printName(name):
    name = name + "a"
    return name

#name = printName("ihsaan")
#print(name)




#printFileWords("filename123213213.txt")

def numberAdd10(number):
    try:
        number = number + 10
        #print(number)
    except TypeError:
        print("Number not found")
    except ZeroDivisionError as e:
        print("Calculation not valid", e)
    return number





def countWord(word):
    counter = 0
    with open("test.txt", "r") as file:
        for line in file:
            if word in line:
                counter = counter + 1
    return counter

number = countWord("Rome")
number = numberAdd10(number)
print(number)


            
