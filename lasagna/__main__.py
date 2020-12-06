import numpy as np
import trimesh
from trimesh.base import Trimesh
from . import testpy

if __name__ == '__main__':
    # attach to logger so trimesh messages will be printed to console
    # trimesh.util.attach_to_log()
    mesh: Trimesh
    mesh = trimesh.load('Cube.stl')
    print('here')
    #print(mesh.face_adjacency)
    print(mesh.edges_sorted)
    mesh.show()
    print('done')
