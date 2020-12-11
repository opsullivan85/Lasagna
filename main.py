import lasagna

import numpy as np
import trimesh
from trimesh.base import Trimesh
from time import time


def get_section(tmesh: Trimesh, height: float):
    # (face, side, vert, xyz)
    mesh = np.asarray(tmesh.vertices)[tmesh.edges_unique][tmesh.faces_unique_edges]

    # Are vertices of face above height
    vertices = np.greater(np.reshape(mesh[:, :, :, 2], (-1, 6)), height)

    # perform xor on each row
    intersection_mask = np.logical_and(np.logical_not(np.all(vertices, 1)), np.any(vertices, 1))


def get_intersecting_faces(tmesh: Trimesh, height: float):

    # are vertices above  height
    vertices = np.greater(tmesh.vertices[:, 2], height)

    # each vertex appears twice here. Find better implementation. slowest part right now
    # are the verticies in each face above height
    array_vertices = np.reshape(vertices[tmesh.edges_unique][tmesh.faces_unique_edges], (-1, 6))

    intersection_mask = np.logical_and(np.logical_not(np.all(array_vertices, 1)), np.any(array_vertices, 1))

    return intersection_mask



if __name__ == '__main__':
    # attach to logger so trimesh messages will be printed to console
    # trimesh.util.attach_to_log()

    mesh: Trimesh
    mesh = trimesh.load('bunny.stl')
    # = trimesh.load('Cube.stl')
    t = time()
    get_intersecting_faces(mesh, 1)
    print(time() - t)

    t = time()
    get_section(mesh, 1)
    print(time() - t)

    t = time()
    get_intersecting_faces(mesh, 1)
    print(time() - t)

