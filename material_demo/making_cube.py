import bpy

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
#            (0,1,2,3),
#            (4,5,6,7),
            (0,4,7,3),
            (0,4,5,1)
            ]
    mesh_data = bpy.data.meshes.new("cube_data")
    mesh_data.from_pydata(verts, edges, faces)
    mesh_obj = bpy.data.objects.new("cube_object", mesh_data)
    mesh_obj.location = (0, 0, 1)
    mesh_obj.scale.x = 2
    bpy.context.collection.objects.link(mesh_obj)

def main():
    clean_the_scene()
    create_wall()
main()










