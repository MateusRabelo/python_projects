from tkinter import *
from tkinter import ttk

# import Pillow to image manipulation
from PIL import Image, ImageTk

# import tandom to pseudo-randomize the pc choose
import random


co0 = "#FFFFFF"  # white
co1 = "#333333"  # black
co2 = "#fcc058"  # orange
co3 = "#fff873"  # yellow
co4 = "#34eb3d"   # green
co5 = "#e85151"   # red
bg = "#3b3b3b"

# configurations of main window
window = Tk()
window.title("Better Jokenpo")
# ("1280x720")
window.geometry("260x310")
window.configure(background = bg)


# splitting the frames
# (w = 1280, h = 280)
frame_up = Frame(window, width = 260, height = 100, background = co1, relief = 'raised')
frame_up.grid(column = 0, row = 0, sticky = NW)
# (w = 1280, h = 720)
frame_down = Frame(window, width = 260, height = 300, background = co0, relief = 'flat')
frame_down.grid(column = 0, row = 2, sticky = NW)

# stylizing the window
style = ttk.Style(window)
style.theme_use('clam')

# configuring frame_up (user's Labels)
# user label (name and position)
user_play_label = Label(frame_up, text = 'You', height=1, anchor='center', font='Ivy 10 bold', bg=co1, fg=co0)
user_play_label.place(x = 25, y = 70)
# indicator of win (user side)
user_win_line = Label(frame_up, text = '', height=10, anchor='center', font='Ivy 10 bold', bg=co0, fg=co0)
user_win_line.place(x = 0, y = 0)
# user score
user_play_score = Label(frame_up, text = '0', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
user_play_score.place(x = 50, y = 20)

# division of scores
division = Label(frame_up, text = ':', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
division.place(x = 120, y = 20)

# pc label (name and position)
pc_play_label = Label(frame_up, text = 'Pc', height=1, anchor='center', font='Ivy 10 bold', bg=co1, fg=co0)
pc_play_label.place(x = 205, y = 70)
# indicator of win (pc side)
pc_win_line = Label(frame_up, text = '', height=10, anchor='center', font='Ivy 10 bold', bg=co0, fg=co0)
pc_win_line.place(x = 255, y = 0)
# PC score
pc_play_score = Label(frame_up, text = '0', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
pc_play_score.place(x = 175, y = 20)

# line of draw
draw_line = Label(frame_up, text = '', width=255, anchor='center', font='Ivy 1 bold', bg=co0, fg=co0)
draw_line.place(x = 0, y = 95)

pc_playing = Label(frame_down, text = '', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co1)
pc_playing.place(x = 180, y = 10)


global user_play, pc_play, rounds, user_score, pc_score

user_score = 0
pc_score = 0
rounds = 5


# main function (l??gic)
def play(i):
    
    global rounds, user_score, pc_score
    
    if rounds > 0:
        
        print(rounds)
        pc_list = ['Rock', 'Paper', 'Scissors']
        pc_play = random.choice(pc_list)
        user_play = i
        
        pc_playing['text'] = pc_play
        pc_playing['fg'] = co1
        
        print(user_play, pc_play)
        
        if user_play == 'Rock' and pc_play == 'Rock':
            print('Draw')
            
            user_win_line['bg'] = co0
            pc_win_line['bg'] = co0
            draw_line['bg'] = co3
                        
        elif user_play == 'Paper' and pc_play == 'Paper':
            print('Draw')
            
            user_win_line['bg'] = co0
            pc_win_line['bg'] = co0
            draw_line['bg'] = co3
                        
        elif user_play == 'Scissors' and pc_play == 'Scissors':
            print('Draw')
            
            user_win_line['bg'] = co0
            pc_win_line['bg'] = co0
            draw_line['bg'] = co3
                        
        elif user_play == 'Rock' and pc_play == 'Scissors':
            print('Win!')
            
            user_win_line['bg'] = co4
            pc_win_line['bg'] = co0
            draw_line['bg'] = co0
            
            user_score += 10
            
        elif user_play == 'Scissors' and pc_play == 'Paper':
            print('Win!')
            
            user_win_line['bg'] = co4
            pc_win_line['bg'] = co0
            draw_line['bg'] = co0
            
            user_score += 10
            
        elif user_play == 'Paper' and pc_play == 'Rock':
            print('Win!')
            
            user_win_line['bg'] = co4
            pc_win_line['bg'] = co0
            draw_line['bg'] = co0
            
            user_score += 10
            
        elif user_play == 'Rock' and pc_play == 'Paper':
            print('Lose!')
            
            user_win_line['bg'] = co0
            pc_win_line['bg'] = co5
            draw_line['bg'] = co0
            
            pc_score += 10
            
        elif user_play == 'Scissors' and pc_play == 'Rock':
            print('Lose!')
            
            user_win_line['bg'] = co0
            pc_win_line['bg'] = co5
            draw_line['bg'] = co0
            
            pc_score += 10
            
        elif user_play == 'Paper' and pc_play == 'Scissors':
            print('Lose!')
            
            user_win_line['bg'] = co0
            pc_win_line['bg'] = co5
            draw_line['bg'] = co0
            
            pc_score += 10
        
        # updating values to score
        user_play_score['text'] = user_score
        pc_play_score['text'] = pc_score
        
        # updating rounds
        rounds -= 1
        
    else:
        
        user_play_score['text'] = user_score
        pc_play_score['text'] = pc_score
        
        # calling the end function
        end_game()


# start game function
def start_game():
    
    global rock_icon, paper_icon, scissors_icon, rock_button_icon, paper_button_icon, scissors_button_icon, clear_button
    
    play_button_icon.destroy()
    
    # configuring frame_down
    # added an icon to rock
    rock_icon = Image.open("jokenpo/icons/rock.png")
    # resizing the icon
    rock_icon = rock_icon.resize((50, 50))
    # necessary to run the Image.open()
    rock_icon = ImageTk.PhotoImage(rock_icon)

    # added a button to rock, and all the requisites
    rock_button_icon = Button(frame_down, width=50, command = lambda: play('Rock'), image=rock_icon, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), relief=FLAT) #relief <style of button>
    # position to button
    rock_button_icon.place(x=15, y=60)



    # added an icon to paper
    paper_icon = Image.open("jokenpo/icons/paper.png")
    # resizing the icon
    paper_icon = paper_icon.resize((50, 50))
    # requisite of Image.open()
    paper_icon = ImageTk.PhotoImage(paper_icon)

    # added a button to paper, and all the requisites
    paper_button_icon = Button(frame_down, width=50, command = lambda: play('Paper'), image=paper_icon, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), relief=FLAT) #relief <style of button>
    # position to button
    paper_button_icon.place(x=100, y=60)



    # added scissors icon
    scissors_icon = Image.open("jokenpo/icons/scissors.png")
    # resizing the icon
    scissors_icon = scissors_icon.resize((50, 50))
    # necessary to run Image.open()
    scissors_icon = ImageTk.PhotoImage(scissors_icon)

    # added a button to scissors, and all the requisites
    scissors_button_icon = Button(frame_down, width=50, command = lambda: play('Scissors'), image=scissors_icon, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), relief=FLAT) #relief <style of button>
    # position to button
    scissors_button_icon.place(x=185, y=60)


