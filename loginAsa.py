from tkinter import *
from PIL import ImageTk, Image
import toAsk
import aboutUs


class LoginAsA:
    def __init__(self):
        frame = Tk()
        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.configure(bg="white")

        frame.title("CAMPUS CONNECT")
        myicon = PhotoImage(file='images/myIcon.png')
        frame.iconphoto(False, myicon)

        def loginClick():
            frame.destroy()
            toAsk.ToAsk()

        def moveToAboutUs():
            frame.destroy()
            aboutUs.AboutUs()

        myWallpaper = ImageTk.PhotoImage(Image.open("images/zareyouaa2.jpg"))
        areYouA = Label(frame, image=myWallpaper)
        areYouA.place(x=0, y=0)

        newWindow = Frame(frame)
        newWindow.place(x=233, y=180, width=800, height=175)
        newWindow.config(bg="white")

        areYouA = Label(newWindow, text="Welcome to Campus Connect",
                        font=("Product Sans", 34, "bold"))
        areYouA.place(x=75, y=40, width=650, height=50)
        areYouA.config(bg="white")

        areYouA2 = Label(newWindow, text="Your One-Stop Shop for Campus Needs..!",
                         font=("Product Sans", 18, "bold"))
        areYouA2.place(x=75, y=100, width=650, height=35)
        areYouA2.config(bg="white")

        header = Label(frame, text="CAMPUS CONNECT", bg="white",
                       font=("Product Sans", 30, "bold"))
        header.place(x=0, y=0, width=1266, height=65)

        login = Button(header, text="LOGIN", bg="white", font=("Product Sans", 20), borderwidth=0,
                       activeforeground="black",

                       command=loginClick)
        login.place(x=20, y=5, width=80, height=50)

        aboutUss = Button(header, text="ABOUT US", bg="white", font=("Product Sans", 20), borderwidth=0,
                          activeforeground="white",
                          activebackground="black", command=moveToAboutUs)
        aboutUss.place(x=1111, y=5, width=140, height=50)
        aboutUss.config(activeforeground="#4D50F1", fg="black")

        # mainPic = ImageTk.PhotoImage(Image.open("images/book.png"))

        # tosetImage = Label(frame, image=mainPic)
        # tosetImage.place(x=0, y=60, width=1266, height=688)

        frame.mainloop()


if __name__ == "__main__":
    myPage = LoginAsA()
