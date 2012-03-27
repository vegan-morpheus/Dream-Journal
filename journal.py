from Tkinter import *

root = Tk()
root.title("edyth")
root.config(background="black")
root.wm_state("normal")

editor = Text(root)
editor.pack(fill=Y, expand=1)

editor.config(
    borderwidth=0,
    font="{Lucida Sans Typewriter} 12",
    foreground="green",
    background="black",
    insertbackground="white", # cursor
    selectforeground="green", # selection
    selectbackground="#008000",
    wrap=WORD, # use word wrapping
    width=64,
    undo=True, # Tk 8.4
    )

editor.focus_set()

mainloop()
