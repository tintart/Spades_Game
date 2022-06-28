from tkinter import *

root = Tk()
root.title("Best Spade Game Ever")
root.iconbitmap("d:/IBT/Analyzing Requirements and Defining .NET Solutions Architectures/SpadesGame")
root.geometry("900x500")
root.configure(background="green")


my_menu = Menu(root)
root.config(menu=my_menu)

#click command
def our_command():
    my_label = Label(root, text="You Clicked a Dropdown Menu!").pack()
def rul_command():
    my_label = Label(root, text="THE PACK-The standard 52-card pack is used.\nRANK OF SUITS-The spade suit is always trump.\nRANK OF CARDS-A (high), K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2.\nOBJECT OF THE GAME-To win at least the number of tricks bid.").pack()


#create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="Authentication", menu=file_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Character", menu=file_menu)
file_menu.add_command(label="Actors", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Heroes", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Politicians", command=our_command)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Level", menu=file_menu)
file_menu.add_command(label="Beginner", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Medium", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Hard", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Expert", command=our_command)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Team", menu=file_menu)
file_menu.add_command(label="Partnership", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Alone", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Choose your team", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Level of team", command=our_command)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Rules", command=rul_command)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="New game", menu=file_menu)
file_menu.add_command(label="Start new game", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Keep going", command=our_command)


root.mainloop()
