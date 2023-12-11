import re
import numpy as np
import math
import matplotlib.pyplot as plt
def checking(in1):
    if in1 == 'log':
        log = input("Enter a logarithmic equation: ")
        log = log.replace(' ','')
        while (log == ''):
            print("Don't leave the prompt empty.")
            log = input("Enter a logarithmic equation: ")
            log = log.replace(' ','')
        placement = log.find('log')
        count = 0
        print(log)
        if log[0] != 'l':
            try: # what the log is being multiplied by
                int(log[:placement])
            except ValueError:
                print("Make sure no other variables than x are being used")
                checking('log')
        one = int(log.find('(')) + 1
        two = int(log.find(')'))
        parenthesis = log[one:two]
        placement = int(parenthesis.find('x'))
        if '+' in parenthesis[placement:two]:
            placement2 = parenthesis.find('+')
            if parenthesis[0] == 'x':
                try:
                    int(parenthesis[placement2:])
                except ValueError:
                    print("make sure x is the only variable being used. 1")
                    checking('log')
            elif parenthesis[0] != 'x':
                try: # within the parenthesis 
                    int(parenthesis[:placement])
                    int(parenthesis[placement2:])
                except ValueError:
                    print("Make sure x is the only variable being used. 2")
                    checking('log')
        elif '-' in parenthesis[placement:two]:
            placement2 = parenthesis.find('-')
            if log[one] == 'x':
                try:
                    int(parenthesis[placement2:])
                except ValueError:
                    print("make sure x is the only variable being used. 3")
                    checking('log')
            elif log[one] != 'x':
                try: # within the parenthesis 
                    int(parenthesis[:placement])
                    int(parenthesis[placement2:])
                except ValueError:
                    print("Make sure x is the only variable being used.4 ")
                    checking('log')
        elif '-' not in parenthesis[placement:] and '+' not in parenthesis[placement:]:
            if log[one] == 'x':
                pass
            elif log[one] != 'x':
                int(parenthesis[:placement])
        two = two + 1
        placement3 = int(log.find('+', two )) + 1
        placeholder = log.find(')')
        vertical  = log[placeholder:]
        print(vertical)
        if '+' not in vertical and '-' not in vertical:
            pass
        elif '+' in vertical or '-' in vertical:
            if '+' in vertical:
                placeholder = vertical.find('+')
                try: # vertical shift
                    int(vertical[placeholder:])
                except ValueError:
                    print("Make sure x is the only variable being used.")
                    checking('log')
            elif '-' in vertical:
                placeholder = vertical.find('-')
                try:
                    int(vertical[placeholder:])
                except ValueError:
                    print("Make sure x is the only variable being used.")
                    checking('log')
          
        if ('+' not in parenthesis[placement:] and '-' not in parenthesis[placement:]) and log[one] == 'x':
            return parenthesis, None, None, log
        elif ('+' not in parenthesis[placement:] and '-' not in parenthesis[placement:]) and log[one] != 'x':
            return( parenthesis, placement3, None, log)
        elif ('-' in parenthesis[placement:] or '+' in parenthesis[placement:]) and log[one] == 'x':
            return( parenthesis, placement2, None, log)
        elif ('-' in parenthesis[placement:] or '+' in parenthesis[placement:]) and log[one] != 'x':
            return (parenthesis, placement3, placement2, log)
                        
def settings(in1):
    decision = in1
    if  decision.lower() == 'yes':
        #input validation. 
        while True: 
            try:
                xmini = float(input("X-min: ")) # minimum value for x-axis
                break
            except ValueError:
                print("Only input numbers.")
                pass
        while True: 
            try:
                xmaxi = float(input("X-max: ")) # max value for x-axis
                xmaxi += 0.001 # the np.arrange function stops one step before what the end is set as, so this is just to have it end at the correct number.
                break
            except ValueError:
                print("Only input numbers.")
                pass
        while True: 
            try:
                ymini = float(input("Y-min: ")) # min value for y-axis
                break
            except ValueError:
                print("Only input numbers.")
                pass
        while True: 
            try:
                ymaxi = float(input("Y-max: ")) # max value for y-axis
                break
            except ValueError:
                print("Only input numbers.")
                pass
        return(xmini, xmaxi, ymini, ymaxi)
    elif decision.lower() == 'no':
        print("Default settings will remain.")
        # default values below
        xmini = -10
        xmaxi = 10.001
        ymini = -10
        ymaxi = 10
        return(xmini, xmaxi, ymini, ymaxi)




