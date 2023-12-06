import speedtest
import tkinter as tk
import tkinter.font as tkFont
from tkinter import Label
import threading
def check_internet_speed():
    tests = 0
    errors = 0
    while True:
        tests += 1
        try:
            st = speedtest.Speedtest(secure=True)
            st.get_best_server()
            download_speed = st.download() / 1000000
            upload_speed = st.upload() / 1000000
            download_speed_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
            upload_speed_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")
            internet_status_label.config(text="Internet is connected", fg="white", highlightbackground="green", highlightthickness=4)
        except Exception as e:
            print(e)
            download_speed_label.config(text="Download Speed: N/A")
            upload_speed_label.config(text="Upload Speed: N/A")
            internet_status_label.config(text="Internet is not connected", fg="white", highlightbackground="red", highlightthickness=4)
            errors += 1
        print(f"{errors} / {tests} have run into an error")
root = tk.Tk()
root.title("WIFI Tester")
root.geometry("450x250")
root.resizable(False, False)
root.configure(bg="black")
font = tkFont.nametofont("TkDefaultFont")
font.configure(size=18)
download_speed_label = Label(root, text="Testing Internet Speed...", fg="white", bg="black", font=font)
download_speed_label.pack()
upload_speed_label = Label(root, text="", fg="white", bg="black", font=font)
upload_speed_label.pack()
internet_status_label = Label(root, text="Checking internet status...", fg="black", bg="black", font=font)
internet_status_label.pack()
thread = threading.Thread(target=check_internet_speed)
thread.daemon = True
thread.start()
root.mainloop()