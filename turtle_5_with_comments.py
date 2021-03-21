def add():
    import random
    #local variables for addition
    number_one = int()
    number_two = int()
    answer = int()
    response = str()
    problem = str()
    response = "y"
    turtle.penup()
    #while loop to repeat addition exercise/return to main
    while response != "n":
        number_one = random.randrange(0,100)
        number_two = random.randrange(0,100)
        set()
        turtle.penup()
        speak(str(number_one)+ " + " +str(number_two), "center", 0, 0)
        turtle.goto(0,-25)
        answer = user_input_num("Answer", "What is your answer?")
        correct = number_one + number_two
        #repsonse if user input is incorrect
        while answer != correct:
            set()
            turtle.penup()
            speak("That is not correct!  Try again!", center, 0, 25)
            speak(str(number_one)+ " + " +str(number_two), "center", 0, 0)
            answer = user_input_num("Answer", "What is your answer?")
        #repsonse if user input is correct
        speak("Good work!  That is correct!", "center", 0, -50)
        #prompt to play again or be returned to main game screen for selection
        speak("Do you want to go again, y or n?", "center", 0, -75)
        turtle.goto(0,-100)
        response = user_input_text('Good job!', 'Play again, y or n?')
    main()

def subtract():
    import random
    #local variables for subtration exercise
    number_one = float()
    number_two = float()
    answer = float()
    response = str()
    response = "y"
    #while loopt repeat subration exercise/return to main
    while response != "n":
        number_one = random.randrange(0,100)
        number_two = random.randrange(0,100)
        set()
        turtle.penup()
        #prompt with random number selection
        if number_one >= number_two:
            speak(str(number_one)+ " - " +str(number_two), "center", 0, 0)
            turtle.goto(0,-25)
            answer = user_input_num("Answer", "What is your answer?")
            correct = number_one - number_two
            #prompt if user input incorrect
            while answer != correct:
                set()
                turtle.penup()
                speak("That is not correct!  Try again!", "center", 0, 25)
                speak(str(number_one)+ " - " +str(number_two), "center", 0, 0)
                turtle.goto(0,-25)
                answer = user_input_num("Answer", "What is your answer?")
            #prompt if user input correct
            speak("Good work!  That is correct!", "center", 0, -25)
            turtle.goto(0,-50)
            #prompts to reapet or return to main
            speak("Do you want to go again, y or n?", "center", 0, -50)
            turtle.goto(0,-75)
            response = user_input_text('Good job!', 'Play again, y or n?')
        #pompt with random number selection
        else:
            speak(str(number_two)+ " - " +str(number_one), "center", 0, 0)
            turtle.goto(0,-25)
            answer = user_input_num("Answer", "What is your answer?")
            correct = number_two - number_one
            #prompt if user input incorrect
            while answer != correct:
                set()
                turtle.penup()
                speak("That is not correct!  Try again!", center, 0, 25)
                turtle.goto(0,0)
                speak(str(number_two)+ " - " +str(number_one), "center", 0, 0)
                turtle.goto(0,-25)
                answer = user_input_num("Answer", "What is your answer?")
            #prompt if user input correct
            speak("Good work!  That is correct!", "center", 0, -25)
            turtle.goto(0,-50)
            #prompt to repeat loop or return to main
            speak("Do you want to go again, y or n?", "center", 0, -50)
            turtle.goto(0,-75)
            response = user_input_text('Good job!', 'Play again, y or n?')
    main()
        
def shapes():
    import turtle
    import random
    import time
    #variables
    ArrayS=["circle","square","triangle","rectangle"]
    counter=int(1)
    shape=str()
    answer=str()
    #set up
    set()
    speak("Welcome to the guessing shapes game", "center" ,0,0)
    turtle.goto(0,-25)
    time.sleep(2)
    set()
    speak("This game will have you name the shapes you see", "center" ,0,0)
    turtle.goto(0,-25)
    time.sleep(2)
    set()
    #main coding area
    while counter!=0:
        index=random.randint(0,3)
        shape=ArrayS[index]
        turtle.pensize(10)
        if shape=="circle":
            turtle.fillcolor("green")
            #draw a circle using turtle
            turtle.penup()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(150)
            turtle.end_fill()
            #ask what shape it is
            counter = shape_answer(shape)
            
        elif shape=="square":
            #draw a square using turtle
            turtle.fillcolor("blue")
            turtle.penup()
            turtle.goto(-150,150)
            turtle.pendown()
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(300)
                turtle.right(90)
            turtle.end_fill()
            #ask what shape it is
            counter = shape_answer(shape)
                                
        elif shape=="triangle":
            #draw a square using turtle
            turtle.fillcolor("red")
            turtle.penup()
            turtle.goto(-190,-100)
            turtle.pendown()
            turtle.begin_fill()
            for i in range(3):
                turtle.forward(400)
                turtle.left(120)
            turtle.end_fill()
            #ask what shape it is
            counter = shape_answer(shape)
                
        elif shape=="rectangle":
            #draw a square using turtle
            turtle.fillcolor("cyan")
            turtle.penup()
            turtle.goto(-125,200)
            turtle.pendown()
            turtle.begin_fill()
            for i in range(2):
                turtle.forward(250)
                turtle.right(90)
                turtle.forward(400)
                turtle.right(90)
            turtle.end_fill()
            counter = shape_answer(shape)
    main()
                
