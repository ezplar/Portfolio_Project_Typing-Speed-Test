from tkinter import *
from wonderwords import RandomWord


window = Tk()
window.title("Typing Speed Test")
window.configure(padx=10, pady=10, background='gray')
window.geometry("1200x400")


canvas = Canvas(window,height=17,width=20)
canvas.grid(column=5,row=0)
# canvas.configure(width=800,height=400)

cpm_score = 0
seconds = 60

def key_pressed(event):
    # space = Label(text="Key Press: "+event.char)
    print(event.keysym, event.keysym == "space")
    print(event)
    global cpm_score
    cpm_score += len(event.char)
    cpm.config(text=cpm_score)
    print(cpm_score)

    if event.keysym == "BackSpace":
        cpm_score -= 1

    if cpm_score == 1:
        update_clock()

    if event.keysym == "space":
        cpm_score -= 1
        get_text()

####Check key press to check input in entry
def get_text():
    global wpm_score
    text = input_text.get()
    if text in word_list_space:
        word_list_space.remove(text)
        print(word_list_space)
        input_text.delete(0,'end')

        words.delete('1.0', "end")
        for wrd in word_list_space:
            words.insert(END,wrd)

        wpm_score = int(cpm_score / 5)

        wpm.config(text=wpm_score)
        print(wpm_score)
        input_text.configure(fg="black")

        words.tag_add('text','1.0',f'1.{len(word_list_space[0])}')
        words.tag_config('text',background='light green')
    else:
        input_text.configure(fg="red")

def update_clock():
    global clock_text
    clock_text = seconds
    canvas.itemconfig(clock,text=clock_text)
    global ws
    ws = window.after(1000,dec_time)
    if seconds < 11:
        canvas.itemconfig(clock,fill='red')

    if seconds <= 0:
        window.after_cancel(ws)
        input_text.config(state="disabled")
        window.unbind("<KeyPress>")
        words.config(state="disabled")

def dec_time():
    global seconds
    seconds -= 1
    update_clock()

def restart():
    word_list_space = []
    ran_word = RandomWord()
    for w in range(10):
        item = ran_word.word(include_parts_of_speech=['verbs', 'adjectives'])
        word_list_space.append(item + " ")

    words.delete('1.0', "end")
    words.insert(END, word_list_space)

    cpm_score = 0
    cpm.config(text=cpm_score)
    wpm_score = 0
    wpm.config(text=wpm_score)

    window.after_cancel(ws)
    seconds = 0
    canvas.itemconfig(clock, text=clock_text)



# Labels
correct_cpm_label = Label(text="Corrected CPM: ", background='gray')
correct_cpm_label.grid(column=0, row=0)

wpm_label = Label(text="WPM: ", background='gray')
wpm_label.grid(column=2, row=0, columnspan=2)

time_left_label = Label(text="Time Left: ", background='gray')
time_left_label.grid(column=4, row=0, columnspan=2)

# Texts
cpm = Label(height=1, width=3)
cpm.grid(column=1, row=0)

wpm = Label(height=1, width=3)
wpm.grid(column=3, row=0)

time_left = Label(height=1, width=3)
# time_left.grid(column=5, row=0)

word_list_space = []
word_list_display = []
ran_word = RandomWord()
for w in range(50):
    item = ran_word.word(include_parts_of_speech=['verbs','adjectives'],word_min_length=2,word_max_length=8)
    word_list_display.append(item)
    word_list_space.append(item+" ")

words = Text(height=10, width=60, font=("Arial",20,))
words.grid(column=2, row=2, columnspan=3)

words.config(state="normal")
for wrd in word_list_space:
    words.insert(END, wrd)

words.tag_add('text','1.0',f'1.{len(word_list_space[0])}')
words.tag_config('text',background='light green')


input_text = Entry(width=50,font=("Arial",20))
input_text.grid(column=2, row=4, columnspan=3)
input_text.focus_set()


reset_button = Button(text="Restart", command=restart)
# reset_button.grid(column=7,row=0)


clock = canvas.create_text(11,11,font=('', 10), fill="black")
# update_clock()

window.bind("<KeyPress>", key_pressed)

window.mainloop()

#For Improvement/future development
# Restart function
