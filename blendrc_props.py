from bpy.types import PropertyGroup
from bpy.props import StringProperty, BoolProperty

class Server_Props(PropertyGroup):
    server_running : BoolProperty(name='Server running', description='Is the server currently running', default=False)
    server_ip : StringProperty(name='Server IP', description='IP address of the server', default='127.0.0.1')
    server_port : StringProperty(name='Server port', description='Port of the server', default='8888')