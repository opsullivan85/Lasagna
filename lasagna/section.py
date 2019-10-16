import trimesh
import numpy as np
from shapely.geometry import LineString

#mesh = trimesh.load_mesh('C:/Users/Owen/Desktop/3D Printer/Print Files/Snowflake/files/Snowflake.STL')
mesh = trimesh.load_mesh('C:/Users/Owen/Desktop/3D Printer/Print Files/Fluffy_sheep_single___multi-material/files/single_no_support.STL')
print(type(mesh))
mesh.show()
#slice.show()