def calculator():
    while True:
        print("Please type in the math operation you would like to complete:")
        print(" * for multiplication")
        print(" / for division")
        print(" + for addition")
        print(" - for subtraction")
        print(" ** for exponents")
        print(" # for square root")
        # Variables used throughout the calculator
        response = input('Enter an equation: ')
        sortedlist = re.split('(\W+)', response) #splits a string using any nonword character as the spots to split up the string.
        f = ''
        placeholder = ''
        for i in sortedlist:
            # goes through the list sets any arithemtic operation symbol as the placeholder variable.
            if '*' in i:
                placeholder = '*'
            elif '/' in i:
                placeholder = '/'
            elif '+' in i:
                placeholder = '+'
            elif '-' in i:
                placeholder = '-'
            elif '^' in i:
                placeholder = '^'
            elif '#' in i:
                placeholder = '#'
            else:
                # sets only the first number in the users requested equation as the f varaible.
                try: #tests out if the users input works with the code below. 
                    if f == '':
                        f = float(i)
                except ValueError:  #if the users input causes an error, it tells the user the problem and reruns the program to allow the user to fix their mistake.
                    print("Program can only process numbers and arithmetic operation symbols ")
                    calculator()
                else:
                    # performs the arithemtic operation and sets the result equal to f.
                    try:     #the try and except code blocks conduct a form of input validation. 
                        if placeholder == '*':
                            f *= float(i)
                        elif placeholder == '/':
                            f /= float(i)
                        elif placeholder == '+':
                            f += float(i)
                        elif placeholder == '-':
                            f -= float(i)
                        elif placeholder == '^':
                            f **= float(i)
                        elif placeholder == '#':
                            pass
                    except ValueError: 
                        print(" Program can only process numbers and arithmetic operation symbols ")
                        calculator()
        print("The result is", f)
        while True: #the while True code blocks conducts input validation before any of the code afterward runs. 
            restart = input("Would you like do another calculation? ")
            if restart.lower() == 'yes' or restart.lower() == 'no':
                break
            else:
                print("Respond with yes or no.")
                pass
        if restart.lower() == 'yes':
            calculator()
        elif restart.lower() == 'no':
            while True:
                otheroptions = input("Would you like to use another function of the graphing calculator?")
                if otheroptions.lower() == 'yes' or otheroptions.lower() == 'no':
                    break
                else:
                    print("Respond with yes or no.")
            if otheroptions.lower() == 'yes':
                graphingcalc()
            if otheroptions.lower() == 'no':
                print("Thank you for using J.G's Graphing Calculator.")
                break
            else:
                print("Only respond with yes or no please")


