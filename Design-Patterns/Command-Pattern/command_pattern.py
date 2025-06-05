class Command:
    def execute(self):
        raise NotImplementedError
    
class Light:
    def on(self):
        print("Light: ON")
        
    def off(self):
        print("Light: OFF")
        
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.on()
        
class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.off()

class RemoteControl:
    def submit(self, command: Command):
        command.execute()
        
# Test
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote =  RemoteControl()
remote.submit(light_on)
remote.submit(light_off)