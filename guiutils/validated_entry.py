import tkinter as tk
import re


class ValidatedEntry(tk.Entry):
    OK = "#22c55e"
    BAD = "#ef4444"
    NEUTRAL = "#d1d5db"
    FOCUS = "#3b82f6"

    def __init__(self, master=None, pattern=None, **kwargs):
        kwargs.setdefault("font", ("Helvetica", 12))
        kwargs.setdefault("relief", "flat")
        kwargs.setdefault("bd", 0)
        kwargs.setdefault("highlightthickness", 2)
        kwargs.setdefault("highlightbackground", self.NEUTRAL)
        kwargs.setdefault("highlightcolor", self.FOCUS)
        kwargs.setdefault("insertwidth", 2)
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
        if not text:
            color, bg = self.NEUTRAL, "white"
        elif ok:
            color, bg = self.OK, "#f0fdf4"
        else:
            color, bg = self.BAD, "#fef2f2"
        self.configure(bg=bg, highlightbackground=color, highlightcolor=color)