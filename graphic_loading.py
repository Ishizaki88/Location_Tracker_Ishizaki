import tkinter as tk
from PIL import Image, ImageTk


def load_and_bind_images(fenster, table):
    images_info = [
        ('../Tracker_Ishizaki/images/Equipment/Goron-Tunic.png', 3, 1),
        ('../Tracker_Ishizaki/images/Equipment/Kokiri-Sword.png', 0, 0),
        ('../Tracker_Ishizaki/images/Equipment/Master-Sword.png', 0, 1),
        ('../Tracker_Ishizaki/images/Equipment/Mirror-Shield.png', 1, 2),
        ('../Tracker_Ishizaki/images/Equipment/Zora-Tunic.png', 3, 2),
        ('../Tracker_Ishizaki/images/Equipment/Hover-Boots.png', 2, 2),
        ('../Tracker_Ishizaki/images/Equipment/Iron-Boots.png', 2, 1),
        ('../Tracker_Ishizaki/images/Equipment/Biggoron-Sword.png', 0, 2),
        ('../Tracker_Ishizaki/images/Equipment/Hylian-Shield.png', 1, 1),
        ('../Tracker_Ishizaki/images/Equipment/Kokiri-Tunic.png', 3, 0),
        ('../Tracker_Ishizaki/images/Equipment/Kokiri-Boots.png', 2, 0),
        ('../Tracker_Ishizaki/images/Equipment/Deku-Shield.png', 1, 0),
    ]

    loaded_images = []

    for image_path, row, column in images_info:
        image = tk.PhotoImage(file=image_path)
        image_label = tk.Label(fenster, image=image)
        image_label.bind("<Button-1>", lambda event, path=image_path: make_bw(event, path))
        image_label.grid(in_=table, row=row, column=column)
        loaded_images.append(image)

    return loaded_images

# Funktion, um das Bild schwarz-weiß zu machen
def make_bw(event, bild_pfad):

    bild_label = event.widget
    if not hasattr(bild_label, 'is_bw'):
        bild_label.is_bw = False

    if not bild_label.is_bw:
        img = Image.open(bild_pfad).convert("L")
        bw_img = ImageTk.PhotoImage(img)
        bild_label.config(image=bw_img)
        bild_label.image = bw_img
        bild_label.is_bw = True
    else:
        color_img = ImageTk.PhotoImage(Image.open(bild_pfad))
        bild_label.config(image=color_img)
        bild_label.image = color_img
        bild_label.is_bw = False