import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer", fg=GREEN)
    global reps
    reps = 0
    label_check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_seconds)
        label_title.config(text="Break",fg=RED)
        reps = 0
    elif reps % 2 == 0:
        countdown(short_break_seconds)
        label_title.config(text="Break", fg=PINK)
    else:
        countdown(work_seconds)
        label_title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        global timer
        timer = (window.after(1000, countdown, count - 1))
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label_check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50)
window.config(bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image( 100,112,image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1)

label_title = Label(text="Timer", fg=GREEN, bg=YELLOW  ,font=(FONT_NAME, 55, "bold"), anchor="center", width=7)
label_title.grid(row=0, column=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command =reset_timer)
button_reset.grid(row=2, column=2)

label_check_mark = Label(text="", bg=YELLOW, fg=GREEN,font=(FONT_NAME, 18, "bold"))
label_check_mark.grid(row=3, column=1)

window.mainloop()