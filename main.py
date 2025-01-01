import ttkbootstrap as ttk

def open_dashboard():
    root = ttk.Window(themename="solar")
    root.title("داشبورد")
    root.geometry("300x200")

    ttk.Label(root, text="به داشبورد خوش آمدید!", font=("Arial", 16)).pack(pady=20)
    ttk.Button(root, text="خروج", command=root.destroy).pack(pady=20)

    root.mainloop()
