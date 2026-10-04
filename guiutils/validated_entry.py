#validated_entry.py
import tkinter as tk
import re
class ValidatedEntry(tk.Entry):
    def __init__(self, master=None, pattern=None, **kwargs):
        super().__init__(master, **kwargs)
        self._pattern = re.compile(pattern) if pattern else None        
        self._var = tk.StringVar()
        self.configure(textvariable=self._var)
        self._var.trace_add("write", self._on_change)
        self._valid = False 

    @property
    def valid(self): 
        return self._valid

    def _on_change(self, *args):
        text = self._var.get()
        ok = True if self._pattern is None else bool(self._pattern.fullmatch(text))
        self._valid = ok
        self.configure(
            bg="#ddffdd" if ok and text else "#ffdddd" if text else "white"
            )