def shape_answer(shape):
        answer=user_input_text("Answer","What Shape is this? (lowercase only):   ")
        #make inner loop to end loop or keep playing or if answer is wrong
        if answer!=shape:
            set()
            turtle.penup()
            speak("That is not correct!  Do you want to try again?", "center", 0, 0)
            turtle.goto(0,-25)
            inLoopAns=user_input_text("Continue?",'Play again, y or n?')
            if inLoopAns=="n":
                counter=0
            elif inLoopAns=="y":
                turtle.reset()
                counter=1
        elif answer==shape:
            set()
            turtle.penup()
            speak("That is correct!  Do you want to try again?", "center", 0, 0)
            turtle.goto(0,-25)
            inLoopAns=user_input_text("Continue?", 'Play again, y or n?')
            if inLoopAns=="n":
                counter=0
            elif inLoopAns=="y":
                turtle.reset()
                counter=1
        return(counter)
                        
def GetColor():
    import random
    #local variables
    radius = int()
    colors = ['red', 'blue' , 'yellow','green','purple','orange']
    pen_size = int()
    index_num = int()
    guess = str()
    answer = str()
    #starting location prompt
    set()
    speak('Guess these colors!','center', 0 , 0)
    turtle.goto(0,-25)
    time.sleep(3)
    set()
    index = 0
    #user input loop
    while answer != 'n':
        set()
        index_num = random.randrange(0,len(colors))
        turtle.bgcolor(colors[index_num])
        turtle.penup()
        speak('What color is this?', 'center', 0,0)
        turtle.goto(0,-25)
        time.sleep(2)
        guess = user_input_text('Answer', 'The color is ')
        #correct user input
        if colors[index_num] == guess:
            speak('That is correct!','center',0,-25)
            turtle.goto(0,-50)
            #repeat or return to main
            answer = user_input_text('Good job!', 'Play again, y or n?')
        #incorrect user input
        else:
            speak('Sorry that is not correct','center',0,-25)
            turtle.goto(0,-50)
            #repeat or return to main
            answer = user_input_text('Play more?', 'y or n')              
    main()
                        
def main():
    set()
    selection = int()
    x = False
    while x == False:
        #menu options
        turtle.penup()
        speak("What do you want to practice today?", "center" , 0 ,75)
        speak("===============================", "center", 0, 50)
        speak("1. Addition", "left", -125, 25)
        speak("2. Subtraction", "left", -125, 0)
        speak("3. Shapes", "left", -125, -25)
        speak("4. Colors", "left", -125, -50)
        speak("5. Quit", "left", -125, -75)
        turtle.goto(-125,-100)
        selection = user_input_num("Practice Selection", "Enter 1, 2, 3, 4 or 5...")
        # user input selection of functions
        if selection == 1:
            add()
            x = True
        elif selection == 2:
            subtract()
            x = True
        elif selection == 3:
            shapes()
            x = True
        elif selection == 4:
            GetColor()
            x = True
        elif selection == 5:
            x = True
        else:
            print("Incorrect selection, please select an available option.")
#turtle reset function
def set():
    turtle.clearscreen()
    turtle.clear()
    turtle.shape("turtle")
    turtle.color("green")
    turtle.turtlesize(2)
    turtle.pencolor("black")
#user prompt function
def speak(phrase, position, x, y):
    turtle.goto(x,y)
    turtle.write(phrase, False, align=position, font = ("Arial", 12, "bold"))
#print to screen , text above user prompt function
def user_input_num(title, question):
    return turtle.numinput(title, question)
#print to screen, text above user prompt function
def user_input_text(title, question):
    return turtle.textinput(title, question)
        
import turtle
import time
main()
