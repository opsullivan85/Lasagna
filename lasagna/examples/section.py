import trimesh
import numpy as np
from shapely.geometry import LineString

# load the mesh from filename
# file objects are also supported
# mesh = trimesh.load_mesh('C:/Users/Owen/Desktop/3D Printer/Print Files/Snowflake/files/Snowflake.STL')
mesh = trimesh.load_mesh(
    'C:/Users/Owen/Desktop/3D Printer/Print Files/.11.3.19/Fluffy_sheep_single___multi-material/files/single_no_support.STL')

''''
mesh2 = mesh.copy()

mesh2.apply_translation((1,0,0))
print(len(mesh.vertices))
mesh3 = mesh.difference(mesh2, 'scad')
'''
# mesh3 = mesh.difference(mesh2, 'blender')

# get a single cross section of the mesh
slice = mesh.section(plane_origin=mesh.centroid,
                     plane_normal=[0, 0, 5])
#
# the section will be in the original mesh frame
mesh.show()
slice.show()

'''
# we can move the 3D curve to a Path2D object easily
slice_2D, to_3D = slice.to_planar()
slice_2D.show()

# if we wanted to take a bunch of parallel slices, like for a 3D printer
# we can do that easily with the section_multiplane method
# we're going to slice the mesh into evenly spaced chunks along z
# this takes the (2,3) bounding box and slices it into [minz, maxz]
z_extents = mesh.bounds[:,2]
# slice every .125 model units (eg, inches)
z_levels  = np.arange(*z_extents, step=.125)
'''
