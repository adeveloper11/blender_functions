# given python access to belender functionality
import bpy
# extend match functionality
import math
# create cube
bpy.ops.mesh.primitive_cube_add()
# get a reference to the currently active ocject 
cube = bpy.context.active_object
cube.location = (0,0,0)
cube.rotation_euler[0] = 0
cube.rotation_euler[1] = 0

# insert the keyframe at frame one
start_frame = 1
cube.keyframe_insert("rotation_euler", frame=1)

# change the rotation of the cube around the z-axis
degrees = 360
radians = math.radians(degrees)
cube.rotation_euler.z = radians


# insert keyframe at the last frame
end_frame = 180
cube.keyframe_insert("rotation_euler", frame=end_frame)