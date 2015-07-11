import tkinter as tk
import os
from design import *
import RPi.GPIO as GPIO
import graphics

graph = graphics.Popups()

class ResettubePU:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.reset_tube_life)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

class ResettubeOutPU:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.reset_tube_life_outlet)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

class ResetconsumuvPU:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.reset_consum_uv)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

class Resetconsumo3PU:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.reset_consum_o3)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

class Resetstats:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.reset_stats)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

class GemaPU:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.gema_pu)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

class VaPU:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.va_pop)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

class SteriPU:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.steri_pu)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

class ShutdownPU:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.shutdown_pu)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

class FeedTk:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.feedtk)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

        self.lbl1 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl1.place(x=130, y=67)
        self.lbl2 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl2.place(x=130, y=109)
        self.lbl3 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl3.place(x=130, y=151)
        self.c_feed = tk.Canvas(self.master, width=50, height=77, bg=BG_COLOR, borderwidth=0, highlightthickness=0)
        self.c_feed.place(x=25, y=58)
        self.c_feed.create_rectangle(0, 0, 50, 77, fill=GREEN_COLOR, outline=GREEN_COLOR, tags='obj1', )

    def update_pop(self, master):
        # TODO: Implement alarms (fg='red'...)
        self.constructor.update_db()
        # self.var1 = self.constructor.db['pop_feedtk'][0]
        self.var1 = master.level_percent
        self.var3 = self.constructor.db['pop_feedtk'][2]
        self.var2 = self.var1 * self.var3 / 100

        self.lbl1['text'] = self.var1
        self.lbl2['text'] = self.var2
        self.lbl3['text'] = self.var3
        self.y_feedtk_level = int(77 * (1 - self.var1 / 100))
        self.c_feed.coords('obj1', 0, self.y_feedtk_level, 50, 77)

        if self.var1 > 90 or self.var1 < 10:
            self.c_feed.itemconfig('obj1', fill=RED_COLOR, outline=RED_COLOR)
            self.lbl1['fg'] = RED_COLOR
            self.lbl2['fg'] = RED_COLOR
        elif self.var1 > 10 and self.var1 < 90:
            self.c_feed.itemconfig('obj1', fill=GREEN_COLOR, outline=GREEN_COLOR)
            self.lbl1['fg'] = GREEN_COLOR
            self.lbl2['fg'] = GREEN_COLOR

class Reactor:
    def __init__(self, constructor, master, width=300, height=200):
        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.reactor)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

        self.c_reactor_lmax = tk.Canvas(self.master, width=10, height=10, bg=GREEN_COLOR, borderwidth=0, highlightthickness=0)
        self.c_reactor_lmax.place(x=51, y=58)
        self.c_reactor_lmin = tk.Canvas(self.master, width=10, height=10, bg=GREEN_COLOR, borderwidth=0, highlightthickness=0)
        self.c_reactor_lmin.place(x=51, y=103)
        self.lbl1 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl1.place(x=130, y=67)
        self.lbl2 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl2.place(x=130, y=109)
        self.lbl3 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl3.place(x=130, y=151)

    def update_pop(self):
        self.constructor.update_db()
        self.var1 = self.constructor.db['status_flag']
        if self.var1 == 'idle':
            self.lbl1['text'] = 'Idle state'
        elif self.var1 == 'steri':
            self.lbl1['text'] = 'Sterilization stage'
        elif self.var1 == 'filling':
            self.lbl1['text'] = 'Filling'
        elif self.var1 == 'emptying':
            self.lbl1['text'] = 'Emptying'
        self.var2 = not GPIO.input(self.constructor.reactor_llow_pin)
        self.var3 = not GPIO.input(self.constructor.reactor_lhigh_pin)
        if self.var2: # Se há nível mínimo
            self.lbl2['text'] = 'Min level ok'
            self.lbl2['fg'] = GREEN_COLOR
            self.c_reactor_lmin['bg'] = GREEN_COLOR
        else:
            self.lbl2['text'] = 'Low level alarm'
            self.lbl2['fg'] = RED_COLOR
            self.c_reactor_lmin['bg'] = RED_COLOR
        self.lbl2.place(x=130, y=151)
        if self.var3: # Se há nível máximo
            self.lbl3['text'] = 'High level alarm'
            self.lbl3['fg'] = RED_COLOR
            self.c_reactor_lmax['bg'] = RED_COLOR
        else: # No max level
            self.lbl3['text'] = 'High level ok'
            self.lbl3['fg'] = GREEN_COLOR
            self.c_reactor_lmax['bg'] = GREEN_COLOR
        self.lbl3.place(x=130, y=109)

class FeedPmp:
    def __init__(self, constructor, master, width=300, height=200):

        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.feedpmp)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

        self.lbl1 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl1.place(x=130, y=67)
        self.lbl2 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl2.place(x=130, y=109)
        self.lbl3 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl3.place(x=130, y=151)

    def update_pop(self):
        self.constructor.update_db()
        # State - Running or Stopped
        if GPIO.input(self.constructor.feedpmp_pin) == self.constructor.db['ON']:
            self.var1 = 'Running'
        elif GPIO.input(self.constructor.feedpmp_pin) == self.constructor.db['OFF']:
            self.var1 = 'Stopped'
        # Total operation time
        self.var2 = self.constructor.db['feedpmp_op_time'][0]
        # Tube life
        self.var3 = self.constructor.db['feedpmp_tubelife'][0]

        self.lbl1['text'] = self.var1
        self.lbl2['text'] = format(self.var2, '.1f')
        self.lbl3['text'] = format(self.var3, '.1f')


