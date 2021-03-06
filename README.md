# Tkinter

Tkinter (tee-kay-in-ter) is a toolkit for creating graphical user interfaces with Python. It's by no means the only one available, and we also have options like Kivy or PyQt. Tkinter is, however, something of a default option for creating GUIs with Python, and actually comes with most Python installations.

### Geometry manager

When we go about creating a GUI with Tkinter, we start with a window, or multiple windows, and inside this windows live a number of widgets. A widget is something like a component. Together these widgets, or components, make up our complete application. We might have buttons, and containers, text areas, and menus. These are all widgets.

The geometry managers are responsible for controlling how these widgets fit into our application windows, and where these widgets are ultimately placed.

Tkinter has a number of geometry managers which behave in different ways. Here we'll be focusing on the pack geometry manager, which is really best for simpler applications, where the interface isn't particularly complicated.

While pack is quite easy to get started with, it can sometimes be quite difficult to visualise how elements are going to fit together, which is why we probably wouldn't use it for a complex interface.

## Files

### app.py

This file is just showing a basic gui Notebook using the `pack` geometry manager. We can **open**, **save** and **create** files.

### entry_form_pack / entry_form_grid

In this file I created a basic entry form using the `pack` and `grid` geometry manager.

### dice.py

This is a program that simulates rolling a six-sided dice.

### temperature_converter.py

A simple gui, to convert fahrenheit to celsius.

#### Credits

[Tkinter with Real Python](https://realpython.com/python-gui-tkinter/)

[Teclado]()