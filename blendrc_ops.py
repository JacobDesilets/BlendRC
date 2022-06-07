from lib2to3.pgen2.token import OP
from bpy.types import Operator
from bpy.ops import wm
from . server import ServerThread
from . input import input_queue

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

        wm.run_input()

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

class BLENDRC_OT_RunInput(Operator):
    bl_idname = 'wm.run_input'
    bl_label = 'Run input'
    bl_description = 'Run input'

    timer = None

    def modal(self, context, event):
        server_settings = context.window_manager.server_settings
        if not server_settings.server_running:
            return {'CANCELLED'}
        
        if event.type == 'TIMER':
            if not input_queue.empty():
                print(input_queue.get(), end=' ')

        return {'PASS_THROUGH'}

    def execute(self, context):
        print('Starting to check for input')
        wm = context.window_manager
        self.timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        print('No longer checking for input')
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
