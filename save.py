import requests
import re
from bs4 import BeautifulSoup

file_w = open('links.txt', 'a')
file_r = open('links.txt', 'r')

print("Welcome to the links app, courtesy of Shakeel. You can save links here, and if they're YouTube videos I automatically save the title")
link = input("Enter the URL\n")

matches = re.search("youtube", link)

if matches == None:
    want_title =  input("This isn't a youtube video, would you like to add a title to reference from? (Y/N)")
    
    if want_title == 'Y':
        title = input('Please enter a title:\n')
        fullref = title + ': ' + link + '\n'
        file_w.write(fullref)
        print("Awesome, saved!")
    elif want_title == 'y':
        title = input('Please enter a title:\n')
        fullref = title + ': ' + link + '\n'
        file_w.write(fullref)
        print("Awesome, saved!")
    else:
        title = 'No Title'
        fullref = title + ': ' + link + '\n'
        file_w.write(fullref)
        print("No worries, your link has been saved!")
else:
    print("Working...")
    r = requests.get(link)

    soup = BeautifulSoup(r.content, 'html.parser')

    content = soup.find_all('meta', property = 'og:title')

    for items in content:
        title = items.get("content")

    fullref = title + ': ' + link + '\n'
    file_w.write(fullref)
    print("Awesome, saved!")


