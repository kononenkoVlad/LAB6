from tkinter import Tk, Canvas
from functions import *
from random import seed

window = Tk()
window.geometry(f'{window_width}x{window_height}')
window.title("Graphs")
window.resizable(False, False)

canvas = Canvas(width=window_width, height=window_height)
canvas.pack()

seed(seed_value)

print("матриця напрямленого графа:")
matrix_for_directed_graph = create_matrix_for_directed_graph(count_of_vertexes)
for row in matrix_for_directed_graph:
    print(row)
canvas.create_text(300, 20, text="напрямлений граф", font=("Arial", 20))
vertexes_for_directed_graph = create_vertexes(300, 300, graph_size, count_of_vertexes, canvas)
draw_edges(matrix_for_directed_graph, vertexes_for_directed_graph, True, canvas)

print("\nматриця ненапрямленого графа:")
matrix_for_undirected_graph = create_matrix_for_undirected_graph(matrix_for_directed_graph)
for row in matrix_for_undirected_graph:
    print(row)
canvas.create_text(800, 20, text="ненапрямлений граф", font=("Arial", 20))
vertexes_for_undirected_graph = create_vertexes(800, 300, graph_size, count_of_vertexes, canvas)
draw_edges(matrix_for_undirected_graph, vertexes_for_undirected_graph, False, canvas)

window.mainloop()
