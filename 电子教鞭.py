# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 12:18
# @File    : jiao功能.py
# @Software: PyCharm Community Edition

import tkinter as tk
from tkinter import colorchooser


class ButtonList:
    def __init__(self, master):
        self.master = master
        self.screen_width = self.master.winfo_screenwidth()
        self.master.geometry("{}x{}+{}+{}".format("100", "400", self.screen_width-300, "100"))
        self.master.title("电子教鞭")
        # self.master.geometry("100x400"+{self.canvas_width}+"0")

        # Set the main window to be always on top
        self.master.attributes("-topmost", True)

        self.canvas_width = self.master.winfo_screenwidth()
        self.canvas_height = self.master.winfo_screenheight()

        # Create a toolbar frame
        self.toolbar_frame = tk.Frame(self.master, bg='lightgray')
        self.toolbar_frame.pack(side='left', fill='y')

        # Add a "Create" button to the toolbar
        self.create_button = tk.Button(self.toolbar_frame, text="Create", command=self.create_layer)
        self.create_button.pack(side='top', pady=5, padx=10)

        # Add a "Text" button to the toolbar
        self.text_button = tk.Button(self.toolbar_frame, text="Text", command=self.add_text)
        self.text_button.pack(side='top', pady=5, padx=10)

        # Add a "Color" button to the toolbar
        self.color_button = tk.Button(self.toolbar_frame, text="Color", command=self.choose_color)
        self.color_button.pack(side='top', pady=5, padx=10)

        # Add a "Clean" button to the toolbar
        self.clean_button = tk.Button(self.toolbar_frame, text="Clean", command=self.clean_layer)
        self.clean_button.pack(side='top', pady=5, padx=10)

        # Add a "Cancel" button to the toolbar
        self.cancel_button = tk.Button(self.toolbar_frame, text="Cancel", command=self.cancel_layer)
        self.cancel_button.pack(side='top', pady=5, padx=10)

        # Add a "Pan" button to the toolbar
        self.pan_button = tk.Button(self.toolbar_frame, text="Pan", command=self.start_pan)
        self.pan_button.pack(side='top', pady=5, padx=10)

        # Initialize the pen color to black
        # self.pen_color = 'black'


        self.master.mainloop()

    def create_layer(self):
        # Create a new window for the layer
        self.layer_window = tk.Toplevel(self.master)
        self.layer_window.geometry(f"{self.canvas_width-300}x{self.canvas_height}+{0}+{110}")

        # Set the window to be always on top
        # self.layer_window.attributes("-topmost", True)

        # Set the window to be transparent
        self.layer_window.attributes("-alpha", 0.5)

        # Create a canvas on the window
        self.canvas = tk.Canvas(self.layer_window, width=self.canvas_width, height=self.canvas_height,
                                background="systemTransparent")
        self.canvas.pack(side='left', fill='both', expand=True)

        # Bind mouse events to the canvas
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        # Set default pen color
        self.pen_color = 'black'

        # Disable text input by default
        self.text_mode = False

    def add_text(self):
        # Enable text input mode
        self.text_mode = True

        # Unbind drawing events from the canvas
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        # Bind mouse events to the canvas
        self.canvas.bind("<Button-1>", self.add_text_mark)

    def choose_color(self):
        # Let the user choose a pen color
        self.pen_color = colorchooser.askcolor(title="Choose Color")[1]
        # Get the position of the main window
        x, y = self.master.winfo_x(), self.master.winfo_y()


    def start_draw(self, event):
        # Start drawing with the current pen color
        if not self.text_mode:
            self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        # Draw a line on the canvas with the current pen color
        if not self.text_mode:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.pen_color)
            self.last_x, self.last_y = event.x, event.y

    def stop_draw(self, event):
        # Stop drawing
        pass

    def add_text_mark(self, event):
        # Create a text box on the canvas
        self.text_box = tk.Text(self.canvas, width=20, height=2, bg='lightyellow')
        self.text_box.place(x=event.x, y=event.y, anchor='nw')
        self.text_box.focus_set()
        self.text_box.bind("<Return>", lambda e: self.canvas.unbind("<Button-1>"))

    def clean_layer(self):
        # Clear the layer
        self.canvas.delete("all")

    def cancel_layer(self):
        # Destroy the layer window
        self.layer_window.destroy()

    def start_pan(self):
        # Disable text input mode
        self.text_mode = False

        # Unbind text events from the canvas
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        # Bind mouse events to the canvas
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)


root = tk.Tk()
# 设置窗口始终置顶
root.wm_attributes('-topmost', True)
button_list = ButtonList(root)
