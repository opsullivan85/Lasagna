import lasagna

import numpy as np
import trimesh
from trimesh.base import Trimesh
from time import time


def get_intersecting_faces(tmesh: Trimesh, height: float):
    # are vertices above  height
    vertices = np.greater(tmesh.vertices[:, 2], height)

    # each vertex appears twice here. Find better implementation. slowest part right now
    # are the verticies in each face above height
    array_vertices = np.reshape(vertices[tmesh.edges_unique][tmesh.faces_unique_edges], (-1, 6))

    intersection_mask = np.logical_and(np.logical_not(np.all(array_vertices, 1)), np.any(array_vertices, 1))

    return intersection_mask


def get_intersecting_faces_2(tmesh: Trimesh, height: float):
    # are vertices above height
    vertices = np.greater(tmesh.vertices[:, 2], height)

    faces_vert_indices = np.reshape(tmesh.edges_unique[tmesh.faces_unique_edges], (-1, 6))
    faces_unique_vert_indices = np.sort(faces_vert_indices)[:, ::2]

    # are the vertices in each face above height
    array_vertices = vertices[faces_unique_vert_indices]

    intersection_mask = np.logical_and(np.logical_not(np.all(array_vertices, 1)), np.any(array_vertices, 1))

    return intersection_mask


if __name__ == '__main__':
    # attach to logger so trimesh messages will be printed to console
    # trimesh.util.attach_to_log()

    mesh: Trimesh
    mesh = trimesh.load('bunny.stl')
    # = trimesh.load('Cube.stl')
    num = 5


    for i in range(num):
        t = time()
        get_intersecting_faces(mesh, 1)
        print(time() - t)

    print('\n')

    for i in range(num):
        t = time()
        get_intersecting_faces_2(mesh, 1)
        print(time() - t)
