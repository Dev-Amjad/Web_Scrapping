import tkinter as tk
from tkinter import PhotoImage, END,messagebox
import ReadExeclFile
import WriteExcelFile

window = tk.Tk()
window.title("Web Scrapper")

def show_Error():
    messagebox.showerror('Error', 'kindly, enter BBC website URL only')

def get_Command():
    command=''
    url = text.get()
    if url=="https://www.bbc.com/urdu" or url=="www.bbc.com/urdu" or url=="www.bbc.com":
        WriteExcelFile.parse_and_write_data()
    else:
        show_Error()

#centre and size the window
window_width = 1180
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)

bg = PhotoImage(file = "Background.png")

label1 = tk.Label(window, image = bg)
label1.place(x = 0, y = 0)

label = tk.Label(text='Enter Website Link ',font=('fantasy 10'),width=20)
label.place(x=270,y=22)
text = tk.Entry(textvariable="",font=('fantasy 12'),width=35,relief='groove',borderwidth=2)
text.place(x=445,y=20)
button = tk.Button(text='Start Scrapping',bg='maroon4',fg='white',command=get_Command,font=('Arial 16 bold'))
button.place(x=500,y=75)
label1 = tk.Label(text='Shortest/Longest Story In Dataset:',font=('Arial 16 bold'),bg='#34495E')
label1.place(x=70,y=180)
button1 = tk.Button(text='View',bg='#27AE60',fg='white',command=ReadExeclFile.smallest_and_longest_story,font=('Arial 16 bold'))
button1.place(x=1000,y=180)
label3 = tk.Label(text='Most Frequent Words In Dataset',font=('Arial 16 bold'),bg='#34495E')
label3.place(x=82,y=260)
button3 = tk.Button(text='View',bg='#27AE60',fg='white',command=ReadExeclFile.k_times_Most_Reapeated,font=('Arial 16 bold'))
button3.place(x=1000,y=260)
label4 = tk.Label(text='Number Of Unique Words',font=('Arial 16 bold'),bg='#34495E')
label4.place(x=110,y=340)
button4 = tk.Button(text='View',bg='#27AE60',fg='white',command=ReadExeclFile.find_Unique_Words,font=('Arial 16 bold'))
button4.place(x=1000,y=340)
label5 = tk.Label(text='Volumes Of Categories',font=('Arial 16 bold'),bg='#34495E')
label5.place(x=120,y=420)
button5 = tk.Button(text='View',bg='#27AE60',fg='white',command=ReadExeclFile.find_times_of_category,font=('Arial 16 bold'))
button5.place(x=1000,y=420)
label6 = tk.Label(text='Visualize The Dataset:',font=('Arial 16 bold'),bg='#34495E')
label6.place(x=125,y=500)
button6 = tk.Button(text='View',bg='#27AE60',fg='white',command=ReadExeclFile.visualize_Data,font=('Arial 16 bold'))
button6.place(x=1000,y=500)

window.iconbitmap('./icon.ico')
window.mainloop()