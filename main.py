import tkinter as tk
import time
from tkinter.messagebox import showwarning


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.bind('<KeyPress>', self.pressed_key)
        self.window.title('Dangerous Writing App')
        self.window.geometry('800x600')
        self.window.configure(bg='green')
        self.title_label = tk.Label(self.window,
                                    text="Dangerous Writing App- You can't stop writing more than 5 seconds",
                                    font=("Courier", 15, "normal"))
        self.title_label.config(bg='white')
        self.title_label.pack(fill=tk.BOTH)
        self.text_space = tk.Text(self.window)
        self.text_space.pack(expand=True)
        self.text_space.focus()
        self.time_of_last_click = 0
        self.condition = True
        self.window.mainloop()

    def pressed_key(self, event):
        if len(event.keysym) == 1 or \
                event.keysym == 'space' or \
                event.keysym == 'question' or \
                event.keysym == 'comma' or \
                event.keysym == 'period' or \
                event.keysym == 'colon' or \
                event.keysym == 'semicolon' or \
                event.keysym == 'Return' or \
                event.keysym == 'quoteright' or \
                event.keysym == 'exclam' or \
                event.keysym == 'at' or \
                event.keysym == 'numbersign' or \
                event.keysym == 'dollar' or \
                event.keysym == 'percent' or \
                event.keysym == 'asciicircum' or \
                event.keysym == 'ampersand' or \
                event.keysym == 'asterisk' or \
                event.keysym == 'parenleft' or \
                event.keysym == 'parenright' or \
                event.keysym == 'underscore' or \
                event.keysym == 'plus' or \
                event.keysym == 'minus' or \
                event.keysym == 'equal' or \
                event.keysym == 'braceleft' or \
                event.keysym == 'braceright' or \
                event.keysym == 'bracketleft' or \
                event.keysym == 'bracketright' or \
                event.keysym == 'quotedbl' or \
                event.keysym == 'bar' or \
                event.keysym == 'backslash' or \
                event.keysym == 'less' or \
                event.keysym == 'greater' or \
                event.keysym == 'slash':

            self.time_of_last_click = time.time()
            self.window.configure(bg='green')
            if self.condition:
                self.timer()
                self.condition = False

    def timer(self):
        if time.time() - self.time_of_last_click > 5:
            self.window.configure(bg='red')
            showwarning('Too long!!', 'Too long without key!!')
            self.condition = True
            self.window.configure(bg='green')
            self.window.after_cancel(self.after)
        else:
            if time.time() - self.time_of_last_click > 2:
                self.window.configure(bg='#CCCC33')
            if time.time() - self.time_of_last_click > 3:
                self.window.configure(bg='yellow')
            if time.time() - self.time_of_last_click > 4:
                self.window.configure(bg='#FF9900')
            self.after = self.window.after(500, self.timer)


app = Application()
