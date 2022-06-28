from tkinter import *
import random
#from PILLOW import Image, ImageTk


root = Tk()
root.title("Best Spade Game Ever - Card Deck")
root.iconbitmap("d:/IBT/Analyzing Requirements and Defining .NET Solutions Architectures/SpadesGame")
root.geometry("1000x700")
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


#resize cards
def resize_cards(card):
    our_card_img = Image.open(card)
    our_card_resize_image = our_card_img.resize((150,218))
    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)
    return our_card_image 


#shuffle the cards
def shuffle():
    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = range(2,15)
    #11=jack,12=queen,13=king,14=ace
    global deck
    deck=[]
    for suit in suits:
        for value in values:
            deck.append(f"{value}_of_{suit}")
             
    #create our players
    global dealer, playerone, playertwo, playerthree
    dealer = []
    playerone = []
    playertwo = []
    playerthree = []

    #grab a random card
    card = random.choice(deck)
    deck.remove(card)
    dealer.append(card)
    dealer_label.config(text=card)

    card = random.choice(deck)
    deck.remove(card)
    playerone.append(card)
    playerone_label.config(text=card)

    card = random.choice(deck)
    deck.remove(card)
    playertwo.append(card)
    playertwo_label.config(text=card)

    card = random.choice(deck)
    deck.remove(card)
    playerthree.append(card)
    playerthree_label.config(text=card)

    #put nr of remaining cards in title bar
    root.title(f"Best Spade Game Ever - {len(deck)}Cards left")
    
#deal out cards
def deal_cards():
    try:
        #get the dealer card
        card = random.choice(deck)
        deck.remove(card)
        dealer.append(card)
        global dealer_image
        dealer_image = resize_cards(f"d:/IBT/Analyzing Requirements and Defining .NET Solutions Architectures/SpadesGame/deck{card}.jpeg")
        dealer_label.config(image=dealer_image)
        #get the players card
        card = random.choice(deck)
        deck.remove(card)
        playerone.append(card)
        global playerone_image
        playerone_image = resize_cards(f"d:/IBT/Analyzing Requirements and Defining .NET Solutions Architectures/SpadesGame/deck{card}.jpeg")
        playerone_label.config(image=playerone_image)
        
        card = random.choice(deck)
        deck.remove(card)
        playertwo.append(card)
        global playertwo_image
        playertwo_image = resize_cards(f"d:/IBT/Analyzing Requirements and Defining .NET Solutions Architectures/SpadesGame/deck{card}.jpeg")
        playertwo_label.config(image=playertwo_image)

        card = random.choice(deck)
        deck.remove(card)
        playerthree.append(card)
        global playerthree_image
        playerthree_image = resize_cards(f"d:/IBT/Analyzing Requirements and Defining .NET Solutions Architectures/SpadesGame/deck{card}.jpeg")
        playerthree_label.config(image=playerthree_image)

        root.title(f"Best Spade Game Ever - {len(deck)}Cards left")
    except:
       root.title(f"Best Spade Game Ever - {len(deck)}Cards left") 


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=2, padx=20, ipadx=20)
 
playerone_frame = LabelFrame(my_frame, text="PlayerOne", bd=0)
playerone_frame.grid(row=2, column=1, ipadx=20)

playertwo_frame = LabelFrame(my_frame, text="PlayerTwo", bd=0)
playertwo_frame.grid(row=4, column=2, ipadx=20)

playerthree_frame = LabelFrame(my_frame, text="PlayerThree", bd=0)
playerthree_frame.grid(row=2, column=3, ipadx=20)

#put cards in frames
dealer_label = Label(dealer_frame, text="")
dealer_label.pack(pady=20)

playerone_label = Label(playerone_frame, text="")
playerone_label.pack(pady=20)

playertwo_label = Label(playertwo_frame, text="")
playertwo_label.pack(pady=20)

playerthree_label = Label(playerthree_frame, text="")
playerthree_label.pack(pady=20)

#create buttons
bid_button = Button(root, text="Number of Bids", font=("Helvetica, 16"))
bid_button.pack(pady=20)

shuffle_button = Button(root, text="Shuffle Deck", font=("Helevtica, 16"), command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Deal Cards", font=("Helevtica, 16"), command=deal_cards)
card_button.pack(pady=20)




shuffle()
root.mainloop()
