from tkinter import LAST
from math import pi, cos, sin, sqrt
from random import random
from data import *


def create_vertex(left, top, text, canvas):
    canvas.create_text(left, top, text=text+1, font=("Arial", vertex_size))
    canvas.create_oval(left - vertex_size, top - vertex_size, left + vertex_size, top + vertex_size,
                       fill="", outline="red")


def create_vertexes(left, top, size, count, canvas):
    vertexes = [{}] * count
    for i in range(count):
        angle = i * 2 * pi/count
        vertex_left = left + size * sin(angle)
        vertex_top = top - size * cos(angle)
        create_vertex(vertex_left, vertex_top, i, canvas)
        vertex = {
            "left": vertex_left,
            "top": vertex_top,
        }
        vertexes[i] = vertex
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


def draw_self_arrow(left, top, i, count_of_vertexes_in_this_graph, canvas):
    main_angle = i / count_of_vertexes_in_this_graph * 2 * pi
    lefter_angle = main_angle + extra_angle_in_self_arrow
    righter_angle = main_angle - extra_angle_in_self_arrow
    first_point_x = left+sin(lefter_angle)*2*vertex_size
    first_point_y = top-cos(lefter_angle)*2*vertex_size
    second_point_x = left+sin(righter_angle)*2*vertex_size
    second_point_y = top-cos(righter_angle)*2*vertex_size
    canvas.create_line(first_point_x, first_point_y, second_point_x, second_point_y)
    canvas.create_line(left + vertex_size*sin(lefter_angle), top - vertex_size*cos(lefter_angle),
                       first_point_x, first_point_y)
    canvas.create_line(second_point_x, second_point_y, left + vertex_size*sin(righter_angle),
                       top - vertex_size*cos(righter_angle), arrow=LAST)


def draw_line(left_i, top_i, left_j, top_j, sin_angle, cos_angle, canvas):
    left_from = left_i - vertex_size * cos_angle
    left_to = left_j + vertex_size * cos_angle
    top_from = top_i + vertex_size * sin_angle
    top_to = top_j - vertex_size * sin_angle
    canvas.create_line(left_from, top_from, left_to, top_to)


def draw_arrow(left_i, top_i, left_j, top_j, sin_angle, cos_angle, canvas):
    left_from = left_i - vertex_size * cos_angle + sin_angle * space_between_edges
    left_to = left_j + vertex_size * cos_angle + sin_angle * space_between_edges
    top_from = top_i + vertex_size * sin_angle + cos_angle * space_between_edges
    top_to = top_j - vertex_size * sin_angle + cos_angle * space_between_edges
    canvas.create_line(left_from, top_from, left_to, top_to, arrow=LAST)


def draw_edges(matrix, vertexes, directed, canvas):
    length = len(matrix)
    for i in range(length):
        for j in range(length if directed else i+1):
            if not matrix[i][j]:
                continue
            if i == j:
                left = vertexes[i]["left"]
                top = vertexes[i]["top"]
                draw_self_arrow(left, top, i, length, canvas)
                continue
            left_i = vertexes[i]["left"]
            left_j = vertexes[j]["left"]
            top_i = vertexes[i]["top"]
            top_j = vertexes[j]["top"]
            dx = left_i - left_j
            dy = top_i - top_j
            line_length = sqrt(dx * dx + dy * dy)
            cos_angle = dx/line_length
            sin_angle = -dy/line_length
            draw_arrow(left_i, top_i, left_j, top_j, sin_angle, cos_angle, canvas) if directed else (
                draw_line(left_i, top_i, left_j, top_j, sin_angle, cos_angle, canvas))
