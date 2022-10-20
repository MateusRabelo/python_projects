import random
from tkinter import *

# main function when the game was run only in terminal
def jokenpo():
    pc_list = ["Rock","Paper","Scissors"]
    
    #print(pc_play)
    #print(user_play)
    
    opt = 'Y'
    while True:
        if opt == 'Y' or opt == 'y':       
            user_play = str(input("\nWhat's your play? "))
            print(("\n"))
              
            pc_play = random.choice(pc_list)    
            if pc_play == "Rock" and user_play == "Rock":
                print("Pc play =", pc_play)
                print("We have a DRAW!!!!!\n")
                
            elif pc_play == "Paper" and user_play == "Paper":
                print("Pc play =", pc_play)
                print("We have a DRAW!!!!!\n")

            elif pc_play == "Scissors" and user_play == "Scissors":
                print("Pc play =", pc_play)
                print("We have a DRAW!!!!!\n")
                
            elif pc_play == "Rock" and user_play == "Paper":
                print("Pc play =", pc_play)
                print("You Win! :)\n")
            
            elif pc_play == "Paper" and user_play == "Scissors":
                print("Pc play =", pc_play)
                print("You Win! :)\n")
                
            elif pc_play == "Scissors" and user_play == "Rock":
                print("Pc play =", pc_play)
                print("You Win! :)\n")
                
            elif pc_play == "Rock" and (user_play == "Scissors"):
                print("Pc play =", pc_play)
                print("You Lost! :/\n")
                
            elif pc_play == "Paper" and (user_play == "Rock"):
                print("Pc play =", pc_play)
                print("You Lost! :/\n")
                
            elif pc_play == "Scissors" and (user_play == "Paper"):
                print("Pc play =", pc_play)
                print("You Lost! :/\n")
                
            opt = input("Can you try againw [y/n] ")
            if opt == 'Y' or opt == 'y':
                print("\nOkay let's go!")
            
            elif opt == 'N' or opt == 'n':
                print("\nHmm...Bye Bye!")
                break
        
            else: print("Error - Incorrect Option. Try again.")

# end of this old main function        
            
            
def user_rock():
    clear_result = Label(window, text='                                 \n',)
    clear_result.grid(column = 1, row = 3)
    
    clear_pc_play = Label(window, text='                                 \n',)
    clear_pc_play.grid(column = 1, row = 2)
    
    pc_list = ["Rock","Paper","Scissors"]
    pc_play = random.choice(pc_list) 
    
    if pc_play == "Rock":

        pc_play_string = Label(window, text="'Pc play: {}'".format(pc_play))
        pc_play_string.grid(column = 1, row = 2)
        
        result = Label(window, text="We've a DRAW!!!", background='yellow')
        result.grid(column=1, row = 3)
        
    elif pc_play == "Paper":

        pc_play_string = Label(window, text="'Pc play: {}'".format(pc_play))
        pc_play_string.grid(column = 1, row = 2)
        
        result = Label(window, text="You Lost! :(", background='red')
        result.grid(column=1, row = 3)
        
    else:

        pc_play_string = Label(window, text="'Pc play: {}'".format(pc_play))
        pc_play_string.grid(column = 1, row = 2)
        
        result = Label(window, text="You Win! ;)", background='green')
        result.grid(column=1, row = 3)
        
        
        
        
def user_paper():
    clear_result = Label(window, text='                                 \n',)
    clear_result.grid(column = 1, row = 3)
    
    clear_pc_play = Label(window, text='                                 \n',)
    clear_pc_play.grid(column = 1, row = 2)
    
    pc_list = ["Rock","Paper","Scissors"]
    pc_play = random.choice(pc_list) 
    
    if pc_play == "Rock":
        pc_play_string = Label(window, text="'Pc play: {}'".format(pc_play))
        pc_play_string.grid(column = 1, row = 2)
        
        result = Label(window, text="You Win! ;)", background='green')
        result.grid(column=1, row = 3)
        
    elif pc_play == "Paper":
        pc_play_string = Label(window, text="'Pc play: {}'".format(pc_play))
        pc_play_string.grid(column = 1, row = 2)
        
        result = Label(window, text="We've a DRAW!", background='yellow')
        result.grid(column=1, row = 3)
        
    else:
        pc_play_string = Label(window, text="'Pc play: {}'".format(pc_play))
        pc_play_string.grid(column = 1, row = 2)
        
        result = Label(window, text="You Lost! :(", background='red')
        result.grid(column=1, row = 3)
        
        
        
def user_scissors():
    clear_result = Label(window, text='                                 \n',)
    clear_result.grid(column = 1, row = 3)
    
    clear_pc_play = Label(window, text='                                 \n',)
    clear_pc_play.grid(column = 1, row = 2)
    
    pc_list = ["Rock","Paper","Scissors"]
    pc_play = random.choice(pc_list) 
    
    if pc_play == "Rock":
        pc_play_string = Label(window, text="'Pc play: {}'".format(pc_play))
        pc_play_string.grid(column = 1, row = 2)
        
        result = Label(window, text="You Lost! :/", background='red')
        result.grid(column=1, row = 3)
        
    elif pc_play == "Paper":
        pc_play_string = Label(window, text="'Pc play: {}'".format(pc_play))
        pc_play_string.grid(column = 1, row = 2)
        
        result = Label(window, text="You Win! ;)", background='green')
        result.grid(column=1, row = 3)
        
    else:
        pc_play_string = Label(window, text="'Pc play: {}'".format(pc_play))
        pc_play_string.grid(column = 1, row = 2)
        
        result = Label(window, text="We've a DRAW!", background='yellow')
        result.grid(column=1, row = 3)
    
    
    
window = Tk()
window.title("Jokenpo")
#window.geometry("400x400")

introduction = Label(window, text="Make your play\nChoose between 'Rock', 'Paper' or 'Scissors")
introduction.grid(column = 1, row = 4)


rock = Button(window, text="Rock", command=user_rock)#, padx=5, pady=5, justify=CENTER)
rock.grid(column = 0, row = 6)

paper = Button(window, text="Paper", command=user_paper)#, padx=5, pady=5, justify=CENTER)
paper.grid(column = 1, row = 6)

scissors = Button(window, text="Scissors", command=user_scissors)#, padx=5, pady=5, justify=CENTER)
scissors.grid(column = 2, row = 6)

window.mainloop()
    
#jokenpo()