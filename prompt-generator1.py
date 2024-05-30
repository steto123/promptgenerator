# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:07:35 2024

@author: wotan


Uebung: Ich bau mir einen prompt Generator

Es soll ein Objekt prompt erstellt werden

Die Generierung und Ausgabe erfolgt in Tkinter- Fenster


"""

from tkinter import *  # import alle Funktionen des Moduls
import random


def copy_to_clipboard(text):
    window.clipboard_clear()  # Clear the clipboard
    window.clipboard_append(text)  # Append the desired text
    window.update()  # Update the clipboard

'''
Subjekt aus dropdown Liste waehlen und dateinamen zuweisen
'''

def auswahl_aendern(*args):
    # Define the subject list of words
    waehler = variable.get()
    
    '''
    
    if waehler== "Mixed": Subjectfile='subject.txt'
    if waehler== "Fantasy": Subjectfile='fantasy.txt'
    if waehler== "Weltall": Subjectfile='weltall.txt'
    if waehler== "Monster": Subjectfile='monster.txt'
    if waehler== "Sagen": Subjectfile='sagen.txt'
    if waehler== "Maerchen": Subjectfile='maerchen.txt'
    
    '''

def ausgeben():           # Gibt Text aus
    ausgabe.delete('1.0', END)  # Ausgabefenster loeschen
    
    
    waehler = variable.get()
#   print(waehler)
    if waehler== "Mixed": Subjectfile='subject.txt'
    if waehler== "Fantasy": Subjectfile='fantasy.txt'
    if waehler== "Weltall": Subjectfile='weltall.txt'
    if waehler== "Monster": Subjectfile='monster.txt'
    if waehler== "Sagen": Subjectfile='sagen.txt'
    if waehler== "Maerchen": Subjectfile='maerchen.txt'
    
    '''
    Prompt generieren
    '''
#   print (Subjectfile)
    with open(Subjectfile, 'r') as file:
    # Or read the file line by line
         list1 = [line.strip() for line in file]
    with open('medium.txt', 'r') as file:
    # Or read the file line by line
         list2 = [line.strip() for line in file]
    with open('stil.txt', 'r') as file:
    # Or read the file line by line
         list3 = [line.strip() for line in file]

    with open('resolution.txt', 'r') as file:
    # Or read the file line by line
         list5 = [line.strip() for line in file]

    with open('lighting.txt', 'r') as file:
    # Or read the file line by line
         list6 = [line.strip() for line in file]

    with open('color.txt', 'r') as file:
    # Or read the file line by line
         list8 = [line.strip() for line in file]

    list4 = ['pixiv', 'Artstation', 'deviant art', 'tumblr'] #Art sharing webseite
    list7 = ['dramatic', 'silk', 'expansive','low angle shot','god rays','psychedelic' ] # additional details


        # Select random words from each list
    word1 = random.choice(list1)
    word2 = random.choice(list2)
    word3 = random.choice(list3)
    word4 = random.choice(list4)
    word5 = random.choice(list5)
    word6 = random.choice(list6)
    word7 = random.choice(list7)
    word8 = random.choice(list8)

    # Combine the selected words into a sentence  
    # f-strings heisst die Methode
    sentence = f"{word1}, {word2}, {word3}, trending on {word4}, {word5}, {word6}, {word7}, {word8}"
  
    
    '''
    Ergebnis ausgeben
    '''
    ergebnistext = sentence
    ausgabe.insert("1.0", ergebnistext)
    button3= Button(window, text="copy",width=10, height=2, command=lambda: copy_to_clipboard(sentence)).grid(column=2, row=5)

'''
Hauptprogramm
'''
#Subjectfile='subject.txt'  # erst mal eine Datei zuweisen sicherheitshalber

window = Tk()   # Fensterobjekt definieren
# 300Pixel hoch, 600 Pixel breit,  unbedingt als string definieren
window.geometry('800x250')
window.title("Promptgenerator")    # Titel vergeben

# Generieren Titel
label = Label(window, text="Promptausgabe", fg='blue',font=('Arial',18))
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

'''
Generiere dropdown liste
'''
variable = StringVar(window)
variable.set("Wähle ein Thema")  # Standardwert

optionen = ["Mixed", "Fantasy", "Weltall", "Monster","Sagen","Maerchen"]
dropdown = OptionMenu(window, variable, *optionen)
dropdown.grid(row=1, column=0)
variable.trace("w", auswahl_aendern)  # Bei Änderung des Werts


'''
Generieren Kopf
'''

button1 = Button(window, text='Generieren', width=10, height=2, command=ausgeben)
button1.grid(row=5, column=0, padx=10, pady=10)

'''
Schliessen Knopf erzeugen
'''
button2 = Button(window, text='Exit', width=10, height=2,
                 command=window.destroy)  # button definieren
button2.grid(row=5, column=1, padx=10, pady=10)

'''
Textausgabe fuer prompt erzeugen
'''

ausgabe = Text(width=70, height=4)
ausgabe.grid(row=2, column=1,columnspan=2)


window.mainloop()  # Fenster erzeugen
