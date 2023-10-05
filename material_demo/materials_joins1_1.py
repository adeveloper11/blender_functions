import bpy
import random
import math


def clean_the_scene():
    # select all tje objects in the scene
    bpy.ops.object.select_all(action="SELECT")

    # DELETE ALL selected objects in the scene
    bpy.ops.object.delete()

    # cleans the multiple materials creating 
    bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)


def create_noise_mask(material):
    
     
    
    #setting the location 
    node_location_x_step = 300
    current_node_location_x = -node_location_x_step
    
    # created color Ramp node
    color_ramp_node = material.node_tree.nodes.new(type = "ShaderNodeValToRGB")
    
    color_ramp_node.color_ramp.elements[0].position = 0.45
    color_ramp_node.color_ramp.elements[1].position = 0.5
    
    
    color_ramp_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    
    
    # create a noise Texture node
    
    noise_texture_node = material.node_tree.nodes.new(type = "ShaderNodeTexNoise")
    
    # setting the Scale of noise texture
    noise_texture_node.inputs["Scale"].default_value = random.uniform(1.0, 20.0)

    
    
    
    noise_texture_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    
    
    # creating a mapping node
    
    mapping_node = material.node_tree.nodes.new(type = "ShaderNodeMapping")
    
    mapping_node.inputs["Rotation"].default_value.x = math.radians(random.uniform(0.0, 360.0))
    mapping_node.inputs["Rotation"].default_value.y = math.radians(random.uniform(0.0, 360.0))
    mapping_node.inputs["Rotation"].default_value.z = math.radians(random.uniform(0.0, 360.0))

    
    mapping_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    
    # create a texture Coordinate node
    
    texture_coordinate_node = material.node_tree.nodes.new(type = "ShaderNodeTexCoord")
    texture_coordinate_node.location.x = current_node_location_x
    current_node_location_x -= node_location_x_step
    
    
    ######### connecting the nodes
#    material.node_tree.links.new(color_ramp_node.outputs["Color"], 
#                            principle_bsdf_node.inputs["Roughness"])
    
    ## connecting the other node
    material.node_tree.links.new(noise_texture_node.outputs["Color"],
                                        color_ramp_node.inputs["Fac"])

    ## connect node
    material.node_tree.links.new(mapping_node.outputs["Vector"],
                        noise_texture_node.inputs["Vector"])
    
    ## connect node
    
    material.node_tree.links.new(texture_coordinate_node.outputs["Generated"],
                                    mapping_node.inputs["Vector"])
                                    
    
    return color_ramp_node
    
    




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
    principle_bsdf_node.inputs["Metallic"].default_value = 1.0

    # set the roughness using random module
#    principle_bsdf_node.inputs["Roughness"].default_value = random.uniform(0.1, 1.0)
   
    
    color_ramp_node = create_noise_mask(material)
    
    material.node_tree.links.new(color_ramp_node.outputs["Color"], 
                            principle_bsdf_node.inputs["Roughness"])

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