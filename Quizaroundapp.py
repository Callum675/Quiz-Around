#---------------
#Quiz Around App
#Callum mcintosh
#2021
#v1.00
#---------------

class quiz:

    def __init__(self):
        #user input
        self.qnumber = 1
        self.topic = "Mixed"
        #quiz data
        self.qcurrent = 1
        self.score = 0
        #current question data
        self.question = ["Questions: "]
        self.correct_answer = ["Correct Answer: "]
        self.option1 = ["Option 1: "]
        self.option2 = ["Option 2: "]
        self.option3 = ["Option 3: "]
        self.option4 = ["Option 4: "]
        #gui data
        self.q_gui = False

    #getter
    def get_qnumber(self):
        return self.qnumber

    def get_topic(self):
        return self.topic

    def get_qcurrent(self):
        return self.qcurrent

    def get_question(self, x):
        return self.question[x]

    def get_option1(self, x):
        return self.option1[x]

    def get_option2(self, x):
        return self.option2[x]

    def get_option3(self, x):
        return self.option3[x]

    def get_option4(self, x):
        return self.option4[x]

    def get_correct_answer(self, x):
        return self.correct_answer[x]

    def get_score(self):
        return self.score

    def get_q_gui(self):
        return self.q_gui

    #setters
    def set_number(self, x):
        self.qnumber = x
        print(self.qnumber)

    def set_topic(self, x):
        self.topic = x
        print(self.topic)

    def set_q_gui(self, x):
        self.q_gui = x
        print(self.q_gui)

    #other
    def gen_quiz(self):
        if (self.topic == "Mixed"):
            cursor = conn.execute("SELECT * FROM tblQuestions ORDER BY RANDOM()")
            row = cursor.fetchone()
            for x in range(int(self.qnumber)):
                self.question.append(row[2])
                print("added " + self.question[x])
                
                self.option1.append(row[3])
                print("added " + self.option1[x])
                
                self.option2.append(row[4])
                print("added " + self.option2[x])
                
                self.option3.append(row[5])
                print("added " + self.option3[x])
                
                self.option4.append(row[6])
                print("added " + self.option4[x])
                
                self.correct_answer.append(row[7])
                print("added " + str(self.correct_answer[x]))

                #move to next line in database
                row = cursor.fetchone()
        else:
            cursor = conn.execute("SELECT * FROM tblQuestions WHERE Topic == ? ORDER BY RANDOM()", [self.topic,])
            row = cursor.fetchone()
            for x in range(int(self.qnumber)):
                self.question.append(row[2])
                print("added " + self.question[x])
                
                self.option1.append(row[3])
                print("added " + self.option1[x])
                
                self.option2.append(row[4])
                print("added " + self.option2[x])
                
                self.option3.append(row[5])
                print("added " + self.option3[x])
                
                self.option4.append(row[6])
                print("added " + self.option4[x])
                
                self.correct_answer.append(row[7])
                print("added " + str(self.correct_answer[x]))

                #move to next line in database
                row = cursor.fetchone()
        
    def add_score(self):
        #adds 1 to score
        self.score = self.score + 1

    def reset(self):
        #resets values
        self.qcurrent = 1
        self.score = 0
        self.question = ["Questions: "]
        self.correct_answer = ["Correct Answer: "]
        self.option1 = ["Option 1: "]
        self.option2 = ["Option 2: "]
        self.option3 = ["Option 3: "]
        self.option4 = ["Option 4: "]
        
    
    def next_question(self):
        #changes the pointer for questions
        self.qcurrent = self.qcurrent + 1

#imports
import sys, sqlite3
from datetime import datetime
import time as t
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image

now = datetime.now()
q = quiz()

#conecting database
conn = None
try:
    conn = sqlite3.connect('QuizAround.db')
except Error as e:
    print(e)
    tkinter.messagebox.showinfo("Database ERROR", "Error: " + e)
else:
    print ("Opened database successfully");
    

