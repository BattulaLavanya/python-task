from tkinter import *
import requests
import json
import pprint
import random
import html
from tkinter import messagebox as mb

def qna(url):
    global Question, ans, correct_ans
    r = requests.get(url)
    if (r.status_code != 200):
        end = input("Sorry, there was a problem retrive the question. Press enter to try again or type 'quit' to quit the game.")
    else:
        print("ok")
        q= json.loads(r.text)
##        pprint.pprint(q)
        ##print(type(q))
        user_ans = 0
        answers = []
        Question = q['results'][0]['question']
        correct_ans = q['results'][0]['correct_answer']
        answers = q['results'][0]['incorrect_answers']
        answers.append(correct_ans)
        a = []
        random.shuffle(answers)
        s=len(answers)
        a = []
        for i in range(s):
            a.append(i+1)
        ans = dict(zip(a, answers))
        return Question, ans, correct_ans

def Submit():
    global Question, ans, correct_ans, v,p,Total_count,Correct_count,Incorrect_count
    if v.get() == "0":
        selection = "Please enter option."
        mb.showwarning('Not correct', selection)
    elif v.get() == correct_ans:
        Total_count+=1
        Correct_count+=1
        selection = "Correct option " + str(v.get())
        selection1 =  "Total_count = "+ str(Total_count) +"\t Correct_count = " + str(Correct_count) + "\t Incorrect_count = " + str(Incorrect_count)
    elif v.get() != correct_ans:
        Total_count+=1
        Incorrect_count+=1
        selection = "Incorrect option " + str(v.get()) + ". Correct option is " + correct_ans 
        selection1 = "Total_count = "+ str(Total_count)+ "\t Correct_count = " + str(Correct_count) + "\t Incorrect_count = " + str(Incorrect_count)
    if v.get()!= "0":
        if mb.askyesno('answer', selection+'\nDo you want to contine?'):
            clearFrame()
            label = Label(window)
            label.pack(fill='x', padx=15, pady=15)
            label.config(text = selection1)
            qus_gen(p)
        else:
            window.destroy()
    

    

window=Tk()
window.title('JSON used project using API')
window.geometry("800x800")
window.resizable(True, False)
Total_count = 0
Correct_count = 0
Incorrect_count = 0
##url = "https://opentdb.com/api.php?amount=1&difficulty=easy"

def url1():
    global z, p
    urls = {"ANY":"https://opentdb.com/api.php?amount=1&difficulty=easy",
           "COMPUTER":"https://opentdb.com/api.php?amount=1&category=18",
           "MATHEMATICS":"https://opentdb.com/api.php?amount=1&category=19",
           "VEHICLES":"https://opentdb.com/api.php?amount=1&category=28",
           "GADGETS":"https://opentdb.com/api.php?amount=1&category=30",
           "CARTOON & ANIMATIONS":"https://opentdb.com/api.php?amount=10&category=32"}
    z = StringVar(window, "-1")
    for (text, value) in urls.items():
            Radiobutton(window, text = text, variable = z,
                            value = value).pack(fill='x', padx=5, pady=5)
    Butt1 = Button(window, text ="ok", command = ok)
    Butt1.pack(fill='x', padx=5, pady=5)


def ok():
    global z, p
    if z.get() == "-1":
        selection = "Please enter url."
        mb.showwarning('Not correct', selection)
    elif z.get()!= "-1":
        clearFrame()
        p=z.get()
        qus_gen(z.get())
   
def qus_gen(url):
    global v
    v = StringVar(window, "0")
    b = qna(url)
    question = html.unescape(b[0])
    answer = html.unescape(b[1])
    lbl=Label(window, text=question, fg='black', font=("Times", "12", "bold"))
    lbl.pack(fill='x', padx=5, pady=5)
    for (text, value) in answer.items():
        Radiobutton(window, text = value, variable = v,
                        value = value).pack(fill='x', padx=5, pady=5)

    Butt = Button(window, text ="Submit", command = Submit)
    Butt.pack(fill='x', padx=5, pady=5)
    print("Thanks for playing")
    label = Label(window)
    label.pack(fill='x', padx=5, pady=5)
    window.mainloop()


def clearFrame():
    # destroy all widgets from frame
    for widget in window.winfo_children():
       widget.destroy()

url1()


