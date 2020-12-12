import lasagna

import numpy as np
import trimesh
from trimesh.base import Trimesh
from time import time


def get_intersecting_faces(tmesh: Trimesh, height: float):
    # are vertices above  height
    vertices = np.greater(tmesh.vertices[:, 2], height)

    # each vertex appears twice here, but keeping them is faster than the overhead required to remove them
    # are the verticies in each face above height
    array_vertices = np.reshape(vertices[tmesh.edges_unique][tmesh.faces_unique_edges], (-1, 6))

    intersection_mask = np.logical_and(np.logical_not(np.all(array_vertices, 1)), np.any(array_vertices, 1))

    intersections = np.where(intersection_mask)

    return intersection_mask


if __name__ == '__main__':
    # attach to logger so trimesh messages will be printed to console
    # trimesh.util.attach_to_log()

    mesh: Trimesh
    #mesh = trimesh.load('bunny.stl')
    mesh = trimesh.load('Cube.stl')
    print(get_intersecting_faces(mesh, 1))
    num = 1000
    num2 = 1

    t = time()
    for i in range(num):
        intersections = get_intersecting_faces(mesh, 1)
        for j in range(num2):
            mesh.faces[intersections]
    print(time() - t)



