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

from bpy.types import WindowManager
from bpy.utils import register_class, unregister_class
from bpy.props import PointerProperty

bl_info = {
    "name" : "BlendRC",
    "author" : "Jacob Desilets",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

from . blendrc_props import Server_Props
from . blendrc_panel import BLENDRC_PT_Menu
from . blendrc_ops import BLENDRC_OT_StartServer, BLENDRC_OT_StopServer, BLENDRC_OT_RunInput

classes = (Server_Props, BLENDRC_PT_Menu, BLENDRC_OT_StartServer, BLENDRC_OT_StopServer, BLENDRC_OT_RunInput)

def register():
    # Register classes
    for c in classes:
        register_class(c)

    # Set up properties
    WindowManager.server_settings = PointerProperty(type=Server_Props)

def unregister():
    # Unregister classes
    for c in reversed(classes):
        unregister_class(c)

    # Delete properties
    del WindowManager.server_settings