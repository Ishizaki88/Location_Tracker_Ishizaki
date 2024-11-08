import tkinter as tk



def autocomplete(event, fenster, eingabefeld):
    suggestions = {
        "Crater": ["cra", "crat", "c", "cr", "crate", "crater"],
        "Lost Woods": ["los", "lost", "lo", "l", "lost w", "lost wo", "lost woo", "lost wood", "lost woods"],
        "Lon Lon Ranch": ["lon", "ranch", "lo", "l", "lon l", "lon lo", "lon lon", "lon lon r", "lon lon ra", "lon lon ran", "lon lon ranch"],
    }
    text = eingabefeld.get().lower()
    dropdown_menu = tk.Menu(fenster, tearoff=0)
    for label, prefixes in suggestions.items():
        if any(prefix in text for prefix in prefixes):
            dropdown_menu.add_command(label=label, command=lambda l=label: eingabefeld.delete(0, tk.END) or eingabefeld.insert(0, l))
    if dropdown_menu.index("end") is not None:
        dropdown_menu.post(eingabefeld.winfo_rootx(), eingabefeld.winfo_rooty() + eingabefeld.winfo_height())

    eingabefeld.bind("<KeyRelease>", autocomplete)