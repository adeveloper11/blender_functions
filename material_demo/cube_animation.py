import bpy

cubes = bpy.data.collections['Cubes'].objects

for x in cubes:
    x.scale = [0,0,0]