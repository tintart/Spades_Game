from tkinter import *


#Create an instance of tkinter frame or window
root = Tk()
root.title("Best Spade Game Ever")

#Define the geometry
root.geometry("900x500")
root.configure(background="green")

#Create a Frame
frame= Frame(root)
def close():
   root.destroy()

#Create a Label widget in the frame
text= Label(frame, text= "Register", font= ('Helvetica bold', 14))
text.pack(pady=20)



#Add Entry Widgets
Label(frame, text= "Login").pack()
username= Entry(frame, width= 20)
username.pack()
Label(frame, text= "Password").pack()
password= Entry(frame, show="*", width= 15)
password.pack()


#Create widget in the frame
button= Button(frame, text= "Start Game",font= ('Helvetica bold',14),command= open)
button.pack(pady=20)
frame.pack()

root.mainloop()
    
