# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "NewAddOn",
    "author" : "abhi",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "category" : "Object"
}

import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon' # if we wamt to create new or we can add it in already available category.
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Add an object", icon = 'CUBE')
        row = layout.row() #create a space for one line
        row.operator("mesh.primitive_cube_add")
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add")
        row.operator("object.text_add")
        

class PanelA(bpy.types.Panel):
    bl_label = "Scalling"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    bl_parent_id = "PT_TestPanel"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(text = "Select your option to scale object", icon= 'FONT_DATA')
        row = layout.row()
        row.operator("transform.resize")
        row = layout.row()
        
        col = layout.column()
        col.prop(obj, "scale")

class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    bl_parent_id = "PT_TestPanel"
    
    def draw(self, context):
        layout = self.layout

        
        
        row = layout.row()
        row.label(text= "Select a Special Option", icon = 'COLOR_BLUE')

        row.operator("object.shade_smooth")
        row = layout.row()
        row.operator("object.subdivision_set")
        row = layout.row()
        row.operator("object.modifier_add")


class ShaderMainPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    bl_parent_id = "PT_TestPanel"
    
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Select a Shader to be added")
        row.operator('shader.diamond_operator')


# Created Custom operator
class Shared_Ot_Diamond(bpy.types.Operator):
    bl_label = "Add Diamond"
    bl_idname = "shader.diamond_operator"

    def execute(self, context ):

        material_diamond = bpy.data.materials.new(name = "Diamond")
        material_diamond.use_nodes = True

        material_diamond.node_tree.nodes.remove(material_diamond.node_tree.nodes.get('Principled BSDF'))
        material_output = material_diamond.node_tree.nodes.get('Material Output')
        # set location of Node
        material_output.location = (-400, 0)

        #Adding Glass1 Node. NODE IS ADDED
        glass1_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass1_node.location = (-600, 0)
        #setting the default color
        glass1_node.inputs[0].default_value = (1, 0, 0, 1) 
        # Setting the default IOR value
        glass1_node.inputs[2].default_value = 1.446



        #Adding Glass2 Node
        glass2_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass2_node.location = (600, -150)

        #setting the default color
        glass2_node.inputs[0].default_value = (0, 1, 0, 1) 
        # Setting the default IOR value
        glass2_node.inputs[2].default_value = 1.446



        #Adding Glass3 Node
        glass3_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass3_node.location = (-600, -300)

        #setting the default color
        glass3_node.inputs[0].default_value = (0, 0, 1, 1) 
        # Setting the default IOR value
        glass3_node.inputs[2].default_value = 1.450


        add1_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add1_node.location = (-400, -50)

        add1_node.label = "Add 1"

        add1_node.hide = True

        add1_node.select = False


        add2_node = material_diamond.node_tree.nodes.new('ShaderNodeAddShader')
        add2_node.location = (-100, 0)
        add1_node.label = "Add 2"

        add1_node.hide = True

        add1_node.select = False


        glass4_node = material_diamond.node_tree.nodes.new('ShaderNodeBsdfGlass')
        glass4_node.location = (-150, -150)
        glass4_node.inputs[0].default_value = (1, 1, 1, 1) 
        # Setting the default IOR value
        glass4_node.inputs[2].default_value = 1.450

        glass4_node.select = False

        mix1_node = material_diamond.node_tree.nodes.new('ShaderNodeMixShader')
        mix1_node.location = (200, 0)
        mix1_node.select = False


        # created the node from one connectio to other
        material_diamond.node_tree.links.new(glass1_node.outputs[0],add1_node.inputs[0])
        material_diamond.node_tree.links.new(glass2_node.outputs[0],add1_node.inputs[1])
        material_diamond.node_tree.links.new(add1_node.outputs[0],add2_node.inputs[0])
        material_diamond.node_tree.links.new(glass3_node.outputs[0],add1_node.inputs[1])
        material_diamond.node_tree.links.new(glass2_node.outputs[0],mix1_node.inputs[1])
        material_diamond.node_tree.links.new(glass4_node.outputs[0],mix1_node.inputs[2])
        material_diamond.node_tree.links.new(mix1_node.outputs[0],material_output.inputs[0])
        



        bpy.context.object.active_material = material_diamond

        return {'FINISHED'}






def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    bpy.utils.register_class(ShaderMainPanel)
    bpy.utils.register_class(Shared_Ot_Diamond)

    
    
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)
    bpy.utils.unregister_class(ShaderMainPanel)
    bpy.utils.unregister_class(Shared_Ot_Diamond)
    
if __name__ == "__main__":
    register()