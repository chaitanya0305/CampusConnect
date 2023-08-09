from tkinter import *
from tkinter import ttk
import mySQLConnection as database
import clientMain
from tkinter import ttk


class RentTable():
    def __init__(self, loginId):

        def show_details(event):
            item = tree.item(tree.focus())
            if item:
                values = item['values']
                # Show more details for the selected row here
                print(values)

        def view_details():
            # Get the selected row
            item = tree.focus()
            values = tree.item(item, 'values')

            # Create a new window to show more details
            details_window = Toplevel(frame)
            details_window.title("Details")
            details_window.geometry("600x400")
            details_window.resizable(0, 0)

            # Add style to the details window
            style = ttk.Style(details_window)
            style.configure('Details.TLabel', font=(
                'Product Sans', 14), padding=5)

            # Create labels to show the details
            id_label = ttk.Label(
                details_window, text=f"ID: {values[0]}", style='Details.TLabel', anchor='w')
            id_label.pack(fill='x')
            name_label = ttk.Label(
                details_window, text=f"NAME: {values[1]}", style='Details.TLabel', anchor='w')
            name_label.pack(fill='x')
            address_label = ttk.Label(
                details_window, text=f"TITLE: {values[2]}", style='Details.TLabel', anchor='w')
            address_label.pack(fill='x')
            btype_label = ttk.Label(
                details_window, text=f"SEM: {values[3]}", style='Details.TLabel', anchor='w')
            btype_label.pack(fill='x')
            atype_label = ttk.Label(
                details_window, text=f"PRICE: {values[4]}", style='Details.TLabel', anchor='w')
            atype_label.pack(fill='x')
            loc_label = ttk.Label(
                details_window, text=f"DONATION: {values[5]}", style='Details.TLabel', anchor='w')
            loc_label.pack(fill='x')
            loc_label = ttk.Label(
                details_window, text=f"CONTACT: {values[6]}", style='Details.TLabel', anchor='w')
            loc_label.pack(fill='x')
            landmark_label = ttk.Label(
                details_window, text=f"CONDITION: {values[7]}", style='Details.TLabel', anchor='w')
            landmark_label.pack(fill='x')
            up_label = ttk.Label(
                details_window, text=f"DESCRIPTION: {values[8]}", style='Details.TLabel', anchor='w')
            up_label.pack(fill='x')

        frame = Tk()

        frame.geometry("1286x668+50+20")
        frame.minsize(1266, 668)
        frame.maxsize(1266, 668)
        frame.title("CampusConnect")
        myicon = PhotoImage(file='images/myIcon.png')
        frame.iconphoto(False, myicon)

        myTitle = Label(frame, text="STUDENT MARKET PLACE",
                        font=("Product Sans", 24, "bold"))
        myTitle.place(x=0, y=0, width=1266, height=50)
        myTitle.config(bg="#4D50F1", fg="white")
        database.myQuery.execute("select * from mysell")

        def toMoveBack():
            frame.destroy()
            clientMain.ClientMain(loginId)

        Back = Button(myTitle, text="<<", font=("Product Sans", 16, "bold"))
        Back.place(x=10, y=4)
        Back.config(bg="#4D50F1", fg="white", activeforeground="white", activebackground="#4D50F1",
                    borderwidth=0, command=toMoveBack)

        tree = ttk.Treeview(frame)
        tree['show'] = "headings"
        # jitna headings mein chahta hoon utna he dikhaaye aur apna blank space add na kareee.

        # to get the styles
        styles = ttk.Style()
        styles.theme_use("clam")
        styles.configure(".", font=("Product Sans", 14))
        styles.configure("Treeview.Heading", foreground="#4D50F1", font=('Product Sans', 11, "bold"), background="white",
                         borderwidth=0)

        tree["columns"] = ("ID", "NAME", "TITLE", "SEM", "PRICE",
                           "DONATION", "CONTACT", "CONDITION", "DESCRIPTION")
        tree.column("ID", width=10, minwidth=50, anchor=CENTER)
        tree.column("NAME", width=50, minwidth=50, anchor=CENTER)
        tree.column("TITLE", width=50, minwidth=50, anchor=CENTER)
        tree.column("SEM", width=50, minwidth=50, anchor=CENTER)
        tree.column("PRICE", width=50, minwidth=50, anchor=CENTER)
        tree.column("DONATION", width=50, minwidth=50, anchor=CENTER)
        tree.column("CONTACT", width=50, minwidth=50, anchor=CENTER)
        tree.column("CONDITION", width=50, minwidth=50, anchor=CENTER)
        tree.column("DESCRIPTION", width=50, minwidth=50, anchor=CENTER)

        tree.heading("ID", text="ID", anchor=CENTER)
        tree.heading("NAME", text="NAME", anchor=CENTER)
        tree.heading("TITLE", text="TITLE", anchor=CENTER)
        tree.heading("SEM", text="SEMESTER", anchor=CENTER)
        tree.heading("PRICE", text="PRICE", anchor=CENTER)
        tree.heading("DONATION", text="DONATION", anchor=CENTER)
        tree.heading("CONTACT", text="CONTACT", anchor=CENTER)
        tree.heading("CONDITION", text="CONDITION", anchor=CENTER)
        tree.heading("DESCRIPTION", text="DESCRIPTION", anchor=CENTER)

        i = 0
        for row in database.myQuery:
            if row[0] % 2 == 0:
                tree.insert('', i, text="",
                            values=(
                                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]),
                            tags=("even",))
            else:
                tree.insert('', i, text="",
                            values=(
                                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]),
                            tags=("odd",))
            i = i + 1

        tree.tag_configure(
            "even", background="#4D50F1", foreground="white")
        tree.tag_configure("odd", background="white",
                           foreground="#4D50F1")
        tree.bind("<Double-1>", lambda event: view_details())

        horiScrollBar = ttk.Scrollbar(frame, orient="horizontal")
        tree.configure(xscrollcommand=horiScrollBar.set)
        horiScrollBar.pack(fill=X, side="bottom")

        veriScrollBar = ttk.Scrollbar(frame, orient="vertical")
        tree.configure(xscrollcommand=horiScrollBar.set)
        veriScrollBar.pack(fill=Y, side="right")

        tree.place(x=0, y=50, width=1286, height=668)
        frame.mainloop()


if __name__ == "__main__":
    newPage = RentTable(4)
