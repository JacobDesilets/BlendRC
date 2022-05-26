from lib2to3.pgen2.token import OP
from bpy.types import Operator
from . server import ServerThread

class Server:
    server = None

class BLENDRC_OT_StartServer(Operator):
    bl_idname = 'server.start'
    bl_label = 'Start server'
    bl_description = 'Start server'

    def execute(self, context):
        server_settings = context.window_manager.server_settings
        host = server_settings.server_ip
        port = server_settings.server_port
        server_settings.server_running = True
        Server.server = ServerThread(host, port)
        Server.server.start()
        return {'FINISHED'}

class BLENDRC_OT_StopServer(Operator):
    bl_idname = 'server.stop'
    bl_label = 'Stop server'
    bl_description = 'Stop server'

    def execute(self, context):
        server_settings = context.window_manager.server_settings
        server_settings.server_running = False
        Server.server.quit()
        return {'FINISHED'}