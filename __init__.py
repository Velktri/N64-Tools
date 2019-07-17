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
    "name" : "N64-Tools",
    "author" : "Geoffrey Murray",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D > Sidebar > N64 Tab",
    "warning" : "",
    "category" : "Generic"
}

import bpy

class OBJECT_OT_N64Import(bpy.types.Operator):
    bl_idname = "object.n64import"
    bl_label = "Import N64 scene"

    def execute(self, context):
        bpy.ops.import_scene.x3d(filepath = "C:\VRML\output.wrl")
        return {'FINISHED'}


class N64_PT_Panel(bpy.types.Panel):
    bl_idname = "N64_Panel"
    bl_label = "N64 Panel"
    bl_category = "N64"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI" 

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('object.n64import', text="Import N64 Scene")

classes = (OBJECT_OT_N64Import, N64_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)