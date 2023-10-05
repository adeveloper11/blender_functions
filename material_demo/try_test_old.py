import bpy
import math
## clean the scene
def clean_the_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
## create material
def create_marerial():
    material = bpy.data.materials.new(name="test1")
    material.use_nodes = True
    principled_bsdf_node = material.node_tree.nodes["Principled BSDF"]
    image_tex_node = create_nodes(material)
    material.node_tree.links.new(image_tex_node.outputs["Color"], principled_bsdf_node.inputs["Base Color"])
    return material
## create different nodes
def create_nodes(material):
    #set_location
    node_location_step = 250
    current_node_location = -node_location_step
    image_tex_node = material.node_tree.nodes.new(type ="ShaderNodeTexImage")
    image_tex_node.location.x = current_node_location
    current_node_location -= node_location_step

    image_path = "C:/Users/it/Downloads/blendertexture/golden_color.png"
    image = bpy.data.images.load(image_path)
    image_tex_node.image = image
# creating mapping Node
    mapping_node = material.node_tree.nodes.new(type= "ShaderNodeMapping")
    mapping_node.inputs["Scale"].default_value.x = 2
    mapping_node.location.x = current_node_location
    current_node_location -= node_location_step
# Texture Cordinate node
    texture_cordinate_node = material.node_tree.nodes.new(type= "ShaderNodeTexCoord") 
    texture_cordinate_node.location.x = current_node_location
    current_node_location -= node_location_step
# link nodes
    material.node_tree.links.new(texture_cordinate_node.outputs["UV"], mapping_node.inputs["Vector"])
    material.node_tree.links.new(mapping_node.outputs["Vector"], image_tex_node.inputs["Vector"])
    return image_tex_node
## create mesh
def create_mesh():
    bpy.ops.mesh.primitive_cube_add()
    mesh_obj = bpy.context.active_object
    mesh_obj.location = (1,1,2)
    return mesh_obj

## create floor
def floor():
    bpy.ops.mesh.primitive_plane_add(size=20)
    floor_obj = bpy.context.active_object
    floor_obj.location = (0, 0, 0.5)
    return floor_obj

## add light
def create_light():
    light_data = bpy.data.lights.new('light', type='AREA')
    light = bpy.data.objects.new('light', light_data)
    bpy.context.collection.objects.link(light)
    light.location=(3, -3, 5)
    light.data.energy=400.0
    #axis angle
    light.rotation_euler[0] = math.radians(125)
    return light
## add camera
def create_camera():
    camera_data = bpy.data.cameras.new('camera')
    cam1 = bpy.data.objects.new('cemera1', camera_data)
    bpy.context.collection.objects.link(cam1)
    cam1.location = (4, -3, 12.51)
    cam1.scale=(1, 2, 4)
    cam1.rotation_euler[0] = math.radians(4)
    cam1.rotation_euler[1] = math.radians(-7)
    cam1.rotation_euler[2] = math.radians(21)
    constraint = cam1.constraints.new(type= 'TRACK_TO')
    constraint.target = create_mesh()
    return cam1

## add scene for showing image
def create_scene():
    scene = bpy.context.scene
    scene.camera = create_camera()
    scene.render.resolution_x = 3840
    scene.render.resolution_y = 2160
    scene.render.image_settings.file_format = 'PNG'
    scene.render.filepath = "C:\\Users\\it\\Downloads\\blendertexture\\renderedImage\\created_now.png" 
    bpy.ops.render.render(write_still=1)
    return scene
## add main 
def main():
    clean_the_scene()
    mesh_obj = create_mesh()
    material = create_marerial()
    floor()
    create_camera()
    create_light()
    scene = create_scene()
    mesh_obj.data.materials.append(material)
main()

