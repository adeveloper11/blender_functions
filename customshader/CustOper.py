import bpy


class Shader_Ot_neon(bpy.types.Operator):
    bl_label = "Add Neon Shader"
    bl_idname = "shader.neon_operator"

    def execute(self, context):

        cur_frame = bpy.context.scene.frame_current # reference for the current frame


        material_neon = bpy.data.materials.new(name = "neon")
        material_neon.use_nodes = True


        tree = material_neon.node_tree



        material_neon.node_tree.nodes.remove(material_neon.node_tree.nodes.get('Principled BSDF'))
        material_output = material_neon.node_tree.nodes.get('Material Output')
        # set location of Node
        material_output.location = (400, 0)

        #NODE IS ADDED
        emiss_node = material_neon.node_tree.nodes.new('ShaderNodeEmission')
        emiss_node.location = (200, 0)
        #setting the default color
        emiss_node.inputs[0].default_value = (1, 0, 0, 1) 
        # Setting the default Strength value
        emiss_node.inputs[1].default_value = 2
        emiss_node.inputs[1].keyframe_insert("default_value", frame= cur_frame)

        data_path = f'nodes["{emiss_node}"].inputs[1].default_value'

        fcurves = tree.animations_data.action.fcurves
        fc = fcurves.find(data_path)

        if fc:
            new_mod = fc.modifiers.new('NOISE')
            new_mod.strength = 10
            new_mod.depth = 1





        material_neon.node_tree.links.new(emiss_node.outputs[0], material_output.inputs[0])



        return {'FINISHED'}

