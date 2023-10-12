# give python access to blender's functionality
import bpy
# extend python's math functionality
import math


radians_step = 0.1
number_triangles = 50

bpy.ops.object.light_add(type='SUN', align='WORLD', location=(-4, 0.3, 11.56), scale=(1, 1, 1))



bpy.ops.object.camera_add()
camera = bpy.context.active_object

for i in range(number_triangles):
    # add a triangle to the  currently actve scene 
    current_radius = i* radians_step
    bpy.ops.mesh.primitive_circle_add(vertices=6, radius = current_radius)
    triangle_mesh = bpy.context.active_object
    triangle_mesh.location = (0, 0, 2)
    # rotate the mesh into a curve
    degrees = 90
    radians = math.radians(degrees)
    triangle_mesh.rotation_euler.x = radians
    triangle_mesh.rotation_euler.z = radians-i
    # convert mesh into a curve
    bpy.ops.object.convert(target='CURVE')

    # add bevel to curve
    bpy.context.object.data.bevel_depth = 0.05
    bpy.context.object.data.bevel_resolution = 16
    # shade smooth
    bpy.ops.object.shade_smooth()