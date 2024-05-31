from tkinter import Tk, Canvas, Button
from functions import *
from random import seed
from create_W import create_W, A
from Kruskals_algorithm import Kruskals_algorithm

window = Tk()
window.geometry(f'{window_width}x{window_height}')
window.title("Graphs")
window.resizable(False, False)

canvas = Canvas(width=window_width, height=window_height)
canvas.pack()

seed(seed_value)
W = create_W()

canvas.create_text(300, 20, text="ненапрямлений граф", font=("Arial", 20))
vertexes = draw_graph(300, 300, graph_size, W, canvas)

button = Button(window, text="start", bg=buttonColors, fg="black", font=("Arial", 20),
                command=lambda: Kruskals_algorithm(W, canvas, vertexes, button))
button.place(x=600, y=300)

window.mainloop()
