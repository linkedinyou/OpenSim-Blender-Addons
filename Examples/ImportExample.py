from bpy.props import *
from bpy_extras.io_utils import ExportHelper, ImportHelper

class IMPORT_OT_yourformatname(bpy.types.Operator, ImportHelper):
    bl_idname= "import_scene.yourformat"
    bl_description = 'Your description'
    bl_label = "Label for the button in the GUI"
    filename_ext = ".yourextension"
    filter_glob = StringProperty(default="*.defaultextension", options={'HIDDEN'})
    
    filepath= StringProperty(name="File Path", description="Filepath
        used for importing the yourformatname file", maxlen=1024, default="")
    
    def execute(self, context): 
        yourfunctiontorun()
        return {'FINISHED'}
        
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
        
def menu_func(self, context):
    self.layout.operator(IMPORT_OT_yourformatname.bl_idname, text="your description")

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(menu_func)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_import.remove(menu_func)

if __name__ == "__main__":
    register()