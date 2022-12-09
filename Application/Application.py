import tkinter
import customtkinter as ctk

def AccessLoginSystem():
    print("Login")

def AccessRegistrationSystem():
    print("Register")

def RecordedFeed():
    print("Recorded Feed")

def LiveFeed():
    print("Live Feed")

class app(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        self._frame = None
        self.title("Baby Monitor Application")
        self.switch_frame(StartPage)
        self.geometry("600x600")

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self, text="Baby Monitor").pack(side="top", fill="x", pady=10)
        ctk.CTkButton(self, text="Login",
                  command=lambda: master.switch_frame(PageOne)).pack(pady=10)
        ctk.CTkButton(self, text="Registration",
                  command=lambda: master.switch_frame(PageTwo)).pack(pady=10)
        


class PageOne(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self, text="Login Page:").pack(side="top", fill="x", pady=10)

        ctk.CTkLabel(self, text="Username:",anchor="w").pack(side="top", fill="x", pady=10)
        entry_1 = ctk.CTkEntry(master=self, placeholder_text="")
        entry_1.pack()

        ctk.CTkLabel(self, text="Password:",anchor="w").pack(side="top", fill="x", pady=10)
        entry_1 = ctk.CTkEntry(master=self, placeholder_text="",show='*')
        entry_1.pack()

        checkbox_1 = ctk.CTkCheckBox(master=self,text="Remember Me")
        checkbox_1.pack(pady=10, padx=10)

        ctk.CTkButton(self, text="Login",
                command=lambda: master.switch_frame(PageThree)).pack(pady=10)

        
        
        ctk.CTkButton(self, text="Return to start page",
                command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self, text="Registration Page:").pack(side="top", fill="x")

        ctk.CTkLabel(self, text="Full Name:",anchor="w").pack(side="top", fill="x")
        entry_1 = ctk.CTkEntry(master=self, placeholder_text="")
        entry_1.pack()

        ctk.CTkLabel(self, text="Phone Number:",anchor="w").pack(side="top", fill="x")
        entry_1 = ctk.CTkEntry(master=self, placeholder_text="")
        entry_1.pack()

        ctk.CTkLabel(self, text="Username:",anchor="w").pack(side="top", fill="x")
        entry_1 = ctk.CTkEntry(master=self, placeholder_text="")
        entry_1.pack()

        ctk.CTkLabel(self, text="Password:",anchor="w").pack(side="top", fill="x")
        entry_1 = ctk.CTkEntry(master=self, placeholder_text="",show="*")
        entry_1.pack()

        ctk.CTkLabel(self, text="Confirm Password:",anchor="w").pack(side="top", fill="x")
        entry_1 = ctk.CTkEntry(master=self, placeholder_text="",show="*")
        entry_1.pack()

        ctk.CTkButton(self, text="Register",
                command=lambda: master.switch_frame(PageOne)).pack(pady=10)

        
        
        ctk.CTkButton(self, text="Return to start page",
                command=lambda: master.switch_frame(StartPage)).pack()
class PageThree(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self, text="Main Menu:").pack(side="top", fill="x", pady=10)

        ctk.CTkButton(self, text="Camera Feed",
                command=lambda: master.switch_frame(PageFour)).pack(pady=10)

        ctk.CTkButton(self, text="Notification Feed",
                command=lambda: master.switch_frame(PageFive)).pack(pady=10)

        
        ctk.CTkButton(self, text="Log Out",
                command=lambda: master.switch_frame(StartPage)).pack(pady=10)    

class PageFour(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self, text="Camera Feed:").pack(side="top", fill="x", pady=10)

        ctk.CTkButton(self, text="Live Camera Feed",
                command=LiveFeed).pack(pady=10)

        ctk.CTkButton(self, text="Recorded Camera Feed",
                command=RecordedFeed).pack(pady=10)

        
        ctk.CTkButton(self, text="Return to Main Menu",
                command=lambda: master.switch_frame(PageThree)).pack(pady=10) 

class PageFive(ctk.CTkFrame):
    def __init__(self, master):
        
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self, text="Notification Feed:").pack(side="top", fill="x", pady=10)

        text_1 = ctk.CTkTextbox(master=self, width=200, height=140)
        text_1.pack(pady=10, padx=10)
        text_1.insert("0.0", "")
        
        ctk.CTkButton(self, text="Return to Main Menu",
                command=lambda: master.switch_frame(PageThree)).pack(pady=10) 

if __name__ == "__main__":
    app = app()
    app.mainloop()
