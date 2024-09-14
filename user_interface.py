import tkinter

class UI:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Pixela")
        self.window.geometry("1045x800")

        self.bg_signin_image = tkinter.PhotoImage(file="images/signin_bg.png")
        self.signin_canvas = tkinter.Canvas(self.window, width=1045, height=800, bd= 0, highlightthickness= 0)
        self.signin_canvas.create_image(521, 400, image=self.bg_signin_image)

        self.signin_canvas.place(x=0, y=0)

    def exit_window(self):
        self.window.mainloop()


ui = UI()
ui.exit_window()