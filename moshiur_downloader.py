import os,sys
os.system("pip install tkinter")
os.system("pip install yt-dlp")
os.system("pip install threading")
os.system("pip install --upgrade yt-dlp")
import os
os.system('cls' if os.name == 'nt' else 'clear')



import tkinter as tk
from tkinter import ttk
import os
import yt_dlp
import threading

def update_progress(d, progress_var, speed_var):
    downloaded_bytes = d.get('downloaded_bytes', 0)  # ডাউনলোড হওয়া সাইজ
    total_bytes = d.get('total_bytes')  # মোট সাইজ

    if total_bytes:  # total_bytes থাকলে হিসাব কর
        percent = (downloaded_bytes / total_bytes) * 100
    else:
        percent = 0  # total_bytes না থাকলে 0%

    progress_var.set(f"{percent:.2f}%")
    
    # Speed যদি None হয়, তাহলে 0.00 B/s সেট কর
    speed = d.get('speed', 0) or 0
    speed_var.set(f"{speed:.2f} B/s")

def download_video(url, progress_var, speed_var):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]+bestvideo[ext=mp4]',
        'progress_hooks': [lambda d: update_progress(d, progress_var, speed_var)],
        'outtmpl': '/home/moshiur/downloader/downloads/%(title)s.%(ext)s',
        'noplaylist': True,
        'nooverwrites': False,  # আগের ফাইল থাকলেও নতুন করে নামাবে
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio(url, progress_var, speed_var):
    ydl_opts = {
        'format': 'bestaudio',
        'extractaudio': True,
        'audioformat': 'mp3',
        'progress_hooks': [lambda d: update_progress(d, progress_var, speed_var)],
        'outtmpl': '/home/moshiur/downloader/downloads/%(title)s.%(ext)s',
        'noplaylist': True,
        'nooverwrites': False,  # আগের ফাইল থাকলেও নতুন করে নামাবে
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



def on_select(option, url_entry, progress_var, speed_var):
    url = url_entry.get()
    
    # Start download in a separate thread to keep GUI responsive
    if option == "Video":
        threading.Thread(target=download_video, args=(url, progress_var, speed_var)).start()
    elif option == "Audio":
        threading.Thread(target=download_audio, args=(url, progress_var, speed_var)).start()

def create_gui():
    global root
    root = tk.Tk()
    root.title("YouTube Downloader")

    # Set window size and background
    root.geometry("500x350")
    root.configure(bg='black')
    root.tk_setPalette(background="#2e2e2e")  # Dark background color
    root.resizable(False, False)
    
    # Center align the window
    window_width = 500
    window_height = 350
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_left = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')
    
    # Set rounded corners using Canvas
    canvas = tk.Canvas(root, height=350, width=500, bg='#2e2e2e', bd=0, highlightthickness=0)
    canvas.pack()

    # Header label
    header_label = tk.Label(root, text="YouTube Downloader", fg='white', bg='black', font=('San Francisco', 16, 'bold'))
    header_label.place(x=150, y=10)

    # URL entry label
    url_label = tk.Label(root, text="Enter Video URL:", fg='white', bg='black', font=('San Francisco', 12))
    url_label.place(x=20, y=60)

    # URL Entry
    url_entry = tk.Entry(root, bg='white', fg='black', font=('San Francisco', 12), width=40)
    url_entry.place(x=20, y=90)

    # Dropdown Menu for Video/Audio
    option_label = tk.Label(root, text="Select Download Option:", fg='white', bg='black', font=('San Francisco', 12))
    option_label.place(x=20, y=130)

    options = ["Video", "Audio"]
    option_menu = ttk.Combobox(root, values=options, state="readonly", width=37)
    option_menu.place(x=20, y=160)

    # Progress Bar
    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(root, length=400, variable=progress_var, maximum=100)
    progress_bar.place(x=20, y=200)

    # Download Speed Label
    speed_var = tk.StringVar()
    speed_label = tk.Label(root, textvariable=speed_var, fg='white', bg='black', font=('San Francisco', 12))
    speed_label.place(x=20, y=230)

    # Download Button
    download_button = tk.Button(root, text="Download", bg='#00b300', fg='white', font=('San Francisco', 12), command=lambda: on_select(option_menu.get(), url_entry, progress_var, speed_var))
    download_button.place(x=100, y=270)

    # Exit Button
    exit_button = tk.Button(root, text="Exit", bg='#ff3333', fg='white', font=('San Francisco', 12), command=root.quit)
    exit_button.place(x=250, y=270)

    # Footer Text
    footer_label = tk.Label(root, text="All credit goes to Moshiur Rahman", fg='white', bg='black', font=('San Francisco', 10))
    footer_label.place(x=150, y=310)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
