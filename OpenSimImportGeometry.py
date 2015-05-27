#Addon Information
bl_info = {
    "name": "Import an OpenSim geometry file",
    "category": "OpenSim",
}

import xml.dom.minidom
import bpy

# Operator for importing OpenSim geometry files
class OpenSimImportGeometry(bpy.types.Operator):
    """Import an OpenSim geometry file"""
    bl_idname = "opensim.import_geometry"
    bl_label = "Import Geometry"
    bl_options = {'REGISTER'}

	# Member variables
    filepath = bpy.props.StringProperty(subtype="FILE_PATH")

    @classmethod
    def poll(cls, context):
        return context.object is not None

	# Open and parse the geometry file, then add the geometry as a mesh.
    def execute(self, context):
        # Open a debug file
        debugfilename = self.filepath + ".debug.txt"
        debugfile = open(debugfilename,'w')
        debugfile.write(debugfilename + "\n")
         
        # Parse the xml geometry file
        dom = xml.dom.minidom.parse(self.filepath)
        pieceElements = dom.documentElement.getElementsByTagName("Piece")
        NumberOfPoints = pieceElements[0].getAttribute("NumberOfPoints")
        NumberOfFaces = pieceElements[0].getAttribute("NumberOfPolys")
        debugfile.write("root name = " + dom.documentElement.tagName + "\n")
       
        # Read the vertices
        children = pieceElements[0].childNodes
        for child in children:
            if(child.nodeName == "Points"):
                debugfile.write("Found Points node.\n")
                pointsData = child.childNodes
                for data in pointsData:
                    debugfile.write("Found " + data.nodeName + "\n")
            if(child.nodeName == "Polys"):
                debugfile.write("Found Polys node.\n")

        # Create the geometry
        verts = [(1,0,0), (-1,0,0), (0,1,0)]
        faces = [(0,1,2)]
        mesh = bpy.data.meshes.new("Triangle")
        geometry = bpy.data.objects.new("Triangle",mesh)
        geometry.location = context.scene.cursor_location
        context.scene.objects.link(geometry)
        mesh.from_pydata(verts,[],faces)
        mesh.update(calc_edges=True)
        
        # Close the debug file
        debugfile.write("Geometry has " + NumberOfPoints + " vertices and " + NumberOfFaces + " faces.\n")
        debugfile.write("verts = " + str(verts))
        debugfile.write("\n")
        debugfile.write("polys = " + str(faces))
        #debugfile.write("\n")
        debugfile.close

        return {'FINISHED'}

	# Create the file selector dialog.
	# Once the file selector finishes, execute() is called.
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

# Register the Operator
# Uncomment when running as an AddOn
#def register():
#    bpy.utils.register_class(OpenSimImportGeometry)

# Unregister the Operator
# Uncomment when running as an AddOn
#def unregister():
#    bpy.utils.unregister_class(OpenSimImportGeometry)


# Function that specifies how the Operator behaves as a menu button.
def menu_func(self, context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(OpenSimImportGeometry.bl_idname, text="OpenSim Geometry")

# Add a button to the File > Import menu
# Comment out the register line when running as an AddOn.
bpy.utils.register_class(OpenSimImportGeometry)
bpy.types.INFO_MT_file_import.append(menu_func)


# Test call.
# The following line was used during the prototyping of the script.
# It should be commented out once OpenSimImportGeometry is included as a Blender Addon.
bpy.ops.opensim.import_geometry('INVOKE_DEFAULT')