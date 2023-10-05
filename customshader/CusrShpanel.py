import bpy
from .CustOper import Shader_Ot_neon


class CustPanel(bpy.types.Panel):
    bl_label = "Shader Library"
    bl_idname = "CUST_PT_SHADER"
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"
    bl_category = "CustPanel Utils"


    def draw(self, context):
        layout = self.layout

        row = layout.row()

        row.operator('shader.neon_operator') 


        