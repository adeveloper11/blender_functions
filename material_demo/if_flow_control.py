import bpy
import random

curr = 2.3

for i in range(10):
    if i>=5:
        bpy.ops.mesh.primitive_cone_add(location=(0, i*curr,i*curr))
    else:
        bpy.ops.mesh.primitive_monkey_add(location=(0, i*curr,i*curr))