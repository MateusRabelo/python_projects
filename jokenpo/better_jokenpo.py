from tkinter import *
from tkinter import ttk

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
window.geometry("260x280")
window.configure(background = bg)


# splitting the frames
#(w = 1280, h = 280)
frame_up = Frame(window, width = 260, height = 100, background = co1, relief = 'raised')
frame_up.grid(column = 0, row = 0, sticky = NW)
#(w = 1280, h = 720)
frame_down = Frame(window, width = 260, height = 300, background = co0, relief = 'flat')
frame_down.grid(column = 0, row = 2, sticky = NW)

# stylizing the window
style = ttk.Style(window)
style.theme_use('clam')

# configuring frame_up
user_play = Label(frame_up, text = 'You', height=1, anchor='center', font='Ivy 10 bold', bg=co1, fg=co0)
user_play.place(x = 25, y = 70)
user_win_line = Label(frame_up, text = '', height=10, anchor='center', font='Ivy 10 bold', bg=co0, fg=co0)
user_win_line.place(x = 0, y = 0)
user_play_score = Label(frame_up, text = '0', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
user_play_score.place(x = 50, y = 20)

division = Label(frame_up, text = ':', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
division.place(x = 120, y = 20)

pc_play = Label(frame_up, text = 'Pc', height=1, anchor='center', font='Ivy 10 bold', bg=co1, fg=co0)
pc_play.place(x = 205, y = 70)
pc_win_line = Label(frame_up, text = '', height=10, anchor='center', font='Ivy 10 bold', bg=co0, fg=co0)
pc_win_line.place(x = 255, y = 0)
pc_play_score = Label(frame_up, text = '0', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg=co0)
pc_play_score.place(x = 175, y = 20)

draw_line = Label(frame_up, text = '', width=255, anchor='center', font='Ivy 1 bold', bg=co5, fg=co0)
draw_line.place(x = 0, y = 95)



window.mainloop()