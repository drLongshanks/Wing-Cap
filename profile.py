# This program will allow the user to enter their skill level, platform info, and desired category and pass the
# inputs to a database query in a separate script.

import tkinter as tk
from tkinter import ttk

# Reads selected file and returns text values
def get_list(query):
    with open(query+'.txt', 'r') as read:
            contents = read.readlines()
    return (contents)

# Creates a "Next" button after player selects skill level
def test_skill(container):
    if skill_choice.get() == '(choose one)':
        print("")
    else:
        ttk.Button(skillFrame, text="Next", command=skillFrame.destroy).grid(column=0, row=3)
        chosen_skill=skill_choice.get()

# def test_cat(container):
#     if cat_choice.get() == '(choose one)':
#         print("")
#     else:
#         ttk.Button(catFrame, text="Next", command=catFrame.destroy).grid(column=0, row=3)
#         chosen_cat=cat_choice.get()

# Manages the screen where the player selects their skill level
def skill_select(root):

    ttk.Label(skillFrame, text='Select your skill level:').grid(column=0, row=0)
    paddings = {'padx': 50, 'pady': 20}
    options = get_list('skills')
    drop = tk.OptionMenu(skillFrame, skill_choice, *options, command=test_skill)
    drop.config(width=16, height=3)
    drop.grid(column=0, row=2, **paddings)

    return skillFrame

# Manages the screen where the player selects the category they wish to play
# def cat_select(root):
#
#     ttk.Label(catFrame, text ='Select your desired category:').grid(column=0, row=0)
#     paddings = {'padx': 50, 'pady': 20}
#     options = get_list('categories')
#     drop = tk.OptionMenu(catFrame, cat_choice, *options, command=test_skill)
#     drop.config(width=16, height=3)
#     drop.grid(column=0, row=2, **paddings)
#
#     return catFrame

# Manages the screen where the player selects the platform they're playing on
def platform_select():
    platFrame = ttk.Frame()

root = tk.Tk()
root.title('Wing Cap Setup')
root.geometry('800x600+200+100')
root.config(background='#032b5f')

skillFrame = ttk.Frame(root)
skill_choice = tk.StringVar(root)
skill_choice.set('(choose one)')
chosen_skill = tk.StringVar(root)

catFrame = ttk.Frame(root)
cat_choice = tk.StringVar(root)
cat_choice.set('(choose one)')
chose_cat = tk.StringVar(root)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

first_screen = skill_select(root)
first_screen.grid(column=1, row=1)

# second_screen = cat_select(root)
# second_screen.grid(column=1, row=1)

#Dev button to make program exit easier
ttk.Button(root, text='Exit', command=root.destroy).grid(column=2, row=2)

root.mainloop()
