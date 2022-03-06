from tkinter import *
import home

def signup_content():
    #signup_window
    window_signup = Tk()
    window_signup.geometry("1000x600")
    window_signup.configure(bg = "#ffffff")
    #functions
    def open_home_page():
        window_signup.destroy()
        home.home_content()

    def submit_info():
        print("username:",entry0.get(),"password:",entry1.get(),"Confirm Password:",entry2.get())

    canvas = Canvas(
        window_signup,
        bg = "#ffffff",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        500.0, 300.0,
        image=background_img)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = submit_info,
        relief = "flat")

    b0.place(
        x = 433, y = 523,
        width = 171,
        height = 44)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        525.5, 244.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 356.0, y = 211,
        width = 339.0,
        height = 64)

    entry1_img = PhotoImage(file = f"img_textBox1.png")
    entry1_bg = canvas.create_image(
        525.5, 350.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry1.place(
        x = 356.0, y = 317,
        width = 339.0,
        height = 64)

    entry2_img = PhotoImage(file = f"img_textBox2.png")
    entry2_bg = canvas.create_image(
        525.5, 456.0,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry2.place(
        x = 356.0, y = 423,
        width = 339.0,
        height = 64)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = open_home_page,
        relief = "flat")

    b1.place(
        x = 0, y = 0,
        width = 57,
        height = 49)

    window_signup.resizable(False, False)
    window_signup.mainloop()
