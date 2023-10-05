import bpy

bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(-2.06664, -0.909177, 5.88729))

bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\imagine\Documents\test.blend")

