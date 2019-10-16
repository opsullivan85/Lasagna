from trimesh import load_mesh
from trimesh.base import Trimesh


class fileloader:

    @staticmethod
    def load(path: str) -> Trimesh:
        return load_mesh(path)
