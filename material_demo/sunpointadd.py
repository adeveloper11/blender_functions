# Study about Point sun spot and area lights in blender
# Add these light in blender file using python
# Change their position ,rotation , size , color , intensity
# Study about camera and its fov focal length
# Add camera in scene, rotate camera position
# Study about resolution and samples of scene
# Change resolution and sample
# Render image of scene

import bpy
import math
def clean_the_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

def create_material(name):
    # Creating material
    material = bpy.data.materials.new(name=name)
    material.use_nodes = True
    # Getting a reference to the principled BSDF shader node
    principled_bsdf_node = material.node_tree.nodes["Principled BSDF"]
    # calling the image_textur function here and assigning it to a variable
    image_tex_node = create_image_texture(material)
    # Link the image texture node to the Base Color of Principled BSDF
    material.node_tree.links.new(image_tex_node.outputs["Color"], principled_bsdf_node.inputs["Base Color"])
    return material
 
def create_image_texture(material):
    # Setting the location
    node_location_x_step = 300
    current_node_location_x = -node_location_x_step

    # Created image node
    image_tex_node = material.node_tree.nodes.new(type="ShaderNodeTexImage")
    image_tex_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    # Load your image file here
    image_path = "C:/Users/it/Downloads/blendertexture/FoodGrapes001_COL_1K_METALNESS.png" 
    image = bpy.data.images.load(image_path) # load images though bpy
    image_tex_node.image = image

    # Creating a mapping node
    mapping_node = material.node_tree.nodes.new(type="ShaderNodeMapping")
    mapping_node.inputs["Scale"].default_value.x = 2
    mapping_node.inputs["Scale"].default_value.y = 2
    mapping_node.inputs["Scale"].default_value.z = 2
    mapping_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    # Texture Coordinate node
    texture_coordinate_node = material.node_tree.nodes.new(type="ShaderNodeTexCoord")
    texture_coordinate_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    material.node_tree.links.new(texture_coordinate_node.outputs["UV"], mapping_node.inputs["Vector"])
    material.node_tree.links.new(mapping_node.outputs["Vector"], image_tex_node.inputs["Vector"])

    return image_tex_node

def add_mesh():
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5)
    # bpy.ops.object.shade_smooth()
    mesh_obj = bpy.context.active_object
    mesh_obj.location = (3, 1, 2)
    return mesh_obj

def add_floor():
    bpy.ops.mesh.primitive_plane_add(size=20)
    # bpy.ops.object.shade_smooth()
    floor_obj = bpy.context.active_object
    floor_obj.location = (0, 0, .5)
    return floor_obj

def add_light():
    light_data = bpy.data.lights.new('light', type='AREA')  
    light = bpy.data.objects.new('light', light_data)
    bpy.context.collection.objects.link(light)
    light.location=(3, 3, 1)
    light.data.energy=500.0
#    light.data.color = (0.2, 0.6, 1)
#    light.data.["Rotation"].default_value.x = math.radians(random.uniform(0.0, 360.0))
    light.rotation_euler[0] = math.radians(206)
    light.rotation_euler[1] = math.radians(100)
    light.rotation_euler[2] = math.radians(300)
    # 2nd light
    light_data2 = bpy.data.lights.new('light', type='POINT')  
    light2 = bpy.data.objects.new('light', light_data2)
    bpy.context.collection.objects.link(light2)
    light2.location=(0.3, -3, 0.63)
    light2.data.energy=500.0
#    light2.data.color = (0.2, 0.6, 1)
    light2.rotation_euler[0] = math.radians(125)
    light2.rotation_euler[1] = math.radians(-57)
    light2.rotation_euler[2] = math.radians(-93)
    
    return light

#adding a camera
def add_camera():
    cam_data = bpy.data.cameras.new('camera')
    cam = bpy.data.objects.new('camera', cam_data) # create new objects for the camera
    bpy.context.collection.objects.link(cam)   # adding the camera to the scene collection
    cam.location = (4, -3, 12.51)
    cam.scale=(1, 2, 4)
    cam.rotation_euler[0] = math.radians(4)
    cam.rotation_euler[1] = math.radians(-7)
    cam.rotation_euler[2] = math.radians(21)
    # track the object
    constraint = cam.constraints.new(type = 'TRACK_TO')
    constraint.target = add_mesh()

    return cam

def add_scene():
    scene = bpy.context.scene
    scene.camera = add_camera()
    # Set the render resolution
    scene.render.resolution_x = 3840  # Change the width to your desired resolution
    scene.render.resolution_y = 2160  # Change the height to your desired resolution
    scene.render.image_settings.file_format = 'PNG'
#    for angle in range(0, 360):
        
    scene.render.filepath = "C:\\Users\\it\\Downloads\\blendertexture\\renderedImage\\created_3.png"
    bpy.ops.render.render(write_still=1)
    return scene


def main():
    clean_the_scene()
    name = "my_generated_material"
    material = create_material(name)
    light = add_light()
    cam = add_camera()
    mesh_obj = add_mesh()
    floor_obj = add_floor()
    scene = add_scene()
    # Apply the material to the mesh_object we created
    mesh_obj.data.materials.append(material)

main()