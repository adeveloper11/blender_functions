import bpy

cube_count = 10
location_offset = 3
frame_count = 250
fps = 30
def set_end_frame(frame_count):
    bpy.context.scene.frame_end = frame_count
set_end_frame(frame_count)

def set_render_fps():
    bpy.context.scene.render.fps = fps
set_render_fps()

def create_row(cube_count, location_offset):
    for i in range(cube_count):
        bpy.ops.mesh.primitive_cube_add(size=2,
                                        location=(0, i*location_offset, 0))
create_row(cube_count, location_offset)

def create_empty():   
    bpy.ops.object.empty_add()
    empty = bpy.context.active_object
    empty.name = "empty"
    return empty
empty = create_empty()

def create_keyframe(empty, location_offset, frame_count):
    empty.keyframe_insert("location", frame=1)
    empty.location.y = cube_count * location_offset
    empty.keyframe_insert("location", frame=frame_count)
create_keyframe(empty, location_offset, frame_count)


def add_camera(cube_count, location_offset, empty):
    bpy.ops.object.camera_add()
    # empty = create_empty.get("empty")
    camera = bpy.context.active_object

    camera.location.x = 15
    camera.location.y = cube_count* location_offset/2
    camera.location.z = 2
    
    bpy.ops.object.constraint_add(type="TRACK_TO")
    camera.constraints["Track To"].target = empty
add_camera(cube_count, location_offset,empty)