def graphing():
    while True: #continously runs the program until the user responds to the end prompt with no.
        while True:   
            print("Currently supported equation types below: ")
            print("Linear")
            print("Quadratic")
            print("Log (shorthand for logarithmic)")
            equationtype = input("Enter type of equation: ")
            #input validation below.
            if equationtype.lower() == 'linear' or equationtype.lower() == 'quadratic' or equationtype.lower() == 'log': 
                break
            else:
                print("Please choose an option from the list of supported equation types.")
                pass
        if equationtype.lower() == 'linear':
            #input validation
            while True: 
                print("The default settings for range of y-axis and x-axis are listed below.")
                print("X-axis range: -10 to 10")
                print("Y-axis range: -10 to 10")
                choice = input("Would you like to change the ranges for the x-axis and y-axis? ")
                if choice.lower() == 'yes' or choice.lower() == 'no':
                    break
                else:
                    print("Please respond with yes or no.")
                    pass
            xmini,xmaxi,ymini,ymaxi = settings(choice)
                
            while True: #input validation
                try:
                    slope = float(input('enter slope of your equation: '))
                    break
                except ValueError:
                    print("Only input numbers.")
                    pass
            while True: #input validation
                try:
                    yintercept = float(input("Enter y-intercept of your equation: "))
                    break
                except ValueError:
                    print("Only input numbers.")
            xintercept = 0
            xintercept -= yintercept
            xintercept /= slope
            xaxis = []
            yaxis = []
            for i in np.arange(xmini,xmaxi +.01 ,.01): # sets the domain for the x-xaxis
                  xaxis += [i]
            for i in xaxis: #puts all the X values through the slope-intercept form with the slope and y-intercept that the user input.
                 yaxis += [(slope * i) + yintercept]
            img = plt.plot(xaxis, yaxis) #plots a line graph with the xaxis and yaxis data. 
            plt.vlines( x = 0, ymin = ymini, ymax = ymaxi) #Plots the x-axis line on the graph.
            plt.hlines(y = 0, xmin = xmini , xmax = xmaxi) # plots the y-axis line on the graph.
            plt.axis([xmini,xmaxi,ymini,ymaxi]) # sets the limits to the graph window
            plt.text(xintercept, 0, (xintercept,0), fontsize = 'xx-large', fontweight='extra bold') # inputs the x-intercept coordinate next to the x-intercept.
            if float(yintercept) > 0: # if the y-intercept is positive, the equation is presented in the form of y = mx+b.
                print("The equation is: ", slope,'x +',yintercept)
                print("The X-intercept is", '(',xintercept,',',0.0,')', ' and the Y-intercept is','(',yintercept,',',0.0,')')
                print("Close the graph window to continue.") 
            elif float(yintercept) < 0: # if the y-intercept is negative, the equation is presented in the form of y = mx-b
                print("The equation is: ",slope,'x -',yintercept)
                print("The X-intercept is", '(',xintercept,',',0.0,')', 'and The Y-intercept is',',','(',yintercept,',',0.0,')')
                print("Close the graph window to continue.")
            elif float(yintercept) == 0: # if y-intercept is 0, the equation is presented in the form of y = mx
                print("The equation is: ",slope,'x')
                print("The X-intercept is", '(',xintercept,',',0.0,')', 'and The Y-intercept is',',','(',yintercept,',',0.0,')')
                print("Close the graph window to continue.")
            plt.show()
        elif equationtype.lower() == 'quadratic':
            # Input Validation
            while True: 
                print("The default settings for range of y-axis and x-axis are listed below.")
                print("X-axis range: -10 to 10")
                print("Y-axis range: -10 to 10")
                choice = input("Would you like to change the ranges for the x-axis and y-axis? ")
                if choice.lower() == 'yes' or choice.lower() == 'no':
                    break
                else:
                    print("Please respond with yes or no.")
                    pass
            xmini,xmaxi,ymini,ymaxi = settings(choice)

            print("Standard quadratic equation format is: Ax^2 + Bx + C")
            while True: # input validation
                try:
                    a = float(input("Enter value for A: "))
                    break
                except ValueError:
                    print("Only enter numbers")
            while True:
                try:
                    b = float(input("Enter value for B: "))
                    break
                except ValueError:
                    print("Only enter numbers")
            while True:
                try:
                    c = float(input("Enter value for C: "))
                    break
                except ValueError:
                    print("Only enter numbers")
            
            if ((b ** 2) - 4 * (a * c) ) < 0: # accounts for when the part of the quadratic equation that is being square rooted comes out to a negative.
                negative = -1
                # the code below is to account for x-intercepts containing unreal numbers but the positive version of the original number can be square rooted. 
                if math.sqrt(((b ** 2) - 4 * (a * c)) / negative) == int(math.sqrt(((b ** 2) - 4 * (a * c)) / negative)):
                    negative = -1
                    unrealnumber = ((b ** 2) - 4 * (a * c)) / negative
                    unrealnumber = str(((math.sqrt(((b ** 2) - 4 * (a * c)) / negative)))) + 'i'
                    xintercept1 = str(-(b)) + '+' + unrealnumber
                    xintercept1 = xintercept1 + ' / ' + str(2 * a)
                    xintercept2 = str(-(b)) + '-' + unrealnumber
                    xintercept2 = xintercept2 + ' / ' + str(2 * a)
                # the code below is to account for the x-intercepts that contain unreal numbers but the positive version of the original number can't  be square rooted
                elif math.sqrt(((b ** 2) - 4 * (a * c)) / negative) != int(math.sqrt((((b ** 2) - 4 * (a * c))) / negative)):
                    negative = -1
                    unrealnumber = ((b ** 2) - 4 * (a * c)) / negative
                    unrealnumber = '_/(' + str((((b ** 2) - 4 * (a * c)) / negative)) + ')' + 'i'
                    xintercept1 = str(-(b)) + '+' + unrealnumber
                    xintercept1 = xintercept1 + ' / ' + str(2 * a)
                    xintercept2 = str(-(b)) + '-' + unrealnumber
                    xintercept2 = xintercept2 + ' / ' + str(2 * a)
            elif ((b**2) - 4 * (a * c)) >= 0: # accounts for when the part of the quadratic equation that is being square rooted comes out to a positive
                # The code below accounts for when the part of the quadratic equation that is being squared rooted doesn't come out to a perfect square root.
                if ((math.sqrt((b ** 2) - 4 * (a * c)))) != (int((math.sqrt((b ** 2) - 4 * (a * c))))):
                    oddnumber = '_/(' + str((b ** 2) - 4 * (a * c)) + ')'
                    xintercept1 = str(-(b)) + '+' + oddnumber
                    xintercept1 = xintercept1 + ' / ' + str(2 * a)
                    xintercept2 = str(-(b)) + '-' + oddnumber
                    xintercept2 = xintercept2 + ' / ' + str(2 * a)
                # The code below accounts for when the part of the quadratic equation that is being squared rooted does come out to a perfect square root.
                elif ((math.sqrt((b ** 2) - 4 * (a * c)))) == (int((math.sqrt((b ** 2) - 4 * (a * c))))):
                    xintercept1 = -(b) + math.sqrt( (b**2) - (4 * (a * c)))
                    xintercept1 = xintercept1 / (2 * a)
                    xintercept2 = -(b) - math.sqrt( (b**2) - (4 * (a * c)))
                    xintercept2 = xintercept2 / (2 * a)
                
            if xintercept1 == xintercept2:  # if therse only one x-intercept, the code below runs
                print("The X-intercept is", '(',xintercept1,',',0.0,')')
            elif xintercept1 != xintercept2: # if there's two x-intercepts, the code below runs.
                print("The X-Intercepts are", '(',xintercept1,',',0.0,')', 'and',' (',xintercept2,',',0.0,')')
            print("Close the graph window to continue.") 
            xaxis = []
            yaxis = []
            for i in np.arange(xmini,xmaxi,.001): # sets the domain for the x-xaxis
                xaxis += [float(i)]
            for i in xaxis:
                yaxis += [((a * (i**2))) + (b * i) + c] # puts the x-values through the quadratic equation formula with the inputs that the user provided
            img = plt.plot(xaxis, yaxis) # plots a line graph with the xaxis and yaxis data.
            plt.vlines( x = 0, ymin = ymini, ymax = ymaxi) # plots the x-axis line on the graph
            plt.hlines(y = 0, xmin = xmini, xmax = xmaxi) # plots the y-axis line on the graph
            plt.axis([xmini,xmaxi,ymini,ymaxi]) # sets the limits to the graph window.
            plt.show() 
        elif equationtype.lower() == "log":
            while True: 
                print("The default settings for range of y-axis and x-axis are listed below.")
                print("X-axis range: -10 to 10")
                print("Y-axis range: -10 to 10")
                choice = input("Would you like to change the ranges for the x-axis and y-axis? ")
                if choice.lower() == 'yes' or choice.lower() == 'no':
                    break
                else:
                    print("Please respond with yes or no.")
                    pass
            xmini,xmaxi,ymini,ymaxi = settings(choice)
            while True:
                base = input("Enter base: ")
                try:
                    base = int(base)
                    break
                except ValueError:
                    print("Only enter numbers.")
                    pass
            parenthesis,placement,placement2,log = checking('log')
        one = log.find('(') + 1
        two = log.find(')')
        placement = int(parenthesis.find('x'))
        placement2 = parenthesis.find('+')
        placement3 = log.find('+', two)
        placement4 = log.find('-', two)
        placement5 = parenthesis.find('-')
        if log[one] == 'x' and ('+' in parenthesis or '-' in parenthesis):
            if '-' in parenthesis[placement:] and ('+' and '-') not in log[two:]:
                xintercept = 1 + float(parenthesis[placement5:])
            elif '+' in parenthesis[placement:] and ('+' and '-') not in log[two:]:
                xintercept = 1 - float(parenthesis[placement2:])
            elif '-' in parenthesis[placement:] and '+' in log[two:]:
                xintercept = (base ** (-1 * int(log[placement3:]))) + float(parenthesis[placement5:])
            elif '+' in parenthesis[placement:] and '-' in log[two:]:
                xintercept = (base ** int(log[placement4:])) - float(parenthesis[placement2:])
            elif '-' in parenthesis[placement:] and '-' in log[two:]:
                xintercept = (base ** int(log[placement4:])) + float(parenthesis[placement5:])
            elif '+' in parenthesis[placement:] and '+' in log[two:]:
                xintercept = (base ** (-1 * int(log[placement3:]))) - float(parenthesis[placement2:])
        elif log[one] == 'x' and ('+' not in parenthesis[placement:] and '-' not in parenthesis[placement:]) and (('+' and '-') not in log[two:]):
            xintercept = 1
        elif log[one] != 'x' and ('+'in parenthesis[placement:] or '-' in parenthesis[placement:]):
            if '+' in parenthesis[placement:] and ('+' and '-') not in log[two:]:
                xintercept = ( 1 - float(parenthesis[placement2:])) / float(parenthesis[:placement])
            elif '-' in parenthesis[placement:]  and ('+' and '-') not in log[two:]:
                xintercept = ( 1 + float(parenthesis[placement2:])) / float(parenthesis[:placement])
            elif '-' in parenthesis[placement:] and '+' in log[two:]:
                xintercept = ((base ** (-1 * int(log[placement3:]))) + float(parenthesis[placement5:])) / float(parenthesis[:placement])
            elif '+' in parenthesis[placement:] and '-' in log[two:]:
                xintercept = ((base ** int(log[placement4:])) - float(parenthesis[placement2:])) / float(parenthesis[:placement])
            elif '-' in parenthesis[placement:] and '-' in log[two:]:
                xintercept = ((base ** int(log[placement4:])) + float(parenthesis[placement5:])) / float(parenthesis[:placement])
            elif '+' in parenthesis[placement:] and '+' in log[two:]:
                xintercept = ((base ** (-1 * int(log[placement3:]))) - float(parenthesis[placement2:])) / float(parenthesis[:placement])
        elif log [one] != 'x' and ('+' not in parenthesis[placement:] and '-' not in parenthesis[placement:]):
            if ('+' and '-') not in log[two:]:
                xintercept  = 1 / float(parenthesis[:placement])
            elif '+' in log[two:]:
                xintercept = (base ** (-1 * int(log[placement3:]))) / float(parenthesis[:placement])
            elif '-' in log[two:]:
                xintercept = (base ** int(log[placement3:])) / float(parenthesis[:placement])
                 
        xaxis = []
        yaxis = []
        for i in np.arange(xmini,xmaxi,.001):
            xaxis += [float(i)]
        partial = ''
        partial += ', '
        partial += str(base)
        partial += ')'
        log = log.replace(')', partial)
        if log[0] != 'l':
            log = log.replace('log', '*math.log')
        elif log[0] == 'l':
            log = log.replace('log', 'math.log')
        if parenthesis[0] == 'x':
            log = log.replace('x', 'i')
        elif parenthesis[0] != 'x':
            log = log.replace('x', '*i')
        for i in xaxis:
            try:
                yaxis += [eval(log)]
            except ValueError:
                yaxis += [None]
        print("The X-Intercept is ", '(', xintercept, ',', '0)')
        img = plt.plot(xaxis, yaxis) 
        plt.vlines( x = 0, ymin = ymini, ymax = ymaxi) 
        plt.hlines(y = 0, xmin = xmini , xmax = xmaxi) 
        plt.axis([xmini,xmaxi,ymini,ymaxi]) 
        plt.text(xintercept, 0, (xintercept,0), fontsize = 'xx-large', fontweight='extra bold')
        plt.show()
        
        while True: #input validation
            restart = input("Would you like to graph another equation? ")
            if restart.lower() == 'yes' or restart.lower() == 'no':
                break
            else:
                print("Respond with yes or no.")
                
        if restart.lower() == 'yes': #runs the calculation program if the user wants to use it again
            graphing()
        elif restart.lower() == 'no': 
            while True:
                otheroptions = input("Would you like to use another function of the graphing calculator?")
                if otheroptions.lower() == 'yes' or otheroptions.lower() == 'no': # input validation 
                    break
                else:
                    print("Respond with yes or no.")
            if otheroptions.lower() == 'yes': #if the user wants to use one of the other functions, the computer runs the graphingcalc funciton to allow them to choose another.
                graphingcalc()
            if otheroptions.lower() == 'no': # if the user doesn't want to use any function, it closese the program.
                print("Thank you for using J.G's Graphing Calculator.")
                break
        
            
            

def graphingcalc():
    #introduction menu to the graphing calculator.
    print("Welcome to J.G's Graphing Calculator.")
    print("The available functions are listed below.")
    print("Graphing")
    print("Calculation")
    print("Be precise with your spelling when choosing the funciton you'd like to use.")
    while True: #input validation
        decision = input("Which function would you like to use today? ")
        if decision.lower() == 'graphing' or decision.lower() == 'calculation':
            break
        else:
            print("Choose from the provided list of functions")
            pass
    if decision.lower() == 'graphing': #runs graphing program if the user chooses graphing.
        graphing()
    elif decision.lower() == 'calculations': # runs calculation program if the user chooses calculations
        calculator()
        
          
def main():
    graphingcalc()

if __name__ == '__main__': # runs the main function when the user runs the script. 
    main()
        
            
        




