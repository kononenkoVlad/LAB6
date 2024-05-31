from functions import *

groups_of_vertices = create_list()
total_value = 0

def find_group_with_vertex(vertex):
    length = get_length(groups_of_vertices)
    for i in range(length):
        if includes(get(groups_of_vertices, i), vertex):
            return i
    return None


def uniuon_groups(group_1_number, group_2_number):
    group_1 = get(groups_of_vertices, group_1_number)
    group_2 = get(groups_of_vertices, group_2_number)
    length = get_length(group_2)
    for i in range(length):
        add(group_1, get(group_2, i))
    delete(groups_of_vertices, group_2_number)


def Kruskals_algorithm(W, canvas, vertexes, button):
    length = len(W)
    least_weight = 201
    least_i = 0
    least_j = 0
    least_i_group = None
    least_j_group = None
    for i in range(length):
        for j in range(i):
            value = W[i][j]
            if not value:
                continue
            if value > least_weight:
                continue
            i_group = find_group_with_vertex(i)
            j_group = find_group_with_vertex(j)
            if (i_group == j_group) and (type(i_group) is int):
                continue
            least_i_group = i_group
            least_j_group = j_group
            least_weight = value
            least_i = i
            least_j = j

    if least_weight < 201:
        paint_opened_edge(canvas, vertexes, least_i, least_j)
        global total_value
        total_value += least_weight
        i_type = type(least_i_group)
        j_type = type(least_j_group)
        if i_type == int and j_type == int:
            uniuon_groups(least_i_group, least_j_group)
        elif i_type != int and j_type != int:
            new_group = create_list()
            add(new_group, least_i)
            add(new_group, least_j)
            add(groups_of_vertices, new_group)
        elif i_type == int:
            add(get(groups_of_vertices, least_i_group), least_j)
        else:
            add(get(groups_of_vertices, least_j_group), least_i)
    else:
        button.destroy()
        print("\nСума ваг кістяка")
        print(total_value)
