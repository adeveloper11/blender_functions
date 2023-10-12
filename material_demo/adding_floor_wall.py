import bpy
import math
import mathutils
import datetime
def clean_the_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
def create_wall():
    verts = [
        (-1.0, -1.0, -1.0),
        (-1.0, 1.0, -1.0),
        (1.0, 1.0, -1.0),
        (1.0, -1.0, -1.0),
        
        (-1.0, -1.0, 1.0),
        (-1.0, 1.0, 1.0),
        (1.0, 1.0, 1.0),
        (1.0, -1.0, 1.0),         
        ]
    edges = []
    faces = [
            (0,4,7,3),
            (0,4,5,1)
            ]
    mesh_data = bpy.data.meshes.new("cube_data")
    mesh_data.from_pydata(verts, edges, faces)
    mesh_obj = bpy.data.objects.new("cube_object", mesh_data)
    mesh_obj.name = "wall"
    mesh_obj.location = (-0.43, -0.004, 2.23)
    mesh_obj.scale.x = 5
    mesh_obj.scale.y = 5
    mesh_obj.scale.z = 3
    bpy.context.collection.objects.link(mesh_obj)

def add_floor():
    bpy.ops.mesh.primitive_plane_add(size=10)
    floor_obj = bpy.context.active_object
    floor_obj.name = "floor"
    floor_obj.location = (0, 0, .5)

def add_camera():
    cam_data = bpy.data.cameras.new("camera")
    cam1 = bpy.data.objects.new("camera1", cam_data)
    cam1.name = "cam"
    bpy.context.collection.objects.link(cam1)
    cam1.location=(6.85, 8.75, 5.34)
    cam1.rotation_euler[0] = math.radians(-105)
    cam1.rotation_euler[1] = math.radians(-184)
    cam1.rotation_euler[2] = math.radians(-40)

def material_floor():
    floor_material = bpy.data.materials.new(name="flooring")
    floor_material.use_nodes = True
    floor = bpy.context.scene.objects.get("floor")
    floor.data.materials.append(floor_material)
    principle_bsdf_node = floor_material.node_tree.nodes["Principled BSDF"]
    principle_bsdf_node.inputs["Roughness"].default_value = 1

    # Setting the location
    node_location_x_step = 300
    current_node_location_x = -node_location_x_step

    # Created image node
    image_tex_node = floor_material.node_tree.nodes.new(type="ShaderNodeTexImage")
    image_tex_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    # Load your image file here
    image_path ="C:\\Users\\it\\Downloads\\wooden-floor-1853405_1920.jpg"
    image = bpy.data.images.load(image_path) # load images though bpy
    image_tex_node.image = image

    # Creating a mapping node
    mapping_node = floor_material.node_tree.nodes.new(type="ShaderNodeMapping")
    mapping_node.inputs["Scale"].default_value.x = 1
    mapping_node.inputs["Scale"].default_value.y = 2
    mapping_node.inputs["Scale"].default_value.z = 2
    
    
    mapping_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    # Texture Coordinate node
    texture_coordinate_node = floor_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
    texture_coordinate_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    floor_material.node_tree.links.new(texture_coordinate_node.outputs["UV"], mapping_node.inputs["Vector"])
    floor_material.node_tree.links.new(mapping_node.outputs["Vector"], image_tex_node.inputs["Vector"])
    floor_material.node_tree.links.new(principle_bsdf_node.inputs["Base Color"], image_tex_node.outputs["Color"])

def wall_material():
    floor_material = bpy.data.materials.new(name="side wall")
    floor_material.use_nodes = True
    floor = bpy.context.scene.objects.get("wall")
    floor.data.materials.append(floor_material)
    principle_bsdf_node = floor_material.node_tree.nodes["Principled BSDF"]

    # Setting the location
    node_location_x_step = 300
    current_node_location_x = -node_location_x_step

    # Created image node
    image_tex_node = floor_material.node_tree.nodes.new(type="ShaderNodeTexImage")
    image_tex_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    # Load your image file here
    image_path ="C:\\Users\\it\\Downloads\\floor.jpg"
    image = bpy.data.images.load(image_path) # load images though bpy
    image_tex_node.image = image

    # Creating a mapping node
    mapping_node = floor_material.node_tree.nodes.new(type="ShaderNodeMapping")
    mapping_node.inputs["Scale"].default_value.x = -30
    mapping_node.inputs["Scale"].default_value.y = 2
    mapping_node.inputs["Scale"].default_value.z = 2
    
    mapping_node.inputs["Location"].default_value.x = 1.1
    mapping_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    # Texture Coordinate node
    texture_coordinate_node = floor_material.node_tree.nodes.new(type="ShaderNodeTexCoord")
    texture_coordinate_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    floor_material.node_tree.links.new(texture_coordinate_node.outputs["UV"], mapping_node.inputs["Vector"])
    floor_material.node_tree.links.new(mapping_node.outputs["Vector"], image_tex_node.inputs["Vector"])
    floor_material.node_tree.links.new(principle_bsdf_node.inputs["Base Color"], image_tex_node.outputs["Color"])

