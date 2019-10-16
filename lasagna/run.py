import trimesh
from lasagna.printersettings import printersettings
from lasagna.fileloader import fileloader

def main():
    #print('Hello World!')
    #FileLoader.load('C:/Users/Owen/Desktop/3D Printer/Print Files/Fluffy_sheep_single___multi-material/files/single_no_support.STL')
    settings = printersettings("defaultsettings.json")
    print(settings)
    settings.save()

'''
>>>cube = FileLoader.load(cube)
>>>
'''
