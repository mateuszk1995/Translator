from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def translate():
    """ function to translate languages"""
    translator = Translator()
    translated = translator.translate(text=input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)


mainWindow = Tk()
mainWindow.title("Translator by shakalek")
mainWindow.geometry("1024x400")
mainWindow.configure(background="ghost white")
mainWindow.resizable(0, 0)

#   Top and bottom labels
Label(mainWindow, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='white smoke').pack()
Label(mainWindow, text="Copyright MK", font='arial 20 bold', bg='white smoke', width='20')\
    .pack(side='bottom')

#   Input and Output text widget
Label(mainWindow, text="Enter Text", font="arial 13 bold", background="white smoke").place(x=200, y=60)
input_text = Text(mainWindow, font="arial 10", height=11, wrap=WORD, padx=5, pady=5, width=60)
input_text.place(x=30, y=100)

Label(mainWindow, text="Output Text", font="arial 13 bold", background="white smoke").place(x=600, y=60)
output_text = Text(mainWindow, font="arial 10", height=11, wrap=WORD, padx=5, pady=5, width=60)
output_text.place(x=600, y=100)

#   Language import
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(mainWindow, values=language, width=25)
src_lang.place(x=20, y=60)
src_lang.set('Choose Input Language')

dest_lang = ttk.Combobox(mainWindow, values=language, width=25)
dest_lang.place(x=790, y=60)
dest_lang.set('Choose Output Language')

#   Translate button
trans_btn = Button(mainWindow, text='Translate', font='arial 12 bold', pady=5, command=translate, bg='royal blue1',
                   activebackground='sky blue')
trans_btn.place(x=490, y=180)

#   Run the program
mainWindow.mainloop()

