import pandas as pd
import numpy as np
import tkinter as tk
from matplotlib import pyplot as plt
from collections import Counter


def show_On_Desktop(result):
    root = tk.Tk()

    # Centre the GUI
    window_width = 700
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.resizable(False, False)

    # Create text widget and specify size.
    text_Board = tk.Text(root, height=500, width=700)

    # Create label
    label = tk.Label(root, text="Results")
    label.config(font=("Courier", 14))

    label.pack()
    text_Board.pack()

    # Insert The result.
    text_Board.insert(tk.END, result)

    tk.mainloop()

def get_Dataset():
    excel_File = 'News Stories.xlsx'
    file = pd.read_excel(excel_File, usecols=['Headline', 'Category', 'Story'])
    return file

def visualize_Data():

    data=get_Dataset()
    np_array = np.array(data['Category'])
    df = pd.value_counts(np_array)
    labels = ['Pakistan', 'Neighbour', 'World', 'Science', 'Actors', 'Sports']
    plt.bar(df.index,df.values)
    plt.xticks(df.index,labels)
    plt.title('Number of records for each category.')
    plt.xlabel('Category')
    plt.ylabel('Number of records')
    plt.style.use('bmh')
    plt.show()
    return

def remove_special_chars(str):

    str = str.replace(':', '')
    str = str.replace('‘', '')
    str = str.replace('؟', '')
    str = str.replace('،', '')
    str = str.replace('’', '')
    str = str.replace('۔', '')

    return str

def get_title(row):
    str=row[1][0].strip()
    return str

def get_story(row):
    str=row[1][2].strip()
    return str

def get_category(row):
    str=row[1][1].strip()
    return str

def list_of_words_in_a_row(row):
    title = get_title(row)
    story = get_story(row)
    category =get_category(row)
    single_Entity = title+ " " + " " + story + " " + category
    single_Entity=remove_special_chars(single_Entity)

    words = []
    words = single_Entity.split()

    return words

def find_Unique_Words():
    data = get_Dataset()
    collec = []
    for row in data.iterrows():
        words = []
        words = list_of_words_in_a_row(row)
        for word in words:
            if word not in collec:
                collec.append(word)
    result="There are total "+str(len(collec))+" unique words in the entire dataSet."
    show_On_Desktop(result)

def k_times_Most_Reapeated():
    number=10
    data = get_Dataset()
    most_Repeated_words=Counter()

    for row in data.iterrows():
        words = list_of_words_in_a_row(row)
        #Conter method counts the words in the list
        most_Repeated_words += Counter(words)
        #we would pass the top number we need
        tp_words=most_Repeated_words.most_common(number)

    words_On_New_line=""
    for word in tp_words:
        words_On_New_line+=str(word)+"\n"

    show_On_Desktop(words_On_New_line)

def find_times_of_category():
    data = get_Dataset()
    pakistan = 0
    sport = 0
    science = 0
    lollywood = 0
    near_Ones = 0
    world = 0
    Categories = data['Category'].values
    for row in Categories:
        if row == 'پاکستان':
            pakistan += 1
        elif row == 'آس پاس':
            near_Ones += 1
        elif row == 'ورلڈ':
            world += 1
        elif row == 'کھیل':
            sport += 1
        elif row == 'فن فنکار':
            lollywood += 1
        elif row == 'سائنس':
            science += 1
    list1 = [pakistan,near_Ones,world,sport,lollywood,science]
    list2 = ['پاکستان','آس پاس','ورلڈ','کھیل','فن فنکار','سائنس']

    results=""
    counter=0
    for l in list2:

        results+=l+" : "+str(list1[counter])+"\n"
        counter+=1

    show_On_Desktop(results)

def smallest_and_longest_story():
    data = get_Dataset()
    data =data['Story'].values
    longest_Story = ''
    smallest_Story = data[0]

    for story in data:
        if len(longest_Story) < len(story):
            longest_Story = story
        if len(smallest_Story) > len(story) :
            smallest_Story = story
    result="(1)Longest Story"+"\n"+longest_Story+"\n\n\n"+"(2)Smallest Story"+"\n"+smallest_Story

    show_On_Desktop(result)



