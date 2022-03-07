from tkinter import *
import signup

def btn_clicked():
    print("Button Clicked")

def home_content():
    window_home = Tk()
    window_home.geometry("1440x1024")
    window_home.configure(bg = "#10f46c")

    def open_signup_page():
        window_home.destroy()
        signup.signup_content()
    canvas = Canvas(
        window_home,
        bg = "#10f46c",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"D:\BUSINEESN APPLICATION PROJECT\GUI FLODER FROM FIGMA AND PROXLIGHT\Proxlight_Designer_Export\Proxlight_Designer_Export/background.png")
    background = canvas.create_image(
        293.0, 368.5,
        image=background_img)

    img0 = PhotoImage(file = f"D:\BUSINEESN APPLICATION PROJECT\GUI FLODER FROM FIGMA AND PROXLIGHT\Proxlight_Designer_Export\Proxlight_Designer_Export/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 0, y = 12,
        width = 162,
        height = 63)

    img1 = PhotoImage(file = f"D:\BUSINEESN APPLICATION PROJECT\GUI FLODER FROM FIGMA AND PROXLIGHT\Proxlight_Designer_Export\Proxlight_Designer_Export/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = open_signup_page ,
        relief = "flat")

    b1.place(
        x = 621, y = 432,
        width = 214,
        height = 80)

    img2 = PhotoImage(file = f"D:\BUSINEESN APPLICATION PROJECT\GUI FLODER FROM FIGMA AND PROXLIGHT\Proxlight_Designer_Export\Proxlight_Designer_Export\img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place(
        x = 617, y = 512,
        width = 222,
        height = 88)

    img3 = PhotoImage(file = f"D:\BUSINEESN APPLICATION PROJECT\GUI FLODER FROM FIGMA AND PROXLIGHT\Proxlight_Designer_Export\Proxlight_Designer_Export/img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b3.place(
        x = 1287, y = 20,
        width = 153,
        height = 43)

    window_home.resizable(False, False)
    window_home.mainloop()

home_content()
