class Airport():
    def __init__(self, name):
        self.name = name
        self.connection = []
    
    def add_connection(self, connection):
        self.connection.append(connection)
    