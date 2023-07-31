from tkinter import ttk, Text, messagebox
import tkinter as tk
from random import randint


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        # start setting
        self.value1 = []
        self.value2 = []
        self.click1 = 0
        self.click2 = 0
        self.drawn1 = randint(0, 100)
        self.drawn2 = randint(0, 100)
        self.emoji1_win = 0
        self.emoji2_win = 0

        self.title('Game of luck')
        self.geometry('500x400')
        self.resizable(width=False, height=False)
        self.configure(background='steel blue')

        self.player_frame = tk.Frame(self)
        self.player_frame.pack(side='top')

        self.draw_frame = tk.Frame(self, bg='steel blue')
        self.draw_frame.pack()

        self.drawn_numb = tk.Frame(self, bg='grey')
        self.drawn_numb.pack()

        self.drawn_number_frame = tk.Frame(self, bg='gold')
        self.drawn_number_frame.pack()

        self.value_output_frame = tk.Frame(self, bg='gold')
        self.value_output_frame.pack()

        self.your_numbers_frame = tk.Frame(self, bg='grey')
        self.your_numbers_frame.pack()

        self.sum_result_frame = tk.Frame(self, bg='grey')
        self.sum_result_frame.pack()

        self.game_result_frame = tk.Frame(self, bg='gold')
        self.game_result_frame.pack()

        self.emoji_frame = tk.Frame(self, bg='gold')
        self.emoji_frame.pack()

        self.win_streak_frame = tk.Frame(self)
        self.win_streak_frame.pack()

        self.label1 = tk.Label(self.player_frame, text="Player 1", bg='steel blue')
        self.label1.pack(side='left', ipadx=50)

        self.label2 = tk.Label(self.player_frame, text="Player 2", bg='steel blue')
        self.label2.pack(ipadx=50)

        self.draw_button1 = ttk.Button(self.draw_frame, text='draw')
        self.draw_button1['command'] = self.draw_number1
        self.draw_button1.pack(side='left', padx=(0, 70), pady=(10, 20))

        self.draw_button2 = ttk.Button(self.draw_frame, text='draw')
        self.draw_button2['command'] = self.draw_number2
        self.draw_button2.pack(pady=(10, 20))

        self.drawn_result1 = Text(self.drawn_numb, height=1, width=10)
        self.drawn_result1.pack(side='left', padx=31, pady=(10, 0))

        self.drawn_result2 = Text(self.drawn_numb, height=1, width=10)
        self.drawn_result2.pack(padx=30, pady=(10, 0))

        self.drawn_number1 = tk.Label(self.drawn_number_frame, text='Drawn number', bg='grey')
        self.drawn_number1.pack(side='left', ipadx=30, pady=(0, 10))

        self.drawn_number2 = tk.Label(self.drawn_number_frame, text='Drawn number', bg='grey')
        self.drawn_number2.pack(ipadx=30, pady=(0, 10))

        self.value1_output = Text(self.value_output_frame, height=1, width=10)
        self.value1_output.pack(side='left', padx=31)

        self.value2_output = Text(self.value_output_frame, height=1, width=10)
        self.value2_output.pack(padx=30)

        self.your_numbers1 = tk.Label(self.your_numbers_frame, text='Your numbers', bg='gold')
        self.your_numbers1.pack(side='left', ipadx=34, pady=(0, 10))

        self.your_numbers2 = tk.Label(self.your_numbers_frame, text='Your numbers', bg='gold')
        self.your_numbers2.pack(ipadx=30, pady=(0, 10))

        self.sum_result1 = Text(self.sum_result_frame, height=1, width=10)
        self.sum_result1.pack(side='left', padx=31)

        self.sum_result2 = Text(self.sum_result_frame, height=1, width=10)
        self.sum_result2.pack(padx=30)

        self.game_result1 = tk.Label(self.game_result_frame, text='Result!', bg='grey')
        self.game_result1.pack(side='left', ipadx=45, pady=(0, 10))

        self.game_result2 = tk.Label(self.game_result_frame, text='Result!', bg='grey')
        self.game_result2.pack(ipadx=59, pady=(0, 10))

        self.emoji1 = Text(self.emoji_frame, height=1, width=10)
        self.emoji1.pack(side='left', padx=31)

        self.emoji2 = Text(self.emoji_frame, height=1, width=10)
        self.emoji2.pack(padx=30)

        self.win_streak1 = tk.Label(self.win_streak_frame, text='Win streak', bg='gold')
        self.win_streak1.pack(side='left', ipadx=40)

        self.win_streak2 = tk.Label(self.win_streak_frame, text='Win streak', bg='gold')
        self.win_streak2.pack(ipadx=44)

        self.after(2000, Gui.win_streak(self))  # run first time

    def draw_number1(self):
        self.drawn_result1.delete('1.0', '3.0')  # delete from 1 to 3 positions in window
        self.value1_output.delete('1.0', '10.0')
        self.drawn1 = randint(0, 100)
        self.value1.append(self.drawn1)
        self.value1_output.insert('1.0', self.value1)

        self.click1 += 1
        if self.click1 == 3:
            self.sum_result1.insert('1.0', sum(self.value1))
            self.draw_button1.config(state='disabled')
            self.drawn_result1.insert('1.0', self.drawn1)

        return self.drawn1

    def draw_number2(self):
        self.drawn_result2.delete('1.0', '3.0')
        self.value2_output.delete('1.0', '10.0')
        self.drawn2 = randint(0, 100)
        self.value2.append(self.drawn2)
        self.value2_output.insert('1.0', self.value2)
        self.click2 += 1
        if self.click2 == 3:
            self.sum_result2.insert('1.0', sum(self.value2))
            self.draw_button2.config(state='disabled')
            self.drawn_result2.insert('1.0', self.drawn2)

        return self.drawn2

    # DRY
    def reset(self):
        self.click1 = 0
        self.click2 = 0
        self.drawn_result1.delete('1.0', '3.0')
        self.value1_output.delete('1.0', '10.0')
        self.drawn_result2.delete('1.0', '3.0')
        self.value2_output.delete('1.0', '10.0')
        self.sum_result1.delete('1.0', '10.0')
        self.sum_result2.delete('1.0', '10.0')
        self.value2.clear()
        self.value1.clear()
        self.draw_button1.config(state='normal')
        self.draw_button2.config(state='normal')

    def win_streak(self):

        if self.click1 == 3 and self.click2 == 3 and sum(self.value1) > sum(self.value2):

            self.emoji1.insert('1.0', '🔥')
            self.emoji1_win += 1

            if self.emoji1_win == 3:
                messagebox.showinfo(title='Game of luck', message='Win Player 1')
                self.emoji2.delete('1.0', '6.0')
                self.emoji1.delete('1.0', '6.0')
                self.emoji1_win = 0
                self.emoji2_win = 0

            self.reset()

        elif self.click1 == 3 and self.click2 == 3 and sum(self.value1) < sum(self.value2):

            self.emoji2.insert('1.0', '🔥')
            self.emoji2_win += 1

            if self.emoji2_win == 3:
                messagebox.showinfo(title='Game of luck', message='Win Player 2')
                self.emoji2.delete('1.0', '6.0')
                self.emoji1.delete('1.0', '6.0')
                self.emoji1_win = 0
                self.emoji2_win = 0

            self.reset()
        # refreshing
        self.after(2000, self.win_streak)



