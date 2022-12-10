from tkinter import *
from tkinter import messagebox
from customtkinter import * 
from functools import partial
import cv2
import time
import datetime
from tkVideoPlayer import TkinterVideo
System ={}

def LiveFeed():
    cap = cv2.VideoCapture(0)

    messagebox.showinfo("Information","To Quit the Live Feed Press Q")
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    body_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_fullbody.xml")

    detection = False
    detection_stopped_time = None
    timer_started = False
    SECONDS_TO_RECORD_AFTER_DETECTION = 5

    frame_size = (int(cap.get(3)), int(cap.get(4)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        bodies = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) + len(bodies) > 0:
            if detection:
                timer_started = False
            else:
                detection = True
                current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                out = cv2.VideoWriter(
                    f"{current_time}.mp4", fourcc, 20, frame_size)
                print("Started Recording Faces Recognized ")
        elif detection:
            if timer_started:
                if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                    detection = False
                    timer_started = False
                    out.release()
                    print('Stopped Recording No Faces Recognized')
            else:
                timer_started = True
                detection_stopped_time = time.time()

        if detection:
            out.write(frame)

        # for (x, y, width, height) in faces:
        #    cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 3)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break
def AccessLoginSystem():
    Username = username.get()
    Password = password.get()
    if System!={}:
        if Username in System:
            if System[Username][0] == Password:
                messagebox.showinfo("Information","Login Successfu!")
                app.switch_frame(PageThree)
            else:
                 messagebox.showinfo("Information","Password do not match")
        else:  
            messagebox.showinfo("Information","Username is not Registered")       
    else:
        messagebox.showinfo("Information","No Accounts Registered")
    return


def AccessRegistrationSystem():
    Username = username.get()
    Password = password.get()
    Password_confirmation = password2.get()
    if Username in System:
        messagebox.showinfo("Information","Username already exists!")
        return 

    if (Password != Password_confirmation):
        messagebox.showinfo("Information","Passwords do not match")
        return

    if Password == "":
        messagebox.showinfo("Information","Please Enter Password")
        return  

    if Username != "":
        System[Username]=[Password,fullName.get(),number.get(),email.get()]
        messagebox.showinfo("Information","Registration Successful")
        app.switch_frame(PageOne)
    return

def RecordedFeed():
    global videoplayer
    videoplayer = TkinterVideo(app, scaled=False)
    videoplayer.load(r"C:\Users\Khalid\ECCE-336-Project-1\Y2Mate.is - Twins climb out of cots-f_rQqVkEXOU-360p-1654154339715.mp4")
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play() 
    app.switch_frame(PageSix)
    

def CameraFeed():
    videoplayer.destroy()
    app.switch_frame(PageFour)

class app(CTk):
    def __init__(self):
        CTk.__init__(self)
        set_appearance_mode("dark") 
        set_default_color_theme("dark-blue") 
        self._frame = None
        self.title("Baby Monitor Application")
        self.switch_frame(StartPage)
        self.geometry("300x450")
        

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        CTkLabel(self, text="Baby Monitor").pack(side="top", fill="x", pady=10)
        CTkButton(self, text="Login",
                  command=lambda: master.switch_frame(PageOne)).pack(pady=10)
        CTkButton(self, text="Registration",
                  command=lambda: master.switch_frame(PageTwo)).pack(pady=10)
        


class PageOne(CTkFrame):
    def __init__(self, master):
        
        CTkFrame.__init__(self, master)
        CTkLabel(self, text="Login Page:").pack(side="top", fill="x", pady=10)

        global username
        username = StringVar()
        CTkLabel(self, text="Username:",anchor="w").pack(side="top", fill="x", pady=10)
        entry_1 = CTkEntry(master=self, placeholder_text="",textvariable=username)
        entry_1.pack()

        global password
        password = StringVar()
        CTkLabel(self, text="Password:",anchor="w").pack(side="top", fill="x", pady=10)
        entry_1 = CTkEntry(master=self, placeholder_text="",show='*',textvariable=password)
        entry_1.pack()

        checkbox_1 = CTkCheckBox(master=self,text="Remember Me")
        checkbox_1.pack(pady=10, padx=10)

        CTkButton(self, text="Login",
                command=AccessLoginSystem).pack(pady=10)

        
        CTkButton(self, text="Return to start page",
                command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(CTkFrame):
    def __init__(self, master):
        
        
        CTkFrame.__init__(self, master)
        CTkLabel(self, text="Registration Page:").pack(side="top", fill="x")

        global username
        global fullName
        global number
        global email
        global password
        global password2
        
        fullName = StringVar()
        number = StringVar()
        email = StringVar()
        username = StringVar()
        password = StringVar()
        password2 = StringVar()

        CTkLabel(self, text="Full Name:",anchor="w").pack(side="top", fill="x")
        entry_1 = CTkEntry(master=self, placeholder_text="",textvariable=fullName).pack()
       
        CTkLabel(self, text="Phone Number:",anchor="w").pack(side="top", fill="x")
        entry_2 = CTkEntry(master=self, placeholder_text="",textvariable=number).pack()

        CTkLabel(self, text="Email:",anchor="w").pack(side="top", fill="x")
        entry_3 = CTkEntry(master=self, placeholder_text="",textvariable=email).pack()

        CTkLabel(self, text="Username:",anchor="w").pack(side="top", fill="x")
        entry_4 = CTkEntry(master=self, placeholder_text="",textvariable=username).pack()

        CTkLabel(self, text="Password:",anchor="w").pack(side="top", fill="x")
        entry_5 = CTkEntry(master=self, placeholder_text="",show="*",textvariable=password).pack()

        CTkLabel(self, text="Confirm Password:",anchor="w").pack(side="top", fill="x")
        entry_6 = CTkEntry(master=self, placeholder_text="",show="*",textvariable=password2).pack()

        

        CTkButton(self, text="Register",
                command=AccessRegistrationSystem).pack(pady=10)

        CTkButton(self, text="Return to start page",
                command=lambda: master.switch_frame(StartPage)).pack()
        
class PageThree(CTkFrame):
    def __init__(self, master):
        
        CTkFrame.__init__(self, master)
        CTkLabel(self, text="Main Menu:").pack(side="top", fill="x", pady=10)

        CTkButton(self, text="Camera Feed",
                command=lambda: master.switch_frame(PageFour)).pack(pady=10)

        CTkButton(self, text="Notification Feed",
                command=lambda: master.switch_frame(PageFive)).pack(pady=10)

        
        CTkButton(self, text="Log Out",
                command=lambda: master.switch_frame(StartPage)).pack(pady=10)    

class PageFour(CTkFrame):
    def __init__(self, master):
        
        CTkFrame.__init__(self, master)
        CTkLabel(self, text="Camera Feed:").pack(side="top", fill="x", pady=10)

        CTkButton(self, text="Live Camera Feed",
                command= LiveFeed).pack(pady=10)

        CTkButton(self, text="Recorded Camera Feed",
                command=RecordedFeed).pack(pady=10)

        
        CTkButton(self, text="Return to Main Menu",
                command=lambda: master.switch_frame(PageThree)).pack(pady=10) 

class PageFive(CTkFrame):
    def __init__(self, master):
        
        CTkFrame.__init__(self, master)
        CTkLabel(self, text="Notification Feed:").pack(side="top", fill="x", pady=10)

        text_1 = CTkTextbox(master=self, width=200, height=140)
        text_1.pack(pady=10, padx=10)
        text_1.insert("0.0", "")
        
        CTkButton(self, text="Return to Main Menu",
                command=lambda: master.switch_frame(PageThree)).pack(pady=10) 

class PageSix(CTkFrame):
    def __init__(self, master):
        CTkFrame.__init__(self, master)
        CTkLabel(self, text="Recorded Camera Feed:").pack(side="top", fill="x", padx=10)
        CTkButton(self, text="Back to Camera Feed",command=CameraFeed).pack(padx=10)
        


if __name__ == "__main__":
    app = app()
    app.mainloop()
