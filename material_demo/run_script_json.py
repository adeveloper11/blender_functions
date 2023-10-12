import pathlib
import bmesh
import bpy
import json

def delete_all_objects():
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.mode_set(mode = "OBJECT")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

def get_mesh_data(mesh_obj):
    bpy.ops.object.mode_set(mode="EDIT")
    bmesh_obj = bmesh.from_edit_mesh(mesh_obj.data)
    face_to_vert = []
    for face in bmesh_obj.faces:
        face_verts = []
        for vert in face.verts:
            face_verts.append(vert.index)
        face_to_vert.append(face_verts)
    print(face_to_vert)
    vert_count = len(bmesh_obj.verts)
    vert_coords = [None] * vert_count
    for vert in bmesh_obj.verts:
        vert_coords[vert.index] = list(vert.co)
    bpy.ops.object.mode_set(mode="OBJECT")
    data = {
        "object_name" : mesh_obj.name,
        "object_location" : list(mesh_obj.location),
        "face_verts" : face_to_vert, 
        "vert_coordinates" : vert_coords,
    }
    return data
def get_path_to_mesh_data():
    return pathlib.Path.home() / "C:\\ABHINAV\\json_data\\mesh.json"    
def save_data(data):
    path_to_file = get_path_to_mesh_data()
    with open (path_to_file, "w") as out_file_obj:
        text = json.dumps(data, indent=4)
        out_file_obj.write(text)

def create_json_data_from_mesh():
    bpy.ops.mesh.primitive_ico_sphere_add()
    mesh_obj = bpy.context.active_object
    mesh_obj.location = (5, 5, 5)
    data = get_mesh_data(mesh_obj)
    save_data(data)  

def load_data():
    path_to_file = get_path_to_mesh_data()
    with open (path_to_file, "r") as in_file_obj:
        text = in_file_obj.read()
        data = json.loads(text)
    return data
def create_mesh_from_data(data):
    verts = data['vert_coordinates']       
    edges = []
    faces = data['face_verts']
    object_name = data["object_name"]
    mesh_data = bpy.data.meshes.new(f"{object_name}_data")
    mesh_data.from_pydata(verts, edges, faces)
    mesh_obj = bpy.data.objects.new(object_name, mesh_data)
    mesh_obj.location = data["object_location"]
    bpy.context.collection.objects.link(mesh_obj)

def create_mesh_from_json_data():
# create  mesh from json data() :
    data = load_data()
    create_mesh_from_data(data)

def main():
    delete_all_objects()
    # create_json_data_from_mesh()
    create_mesh_from_json_data()
main()

