import tkinter

class UI:

    def __init__(self):

        self.username =  None
        self.password = None

        self.window = tkinter.Tk()
        self.window.title("Pixela")
        self.window.geometry("1045x800")

        # SIGNIN WINDOW - BACKGROUND IMAGE.
        self.bg_signin_image = tkinter.PhotoImage(file="images/signin_bg.png")
        self.signin_canvas = tkinter.Canvas(self.window, width=1045, height=800, bd= 0, highlightthickness= 0)
        self.signin_canvas.create_image(521, 400, image=self.bg_signin_image)
        self.signin_canvas.place(x=0, y=0)

        # USERNAME INPUT AREA.
        self.signin_canvas_username_text = tkinter.Entry(self.window, width= 20, font=('arial', 20, 'bold'), bg= "white",
                                          bd=0, highlightthickness=0, fg= "gray")
        self.signin_canvas_username_text.place(x=410, y=220)

        # PASSWORD INPUT AREA.
        self.signin_canvas_password_text = tkinter.Entry(self.window, width= 20, font=('arial', 20, 'bold'), bg= "white",
                                          bd=0, highlightthickness=0, fg= "gray", show= "*")
        self.signin_canvas_password_text.place(x=410, y=295)

        # LOGIN BUTTON.
        self.login_button = self.signin_canvas.create_rectangle(385, 378, 650, 410, fill="", outline="", stipple="gray25")
        # Bind the click event to the rectangle
        self.signin_canvas.tag_bind(self.login_button, "<Button-1>", self.click_login)


    def exit_window(self):
        self.window.mainloop()

    def click_login(self, event):
        self.username = self.signin_canvas_username_text.get()
        self.password = self.signin_canvas_password_text.get()

ui = UI()
ui.exit_window()