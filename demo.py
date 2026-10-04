#demo.py
import tkinter as tk
from guiutils.validated_entry import ValidatedEntry
from guiutils.slugifier import slug
import re

root = tk.Tk()
root.title("Demo Reusables (Tkinter)")

email = ValidatedEntry(
        root, 
        pattern=r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$", 
        width=40)
email.pack(
            padx=8, 
            pady=6
           )
lbl_estado = tk.Label(root,
                      text="Estado: inválido"
                      ); lbl_estado.pack()
def refresh_estado(*_): 
    lbl_estado.config(
        text=f"Estado: {'válido' if email.valid else 'inválido'}"
        )
email.bind(
    "<KeyRelease>",
    refresh_estado
    )

entrada = ValidatedEntry(
    root,
    pattern=r".+",
    width=40
    )
entrada.pack(
    padx=8,
    pady=6
    )
lbl_slug = tk.Label(root,
                    text="Slug: —"); lbl_slug.pack()
def on_change(*_): 
    lbl_slug.config(
        text=f"Slug: {slug(entrada.get())}"
        )
entrada.bind(
    "<KeyRelease>",
    on_change
             )

root.mainloop()