def table(prop_load_path):
    with bpy.data.libraries.load(prop_load_path) as (data_from, data_to):
        data_to.objects = [name for name in data_from.objects]
    for obj in data_to.objects:
        obj.location = (-0.74, -1.14, 0.51407)
        obj.scale = (2, 2, 2)
        bpy.context.collection.objects.link(obj)
    return data_to.objects

def rocking_chair(prop_load_path):
    with bpy.data.libraries.load(prop_load_path) as (data_from, data_to):
        data_to.objects = [name for name in data_from.objects]
    for obj in data_to.objects:
        obj.location = (-0.66, 1.06, 0.29)
        obj.scale = (2, 2, 2)
        bpy.context.collection.objects.link(obj)
    return data_to.objects

def sofa(prop_load_path):
    with bpy.data.libraries.load(prop_load_path) as (data_from, data_to):
        data_to.objects = [name for name in data_from.objects]
    for obj in data_to.objects:
        obj.location = (-1.61, -3.85, 0.49)
        obj.scale = (2, 2, 2)
        obj.rotation_euler[2] = math.radians(-182)
        bpy.context.collection.objects.link(obj)
    return data_to.objects
def pot(prop_load_path):
    with bpy.data.libraries.load(prop_load_path) as (data_from, data_to):
        data_to.objects = [name for name in data_from.objects]
    for obj in data_to.objects:
        obj.location = (-0.8, -1.1, 2.51)
        obj.scale = (2, 2, 2)
        obj.rotation_euler[2] = math.radians(-182)
        bpy.context.collection.objects.link(obj)
    return data_to.objects
def add_area_light():
    light_data = bpy.data.lights.new('light', type='AREA')
    light = bpy.data.objects.new('light', light_data)
    bpy.context.collection.objects.link(light)
    light.location=(-3, -0.4, 6.21)
    light.data.energy=400.0
    #axis angle
    light.rotation_euler[0] = math.radians(-4)
    light.rotation_euler[1] = math.radians(3)
    light.rotation_euler[2] = math.radians(127)
    return light
def add_sun_light():
    light_data = bpy.data.lights.new('light', type='SUN')
    light = bpy.data.objects.new('light', light_data)
    bpy.context.collection.objects.link(light)
    light.location=(-5, 6, 5.21)
    light.data.energy=4.0
    #axis angle
    light.rotation_euler[0] = math.radians(40)
    light.rotation_euler[1] = math.radians(-71)
    light.rotation_euler[2] = math.radians(-128)
    return light

def environment_background():
    node_tree = bpy.context.scene.world.node_tree
    tree_nodes = node_tree.nodes
    tree_nodes.clear()
    location_x = 0
    world_node_tree = bpy.context.scene.world.node_tree.nodes
    output_node = world_node_tree.new(type="ShaderNodeOutputWorld")
    output_node.location.x = location_x
    location_x -= 250
    background_node = world_node_tree.new(type="ShaderNodeBackground")
    background_node.location.x = location_x
    location_x -= 250

    environment_node = world_node_tree.new(type="ShaderNodeTexEnvironment")
    environment_node.location.x = location_x
    location_x -= 250

    image_path = "C:\\Users\\it\\Downloads\\pine_attic_2k.exr"
    environment_node.image = bpy.data.images.load(image_path)

    mapping_node = world_node_tree.new(type="ShaderNodeMapping")
    mapping_node.location.x = location_x
    location_x -= 250

    texcoord_node = world_node_tree.new(type="ShaderNodeTexCoord")
    texcoord_node.location.x = location_x
    location_x -= 250
    links = node_tree.links
    links.new(environment_node.outputs["Color"], background_node.inputs["Color"])
    links.new(mapping_node.outputs["Vector"], environment_node.inputs["Vector"])
    links.new(texcoord_node.outputs["Generated"], mapping_node.inputs["Vector"])
    links.new(background_node.outputs["Background"], output_node.inputs["Surface"])

def add_scene():
    scene = bpy.context.scene
    scene.camera = bpy.context.scene.objects.get("cam")
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.device = 'GPU'
    bpy.context.scene.cycles.samples = 32
    bpy.context.scene.cycles.adaptive_min_samples = 0
    scene.render.resolution_x = 1080  # Change the width to your desired resolution
    scene.render.resolution_y = 720  # Change the height to your desired resolution
    scene.render.image_settings.file_format = 'PNG'
    crnt_time = datetime.datetime.now()     
    n_add =str(crnt_time)[-6:-1]
    scene.render.filepath = f"C:\\ABHINAV\\blender_output_image\\created{n_add}.png"    
    bpy.ops.render.render(write_still=1)

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
    # create_wall()
    # wall_material()
    add_floor()
    material_floor()
    add_camera()
    add_area_light()
    add_sun_light()
    environment_background()
    table("C:\\Users\\it\Downloads\\round_wooden_table_01_4k.blend\\round_wooden_table_01_4k.blend")
    rocking_chair("C:\\Users\\it\\Downloads\\Rockingchair_01_4k.blend\\Rockingchair_01_4k.blend")
    sofa("C:\\Users\\it\\Downloads\\sofa_03_4k.blend\\sofa_03_4k.blend")
    pot("C:\\Users\\it\\Downloads\\potted_plant_04_4k.blend\\potted_plant_04_4k.blend")
    add_scene()


main()