def generate_quiz():
    #valadation and inputs
    if (selected_number.get() == "Select a Number"):
        print("Error: Please select a value for number of questions")
        tkinter.messagebox.showinfo("ERROR", "Error: Please select a value for number of questions")
        sys.exit()
    else:
        q.set_number(selected_number.get())

    if(selected_topic.get() == "Select a Topic"):
        print("Error: Please select a topic")
        tkinter.messagebox.showinfo("ERROR", "Error: Please select a topic")
        sys.exit()
    else:
        q.set_topic(selected_topic.get())
    
    #reset
    q.reset()

    #destroy old window
    if (q.get_q_gui() == True):
        quiz.destroy()
    else:
        q.set_q_gui(True)
    
    #generate quiz
    q.gen_quiz()
    
    #create gui
    quiz_gui()

def quiz_gui():    
    #gui
    global quiz
    quiz = tk.Toplevel()
    #window config
    quiz.title("Quiz Around - Quiz")
    quiz.geometry('760x450')
    quiz.resizable(width=False, height=False)

    #creating gui elements
    #frames
    q_header_frame = tk.Frame(quiz, bg="DodgerBlue2", height=80)
    q_content_spacer_frame = tk.Frame(quiz, bg="white", height=25)
    #content frames
    q_content_frame_qnumber = tk.Frame(quiz, bg="white")
    q_content_frame_question = tk.Frame(quiz, bg="white")
    q_content_frame_option1 = tk.Frame(quiz, bg="white")
    q_content_frame_option2 = tk.Frame(quiz, bg="white")
    q_content_frame_option3 = tk.Frame(quiz, bg="white")
    q_content_frame_option4 = tk.Frame(quiz, bg="white")
    q_content_frame_buttons = tk.Frame(quiz, bg="white")
    q_footer_frame = tk.Frame(quiz, bg="DodgerBlue2", height=40)
    #spacer frames
    q_content_spacer_frame_question = tk.Frame(q_content_frame_question, bg="white", height=10, width = 15)
    q_content_spacer_frame_option1 = tk.Frame(q_content_frame_option1, bg="white", height=10, width = 15)
    q_content_spacer_frame_option2 = tk.Frame(q_content_frame_option2, bg="white", height=10, width = 15)
    q_content_spacer_frame_option3 = tk.Frame(q_content_frame_option3, bg="white", height=10, width = 15)
    q_content_spacer_frame_option4 = tk.Frame(q_content_frame_option4, bg="white", height=10, width = 15)
    q_content_spacer_frame_buttons = tk.Frame(q_content_frame_buttons, bg="white", height=10, width = 15)
    q_content_spacer_frame_buttons2 = tk.Frame(q_content_frame_buttons, bg="white", height=10, width = 5)

    #global elements for updating
    global q_lbl_qnumber
    global q_lbl_question
    global q_lbl_score
    global q_rad_option1
    global q_rad_option2
    global q_rad_option3
    global q_rad_option4

    #images
    q_logo = Image.open("images/QuizLogo.png")
    q_logo = q_logo.resize((80, 80), Image.ANTIALIAS)
    q_img_header = ImageTk.PhotoImage(q_logo)
    q_lbl_header_logo = tk.Label(q_header_frame, image=q_img_header, bg="DodgerBlue2")
    q_lbl_header_logo.image = q_img_header

    #labels
    q_lbl_header_text = tk.Label(q_header_frame, text="Quiz Around", fg="white", bg="DodgerBlue2", font=("Arial", 20))
    q_lbl_qnumber = tk.Label(q_content_frame_qnumber, text="Question " + str(q.get_qcurrent()), bg="white", font=("Arial", 16))
    q_lbl_question = tk.Label(q_content_frame_question, text=q.get_question(q.get_qcurrent()), bg="white", font=("Arial", 12))
    q_lbl_score = tk.Label(q_footer_frame, text="Score: " + str(q.get_score()) + "/" +str(q.get_qnumber()), fg="white", bg="DodgerBlue2", font=("Arial", 8))

    #radio buttons
    global ans
    ans = tk.IntVar(quiz)
    q_rad_option1 = tk.Radiobutton(q_content_frame_option1, text=q.get_option1(q.get_qcurrent()), bg="white", font=("Arial", 12), variable=ans, value=1, cursor="hand2")
    q_rad_option2 = tk.Radiobutton(q_content_frame_option2, text=q.get_option2(q.get_qcurrent()), bg="white", font=("Arial", 12), variable=ans, value=2, cursor="hand2")
    q_rad_option3 = tk.Radiobutton(q_content_frame_option3, text=q.get_option3(q.get_qcurrent()), bg="white", font=("Arial", 12), variable=ans, value=3, cursor="hand2")
    q_rad_option4 = tk.Radiobutton(q_content_frame_option4, text=q.get_option4(q.get_qcurrent()), bg="white", font=("Arial", 12), variable=ans, value=4, cursor="hand2")
    
    #buttons
    q_btn_submit = tk.Button(q_content_frame_buttons, text="Submit Answer",font=("Arial", 12),  fg="black", bg="white",  cursor="hand2", activebackground = "light grey", command=check_answer)
    q_btn_save = tk.Button(q_content_frame_buttons, text="Save Quiz",font=("Arial", 12),  fg="black", bg="white",  cursor="hand2", activebackground = "light grey", command=save_quiz)

    #placing on gui
    #primary frames
    q_header_frame.pack(fill='both')
    q_content_spacer_frame.pack(fill='both')
    q_content_frame_qnumber.pack(fill='both', expand = True)
    q_content_frame_question.pack(fill='both', expand = True)
    q_content_frame_option1.pack(fill='both', expand = True)
    q_content_frame_option2.pack(fill='both', expand = True)
    q_content_frame_option3.pack(fill='both', expand = True)
    q_content_frame_option4.pack(fill='both', expand = True)
    q_content_frame_buttons.pack(fill='both', expand = True)
    q_footer_frame.pack(fill='both', side='bottom')
    #header frame
    q_lbl_header_logo.pack(side="left")
    q_lbl_header_text.pack(side="left")
    #content frames
    q_lbl_qnumber.pack(side="top")

    q_content_spacer_frame_question.pack(side="left")
    q_lbl_question.pack(side="left")

    q_content_spacer_frame_option1.pack(side="left")
    q_rad_option1.pack(side="left")

    q_content_spacer_frame_option2.pack(side="left")
    q_rad_option2.pack(side="left")

    q_content_spacer_frame_option3.pack(side="left")
    q_rad_option3.pack(side="left")

    q_content_spacer_frame_option4.pack(side="left")
    q_rad_option4.pack(side="left")
    
    q_content_spacer_frame_buttons.pack(side="left")
    q_btn_submit.pack(side="left")
    q_content_spacer_frame_buttons2.pack(side="left")
    q_btn_save.pack(side="left")
    #footer frame
    q_lbl_score.pack(side="right")
    
