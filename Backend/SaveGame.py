import json
import os
import tkinter
from tkinter import filedialog
import datetime







class SaveGame(): #klasa zapisująca rozgrywke
    def __init__(self,game_history,gamename='nazwa gry',p1name = 'Andrei',p2name = 'Alex'):
        dictionary = self.askAboutDirector()

        now = datetime.datetime.now()

        jsonhistory = []
        for x in range(len(game_history)):
            jsonhistory.append({'round': str(x),
                                'pawns': game_history[x]})

        with open(dictionary, 'w') as outfile:
            json.dump({'game_name': gamename,
                       'date': now.strftime("%Y-%m-%d %H:%M"),
                       'player1_name': p1name,
                       'player2_name': p2name,
                       'game_history': jsonhistory}, outfile)


    def askAboutDirector(self):
        root = tkinter.Tk()
        root.withdraw()  # use to hide tkinter window

        currdir = os.getcwd()
        outFileName = filedialog.asksaveasfilename(parent=root, initialdir=currdir, title='Select file',
                                               filetypes=[('txt files', '.txt')],defaultextension='.txt')
        return outFileName