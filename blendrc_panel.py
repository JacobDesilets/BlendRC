from bpy.types import Panel

class BLENDRC_PT_Menu(Panel):
    bl_idname = 'BLENDRC_PT_Menu'
    bl_label = 'BlendRC'
    bl_category = 'BlendRC'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        server_settings = context.window_manager.server_settings
        layout = self.layout

        row = layout.row()
        if not server_settings.server_running:
            row.operator('server.start', text='Start server')
        elif server_settings.server_running:
            row.operator('server.stop', text='Stop server')
        row = layout.row()
        row.prop(server_settings, 'server_ip', text='IP')
        row.prop(server_settings, 'server_port', text='port')