def update_quiz_gui():
    if(q.get_qcurrent() > int(q.get_qnumber())):
        q_lbl_score.config(text="Score: " + str(q.get_score()) + "/" +str(q.get_qnumber()))
        tkinter.messagebox.showinfo("Quiz Finished", "Congratulations, you got " + str(q.get_score()) + "/" +str(q.get_qnumber()) + "\n Quiz will close in 10 secounds", icon="question")
        quiz.after(10000, quiz.destroy)
    else:
        q_lbl_qnumber.config(text="Question " + str(q.get_qcurrent()))
        q_lbl_question.config(text=q.get_question(q.get_qcurrent()))
        q_rad_option1.config(text=q.get_option1(q.get_qcurrent()))
        q_rad_option2.config(text=q.get_option2(q.get_qcurrent()))
        q_rad_option3.config(text=q.get_option3(q.get_qcurrent()))
        q_rad_option4.config(text=q.get_option4(q.get_qcurrent()))
        q_lbl_score.config(text="Score: " + str(q.get_score()) + "/" +str(q.get_qnumber()))

def check_answer():
    x = ans.get()
    print("User Answer: " + str(x))
    if (x == q.get_correct_answer(q.get_qcurrent())):
        print("Correct Answer")
        q.add_score()
        tkinter.messagebox.showinfo("Correct Answer", "Correct Answer, Well Done", icon="question")
    else:
        print("Incorrect Answer")
        tkinter.messagebox.showinfo("Incorrect Answer", "Incorrect Answer, Correct Answer was option" + str(q.get_correct_answer(q.get_qcurrent())), icon="question")
    q.next_question()
    update_quiz_gui()

