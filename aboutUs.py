from tkinter import *
from PIL import ImageTk, Image
import loginAsa


class AboutUs:
    def __init__(self):
        frame = Tk()

        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("Campus Connect")

        myicon = PhotoImage(file='images/myIcon.png')
        frame.iconphoto(False, myicon)

        frame.config(bg="white")
        myWall = ImageTk.PhotoImage(file="images/thank.png")

        wallLabel = Label(frame, image=myWall)
        wallLabel.place(x=0, y=0, width=663, height=668)

        lab1 = Label(frame, text="About Us", bg="white", font=(
            "Product Sans", 32,)).place(x=700, y=100)
        lab2 = Label(frame, text="""  Our goal is to improve the quality of life of students and create  
    robust system for them to help their peers in acquiring knowledge.
    
    Need to rent a textbook for the semester?
     No problem. 
    
    But Campus Connect isn't just for textbooks. 
    
    Need a new laptop or a desk for your dorm room?
    Check out the listings on Campus Connect.
     
    Campus Connect makes it easy to find other students
    who are renting out their textbooks.
     """, bg="white", font=("Product Sans", 16,)).place(x=500, y=160)

        def toMoveBack():
            frame.destroy()
            loginAsa.LoginAsA()

        Back = Button(wallLabel, text="🢘", font=("Product Sans", 30))
        Back.place(x=10, y=10, height=50, width=60)
        Back.config(bg="#4D50F1", fg="white", activeforeground="white", activebackground="#4D50F1",
                    borderwidth=0, command=toMoveBack)

        frame.mainloop()


if __name__ == "__main__":
    myPage = AboutUs()
