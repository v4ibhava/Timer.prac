import datetime
import tkinter as tk

def countdown():
    global t, paused
    if t.total_seconds() <= 0:
        timere.set('Timer completed!')
        return
    if not paused:
        timer = datetime.datetime(1, 1, 1) + t
        timerbet = timer.strftime("%M:%S.%f")[:-3]
        timere.set(timerbet)
        t -= datetime.timedelta(milliseconds=10)
    khidki.after(10, countdown)

def toggle_timer():
    global t, paused, toggle_button_text
    if toggle_button_text.get() == "Start":
        seconds = int(input_entry.get())
        t = datetime.timedelta(seconds=seconds)
        paused = False
        countdown()
        toggle_button_text.set("Pause")
    elif toggle_button_text.get() == "Pause":
        paused = True
        toggle_button_text.set("Resume")
    elif toggle_button_text.get() == "Resume":
        paused = False
        countdown()
        toggle_button_text.set("Pause")

khidki = tk.Tk()
khidki.title("Countdown Timer")

timere = tk.StringVar()
timer_label = tk.Label(khidki, font=("Arial", 20), bg="white", fg="black", textvariable=timere)
timer_label.pack(fill="both", expand=True)

input_entry = tk.Entry(khidki, font=("Arial", 20), justify="center")
input_entry.pack(fill="both", expand=True)

label = tk.Label(khidki, text="Enter the value in seconds", font=("Arial", 11))
label.pack()

toggle_button_text = tk.StringVar()
toggle_button_text.set("Start")
toggle_button = tk.Button(khidki, textvariable=toggle_button_text, font=("Arial", 15), command=toggle_timer)
toggle_button.pack()

t = datetime.timedelta()
paused = False

khidki.mainloop()
