import trimesh
import numpy as np


# Should this inherit from trimesh?
class Mesh:
    def __init__(self, tmesh: trimesh):
        self.vertices = np.asarray(tmesh.vertices)
        self.edges_unique = np.asarray(tmesh.edges_unique)
        self.faces_unique_edges = np.asarray(tmesh.faces_unique_edges)

    def get_intersecting_faces(self, heights: np.ndarray):
        # are vertices above height
        # much faster than converting a call to self.get_vertex_plane_distances
        vertices = np.greater(np.repeat(self.vertices[:, 2, np.newaxis], heights.shape[0], axis=1), heights)

        # each vertex appears twice here, but keeping them is faster than the overhead required to remove them
        face_vertices = np.reshape(vertices[self.edges_unique][self.faces_unique_edges], (-1, 6, heights.shape[0]))

        # does face have vertices above and below a slice
        intersection_mask = np.logical_and(np.logical_not(np.all(face_vertices, 1)), np.any(face_vertices, 1))

        # https://stackoverflow.com/questions/46041811/performance-of-various-numpy-fancy-indexing-methods-also-with-numba

        return intersection_mask

    # How do I vectorize cutting up the triangles to form the layers?

    def get_vertex_plane_distances(self, heights: np.ndarray):
        return np.repeat(self.vertices[:, 2, np.newaxis], heights.shape[0], axis=1) - heights
