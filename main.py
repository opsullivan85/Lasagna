import lasagna

import numpy as np
import trimesh
from trimesh.base import Trimesh
from time import time


def get_section(tmesh: Trimesh, height: float):
    t0 = time()
    # (face, side, vert, xyz)
    mesh = np.asarray(tmesh.vertices)[tmesh.edges_unique][tmesh.faces_unique_edges]

    # List of z coords for each face
    vertices = np.reshape(mesh[:, :, :, 2], (-1, 6))
    vertices = vertices > height

    # perform xor on each row
    intersection_mask = np.logical_and(np.logical_not(np.all(vertices, 1)), np.any(vertices, 1))
    print(time() - t0)


if __name__ == '__main__':
    # attach to logger so trimesh messages will be printed to console
    # trimesh.util.attach_to_log()

    mesh: Trimesh
    mesh = trimesh.load('bunny.stl')
    get_section(mesh, 1)
