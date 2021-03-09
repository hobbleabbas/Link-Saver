from tkinter import *
import requests
import re
from bs4 import BeautifulSoup
import time

root = Tk()
 
file_w = open('links.txt', 'a')
file_r = open('links.txt', 'r') 


link_below = Label(root, text = 'Enter your link below')
link_below.pack()

e = Entry(root, width = 50)
e.pack()

def makeTitle():
    link = e.get()
    yes_lebl = Label(root, text = 'Please enter a title:')
    yes_lebl.pack()
    title = Entry(root, width = 50)
    title.pack()

    submit_title = Button(root, text = "Submit Title", command = writeTitle(title.get()))
    submit_title.pack()



def writeTitle(title):
    fullref = title + ': ' + e.get() + '\n'
    file_w.write(fullref)
    time.sleep(2)

    output = Label(root, text = "Awesome, saved!")
    output.pack()
    output.after(1000, output.destroy)

def dontMakeTitle(): 
    title = 'No Title'
    fullref = title + ': ' + e.get() + '\n'
    file_w.write(fullref)
    output = Label(root, text = "No worries, your link has been saved!")
    output.pack()


confirm_below_yes = Button(root, text = 'Yes', command = makeTitle)
confirm_below_no = Button(root, text = 'No', command = dontMakeTitle)

def myClick():
    link = e.get()

    matches = re.search("youtube", link)

    if matches == None:
        ask_for_title = Label(root, text = "This isn't a youtube video, would you like to add a title to reference from?")
        ask_for_title.pack()
        confirm_below_yes.pack()
        confirm_below_no.pack()
    else:
        temp_output = Label(root, text = "Working...")
        temp_output.pack()

        r = requests.get(link)

        soup = BeautifulSoup(r.content, 'html.parser')

        content = soup.find_all('meta', property = 'og:title')

        for items in content:
            title = items.get("content")

        fullref = title + ': ' + link + '\n'
        file_w.write(fullref)

        output = Label(root, text = "Awesome, saved!")
        output.pack()



title_below = Entry(root, text = 'Add your preferred title below')
e2 = Entry(root, width = 50)


e.get()

myButton = Button(root, text = 'Save Link', command = myClick)
myButton.pack()

your_links_title = Label(root, text = "Your Existing Links")
# your_links_title.pack()

for x in file_r:
    existing_link = Label(root, text = x)
    existing_link.pack()

root.mainloop()

# if matches == None:
#         want_title =  input("This isn't a youtube video, would you like to add a title to reference from? (Y/N)")
        
#         if want_title == 'Y':
#             title = input('Please enter a title:\n')
#             fullref = title + ': ' + link + '\n'
#             file_w.write(fullref)
#             output = Label(root, text = "Awesome, saved!")
#             output.pack()
#         elif want_title == 'y':
#             title = input('Please enter a title:\n')
#             fullref = title + ': ' + link + '\n'
#             file_w.write(fullref)
#             output = Label(root, text = "Awesome, saved!")
#             output.pack()
#         else:
#             title = 'No Title'
#             fullref = title + ': ' + link + '\n'
#             file_w.write(fullref)
#             output = Label(root, text = "No worries, your link has been saved!")
#             output.pack()
#     else:
#         temp_output = Label(root, text = "Working...")
#         temp_output.pack()
#         r = requests.get(link)

#         soup = BeautifulSoup(r.content, 'html.parser')

#         content = soup.find_all('meta', property = 'og:title')

#         for items in content:
#             title = items.get("content")

#         fullref = title + ': ' + link + '\n'
#         file_w.write(fullref)
#         output = Label(root, text = "Awesome, saved!")
#         output.pack()

