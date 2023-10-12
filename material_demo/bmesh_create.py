import bpy
import bmesh

mesh_obj = bpy.context.active_object

bm = bmesh.new()
bm.from_mesh(mesh_obj.data)

bm.free()