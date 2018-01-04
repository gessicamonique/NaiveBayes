# Python 3.5

# Imports

from tkinter import *
import bib_naive_bayes

# Main window
# Janela principal

window_main = Tk()
window_main.title("NAIVE BAYES.PY") 
window_main["bg"] = "light blue" 
window_main.geometry("1350x690+0+0")

# News entry
# Entrada da noticia

lbNews = Label(text = "Enter the news here",font = "Helvetica 12 bold", fg = "Navy blue")
lbNews["bg"] = "light blue" 
lbNews.place(x = 15, y = 10)

input_news=Entry(window_main, width=200)
input_news.place(x = 15, y = 60)

# Exit label
# Label de saída

lb_status = Label(font = "Helvetica 120 bold", fg = "Navy blue")
lb_status["bg"] = "light blue" 
lb_status.place(x = 15, y = 280)

# Ok Button
# Botão OK

def bt_OK_click():
    if(bt_OK["text"] == "OK"):
        news = input_news.get()
        status = bib_naive_bayes.naive_bayes(news.upper())
        if(status[0] >= 0.7):
            lb_status["text"] =  "Popular\n" + status[1]
        else:
            lb_status["text"] =  "Não Popular\n" + status[1]
        bt_OK["text"] = "Clear Fields"
    else: 
        input_news.delete(0, END) 
        lb_status["text"] = "" 
        bt_OK["text"] = "OK" 
        
   
bt_OK = Button(window_main, width=20, text="OK", fg = "white", bg = "Navy blue", font = "Courier 12 bold")
bt_OK["command"]=bt_OK_click
bt_OK.place(x = 15, y = 110) 

mainloop()