class OutPmp:
    def __init__(self, constructor, master, width=300, height=200):

        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.outpmp)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

        self.lbl1 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl1.place(x=130, y=67)
        self.lbl2 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl2.place(x=130, y=109)
        self.lbl3 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl3.place(x=130, y=151)

    def update_pop(self):
        self.constructor.update_db()
        # State - Running or Stopped
        if GPIO.input(self.constructor.outpmp_pin) == self.constructor.db['ON']:
            self.var1 = 'Running'
        elif GPIO.input(self.constructor.outpmp_pin) == self.constructor.db['OFF']:
            self.var1 = 'Stopped'
        # Total operation time
        self.var2 = self.constructor.db['outpmp_op_time'][0]
        # Tube life
        self.var3 = self.constructor.db['outpmp_tubelife'][0]

        self.lbl1['text'] = self.var1
        self.lbl2['text'] = format(self.var2, '.1f')
        self.lbl3['text'] = format(self.var3, '.1f')


class RecirPmp:
    def __init__(self, constructor, master, width=300, height=200):

        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.recirpmp)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

        self.lbl1 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl1.place(x=130, y=67)
        self.lbl2 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl2.place(x=130, y=109)
        self.lbl3 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl3.place(x=130, y=151)

    def update_pop(self):
        self.constructor.update_db()
        # State - Running or Stopped
        if GPIO.input(self.constructor.recirpmp_pin) == self.constructor.db['ON']:
            self.var1 = 'Running'
        elif GPIO.input(self.constructor.recirpmp_pin) == self.constructor.db['OFF']:
            self.var1 = 'Stopped'
        # Total operation time
        self.var2 = self.constructor.db['recirpmp_op_time'][0]
        # Sterilization time
        self.var3 = self.constructor.db['steri_time'][3]

        self.lbl1['text'] = self.var1
        self.lbl2['text'] = format(self.var2, '.1f')
        self.lbl3['text'] = format(self.var3, '.1f')

class Uv:
    def __init__(self, constructor, master, width=300, height=200):

        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.uv)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

        self.lbl1 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl1.place(x=130, y=67)
        self.lbl2 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl2.place(x=130, y=109)
        self.lbl3 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl3.place(x=130, y=151)

    def update_pop(self):
        self.constructor.update_db()
        # State - ON or OFF
        if GPIO.input(self.constructor.uv_pin) == self.constructor.db['ON']:
            self.var1 = 'ON'
        elif GPIO.input(self.constructor.uv_pin) == self.constructor.db['OFF']:
            self.var1 = 'OFF'
        self.var2 = self.constructor.db['uv_op_time'][0]

        self.lbl1['text'] = self.var1
        self.lbl2['text'] = format(self.var2, '.1f')

class O3:
    def __init__(self, constructor, master, width=300, height=200):

        self.constructor = constructor
        self.master = master
        self.ima_pop = tk.PhotoImage(master=self.master, data=graph.ozone)
        self.l = tk.Label(self.master, image=self.ima_pop, bd=0)
        self.l.place(x=0, y=0)

        self.lbl1 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl1.place(x=130, y=67)
        self.lbl2 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl2.place(x=130, y=109)
        self.lbl3 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl3.place(x=130, y=151)

    def update_pop(self):
        self.constructor.update_db()
        # State - ON or OFF
        if GPIO.input(self.constructor.o3_pin) == self.constructor.db['ON']:
            self.var1 = 'ON'
        elif GPIO.input(self.constructor.o3_pin) == self.constructor.db['OFF']:
            self.var1 = 'OFF'
        self.var2 = self.constructor.db['o3_op_time'][0]
        self.var3 = self.constructor.db['steri_time'][3]

        self.lbl1['text'] = self.var1
        self.lbl2['text'] = format(self.var2, '.1f')
        self.lbl3['text'] = format(self.var3, '.1f')

class O2:
    def __init__(self, constructor, master, width=300, height=200):

        self.constructor = constructor
        self.master = master
        self.ima_pop_o2_open = tk.PhotoImage(master=self.master, data=graph.o2_open)
        self.ima_pop_o2_close = tk.PhotoImage(master=self.master, data=graph.o2_close)
        self.l = tk.Label(self.master, image=self.ima_pop_o2_close, bd=0)
        self.l.place(x=0, y=0)

        self.lbl1 = tk.Label(self.master, text='', bg='white', fg=FG_COLOR, font=('Roboto', 10))
        self.lbl1.place(x=130, y=67)

    def update_pop(self):
        self.constructor.update_db()
        if GPIO.input(self.constructor.o2_pin) == self.constructor.db['ON']:
            self.var1 = 'Open'
            self.l['image'] = self.ima_pop_o2_open
            self.lbl1['fg'] = GREEN_COLOR
        elif GPIO.input(self.constructor.o2_pin) == self.constructor.db['OFF']:
            self.var1 = 'Closed'
            self.l['image'] = self.ima_pop_o2_close
            self.lbl1['fg'] = FG_COLOR

        self.lbl1['text'] = self.var1