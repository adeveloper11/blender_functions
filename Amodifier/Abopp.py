import bpy

from bpy.types import Operator

class Ab_opet_Apply_all(Operator):
    bl_idname = "object.apply_all_mods"
    bl_label = "Apply all"
    bl_description = "Apply all operators of the active object"

    

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False

    
    def execute(self, context):
        active_obj = context.view_layer.objects.active

        for mod in active_obj.modifiers:
            bpy.ops.object.modifier_apply(modifier=mod.name)

        return {'FINISHED'}
    
class Ab_opet_Cancel_all(Operator):
    bl_idname = "object.cancel_all_mods"
    bl_label = "Cancel all"
    bl_description = "Cancel all operators of the active object"

    

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is not None:
            if obj.mode == "OBJECT":
                return True
        return False

    
    def execute(self, context):
        active_obj = context.view_layer.objects.active

        active_obj.modifiers.clear()

        return {'FINISHED'}