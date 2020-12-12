from typing import Any

import lasagna

import numpy as np
import trimesh
from trimesh.base import Trimesh
from time import time

from lasagna.mesh import Mesh


if __name__ == '__main__':

    tmesh: Trimesh
    tmesh = trimesh.load('bunny.stl')
    # tmesh = trimesh.load('Cube.stl')
    tmesh = tmesh.subdivide().subdivide()

    mesh = Mesh(tmesh)

    heights = np.linspace(tmesh.bounds[0, 2], tmesh.bounds[1, 2], 1000)

    t = time()
    mesh.get_intersecting_faces(heights)
    print()
    print(time() - t)

