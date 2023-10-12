import bpy
import math
import datetime
def clean_the_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
def create_material(name):
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True
    principled_bsdf_node = material.node_tree.nodes["Principled BSDF"]
    image_tex_node = create_image_texture(material)
    material.node_tree.links.new(image_tex_node.outputs["Color"], principled_bsdf_node.inputs["Base Color"])
    return material  
def create_image_texture(material):
    node_location_x_step = 300
    current_node_location_x = -node_location_x_step

    image_tex_node = material.node_tree.nodes.new(type="ShaderNodeTexImage")
    image_tex_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    image_path = "C:/Users/it/Downloads/blendertexture/golden_color.png"
    image = bpy.data.images.load(image_path) # load images though bpy
    image_tex_node.image = image

    mapping_node = material.node_tree.nodes.new(type="ShaderNodeMapping")
    mapping_node.inputs["Scale"].default_value.x = 2
    mapping_node.inputs["Scale"].default_value.y = 2
    mapping_node.inputs["Scale"].default_value.z = 2
    mapping_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    texture_coordinate_node = material.node_tree.nodes.new(type="ShaderNodeTexCoord")
    texture_coordinate_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    material.node_tree.links.new(texture_coordinate_node.outputs["UV"], mapping_node.inputs["Vector"])
    material.node_tree.links.new(mapping_node.outputs["Vector"], image_tex_node.inputs["Vector"])
    return image_tex_node
def create_material2():
    material2 = bpy.data.materials.new(name="Generated metallic material")
    material2.use_nodes = True
    principle_bsdf_node = material2.node_tree.nodes["Principled BSDF"]
    principle_bsdf_node.inputs["Base Color"].default_value = (0.8, 0.175571, 0.0978418, 1)
    principle_bsdf_node.inputs["Metallic"].default_value = 0
    node_location_x_step = 300
    current_node_location_x = -node_location_x_step

    color_ramp_node = material2.node_tree.nodes.new(type = "ShaderNodeValToRGB") 
    color_ramp_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step 

    noise_texture_node = material2.node_tree.nodes.new(type = "ShaderNodeTexNoise")
    noise_texture_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step 

    mapping_node = material2.node_tree.nodes.new(type = "ShaderNodeMapping")
    mapping_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    texture_coordinate_node = material2.node_tree.nodes.new(type = "ShaderNodeTexCoord")
    texture_coordinate_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    material2.node_tree.links.new(color_ramp_node.outputs["Color"], 
                            principle_bsdf_node.inputs["Roughness"])
    material2.node_tree.links.new(noise_texture_node.outputs["Color"],
                                        color_ramp_node.inputs["Fac"])
    material2.node_tree.links.new(mapping_node.outputs["Vector"],
                        noise_texture_node.inputs["Vector"])
    material2.node_tree.links.new(texture_coordinate_node.outputs["Generated"],
                                    mapping_node.inputs["Vector"])
    return material2

def create_material3():
    material3 = bpy.data.materials.new(name="GreenTexture")
    material3.use_nodes = True
    principled_bsdf_node = material3.node_tree.nodes["Principled BSDF"]
    image_tex_node = green_tex_node(material3)
    material3.node_tree.links.new(image_tex_node.outputs["Color"], principled_bsdf_node.inputs["Base Color"])
    return material3   

def green_tex_node(material3):
    node_location_x_step = 300
    current_node_location_x = -node_location_x_step

    green_tex = material3.node_tree.nodes.new(type="ShaderNodeTexImage")
    green_tex.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    image_path = "C:/Users/it/Downloads/blendertexture/grapee.png"
    image = bpy.data.images.load(image_path) # load images though bpy
    green_tex.image = image

    mapping_node = material3.node_tree.nodes.new(type="ShaderNodeMapping")
    mapping_node.inputs["Scale"].default_value.x = 2
    mapping_node.inputs["Scale"].default_value.y = 2
    mapping_node.inputs["Scale"].default_value.z = 2
    mapping_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    texture_coordinate_node = material3.node_tree.nodes.new(type="ShaderNodeTexCoord")
    texture_coordinate_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    material3.node_tree.links.new(texture_coordinate_node.outputs["UV"], mapping_node.inputs["Vector"])
    material3.node_tree.links.new(mapping_node.outputs["Vector"], green_tex.inputs["Vector"])
    return green_tex
  

