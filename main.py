import math

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
	global reps
	
	reps = 0
	window.after_cancel(timer)
	title_label.config(text="Timer",fg=GREEN)
	canvas.itemconfig(timer_text, text="00:00")
	checkmark_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
	global reps
	
	sec_short_break = SHORT_BREAK_MIN * 60
	sec_work = WORK_MIN * 60
	sec_long_break = LONG_BREAK_MIN * 60
	
	reps +=1
	if reps % 8 == 0:
		title_label.config(text= "Break",fg=RED)
		count_down(sec_long_break)
	elif reps % 2 == 1:
		title_label.config(text="Work")
		count_down(sec_work)
	else:
		title_label.config(text="Break",fg=PINK)
		count_down(sec_short_break)
	
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down (count):
	global timer
	
	count_minutes = math.floor(count / 60)
	count_seconds = count % 60
	
	if count_seconds <= 9:
		count_seconds = "0"+str(count_seconds)
		
	canvas.itemconfig(timer_text,text=f"{count_minutes}:{count_seconds}")
	# if count == 0:
	# 	filename = 'Cinematic_9_311_SP.wav'
	# 	wave_obj = sa.WaveObject.from_wave_file(filename)
	# 	play_obj = wave_obj.play()
	# 	play_obj.wait_done()  # Wait until sound has finished playing
	if count > 0:
		timer= window.after(1000, count_down, count-1)
	else:
		start_timer()
		marks=""
		work_sessions = math.floor(reps/2)
		for _ in range(work_sessions):
			marks += "✓"
		checkmark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
import simpleaudio as sa


from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=20,pady=20)
#The padding resolves the issues with spacing with the padding
window.config(padx=100,pady=50,bg=YELLOW)

#Title Label
title_label= Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50,"bold"))
title_label.grid(column=1,row=0)

#Canvas
#"hightlightthickness" refers to the edge of canvas that was not part of background
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
#Tkinter provide the exact location of file needed by Canvas.
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


#highlightthickness=0 - removes the border discoloring
#Start Button
start_button = Button(text="Start",highlightthickness=0,command= start_timer)
start_button.grid(column=0,row=2)

#Reset Button
reset_button = Button(text="Reset",highlightthickness=0,command= reset_timer)
reset_button.grid(column=2,row=2)

#Check Mark Label
checkmark_label = Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,20,"bold"))
checkmark_label.grid(column=1,row=3)


window.mainloop()