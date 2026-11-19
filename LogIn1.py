import tkinter as tk


class mainPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Page")
        self.root.geometry("400x300")
        self.root.configure(bg="lightblue")
        self.frame1 = tk.Frame(self.root, bg="lightblue")
        self.labelF1 = tk.Label(self.root, text="Welcome to the Denikab Main Page!", font=("Helvetica", 16), bg="lightblue")
        self.labelF1.pack(pady=50)
        self.labelF2 = tk.Label(self.root, text="This is the main page of the application.", font=("Helvetica", 12), bg="lightblue")
        self.labelF2.pack(pady=10)
        self.frame1.pack(pady=20, fill='both', expand=True)
        self.frame2 = tk.Frame(self.root, bg="lightblue")
        self.labelF3 = tk.Label(self.root, text="Please log in to continue.", font=("Helvetica", 12), bg="lightblue")
        self.labelF3.pack(pady=10)
        self.frame2.pack(pady=20, fill='both', expand=True)
        self.button1 = tk.Button(self.root, text="Log In", command=self.open_login_window)
        self.button1.pack(pady=20)

        self.root.mainloop()

    def open_login_window(self):
        self.loginWindow = tk.Toplevel(self.root)
        self.loginWindow.title("Log In")
        self.loginWindow.geometry("300x200")
        self.label1 = tk.Label(self.loginWindow, text="Username:")
        self.label1.pack(pady=10)
        self.entry1 = tk.Entry(self.loginWindow)
        self.entry1.pack(pady=5)
        self.label2 = tk.Label(self.loginWindow, text="Password:")
        self.label2.pack(pady=10)
        self.entry2 = tk.Entry(self.loginWindow, show="*")
        self.entry2.pack(pady=5)
        self.button2 = tk.Button(self.loginWindow, text="Submit", command=self.submit_login)
        self.button2.pack(pady=20)
        self.loginWindow.protocol("WM_DELETE_WINDOW", self.on_login_window_close)

    def submit_login(self):
        username = self.entry1.get()
        password = self.entry2.get()
        # Here you can add your login logic to verify the username and password
        print(f"Username: {username}, Password: {password}")
        self.loginWindow.destroy()

    def on_login_window_close(self):
        self.loginWindow.destroy()


if __name__ == "__main__":
    mainPage()
        