def save_quiz():
    
    f = open("Quiz/Quiz.txt","w+")
    i = 1
    for i in range(int(q.get_qnumber()) + 1):
        f.write(q.get_question(i) + "\n")
    for i in range(int(q.get_qnumber()) + 1):
        f.write(q.get_option1(i) + "\n")
    for i in range(int(q.get_qnumber()) + 1):
        f.write(q.get_option2(i) + "\n")
    for i in range(int(q.get_qnumber()) + 1):
        f.write(q.get_option3(i) + "\n")
    for i in range(int(q.get_qnumber()) + 1):
        f.write(q.get_option4(i) + "\n")
    for i in range(int(q.get_qnumber()) + 1):
        f.write(str(q.get_correct_answer(i)) + "\n")
    f.close()
    tkinter.messagebox.showinfo( "File Created", "File containing quiz questions and answers has been created and saved to your device")

def update_time():
    #function that desplays a system time on the app
    info = "Local time: " + t.strftime('%H:%M:%S') + " " + now.strftime('%d/%m/%Y')
    lbl_time['text'] = info
    home.after(1000,update_time)

#gui
home = tk.Tk()
#window config
home.title("Quiz Around")
home.geometry('300x340')
home.resizable(width=False, height=False)

#creating gui elements
#frames
header_frame = tk.Frame(home, bg="DodgerBlue2", height=80)
content_spacer_frame = tk.Frame(home, bg="white", height=25)
content_frame = tk.Frame(home, bg="white")
content_spacer_frame2 = tk.Frame(content_frame, bg="white", height=25)
content_spacer_frame3 = tk.Frame(content_frame, bg="white", height=25)
footer_frame = tk.Frame(home, bg="DodgerBlue2", height=40)

#images
logo = Image.open("images/QuizLogo.png")
logo = logo.resize((80, 80), Image.ANTIALIAS)
img_header = ImageTk.PhotoImage(logo)
lbl_header_logo = tk.Label(header_frame, image=img_header, bg="DodgerBlue2")
lbl_header_logo.image = img_header

#labels
lbl_header_text = tk.Label(header_frame, text="Quiz Around", fg="white", bg="DodgerBlue2", font=("Arial", 20))
lbl_prompt_num = tk.Label(content_frame, text="Number of Questions", bg="white", font=("Arial", 12))
lbl_prompt_topic = tk.Label(content_frame, text="Topic", bg="white", font=("Arial", 12))
lbl_time = tk.Label(footer_frame, fg="white", bg="DodgerBlue2", font=("Arial", 8))

#buttons
btn_quiz = tk.Button(content_frame, text="Generate Quiz",font=("Arial", 12),  fg="black", bg="white",  cursor="hand2", activebackground = "light grey", command=generate_quiz)

#options menu for number input
number = ["1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "11",
          "12",
          "13",
          "14",
          "15",
          "16",
          "17",
          "18",
          "19",
          "20"]

selected_number = tk.StringVar(home) 
selected_number.set("Select a Number")

number_menu = tk.OptionMenu(content_frame,  selected_number, *number)
number_menu.config(width=18, font=("Arial", 12), bg="white", cursor="hand2")
number_menu['menu'].config(font=("Arial", 12), bg="white")

#options menu for topic input
topics = ["Mixed",
          "Movies",
          "History",
          "Food",
          "Science"]

selected_topic = tk.StringVar(home) 
selected_topic.set("Select a Topic")

topic_menu = tk.OptionMenu(content_frame,  selected_topic, *topics)
topic_menu.config(width=18, font=("Arial", 12), bg="white", cursor="hand2")
topic_menu['menu'].config(font=("Arial", 12), bg="white")

#placing on gui
#primary frames
header_frame.pack(fill='both')
content_spacer_frame.pack(fill='both')
content_frame.pack(fill='both', expand = True)
footer_frame.pack(fill='both', side='bottom')
#header frame
lbl_header_logo.pack(side="left")
lbl_header_text.pack(side="left")
#content frame
lbl_prompt_num.pack()
number_menu.pack()
content_spacer_frame2.pack(fill='both')
lbl_prompt_topic.pack()
topic_menu.pack()
content_spacer_frame3.pack(fill='both')
btn_quiz.pack()
#footer frame
lbl_time.pack(side="right")

#main program loop
update_time()
home.mainloop()
