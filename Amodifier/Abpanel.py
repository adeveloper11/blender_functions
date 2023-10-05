import bpy

from bpy.types import Panel

class Abhi_pt_panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Modifier operations"
    bl_category = "Amodifier Utils"


    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col  = row.column()

        col.operator("object.apply_all_mods", text = "Apply all")
        
        col  = row.column()
        col.operator("object.cancel_all_mods", text = "Cancel all")

