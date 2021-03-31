# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 09:59:11 2020


"""

import imdb_functions as im
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as ScrolledText


fenetre = tk.Tk() # Creates a tkinter object
label = tk.Label(fenetre, text="Bienvenue dans notre application")
label.pack()


def action_1():
    text_area.config(state="normal")
    text_area.delete(1.0,tk.END)
    text_area.insert(tk.INSERT,im.get_movie_info(arg_1.get()))
    text_area.configure(state='disabled')

    
def action_2():
    text_area.config(state="normal")
    text_area.delete(1.0,tk.END) #delete scrolledtext content
    text_area.insert(tk.INSERT,im.get_commun_actors(arg_2.get(),int(arg_3.get()),arg_4.get(),int(arg_5.get())))
    text_area.configure(state='disabled')
def action_3():
    text_area.config(state="normal")
    text_area.delete(1.0,tk.END)
    text_area.insert(tk.INSERT,im.get_actor_info(arg_6.get()))
    text_area.configure(state='disabled')

def action_4():
    text_area.config(state="normal")
    text_area.delete(1.0,tk.END)
    text_area.insert(tk.INSERT,im.get_best_movie(int(arg_7.get()),arg_8.get()))
    text_area.configure(state='disabled')
    
def action_5():
    text_area.config(state="normal")
    text_area.delete(1.0,tk.END)
    text_area.insert(tk.INSERT,im.get_commun_films(arg_9.get(),arg_10.get()))
    text_area.configure(state='disabled')
    
    
### Frame 1  : menu des actions possibles  
### Scrollable frame
frame1 = tk.Frame(fenetre)
canvas = tk.Canvas(frame1,width=200, height=600)
scrollbar = tk.Scrollbar(frame1, orient="vertical", command=canvas.yview)
scrollFrame = tk.Frame(canvas,borderwidth=0, relief=tk.GROOVE)

scrollFrame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollFrame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

frame1.pack(side=tk.LEFT, padx=10, pady=10)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

### fonction get_movie_info
framef1 = tk.Frame(scrollFrame, borderwidth=2, highlightthickness=3, highlightbackground="dodger blue", relief=tk.GROOVE)
framef1.pack(side=tk.TOP, padx=1, pady=1)   


label = tk.Label(framef1, text="get_movie_info")
label.pack()
label = tk.Label(framef1, text="Nom du film")
label.pack()
arg_1 = tk.Entry(framef1, width=30) # argument de la fonction
arg_1.pack()
bouton_f1 = tk.Button(framef1, text="Rechercher", command=action_1)
bouton_f1.pack()

### fonction get_commun_actors
framef2 = tk.Frame(scrollFrame, borderwidth=2,highlightthickness=3, highlightbackground="red", relief=tk.GROOVE)
framef2.pack(side=tk.TOP, padx=1, pady=1)     

label = tk.Label(framef2, text="get_commun_actors")
label.pack()
label = tk.Label(framef2, text="Nom du film 1")
label.pack()
arg_2 = tk.Entry(framef2, width=30)
arg_2.pack()
label = tk.Label(framef2, text="Année du film 1")
label.pack()
arg_3 = tk.Entry(framef2, width=30)
arg_3.pack()
label = tk.Label(framef2, text="Nom du film 2")
label.pack()
arg_4 = tk.Entry(framef2, width=30)
arg_4.pack()
label = tk.Label(framef2, text="Année du film 2")
label.pack()
arg_5 = tk.Entry(framef2, width=30)
arg_5.pack()
bouton_f2 = tk.Button(framef2, text="Rechercher", command=action_2)
bouton_f2.pack()



### fonction get_actor_info
framef3 = tk.Frame(scrollFrame, borderwidth=2, highlightthickness=3, highlightbackground="forest green",relief=tk.GROOVE)
framef3.pack(side=tk.TOP, padx=1, pady=1)     
label = tk.Label(framef3, text="get_actor_info")
label.pack()
label = tk.Label(framef3, text="Nom de l'acteur")
label.pack()
arg_6 = tk.Entry(framef3, width=30)
arg_6.pack()
bouton_f3 = tk.Button(framef3, text="Rechercher", command=action_3)
bouton_f3.pack()


### fonction get_best_movie
framef4 = tk.Frame(scrollFrame, borderwidth=2,highlightthickness=3, highlightbackground="gold", relief=tk.GROOVE)
framef4.pack(side=tk.TOP, padx=1, pady=1)     
label = tk.Label(framef4, text="get_best_movie")
label.pack()
label = tk.Label(framef4, text="Année")
label.pack()
arg_7 = tk.Entry(framef4, width=30)
arg_7.pack()
label = tk.Label(framef4, text="Genre(s)")
label.pack()
arg_8 = tk.Entry(framef4, width=30)
arg_8.pack()
bouton_f4 = tk.Button(framef4, text="Rechercher", command=action_4)
bouton_f4.pack()



### fonction get_commun_film
framef5 = tk.Frame(scrollFrame, borderwidth=2, highlightthickness=3, highlightbackground="dodger blue", relief=tk.GROOVE)
framef5.pack(side=tk.TOP, padx=1, pady=1)     
label = tk.Label(framef5, text="get_commun_films")
label.pack()
label = tk.Label(framef5, text="Nom de l'acteur 1")
label.pack()
arg_9 = tk.Entry(framef5, width=30)
arg_9.pack()
label = tk.Label(framef5, text="Nom de l'acteur 2")
label.pack()
arg_10 = tk.Entry(framef5, width=30)
arg_10.pack()
bouton_f5 = tk.Button(framef5, text="Rechercher", command=action_5)
bouton_f5.pack()

### Frame 2 : affichage du résultat

frame2 = tk.Frame(fenetre, borderwidth=2, relief=tk.GROOVE)
frame2.pack(side=tk.TOP, padx=10, pady=10)
text_area = ScrolledText(frame2, width = 850,  height = 1000) 
text_area.config(state="normal")
text_default = """Votre résultat sera affiché ici !
            \nPour les saisies merci de respecter les majuscules lorsqu'il s'agit de noms d'acteurs.
            \nDescriptions des fonctionnalités:
            \n-> get_movie_info donne des informations sur un film.
            \n-> get_commun_actors donne les noms des acteurs communs à deux films.
            \n-> get_actor_info donne des informations sur un acteur.
            \n-> get_best_movie founit pour une année ainsi qu'un ou plusieurs genres données le top 3 des films selon leurs notes. 
            \n-> get_commun_films founit la liste des films communs à 2 acteurs."""
text_area.insert(tk.INSERT,text_default)
text_area.configure(state='disabled')
text_area.pack()
fenetre.mainloop()
