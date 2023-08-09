from tkinter import *
from PIL import ImageTk, Image
import toAsk
import clientLogin
import myDetails
import listing
import rentPage
import sellPage
import newAddPage0
import mySQLConnection as database


class ClientMain:

    def __init__(self, LoginID):
        frame = Tk()
        frame.geometry("1266x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("CampusConnect")
        myicon = PhotoImage(file='images/zmyicon2.png')
        frame.iconphoto(False, myicon)
        frame.config(bg="white")

        def showMyDetails():
            global myResults
            try:
                database.myQuery.execute(
                    f"select * from myUser where user_id={LoginID}")
                myResults = database.myQuery.fetchone()
                # print(myResults)
            except:
                print("hey bro")
            frame.destroy()
            newPage = myDetails.MyDetails(myResults)

        def toMoveBack():
            frame.destroy()
            newPage = clientLogin.ClientLogin()

        def toMoveOnPurchasePage():
            frame.destroy()
            newPage = listing.RentTable(LoginID)

        def toMoveOnRentPage():
            frame.destroy()
            newPage = rentPage.Rent(LoginID)

        def toMoveOnSellPage():
            frame.destroy()
            newPage = sellPage.Sell(LoginID)

        ren = ImageTk.PhotoImage(Image.open("images/zuser2.png"))
        myFrame2 = Label(frame, image=ren)
        myFrame2.place(x=0, y=0, width=422, height=494)
        myFrame2.config(bg="white")
        myRen = Button(frame, text="USER DETAILS", font=("Product Sans", 24, "bold"), borderwidth=0,
                       command=showMyDetails)
        myRen.place(x=0, y=494, width=422, height=40)
        myRen.config(bg="#4D50F1", fg="white",
                     activeforeground="#4D50F1", activebackground="white")
        # x=422, y=0, width=422, height=494
        # x=0, y=0, width=422, height=494

        # x=0, y=494, width=422, height=40
        # x=422, y=494, width=422, height=40
        pur = ImageTk.PhotoImage(Image.open("images/zpurchaseDis2.jpg"))
        myFrame1 = Label(frame, image=pur)
        myFrame1.place(x=422, y=0, width=422, height=494)
        myFrame1.config(bg="white")
        myPur = Button(frame, text="PURCHASE", font=("Product Sans", 24, "bold"), borderwidth=0,
                       command=toMoveOnPurchasePage)
        myPur.place(x=422, y=494, width=422, height=40)
        myPur.config(bg="#4D50F1", fg="white",
                     activeforeground="#4D50F1", activebackground="white")

        sell = ImageTk.PhotoImage(Image.open("images/zsellDis2.jpg"))
        myFrame3 = Label(frame, image=sell)
        myFrame3.place(x=844, y=0, width=422, height=494)
        myFrame3.config(bg="white")
        mySol = Button(frame, text="SELL", font=("Product Sans", 24, "bold"), borderwidth=0,
                       command=toMoveOnSellPage)
        mySol.place(x=844, y=494, width=422, height=40)
        mySol.config(bg="#4D50F1", fg="white",
                     activeforeground="#4D50F1", activebackground="white")

        Back = Button(frame, text="ç", font=(
            "Wingdings", 30, "bold"), command=toMoveBack)
        Back.place(x=0, y=612.2, width=1266, height=55)
        Back.config(bg="#4D50F1", fg="white", borderwidth=0, activeforeground="white",
                    activebackground="#4D50F1")
        header = Label(frame, text="DASHBOARD", bg="white", fg="black",
                       font=("Product Sans", 30, "bold"))
        header.place(x=0, y=0, width=1266, height=65)

        frame.mainloop()


if __name__ == "__main__":
    myWindow = ClientMain(9)
