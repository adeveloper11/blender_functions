import bpy
import random


def clean_the_scene():
    # select all tje objects in the scene
    bpy.ops.object.select_all(action="SELECT")

    # DELETE ALL selected objects in the scene
    bpy.ops.object.delete()

    # cleans the multiple materials creating 
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)


def create_material(name):
    # creating material
    material = bpy.data.materials.new(name=name)

    #enables creating a material via nodes
    material.use_nodes = True

    #getting a refereance to the principled BSDF shader node
    principle_bsdf_node = material.node_tree.nodes["Principled BSDF"]


    # set the base color to the material
    # bpy.data.materials["Material"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.0924522, 0.119165, 0.8, 1)
    principle_bsdf_node.inputs["Base Color"].default_value = (0.8, 0.175571, 0.0978418, 1)



    # adding code  for the metalic property
    principle_bsdf_node.inputs["Metallic"].default_value = 0

    # set the roughness using random module
#    principle_bsdf_node.inputs["Roughness"].default_value = random.uniform(0.1, 1.0)
    
    
    #setting the location 
    node_location_x_step = 300
    current_node_location_x = -node_location_x_step
    
    # created color Ramp node
    color_ramp_node = material.node_tree.nodes.new(type = "ShaderNodeValToRGB")
    
    color_ramp_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    
    
    # create a noise Texture node
    
    noise_texture_node = material.node_tree.nodes.new(type = "ShaderNodeTexNoise")
    noise_texture_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    
    
    # creating a mapping node
    
    mapping_node = material.node_tree.nodes.new(type = "ShaderNodeMapping")
    mapping_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    
    # create a texture Coordinate node
    
    texture_coordinate_node = material.node_tree.nodes.new(type = "ShaderNodeTexCoord")
    texture_coordinate_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step

    
    

    
    
    
    
    
    ######### connecting the nodes
    material.node_tree.links.new(color_ramp_node.outputs["Color"], 
                            principle_bsdf_node.inputs["Roughness"])
    
    ## connecting the other node
    material.node_tree.links.new(noise_texture_node.outputs["Color"],
                                        color_ramp_node.inputs["Fac"])

    ## connect node
    material.node_tree.links.new(mapping_node.outputs["Vector"],
                        noise_texture_node.inputs["Vector"])
    
    ## connect node
    
    material.node_tree.links.new(texture_coordinate_node.outputs["Generated"],
                                    mapping_node.inputs["Vector"])
    
    



    return material

def add_mesh():
    # creating an ico sphere
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5)

    # shading smooth
    bpy.ops.object.shade_smooth()

    # getting a reference of the object we added into the scene
    mesh_obj = bpy.context.active_object

    return mesh_obj

def main():

    clean_the_scene()
    name = "my_generated_material"
    material = create_material(name)
    mesh_obj = add_mesh()

    


    # apply the material to the mesh_object we created

    mesh_obj.data.materials.append(material)

main()


##############2
# import bpy

# bpy.ops.mesh.primitive_cube_add(size=3, location=(0 , 0, 1.5))
# cube = bpy.context.active_object
# bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
# plane = bpy.context.active_object

# cam_data = bpy.data.cameras.new("camera")
# cam1 = bpy.data.objects.new("camera1", cam_data)
# cam1.location=(25,-3,20)
# bpy.context.collection.objects.link(cam1)

# mat = bpy.data.materials.new(name="material1")
# cube.data.materials.append(mat)
# mat.use_nodes = True

# mat_nodes = mat.node_tree.nodes
# mat_links = mat.node_tree.links
# mat_nodes["Principled BSDF"].inputs["Metallic"].default_value=5.0
# mat_nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.04, 0.02, 0.01, 1.0)

# mat2 = bpy.data.materials.new(name="material2")
# mat2.use_nodes = True
# plane.data.materials.append(mat2)