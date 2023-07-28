from tkinter import ttk, Text, messagebox
import tkinter as tk
from random import randint
from ctypes import windll

# improve resolution
try:
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    pass

value1 = []
value2 = []

click1 = 0
click2 = 0 


def draw_number1():
    drawn_result1.delete('1.0', '3.0')  # delete from 1 to 3 positions in window
    value1_output.delete('1.0', '10.0')
    drawn1 = randint(0, 100)
    value1.append(drawn1)
    value1_output.insert('1.0', value1)

    global click1
    click1 += 1
    if click1 == 3:
        sum_result1.insert('1.0', sum(value1))
        draw_button1.config(state='disabled')
    
    return drawn_result1.insert('1.0', drawn1)


def draw_number2():
    drawn_result2.delete('1.0', '3.0')
    value2_output.delete('1.0', '10.0')
    drawn2 = randint(0, 100)
    value2.append(drawn2)
    value2_output.insert('1.0', value2)
    global click2 
    click2 += 1
    if click2 == 3:
        sum_result2.insert('1.0', sum(value2))
        draw_button2.config(state='disabled')

    return drawn_result2.insert('1.0', drawn2)


def reset():
    global click1
    global click2
    click1 = 0
    click2 = 0
    drawn_result1.delete('1.0', '3.0')
    value1_output.delete('1.0', '10.0')
    drawn_result2.delete('1.0', '3.0')
    value2_output.delete('1.0', '10.0')
    sum_result1.delete('1.0', '10.0')
    sum_result2.delete('1.0', '10.0')
    value2.clear()
    value1.clear()
    draw_button1.config(state='normal')
    draw_button2.config(state='normal')


def reset_emoji():
    global emoji1_win
    global emoji2_win
    emoji2.delete('1.0', '6.0')
    emoji1.delete('1.0', '6.0')
    emoji1_win = 0
    emoji2_win = 0


emoji1_win = 0
emoji2_win = 0


def win_streak():
    if click1 == 3 and click2 == 3 and sum(value1) > sum(value2):
        emoji1.insert('1.0', '🔥')
        global emoji1_win
        emoji1_win += 1

        if emoji1_win == 3:
            messagebox.showinfo(title='Game of luck', message='Win Player 1')
            reset_emoji()
        reset()

    elif click1 == 3 and click2 == 3 and sum(value1) < sum(value2):
        emoji2.insert('1.0', '🔥')
        global emoji2_win
        emoji2_win += 1

        if emoji2_win == 3:
            messagebox.showinfo(title='Game of luck', message='Win Player 2')
            reset_emoji()
        reset()

    root.after(2000, win_streak)  # refreshing 2000 ms


root = tk.Tk()
root.title('Game of luck')
root.geometry('500x400')
root.resizable(width=False, height=False)
root.configure(background='steel blue')

player_frame = tk.Frame(root)
player_frame.pack(side='top')

draw_frame = tk.Frame(root, bg='steel blue')
draw_frame.pack()

drawn_numb = tk.Frame(root, bg='grey')
drawn_numb.pack()

drawn_number_frame = tk.Frame(root, bg='gold')
drawn_number_frame.pack()

value_output_frame = tk.Frame(root, bg='gold')
value_output_frame.pack()

your_numbers_frame = tk.Frame(root, bg='grey')
your_numbers_frame.pack()

sum_result_frame = tk.Frame(root, bg='grey')
sum_result_frame.pack()

game_result_frame = tk.Frame(root, bg='gold')
game_result_frame.pack()

emoji_frame = tk.Frame(root, bg='gold')
emoji_frame.pack()

win_streak_frame = tk.Frame(root)
win_streak_frame.pack()

Label1 = tk.Label(player_frame, text="Player 1", bg= 'steel blue')
Label1.pack(side='left', ipadx=60)

Label2 = tk.Label(player_frame, text="Player 2", bg= 'steel blue')
Label2.pack(ipadx=50)

draw_button1 = ttk.Button(draw_frame, text='draw', command=draw_number1)
draw_button1.pack(side='left', padx=(0,70), pady=(10,20))

draw_button2 = ttk.Button(draw_frame, text='draw', command=draw_number2)
draw_button2.pack(pady=(10,20))

drawn_result1 = Text(drawn_numb, height=1, width=10)
drawn_result1.pack(side='left', padx=30, pady=(10,0))

drawn_result2 = Text(drawn_numb, height=1, width=10)
drawn_result2.pack(padx=30, pady=(10,0))

drawed_number1 = tk.Label(drawn_number_frame, text='Drawn number', bg='grey')
drawed_number1.pack(side='left', ipadx=30, pady=(0,10))

drawed_number2 = tk.Label(drawn_number_frame, text='Drawn number', bg='grey')
drawed_number2.pack(ipadx=30, pady=(0,10))

value1_output = Text(value_output_frame, height=1, width=10)
value1_output.pack(side='left',padx=30)

value2_output = Text(value_output_frame, height=1, width=10)
value2_output.pack(padx= 30)

your_numbers1 = tk.Label(your_numbers_frame, text='Your numbers', bg='gold')
your_numbers1.pack(side='left', ipadx=35, pady=(0,10))

your_numbers2 = tk.Label(your_numbers_frame, text='Your numbers', bg='gold')
your_numbers2.pack(ipadx=32, pady=(0,10))

sum_result1 = Text(sum_result_frame, height=1, width=10)
sum_result1.pack(side='left', padx= 30)

sum_result2 = Text(sum_result_frame, height=1, width=10)
sum_result2.pack(padx= 30)

game_result1 = tk.Label(game_result_frame, text='Result!', bg='grey')
game_result1.pack(side='left', ipadx=55, pady=(0,10))

game_result2 = tk.Label(game_result_frame, text='Result!', bg='grey')
game_result2.pack(ipadx=59, pady=(0,10))

emoji1 = Text(emoji_frame, height=1, width=10)
emoji1.pack(side='left', padx= 30)

emoji2 = Text(emoji_frame, height=1, width=10)
emoji2.pack(padx= 30)

win_streak1 = tk.Label(win_streak_frame, text='Win streak', bg='gold')
win_streak1.pack(side='left', ipadx=45)

win_streak2 = tk.Label(win_streak_frame, text='Win streak', bg='gold')
win_streak2.pack(ipadx=44)

root.after(2000, win_streak)  # run first time

root.mainloop()