def add_mesh():
    bpy.ops.mesh.primitive_cylinder_add()
    bpy.ops.object.shade_smooth()
    mesh_obj = bpy.context.active_object
    mesh_obj.name = "cycl"
    mesh_obj.location = (4, -0, 4)
    mesh_obj.scale = (1.5, 1.5, 3)
    return mesh_obj
def add_icosphere():
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5)
    ico_obj = bpy.context.active_object
    ico_obj.location = (1, 1, 2)
    return ico_obj
def add_floor():
    bpy.ops.mesh.primitive_plane_add(size=20)
    floor_obj = bpy.context.active_object
    floor_obj.location = (0, 0, .5)
    return floor_obj
def add_light():
    light_data = bpy.data.lights.new('light', type='AREA')
    light = bpy.data.objects.new('light', light_data)
    bpy.context.collection.objects.link(light)
    light.location=(3, -3, 5)
    light.data.energy=400.0
    #axis angle
    light.rotation_euler[0] = math.radians(125)
    return light
def add_camera():
    cam_data = bpy.data.cameras.new('camera')
    cam = bpy.data.objects.new('camera', cam_data) # create new objects for the camera
    bpy.context.collection.objects.link(cam)   # adding the camera to the scene collection
    cam.name = "cam"
    cam.location = (2.38, -13.8, 2.51)
    cam.scale=(0.56, .170, 1.74)
    cam.rotation_euler[0] = math.radians(92)
    cam.rotation_euler[1] = math.radians(2)
    cam.rotation_euler[2] = math.radians(3)
    # track the object
    constraint = cam.constraints.new(type = 'TRACK_TO')
    constraint.target = bpy.context.scene.objects.get("cycl")
    return cam
def add_scene():
    scene = bpy.context.scene
    scene.camera = bpy.context.scene.objects.get("cam")
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.device = 'GPU'
    bpy.context.scene.cycles.samples = 32
    bpy.context.scene.cycles.adaptive_min_samples = 0

    # Set the render resolution
    scene.render.resolution_x = 1080  # Change the width to your desired resolution
    scene.render.resolution_y = 720  # Change the height to your desired resolution
    scene.render.image_settings.file_format = 'PNG'
#    for angle in range(0, 360): 
    crnt_time = datetime.datetime.now()     
    n_add =str(crnt_time)[-6:-1]
    scene.render.filepath = f"C:\\Users\\it\\Downloads\\blendertexture\\renderedImage\\created{n_add}.png"    
    bpy.ops.render.render(write_still=1)
    return scene
def load_prop(prop_load_path):
    with bpy.data.libraries.load(prop_load_path) as (data_from, data_to):
        data_to.objects = [name for name in data_from.objects]
    for obj in data_to.objects:
        obj.location = (0, 0, 5)
        obj.scale = (50, 50, 50)
        bpy.context.collection.objects.link(obj)
    return data_to.objects
def add_circle_mesh():
    bpy.ops.mesh.primitive_circle_add(vertices=32, radius = 1)
    circle = bpy.context.active_object
    
    for vert in circle.data.vertices:
        print("coord:", vert.co)
        
    
def main():
    clean_the_scene()
    name = "my_generated_material"
    material = create_material(name)
    marterial2 = create_material2()
    material3 = create_material3()
    ico_object = add_icosphere()
    add_light()
    add_camera()
    add_circle_mesh()
    mesh_obj = add_mesh()
    floor_obj = add_floor()
    prop_load_path = "C:\\Users\\it\\Downloads\\blendertexture\\FoodGrapes001_Grape001_Cycles.blend"
    load_prop(prop_load_path)
    # Apply the material to the mesh_object we created
    mesh_obj.data.materials.append(marterial2)
    ico_object.data.materials.append(material3)
    floor_obj.data.materials.append(material)
    add_scene()


main()