# end game function
def end_game():
    
    global rounds, user_score, pc_score
    
    # restarting the game
    user_play = 0
    pc_score = 0
    rounds = 5
    
    # removing the play buttons
    rock_button_icon.destroy()
    paper_button_icon.destroy()
    scissors_button_icon.destroy()
    
    
    # 
    user_score_verification = 0#int(user_play_score['text'])
    pc_score_verification = 0#int(pc_play_score['text'])
    
    
    
    if user_score_verification > pc_score_verification:
        
        winner_label = Label(frame_down, text = 'CONGRATULATIONS\n YOU WIN!!!', height=2, anchor='center', font='Ivy 12 bold', bg=co0, fg=co4)
        winner_label.place(x = 40, y = 70)
        
    elif user_score_verification < pc_score_verification:
        
        winner_label = Label(frame_down, text = 'You lose :/', height=1, anchor='center', font='Ivy 12 bold', bg=co0, fg=co5)
        winner_label.place(x = 10, y = 70)
        
    else:
        
        winner_label = Label(frame_down, text = 'We have a draw!!', height=1, anchor='center', font='Ivy 12 bold', bg=co0, fg=co1)
        winner_label.place(x = 10, y = 70)


    #winner_label.destroy()
    
    
    def play_again():
        
        user_play_score['text'] = 0
        pc_play_score['text'] = 0
        winner_label.destroy()
        
        play_again_button_icon = Button(frame_down,command=play_again, width=50, image=play_icon, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), relief=FLAT) #relief <style of button>
        play_again_button_icon.place(x=100, y=150)
    


# added play icon
play_icon = Image.open("jokenpo/icons/play.png")
# resizing the icon
play_icon = play_icon.resize((20, 30))
# necessary to run Image.open()
play_icon = ImageTk.PhotoImage(play_icon)

# added a button to play, and all the requisites
play_button_icon = Button(frame_down,command=start_game, width=50, image=play_icon, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), relief=FLAT) #relief <style of button>
# position to play button
play_button_icon.place(x=100, y=150)

# if you want to apply just a simple "play"
#paly_button = Button(frame_down, width=30, text='Jogar', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED)
#paly_button.place(x=5, y=151)


window.mainloop()