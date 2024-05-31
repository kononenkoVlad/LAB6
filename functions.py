from math import *
from random import random
from data import *


def create_list():
    return {
        "data": None,
        "next": None,
    }


def add(head, data):
    while head["next"] is not None:
        head = head["next"]
    node = {
        "data": data,
        "next": None,
    }
    head["next"] = node


def get(head, i):
    for j in range(i+1):
        head = head["next"]
    return head["data"]


def get_length(head):
    length = 0
    while head["next"] is not None:
        length += 1
        head = head["next"]
    return length


def includes(head, data):
    length = get_length(head)
    for i in range(length+1):
        if head["data"] == data:
            return True
        head = head["next"]
    return False


def delete(head, index):
    while head["next"] is not None:
        if index == 0:
            head["next"] = head["next"]["next"]
            return
        head = head["next"]
        index -= 1




def create_vertex(left, top, text, canvas):
    text = canvas.create_text(left, top, text=text+1, font=("Arial", vertex_size))
    oval = canvas.create_oval(left - vertex_size, top - vertex_size, left + vertex_size, top + vertex_size, fill="",
                              outline="red")
    return {
        "text": text,
        "oval": oval
    }


def create_vertexes(left, top, size, count, canvas):
    vertexes = create_list()
    for i in range(count):
        angle = i * 2 * pi/count
        vertex_left = left + size * sin(angle)
        vertex_top = top - size * cos(angle)
        vertex_window_elements = create_vertex(vertex_left, vertex_top, i, canvas)
        vertex = {
            "left": vertex_left,
            "top": vertex_top,
            "text": vertex_window_elements["text"],
            "oval": vertex_window_elements["oval"],
            "number": i
        }
        add(vertexes, vertex)
        i += 1
    return vertexes


def create_matrix_for_directed_graph(size):
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            number = int(random()*2*k)
            matrix[i].append(number)
    return matrix


def create_zero_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append(0)
    return matrix


def create_matrix_for_undirected_graph(matrix_for_directed_graph):
    length = len(matrix_for_directed_graph)
    matrix = create_zero_matrix(length)
    for i in range(length):
        for j in range(length):
            ij = matrix_for_directed_graph[i][j]
            ji = matrix_for_directed_graph[j][i]
            matrix[i][j] = ij if ij else ji
    return matrix


def draw_line(left_i, top_i, left_j, top_j, color, width, canvas):
    dx = left_i - left_j
    dy = top_i - top_j
    line_length = sqrt(dx * dx + dy * dy)
    cos_angle = dx / line_length
    sin_angle = -dy / line_length
    left_from = left_i - vertex_size * cos_angle
    left_to = left_j + vertex_size * cos_angle
    top_from = top_i + vertex_size * sin_angle
    top_to = top_j - vertex_size * sin_angle
    canvas.create_line(left_from, top_from, left_to, top_to, fill=color, width=width)


def draw_edges(matrix, vertexes, canvas):
    length = len(matrix)
    for i in range(length):
        for j in range(i+1):
            if not matrix[i][j]:
                continue
            left_i = get(vertexes, i)["left"]
            left_j = get(vertexes, j)["left"]
            top_i = get(vertexes, i)["top"]
            top_j = get(vertexes, j)["top"]
            dx = left_i - left_j
            dy = top_i - top_j
            line_length = sqrt(dx * dx + dy * dy)
            cos_angle = dx/line_length
            sin_angle = -dy/line_length
            draw_line(left_i, top_i, left_j, top_j, 'black', 1, canvas)
            text_higher_line = 6
            higher = text_higher_line*cos_angle
            lefter = text_higher_line*sin_angle
            angle = asin(sin_angle)*180/pi
            if left_j > left_i:
                angle = -angle
            canvas.create_text((left_i+left_j)/2+lefter, (top_i+top_j)/2+higher, text=matrix[i][j], angle=angle,
                               fill="#0000aa", font=("Arial", weight_text_size))


def draw_graph(left, top, size, matrix, canvas):
    length = len(matrix)
    vertexes = create_vertexes(left, top, size, length, canvas)
    draw_edges(matrix, vertexes, canvas)
    return vertexes


lighted_vertexes = []
def paint_opened_edge(canvas, vertexes, vertex_1_number, vertex_2_number):
    vertex_1 = get(vertexes, vertex_1_number)
    vertex_2 = get(vertexes, vertex_2_number)

    draw_line(vertex_1["left"], vertex_1["top"], vertex_2["left"],
              vertex_2["top"], "red", 3, canvas)
    if not (vertex_1_number in lighted_vertexes):
        lighted_vertexes.append(vertex_1_number)
        canvas.itemconfig(vertex_1["oval"], fill="blue")
        canvas.tag_raise(vertex_1["text"])
    if not (vertex_2_number in lighted_vertexes):
        lighted_vertexes.append(vertex_2_number)
        canvas.itemconfig(vertex_2["oval"], fill="blue")
        canvas.tag_raise(vertex_2["text"])
