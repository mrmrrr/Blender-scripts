bl_info = {
    "name": "New path render",
    "author": "user",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Image editor",
    "description": "New path render",
    "category": "Render",
}


import bpy, os

from datetime import datetime

 

def newPathToRender():
    
    now = datetime.now()
    current_time = now.strftime("%Hh-%Mm-%Ss")
    filename = os.path.dirname(bpy.data.filepath) + '\\' + 'temp' + '\\' + current_time
    
    bpy.data.scenes[bpy.context.scene.name].render.filepath = filename

class newPAthToRenderClass(bpy.types.Operator):
    bl_idname = "mesh.add_new_path"
    bl_label = "Add new path to output"
    bl_options = {"REGISTER", "UNDO"}
    def execute(self, context):
        newPathToRender()
        return {"FINISHED"}




class VIEW3D_PT_my_custom_panel(bpy.types.Panel):  # class naming convention ‘CATEGORY_PT_name’

    # where to add the panel in the UI
    bl_space_type = "IMAGE_EDITOR"  # 3D Viewport area (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/space_type_items.html#rna-enum-space-type-items)
    bl_region_type = "UI"  # Sidebar region (find list of values here https://docs.blender.org/api/current/bpy_types_enum_items/region_type_items.html#rna-enum-region-type-items)

    bl_category = "Image"  # found in the Sidebar
    bl_label = "New render path"  # found at the top of the Panel

    def draw(self, context):
        
        row = self.layout.row()
        row.operator("mesh.add_new_path", text="New path")
        row.scale_y=2
        
        
        
        

def register():
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)
    bpy.utils.register_class(newPAthToRenderClass)


def unregister():
    bpy.utils.register_class(newPAthToRenderClass)
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)


if __name__ == "__main__":
    register()