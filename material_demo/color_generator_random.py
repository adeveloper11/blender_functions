# import bpy
# import random
# bpy.ops.mesh.primitive_plane_add()
# plane = bpy.context.active_object
# # generate random color
# red = random.random()
# green = random.random()
# blue = random.random()
# alpha = 1
# color = (red, green, blue, alpha)
# # create new material
# mat = bpy.data.materials.new("text")
# mat.diffuse_color= color
# plane.data.materials.append(mat)


#give python access to blenders functionality
import bpy
# give python access to blenders mesh editing functionality
import bmesh
# extend python functionality to generate random numbers
import random

def get_random_color():
     # generate random color
    red = random.randint(0.0, 1.0)
    green = random.randint(0.0, 1.0)
    blue = random.randint(0.0,1.0)
    alpha = 1.0
    color = (red, green, blue, alpha)
    return color

def generate_random_color_materials(obj,count):
    for i in range(count):
        # create a new material
        mat = bpy.data.materials.new(f"material_{i}")
        mat.diffuse_color = get_random_color()
        # add material to the object
        obj.data.materials.append(mat)

def add_ico_sphere():   
    # add an ico sphere
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3)
    return bpy.context.active_object
ico_object = add_ico_sphere()
    
def assign_material_to_the_faces(obj):
        # turn on edit mode
    bpy.ops.object.editmode_toggle()
    # deselect all faces
    bpy.ops.mesh.select_all()
    # get grpmetry data from meah object
    ico_bmesh = bmesh.from_edit_mesh(ico_object.data)
    # iterate through each face of the mesh
    for face in ico_bmesh.faces:
        # set active material
        ico_object.active_material_index = random.randint(0, material_count)
        # select the face and assign the active material
        face.select = True
        bpy.ops.object.material_slot_assign()

        face.select = False

    # turn off edit mode
    bpy.ops.object.editmode_toggle()
    
# create a veriable for assign material to the object
material_count = 30
generate_random_color_materials(obj=ico_object,count=material_count)
assign_material_to_the_faces(ico_object)
   