import tkinter as tk
from lib.cboslib import versioncheck
from lib.cboslib import version
from lib.cboslib import magicball

def show_main_page():
    if version_frame:
        version_frame.pack_forget()
    if magic_eight_ball_frame:
        magic_eight_ball_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)

def show_version_page():
    versionchecks = versioncheck(version)
    latestversion = versionchecks.latestversion
    installedversion = versionchecks.version
    available = versionchecks.available

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
    
    version_label = tk.Label(version_frame, text=available, font=("Helvetica", 20), fg="white", bg="black")
    version_label.pack(pady=10)
    
    test_label = tk.Label(version_frame, text=f"Latest Version: {latestversion}", font=("Helvetica", 16), fg="white", bg="black")
    test_label.pack(pady=10)

    test_label = tk.Label(version_frame, text=f"Installed Version: {installedversion}", font=("Helvetica", 16), fg="white", bg="black")
    test_label.pack(pady=10)

def show_magic_eight_ball_page():
    if main_frame:
        main_frame.pack_forget()
    if version_frame:
        version_frame.pack_forget()
    
    global magic_eight_ball_frame
    magic_eight_ball_frame = tk.Frame(root, bg='black')
    magic_eight_ball_frame.pack(fill='both', expand=True)
    
    back_button_frame = tk.Frame(magic_eight_ball_frame, bg="white", padx=1, pady=1)
    back_button_frame.pack(anchor='nw', padx=10, pady=10)
    
    back_button = tk.Button(back_button_frame, text="Back", font=("Helvetica", 16), fg="white", bg="black", 
                            borderwidth=0, command=show_main_page, width=10)
    back_button.pack()
    add_button_effect(back_button)

    # Header label for Magic Eight Ball
    header_label = tk.Label(magic_eight_ball_frame, text="Magic Eight Ball", font=("Helvetica", 24), fg="white", bg="black")
    header_label.pack(pady=(20, 10))

    global entry
    entry = tk.Entry(magic_eight_ball_frame, font=("Helvetica", 16), width=30)
    entry.pack(pady=20)
    entry.bind("<Return>", get_magic_eight_ball_result)

def get_magic_eight_ball_result(event):
    global entry
    result = magicball()
    entry.delete(0, tk.END)
    entry.insert(0, result)

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

# Main button frame
button_frame = tk.Frame(main_frame, bg="white", padx=1, pady=1)
button_frame.pack(pady=10)

help_button = tk.Button(button_frame, text="Version", font=("Helvetica", 16), fg="white", bg="black", 
                        borderwidth=0, command=show_version_page, width=10)
help_button.pack()
add_button_effect(help_button)

# Separate frame for Magic Eight Ball button
magic_eight_ball_button_frame = tk.Frame(main_frame, bg="white", padx=1, pady=1)
magic_eight_ball_button_frame.pack(pady=(5, 10))

magic_eight_ball_button = tk.Button(magic_eight_ball_button_frame, text="Magic Eight Ball", font=("Helvetica", 16), fg="white", bg="black", 
                                    borderwidth=0, command=show_magic_eight_ball_page, width=20)
magic_eight_ball_button.pack()
add_button_effect(magic_eight_ball_button)

version_frame = None
magic_eight_ball_frame = None
entry = None  # Initialize entry as None

root.mainloop()
