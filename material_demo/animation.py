import bpy
import datetime
import math

def clean_the_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
def add_mesh():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
    current_location = 0
    for i in range(10):
        bpy.ops.mesh.primitive_cube_add()
        cube = bpy.context.active_object
        cube.name = "cube"
        cube.location = (current_location, 0, 0)
        current_location +=2.5
def add_camera():
    cam_data = bpy.data.cameras.new("camera")
    cam1 = bpy.data.objects.new("camera1", cam_data)
    cam1.name = "cam"
    cam1.location=(0.62,-2.36,22)
    bpy.context.collection.objects.link(cam1)
def add_light():
    light_data = bpy.data.lights.new('light', type='AREA')
    light = bpy.data.objects.new('light', light_data)
    bpy.context.collection.objects.link(light)
    light.location=(3, -3, 5)
    light.data.energy=400.0
    #axis angle
    light.rotation_euler[0] = math.radians(125)
    return light
def add_animation():
    scene = bpy.context.scene
    scene.camera = bpy.context.scene.objects.get("cam")
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.device = 'GPU'
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
    current_time = datetime.datetime.now()
    n_add = str(current_time)[-6:-1]
    scene.render.filepath = f"C:\\ABHINAV\\blender_output_image\\created{n_add}.mp4"

    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.ffmpeg.codec = 'H264'
    bpy.context.scene.render.ffmpeg.constant_rate_factor = 'MEDIUM'

    bpy.ops.render.render(animation=True)

def main():
    clean_the_scene()
    add_mesh()
    add_camera()
#    material()
    add_light()
    # add_scene()
    add_animation()
main()