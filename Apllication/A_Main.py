from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkfont
import cv2

from Apllication.A_HistoryView import HistoryCheckersWindow
from Backend.LoadedGameManager import LoadedGameManager
from Apllication.A_OptionsView import OptionsClass

class Application:
    def __init__(self):
        self.create_window()
        self.load_background()
        self.create_buttons()
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

    def create_window(self):
        self.root = tk.Tk()  # inicjalizacja rooota
        self.root.title("Checkers")  # tytul okna

    def load_background(self):
        self.background = tk.Label(self.root, compound=tk.CENTER)
        photo = cv2.imread('Image/background_main.png')

        b, g, r = cv2.split(photo)
        image = cv2.merge((r, g, b))
        image2 = Image.fromarray(image)
        tura8 = ImageTk.PhotoImage(image=image2)
        self.background.configure(image=tura8)
        self.background.image = tura8
        self.background.grid(row=0, column=0)

    def create_buttons(self):
        helv36 = tkfont.Font(family='Helvetica', size=15, weight='bold')

        self.button1 = tk.Button(self.background, text="Rozpocznij nową rozgrywkę", command=self.RunCaptureCheckers,
                                 font=helv36).grid(row=0, column=0, padx=(250, 250), pady=(230, 0))

        self.button2 = tk.Button(self.background, text="Wczytaj z historii", command=self.RunHistoryCheckers,
                                 font=helv36).grid(row=1, column=0, padx=(250, 250), pady=(35, 160))

    def RunCaptureCheckers(self):
        OptionsClass()


    def RunHistoryCheckers(self):
        gra = LoadedGameManager("SavedGames/trial_game.txt")  # wczytaj gre pokazowa
        HistoryCheckersWindow(gra)

    def destructor(self):
        self.root.destroy()