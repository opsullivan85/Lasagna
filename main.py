import lasagna

import numpy as np
import trimesh
from trimesh.base import Trimesh
from time import time


def get_intersecting_faces_lst(tmesh: Trimesh, height: np.ndarray):
    if not type(height) == np.ndarray:
        if not hasattr(height, '__iter__'):
            height = np.asarray([height])
        else:
            height = np.asarray(height)

    # are vertices above height
    vertices = np.greater(np.repeat(tmesh.vertices[:, 2, np.newaxis], height.shape[0], axis=1), height)

    # each vertex appears twice here, but keeping them is faster than the overhead required to remove them
    face_vertices = np.reshape(vertices[tmesh.edges_unique][tmesh.faces_unique_edges], (-1, 6, height.shape[0]))

    # does face have vertices above and below a slice
    intersection_mask = np.logical_and(np.logical_not(np.all(face_vertices, 1)), np.any(face_vertices, 1))

    # get this to work?
    intersections = np.nonzero(intersection_mask)

    return intersection_mask


if __name__ == '__main__':
    # attach to logger so trimesh messages will be printed to console
    # trimesh.util.attach_to_log()

    mesh: Trimesh
    mesh = trimesh.load('bunny.stl')
    # mesh = trimesh.load('Cube.stl')
    slices = np.linspace(mesh.bounds[0, 2], mesh.bounds[1, 2], 1000)
    get_intersecting_faces_lst(mesh, 0)

    t = time()
    get_intersecting_faces_lst(mesh, slices)
    print(time() - t)
