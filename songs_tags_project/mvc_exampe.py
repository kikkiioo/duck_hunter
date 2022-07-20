
from msilib.schema import TextStyle
from pkgutil import get_data
from pyexpat import model
from re import X
import tkinter as tk
from tkinter import font
from turtle import color 
import uuid
import dataclasses,json
from dataclasses import dataclass, fields
from dataclasses_json import dataclass_json
from sympy import Mod, root, true
from typing import List

#model

@dataclass_json
@dataclass
class Tag:
    id: int
    tag: str
    # def __init__(self):
    #      self.id = 0
    #      self.tag = ""

@dataclass_json
@dataclass 
class Song:
    id: int
    song_name: str
    tags: List[int]
    # def __init__(self):
    #      self.id = 0
    #      self.song_name = ""
    #      self.tags = []


class Model:
    # def __init__(self):
   
    tag_data=[Tag(0,"Indie"),Tag(1,"Pop"),Tag(2,"Rap")]
   
    song_data = [Song(0,"Happy", [1]),Song(1,"Treehouse",[0]),Song(2,"Doin' Time",[0]),Song(3,"Location",[1,2])]
    # for JSON encoding ?

    # Song.schema().dumps(song_data,many=true)
    
    # for JSON decoding?
    # song_data = '[{"id":0},{"song_name":"Happy"},{"tags":[0,1]}]'
    # Song.schema().loads(song_data, many=True)
    
#controllers
class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_find_songs(self):
        self.view.find_songs()

    def handle_click_change_song_name(self):
        self.view.change_song_name()

#view

class TkView():
    def setup(self, controller):

        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.title("Song finder")

        # UI

        self.frame = tk.Frame(self.root,background="#705e6c")
        self.frame.pack(fill=tk.BOTH, expand=1) 
        self.my_entry = tk.Entry(self.frame, width = 40, font=("Helvetica", 14), background="#c0b6c1")
        self.my_entry.insert(0,'')
        self.my_entry.pack(padx = 5, pady = 5)
        self.label = tk.Label(self.frame, text="Result:", font=("Helvetica", 18), background="#705e6c")
        self.label.pack()
        self.list = tk.Listbox(self.frame,background="#c4a8a5")
        self.list.pack(fill=tk.BOTH, expand=1)
        self.button = tk.Button(self.frame, text="Find songs",font=("Helvetica", 10),width = 40, height= 2,command=controller.handle_click_find_songs,background="#a2807e")
        self.button.pack()
        self.button = tk.Button(self.frame, text="Change song name",font=("Helvetica", 10),width = 40, height= 2, command=controller.handle_click_change_song_name,background="#a2807e")
        self.button.pack()

    def find_songs(self):
        self.list.delete(0,tk.END)
        l = self.my_entry.get()
        for i in Model.tag_data:
            if i.tag == l:
                for j in Model.song_data:
                    for k in j.tags:
                        if i.id == k:
                            a = j.song_name
                            self.list.insert(tk.END, a)
                            bolded = font.Font(weight='bold')
                            self.list.config(font=bolded)

    def start_main_loop(self):
        self.root.mainloop()

# here should be also a entry window for changing the song name
    def change_song_name(self):
        l = self.my_entry.get()
        for j in Model.song_data:
            if l == j.song_name:
                j.song_name="whatever song name you want"
                self.list.insert(tk.END, j.song_name) 
              

# start the application
c = Controller(Model(), TkView())
c.start()