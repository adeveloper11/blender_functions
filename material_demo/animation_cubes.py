import bpy


bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

current_location = 0

for i in range(10):
    bpy.ops.mesh.primitive_cube_add()
    cube = bpy.context.active_object
    cube.location = (current_location, 0, 0)
    current_location +=2.5
    
cubes = bpy.data.collections['Cubes'].objects

for x in cubes:
    x.scale = [0, 0, 0]
    x.keyframe_insert(data_path = "scale", frame = 1)
    x.scale = [1, 1, 5]
    x.keyframe_insert(data_path = "scale", frame = 50)
    x.scale = [1, 2, 1]
    x.keyframe_insert(data_path = "scale", frame = 70)
    x.scale = [1, 1, 1]
    x.keyframe_insert(data_path = "scale", frame = 80)