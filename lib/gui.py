import tkinter as tk
from lib.cboslib import versioncheck
from lib.cboslib import version
from lib.cboslib import getversion

def show_main_page():
    version_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)

def show_version_page():
    latestversion = getversion(version).latestversion
    installedversion = getversion(version).version

    main_frame.pack_forget()
    
    global version_frame
    version_frame = tk.Frame(root, bg='black')
    version_frame.pack(fill='both', expand=True)
    
    back_button_frame = tk.Frame(version_frame, bg="white", padx=1, pady=1)
    back_button_frame.pack(anchor='nw', padx=10, pady=10)
    
    back_button = tk.Button(back_button_frame, text="Back", font=("Helvetica", 16), fg="white", bg="black", 
                            borderwidth=0, command=show_main_page, width=10)
    back_button.pack()
    add_button_effect(back_button)
    
    version_label = tk.Label(version_frame, text=versioncheck(version), font=("Helvetica", 20), fg="white", bg="black")
    version_label.pack(pady=10)
    
    test_label = tk.Label(version_frame, text=f"Latest Version: {latestversion}", font=("Helvetica", 16), fg="white", bg="black")
    test_label.pack(pady=10)

    test_label = tk.Label(version_frame, text=f"Installed Version: {installedversion}", font=("Helvetica", 16), fg="white", bg="black")
    test_label.pack(pady=10)

def add_button_effect(button):
    button.bind("<Enter>", lambda e: button.config(bg="gray20"))
    button.bind("<Leave>", lambda e: button.config(bg="black"))
    button.bind("<Button-1>", lambda e: button.config(bg="gray40"))
    button.bind("<ButtonRelease-1>", lambda e: button.config(bg="black"))

root = tk.Tk()
root.title("C-Bos GUI (Beta)")
root.geometry("1300x800")

main_frame = tk.Frame(root, bg='black')
main_frame.pack(fill='both', expand=True)

title_label = tk.Label(main_frame, text="C-Bos GUI (Beta)", font=("Helvetica", 24), fg="white", bg="black")
title_label.pack(pady=20)

button_frame = tk.Frame(main_frame, bg="white", padx=1, pady=1)
button_frame.pack(pady=10)

help_button = tk.Button(button_frame, text="Version", font=("Helvetica", 16), fg="white", bg="black", 
                        borderwidth=0, command=show_version_page, width=10)
help_button.pack()
add_button_effect(help_button)

version_frame = None

root.mainloop()