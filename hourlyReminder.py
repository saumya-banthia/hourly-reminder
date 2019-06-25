# The playsound module is subject to Copyright (c) 2016 Taylor Marks <taylor@marksfam.com>

###
# The MIT License (MIT)

# Copyright (c) 2016 Taylor Marks <taylor@marksfam.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###

from tkinter import Tk
from tkinter import Button
from threading import Thread
import datetime
from time import sleep
from random import choice
from playsound import playsound
from os.path import dirname, abspath, isfile, join
from os import listdir

START = 1
STOP  = 0
EXIT  = -1

fileDir = dirname(abspath(__file__))+"\\audio\\"

def test_loop():
    global looping
    while True:
        if looping == START:
            now = datetime.datetime.now().minute
            if now == 0:
                files = [name for name in listdir(fileDir) if isfile(join(fileDir, name))]
                rand_file = choice(files)
                playsound(fileDir+rand_file)
            second = datetime.datetime.now().second
            sleep(61-second)
        if looping == EXIT:
            break

def toggle():
    global looping
    if t_btn.config('text')[-1] == 'START':
        looping = START
        t_btn.config(text='STOP')
    else:
        looping = STOP
        t_btn.config(text='START')
 
looping = STOP

root = Tk()

root.iconbitmap(dirname(abspath(__file__))+r'\stopwatch_yiD_icon.ico')
root.title("Hourly Reminder")
root.geometry('{}x{}'.format(300, 50))
root.configure(background='#252525')
root.resizable(0,0)



t_btn = Button(text="START", width=12, command=toggle, fg="#fff", bg="#007acc", font=("Google Sans Medium",12))
t_btn.pack(pady=10)
  
thread = Thread(target=test_loop)
thread.daemon = True
thread.start()
 
root.mainloop()
looping = EXIT