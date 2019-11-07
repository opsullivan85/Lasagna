import trimesh
# import pymesh
from lasagna.printersettings import printersettings
from lasagna.fileloader import fileloader
from lasagna.gcodewriter import gcodewriter
import numpy as np


def main():
    # FileLoader.load('C:/Users/Owen/Desktop/3D Printer/Print Files/Fluffy_sheep_single___multi-material/files/single_no_support.STL')

    settings = printersettings("defaultsettings")
    print(settings)
    settings.save()
    print()
    print(settings._settings)

    # gcodewriter(np.asarray([[1, 1, 1, 1], [2, 2, 2, 2]]), "Name", "")


'''
>>>cube = FileLoader.load(cube)
>>>
'''
