class User:
    def __init__(self, option, ruta):
        self.option = option
        self.ruta = ruta

    def execute_command(self, command):
        command.execute(self.ruta)
