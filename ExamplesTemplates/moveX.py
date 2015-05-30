bl_info = {
    "name": "Move along X Axis",
    "category": "Object",
}

import bpy


class ObjectMoveX(bpy.types.Operator):
    """My Object Moving Script"""       # tooltip
    bl_idname = "object.move_x"         # unique identifier
    bl_label = "Move Object 1.0 in the X direction"    # display in interface
    bl_options = {'REGISTER', 'UNDO'}   # enable undo
    
    def execute(self, context):         # called by Blender
        
        # The code that does something
        scene = context.scene
        for obj in scene.objects:
            obj.location.x += 1.0
        
        return {'FINISHED'}             # Tells Blender done
    
def register():
    bpy.utils.register_class(ObjectMoveX)

def unregister():
    bpy.utils.unregister_class(ObjectMoveX)

# This allows you to run the script directly from the
# Blender text editor window to test the addon without
# having to install as an addon.
if __name__ == "__main__":
    register()
