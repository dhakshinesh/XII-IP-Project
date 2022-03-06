from tkinter import *
import signup


def home_content():
    #Home_window
    window_home = Tk()
    window_home.geometry("1000x600")
    window_home.configure(bg = "#ffffff")
    #functions
    def open_signup_page():
        window_home.destroy()
        signup.signup_content()

    Button(text="Hello", command=open_signup_page).pack()
    window_home.mainloop()

home_content()