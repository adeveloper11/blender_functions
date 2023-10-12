import bpy
import datetime
import math

def clean_the_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
def add_mesh():
    bpy.ops.mesh.primitive_cube_add(size=3, location=(0 , 0, 1.5))
    cube = bpy.context.active_object
    cube.name = "cube"
    cube.rotation_euler[0] = math.radians(129)
    bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
    plane = bpy.context.active_object
    plane.name = "plane"

def add_camera():
    cam_data = bpy.data.cameras.new("camera")
    cam1 = bpy.data.objects.new("camera1", cam_data)
    cam1.name = "cam"
    cam1.location=(0.62,-2.36,22)
    bpy.context.collection.objects.link(cam1)

def material():
    mat = bpy.data.materials.new(name="material1")
    cube = bpy.context.scene.objects.get("cube")
    cube.data.materials.append(mat)
    mat.use_nodes = True
    mat_nodes = mat.node_tree.nodes
    mat_links = mat.node_tree.links
    mat_nodes["Principled BSDF"].inputs["Metallic"].default_value=5.0
    mat_nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.04, 0.02, 0.01, 1.0)

    mat2 = bpy.data.materials.new(name="material2")
    plane = bpy.context.scene.objects.get("plane")
    plane.data.materials.append(mat2)
    mat2.use_nodes = True
    mat2_nodes = mat2.node_tree.nodes
    mat2_nodes["Principled BSDF"].inputs["Metallic"].default_value=5.0
    mat2_nodes["Principled BSDF"].inputs["Base Color"].default_value=(1, 0.02, 0.01, 1.0)

def add_light():
    light_data = bpy.data.lights.new('light', type='AREA')
    light = bpy.data.objects.new('light', light_data)
    bpy.context.collection.objects.link(light)
    light.location=(3, -3, 5)
    light.data.energy=400.0
    #axis angle
    light.rotation_euler[0] = math.radians(125)
    return light
def add_scene():
    scene = bpy.context.scene
    scene.camera = bpy.context.scene.objects.get("cam")
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.device = 'GPU'
    bpy.context.scene.cycles.samples = 32
    bpy.context.scene.cycles.adaptive_min_samples = 0
    scene.render.resolution_x = 1080
    scene.render.resolution_y = 720
    scene.render.image_settings.file_format = 'PNG'
    current_time = datetime.datetime.now()
    n_add =str(current_time)[-6:-1]
    scene.render.filepath = f"C:\\Users\\it\\Downloads\\blendertexture\\renderedImage\\created{n_add}.png"

    bpy.ops.render.render(write_still=1)
    return scene

def add_animation():
    scene = bpy.context.scene
    cube = bpy.context.scene.objects.get("cube")
    plane = bpy.context.scene.objects.get("plane")

    start_frame = 1
    cube.keyframe_insert("rotation_euler", frame=1)
    cube.rotation_euler.z = math.radians(360)
    end_frame = 180
    cube.keyframe_insert("rotation_euler", frame=end_frame)
    current_time = datetime.datetime.now()
    n_add = str(current_time)[-6:-1]
    scene.render.filepath = f"C:\\Users\\it\\Downloads\\blendertexture\\renderedImage\\animation{n_add}.mp4"

    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.ffmpeg.codec = 'H264'
    bpy.context.scene.render.ffmpeg.constant_rate_factor = 'MEDIUM'

    bpy.ops.render.render(animation=True)

def main():
    clean_the_scene()
    add_mesh()
    add_camera()
    material()
    add_light()
    add_scene()
    add_animation()
main()